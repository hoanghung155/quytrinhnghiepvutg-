# -*- coding: utf-8 -*-
"""Sinh hinh-1-1-kien-truc-quy-trinh.png — so do kien truc 12 quy trinh theo 3 lop.

Nguon noi dung: phan-ra-12-quy-trinh.md (cung thu muc).
Ve bang PIL de khong phu thuoc graphviz. Dinh tuyen vuong goc, khong cat cheo qua box.
"""
import math
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

OUT = Path(__file__).parent / "hinh-1-1-kien-truc-quy-trinh.png"

W, H = 1900, 1230
BG = (255, 255, 255)
BLACK = (25, 25, 25)
GREY = (125, 125, 125)
RED = (185, 40, 40)

BAND = {
    "quan-ly": dict(y=170, h=250, fill=(226, 238, 255), edge=(60, 110, 185),
                    title="LỚP QUẢN LÝ — điều phối và ra quyết định"),
    "cot-loi": dict(y=490, h=300, fill=(255, 241, 208), edge=(195, 145, 25),
                    title="LỚP CỐT LÕI — trực tiếp sinh doanh thu"),
    "ho-tro":  dict(y=860, h=250, fill=(228, 246, 228), edge=(60, 145, 75),
                    title="LỚP HỖ TRỢ — duy trì năng lực vận hành"),
}
PROC = {
    "quan-ly": [("M1", "Hoạch định\nnhu cầu"), ("M2", "Quản lý\nnhà cung cấp"),
                ("M3", "Kho và\nđiều chuyển"), ("M4", "Mạng lưới\ncửa hàng")],
    "cot-loi": [("C1", "Bán tại\ncửa hàng"), ("C2", "Bán online,\ngiao & nhận"),
                ("C3", "Bán\ntrả góp"), ("C4", "Bảo hành,\nđổi trả")],
    "ho-tro":  [("S1", "Tuyển dụng\nvà đào tạo"), ("S2", "Vận hành\nERP / POS"),
                ("S3", "Mua sắm\nhạ tầng"), ("S4", "Đối soát\ncông nợ NCC")],
}
BPMN = {"M2", "M3", "C3", "C4", "S1", "S4"}

BOX_W, BOX_H, MARGIN_X = 300, 150, 110
GAP = (W - 2 * MARGIN_X - 4 * BOX_W) // 3          # = 160


def _font(size, bold=False):
    for p in ("C:/Windows/Fonts/segoeuib.ttf" if bold else "C:/Windows/Fonts/segoeui.ttf",
              "C:/Windows/Fonts/arialbd.ttf" if bold else "C:/Windows/Fonts/arial.ttf",
              "/System/Library/Fonts/Supplemental/Arial.ttf",
              "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"):
        try:
            return ImageFont.truetype(p, size)
        except Exception:
            continue
    return ImageFont.load_default()


F_TITLE, F_BAND = _font(34, True), _font(21, True)
F_CODE, F_NAME, F_NOTE, F_BADGE = _font(30, True), _font(19), _font(16), _font(13, True)


def center(d, text, font, cx, y, fill=BLACK):
    b = d.textbbox((0, 0), text, font=font)
    d.text((cx - (b[2] - b[0]) / 2, y), text, font=font, fill=fill)


def box(layer, i):
    x1 = MARGIN_X + i * (BOX_W + GAP)
    y1 = BAND[layer]["y"] + 68
    return x1, y1, x1 + BOX_W, y1 + BOX_H


def cx(layer, i):
    x1, _, x2, _ = box(layer, i)
    return (x1 + x2) / 2


def head(d, p_from, p_to, color, width):
    """Chi ve dau mui ten tai p_to, huong tu p_from."""
    ang = math.atan2(p_to[1] - p_from[1], p_to[0] - p_from[0])
    for s in (2.6, -2.6):
        d.line([p_to, (p_to[0] + 16 * math.cos(ang + s), p_to[1] + 16 * math.sin(ang + s))],
               fill=color, width=width)


def route(d, pts, color=BLACK, width=3):
    """Ve duong gap khuc qua danh sach diem, dau mui ten o diem cuoi."""
    d.line(pts, fill=color, width=width, joint="curve")
    head(d, pts[-2], pts[-1], color, width)


