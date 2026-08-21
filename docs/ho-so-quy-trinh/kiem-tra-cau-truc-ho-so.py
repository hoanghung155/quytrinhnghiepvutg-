# -*- coding: utf-8 -*-
"""Kiem tra ho so quy trinh co dung 12 muc theo template khong.

Dung chung cho ca ba nhom ho so: cot loi (C1-C4), quan ly (M1-M4), ho tro (S1-S4).
Chay: python docs/ho-so-quy-trinh/kiem-tra-cau-truc-ho-so.py
Tren Windows neu console bao loi ma hoa thi dat PYTHONIOENCODING=utf-8 truoc khi chay.

Kiem tra bon thu:
  1. Du 12 muc, dung thu tu, dung ten muc so voi template.
  2. Dem so buoc o muc 5.
  3. Dem so diem ra quyet dinh o muc 6 — ho so co BPMN phai HON 7.
  4. Dem so ngoai le (muc 7) va so quy tac nghiep vu (muc 8).

Thoat voi ma 1 neu co ho so lech cau truc hoac thieu gateway.
"""
import re
import sys
import pathlib

ROOT = pathlib.Path(__file__).resolve().parent
TEMPLATE = ROOT / "_template-ho-so-quy-trinh.md"

# Ma quy trinh co mo hinh BPMN -> bat buoc hon 7 diem ra quyet dinh o muc 6.
CO_BPMN = {"C3", "C4", "M2", "M3", "S1", "S4"}

SEC = re.compile(r"^## (\d+)\. (.+)$", re.M)


def muc(txt, so):
    """Cat noi dung cua mot muc theo so thu tu."""
    phan = txt.split("## %d." % so)
    if len(phan) < 2:
        return ""
    sau = phan[1]
    ke = re.search(r"^## \d+\.", sau, re.M)
    return sau[: ke.start()] if ke else sau


def dem(txt, mau):
    return len(re.findall(mau, txt, re.M))


def main():
    want = SEC.findall(TEMPLATE.read_text(encoding="utf-8"))
    print("Template: %d muc" % len(want))

    loi = 0
    for f in sorted(ROOT.rglob("ho-so-*.md")):
        ma = f.stem.replace("ho-so-", "")
        txt = f.read_text(encoding="utf-8")
        got = SEC.findall(txt)

        cau_truc_ok = got == want
        n_buoc = dem(muc(txt, 5), r"^\| \d+ \|")
        n_gw = dem(muc(txt, 6), r"^\| G\d+\w* \|")
        n_e = dem(muc(txt, 7), r"^\| E\d+ \|")
        n_r = dem(muc(txt, 8), r"^\| R\d+ \|")

        gw_ok = (n_gw > 7) if ma in CO_BPMN else True
        if not cau_truc_ok or not gw_ok:
            loi += 1

        print(
            "%-3s | 12 muc: %-5s | buoc: %2d | quyet dinh: %2d%s | ngoai le: %d | quy tac: %d"
            % (
                ma,
                "khop" if cau_truc_ok else "LECH",
                n_buoc,
                n_gw,
                "" if gw_ok else "  <-- CAN HON 7 (co BPMN)",
                n_e,
                n_r,
            )
        )
        if not cau_truc_ok:
            for i, (g, w) in enumerate(zip(got, want)):
                if g != w:
                    print("      lech muc %d: co '%s' / can '%s'" % (i + 1, g[1], w[1]))
            if len(got) != len(want):
                print("      so muc: %d / can %d" % (len(got), len(want)))

    print()
    print("Ket qua: %s" % ("dat" if loi == 0 else "%d ho so can sua" % loi))
    return 1 if loi else 0


if __name__ == "__main__":
    sys.exit(main())
