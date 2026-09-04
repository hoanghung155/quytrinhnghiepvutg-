# -*- coding: utf-8 -*-
"""Soat caption hinh va bang trong file bao cao Word.

Quy uoc cua nhom (P0-B):
  - Label HINH nam DUOI hinh.
  - Label BANG nam TREN bang.
  - Danh so theo chuong: Hinh 2.1, Bang 4.3...

Chay: python report/soat_caption.py
Tren Windows neu console bao loi ma hoa thi dat PYTHONIOENCODING=utf-8.

Script duyet than tai lieu theo DUNG THU TU xuat hien (doan van va bang xen ke),
nen phat hien duoc caption dat sai phia — thu ma doc tung doan roi tung bang
khong phat hien duoc.

Kiem tra bon thu:
  1. Moi hinh co mot caption "Hinh x.y" ngay SAU no.
  2. Moi bang co mot caption "Bang x.y" ngay TRUOC no.
  3. So thu tu lien tuc trong tung chuong, khong nhay so, khong trung.
  4. Liet ke danh muc hinh va danh muc bang de dan vao dau bao cao.

Thoat voi ma 1 neu co loi caption.
"""
import re
import sys
import pathlib

try:
    import docx
except ImportError:
    print("Can cai python-docx: pip install python-docx")
    sys.exit(2)

FILE = pathlib.Path(__file__).resolve().parent / "bao-cao-quy-trinh-nghiep-vu-TGDD-TopZone.docx"

RE_HINH = re.compile(r"^Hình\s+(\d+)\.(\d+)\.?\s*(.*)$")
RE_BANG = re.compile(r"^Bảng\s+(\d+)\.(\d+)\.?\s*(.*)$")
RE_CHUA = re.compile(r"^\[CHUA CO\]", re.I)


def duyet_than(doc):
    """Tra ve danh sach ('p', paragraph) va ('t', table) theo dung thu tu trong file."""
    from docx.table import Table
    from docx.text.paragraph import Paragraph

    ra = []
    body = doc.element.body
    for child in body.iterchildren():
        if child.tag.endswith("}p"):
            ra.append(("p", Paragraph(child, doc)))
        elif child.tag.endswith("}tbl"):
            ra.append(("t", Table(child, doc)))
    return ra


def co_anh(p):
    return bool(p._element.findall(
        ".//{http://schemas.openxmlformats.org/drawingml/2006/main}blip"))


def main():
    if not FILE.exists():
        print("Khong tim thay %s" % FILE.name)
        return 2

    doc = docx.Document(FILE)
    items = duyet_than(doc)

    hinh, bang, loi, cho_ai = [], [], [], []

    for i, (kind, obj) in enumerate(items):
        if kind == "p":
            txt = obj.text.strip()

            if RE_CHUA.match(txt):
                cho_ai.append(txt)

            m = RE_HINH.match(txt)
            if m:
                # caption hinh phai co anh o doan LIEN TRUOC (bo qua doan rong)
                j, thay_anh = i - 1, False
                while j >= 0 and items[j][0] == "p" and not items[j][1].text.strip():
                    if co_anh(items[j][1]):
                        thay_anh = True
                        break
                    j -= 1
                if j >= 0 and items[j][0] == "p" and co_anh(items[j][1]):
                    thay_anh = True
                hinh.append((int(m.group(1)), int(m.group(2)), m.group(3), thay_anh))
                if not thay_anh:
                    loi.append("Caption '%s' khong co hinh o ngay tren" % txt[:60])

            m = RE_BANG.match(txt)
            if m:
                # caption bang phai co bang o ngay SAU (bo qua doan rong)
                j, thay_bang = i + 1, False
                while j < len(items):
                    if items[j][0] == "t":
                        thay_bang = True
                        break
                    if items[j][0] == "p" and items[j][1].text.strip():
                        break
                    j += 1
                bang.append((int(m.group(1)), int(m.group(2)), m.group(3), thay_bang))
                if not thay_bang:
                    loi.append("Caption '%s' khong co bang o ngay duoi" % txt[:60])

    # --- bang khong co caption phia tren ---
    for i, (kind, obj) in enumerate(items):
        if kind != "t":
            continue
        j, co_cap = i - 1, False
        while j >= 0 and items[j][0] == "p":
            t = items[j][1].text.strip()
            if t:
                co_cap = bool(RE_BANG.match(t))
                break
            j -= 1
        if not co_cap:
            loi.append("Bang thu %d trong file khong co caption 'Bang x.y' o tren"
                       % (sum(1 for k, _ in items[: i + 1] if k == "t")))

    # --- hinh khong co caption phia duoi ---
    for i, (kind, obj) in enumerate(items):
        if kind != "p" or not co_anh(obj):
            continue
        j, co_cap = i + 1, False
        while j < len(items) and items[j][0] == "p":
            t = items[j][1].text.strip()
            if t:
                co_cap = bool(RE_HINH.match(t))
                break
            j += 1
        if not co_cap:
            loi.append("Mot hinh trong file khong co caption 'Hinh x.y' o duoi")

    # --- kiem tra danh so lien tuc theo chuong ---
    def kiem_so(ds, ten):
        theo_chuong = {}
        for ch, so, _, _ in ds:
            theo_chuong.setdefault(ch, []).append(so)
        for ch in sorted(theo_chuong):
            so = sorted(theo_chuong[ch])
            if len(so) != len(set(so)):
                loi.append("%s chuong %d: co so bi trung %s" % (ten, ch, so))
            if so and so != list(range(1, len(so) + 1)):
                loi.append("%s chuong %d: danh so khong lien tuc %s" % (ten, ch, so))

    kiem_so(hinh, "Hinh")
    kiem_so(bang, "Bang")

    # --- in ket qua ---
    print("File: %s" % FILE.name)
    print("Tong: %d hinh co caption, %d bang co caption, %d muc [CHUA CO]\n"
          % (len(hinh), len(bang), len(cho_ai)))

    print("--- DANH MUC HINH VE ---")
    for ch, so, ten, ok in sorted(hinh):
        print("  Hinh %d.%d. %s%s" % (ch, so, ten, "" if ok else "   <-- THIEU HINH"))

    print("\n--- DANH MUC BANG BIEU ---")
    for ch, so, ten, ok in sorted(bang):
        print("  Bang %d.%d. %s%s" % (ch, so, ten, "" if ok else "   <-- THIEU BANG"))

    if cho_ai:
        print("\n--- MUC CHUA CO NOI DUNG (%d) ---" % len(cho_ai))
        for t in cho_ai:
            print("  %s" % t[:110])

    print()
    if loi:
        print("LOI CAPTION (%d):" % len(loi))
        for e in loi:
            print("  - %s" % e)
        return 1
    print("Caption: dat — moi hinh co label o duoi, moi bang co label o tren.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