def main():
    img = Image.new("RGB", (W, H), BG)
    d = ImageDraw.Draw(img)

    center(d, "Hình 1.1 — Kiến trúc quy trình nghiệp vụ chuỗi TGDĐ + TopZone", F_TITLE, W / 2, 26)
    center(d, "12 quy trình chia ba lớp · 6 quy trình được mô hình hóa BPMN (viền đậm, có nhãn BPMN)",
           F_NOTE, W / 2, 72, GREY)

    for key, band in BAND.items():
        d.rounded_rectangle([60, band["y"], W - 60, band["y"] + band["h"]],
                            radius=16, fill=band["fill"], outline=band["edge"], width=2)
        d.text((78, band["y"] + 16), band["title"], font=F_BAND, fill=band["edge"])
        for i, (code, name) in enumerate(PROC[key]):
            x1, y1, x2, y2 = box(key, i)
            on = code in BPMN
            d.rounded_rectangle([x1, y1, x2, y2], radius=12, fill=BG,
                                outline=band["edge"], width=5 if on else 2)
            center(d, code, F_CODE, (x1 + x2) / 2, y1 + 22)
            for j, ln in enumerate(name.split("\n")):
                center(d, ln, F_NAME, (x1 + x2) / 2, y1 + 70 + j * 26)
            if on:
                d.rounded_rectangle([x2 - 74, y1 + 10, x2 - 12, y1 + 32], radius=6,
                                    fill=band["edge"])
                center(d, "BPMN", F_BADGE, x2 - 43, y1 + 13, BG)

    # --- 1. M1 -> M2, 2. M2 -> M3 : ngang trong lop quan ly -------------------
    route(d, [(box("quan-ly", 0)[2], 313), (box("quan-ly", 1)[0], 313)])
    d.text((432, 286), "kế hoạch", font=F_NOTE, fill=BLACK)
    route(d, [(box("quan-ly", 1)[2], 313), (box("quan-ly", 2)[0], 313)])
    d.text((888, 286), "đơn hàng", font=F_NOTE, fill=BLACK)

    # --- 3. M3 -> C1, C2, C3 : bus ngang o kenh giua hai lop ------------------
    BUS = 455
    d.line([(cx("quan-ly", 2), 388), (cx("quan-ly", 2), BUS)], fill=GREY, width=2)
    d.line([(cx("cot-loi", 0), BUS), (cx("quan-ly", 2), BUS)], fill=GREY, width=2)
    for i in (0, 1, 2):
        route(d, [(cx("cot-loi", i), BUS), (cx("cot-loi", i), box("cot-loi", i)[1])], GREY, 2)
    d.text((300, 424), "tồn kho khả dụng → điều kiện xuất hàng", font=F_NOTE, fill=GREY)

    # --- 4. C1, C2, C3 -> C4 : bus ngang trong lop cot loi --------------------
    LOW = 750
    for i in (0, 1, 2):
        d.line([(cx("cot-loi", i), box("cot-loi", i)[3]), (cx("cot-loi", i), LOW)],
               fill=GREY, width=2)
    d.line([(cx("cot-loi", 0), LOW), (cx("cot-loi", 3), LOW)], fill=GREY, width=2)
    route(d, [(cx("cot-loi", 3), LOW), (cx("cot-loi", 3), box("cot-loi", 3)[3] + 2)], GREY, 2)
    d.text((300, 758), "đơn đã bán → căn cứ xác định điều kiện bảo hành", font=F_NOTE, fill=GREY)

    # --- 5. C4 -> M2 : vong phan hoi, di vong ben phai va phia tren -----------
    route(d, [(box("cot-loi", 3)[2], 600), (1858, 600), (1858, 140),
              (cx("quan-ly", 1), 140), (cx("quan-ly", 1), box("quan-ly", 1)[1])], RED, 3)
    d.text((770, 112), "tỷ lệ lỗi theo model  →  vòng phản hồi vào đánh giá nhà cung cấp",
           font=F_NOTE, fill=RED)

    # --- 6. M2 -> S4 : xuong qua kenh giua cot C2 va C3 -----------------------
    CH = box("cot-loi", 1)[2] + GAP / 2          # x = 950, kenh trong giua cac cot
    route(d, [(box("quan-ly", 1)[2] - 40, 388), (box("quan-ly", 1)[2] - 40, 438),
              (CH, 438), (CH, 825), (cx("ho-tro", 3), 825),
              (cx("ho-tro", 3), box("ho-tro", 3)[1])], GREY, 2)
    d.text((1000, 796), "hợp đồng và đơn hàng → căn cứ đối soát công nợ", font=F_NOTE, fill=GREY)

    d.text((78, H - 56), "Nguồn: nhóm tự lập từ quan sát và tài liệu công khai — "
                         "không phải sơ đồ do MWG ban hành.", font=F_NOTE, fill=GREY)
    img.save(OUT)
    print("Da ghi", OUT.name, img.size)


if __name__ == "__main__":
    main()
