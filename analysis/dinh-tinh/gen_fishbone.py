# -*- coding: utf-8 -*-
"""Sinh anh bieu do xuong ca (fishbone / Ishikawa) cho muc 4.5 Chuong 4.

Sinh hai hinh:
  fishbone-C4.png              — van de: thoi gian xu ly mot ca bao hanh keo dai
  fishbone-dieu-chuyen-gap.png — van de: phat sinh dieu chuyen gap giua cua hang

Chay: python analysis/dinh-tinh/gen_fishbone.py

Noi dung nguyen nhan lay tu Issue Register v2 va tu muc 11 cua cac ho so quy trinh.
Ma IR ghi trong ngoac de doi chieu nguoc lai duoc.
"""
import math
import pathlib

from PIL import Image, ImageDraw, ImageFont

D = pathlib.Path(__file__).resolve().parent

BG = (255, 255, 255)
INK = (25, 25, 25)
SPINE = (60, 60, 60)
BONE = (70, 110, 180)
BOX = (200, 60, 60)
SUB = (90, 90, 90)


def font(size, bold=False):
    for p in ("C:/Windows/Fonts/segoeuib.ttf" if bold else "C:/Windows/Fonts/segoeui.ttf",
              "C:/Windows/Fonts/arialbd.ttf" if bold else "C:/Windows/Fonts/arial.ttf",
              "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"):
        try:
            return ImageFont.truetype(p, size)
        except Exception:
            continue
    return ImageFont.load_default()


def wrap(d, text, f, maxw):
    words, lines, cur = text.split(), [], ""
    for w in words:
        t = (cur + " " + w).strip()
        if d.textbbox((0, 0), t, font=f)[2] <= maxw:
            cur = t
        else:
            if cur:
                lines.append(cur)
            cur = w
    if cur:
        lines.append(cur)
    return lines


def ve(path, tieu_de, van_de, xuong, W=2700, H=1260):
    """xuong: list (ten_nhanh, [nguyen_nhan, ...]) — 6 nhanh, 3 tren 3 duoi."""
    img = Image.new("RGB", (W, H), BG)
    d = ImageDraw.Draw(img)
    F_T, F_B, F_C, F_N = font(30, True), font(19, True), font(15), font(13)

    d.text((60, 28), tieu_de, font=F_T, fill=INK)

    y_spine = H // 2
    x0, x1 = 150, W - 470

    # --- xuong song ---
    d.line([(x0, y_spine), (x1, y_spine)], fill=SPINE, width=5)
    for s in (2.7, -2.7):
        a = 0
        d.line([(x1, y_spine),
                (x1 + 22 * math.cos(a + s), y_spine + 22 * math.sin(a + s))],
               fill=SPINE, width=5)

    # --- o van de ---
    bw, bh = 400, 190
    bx, by = x1 + 20, y_spine - bh // 2
    d.rounded_rectangle([bx, by, bx + bw, by + bh], radius=14,
                        fill=(255, 245, 245), outline=BOX, width=3)
    lines = wrap(d, van_de, F_B, bw - 40)
    ty = by + bh // 2 - len(lines) * 13
    for ln in lines:
        bb = d.textbbox((0, 0), ln, font=F_B)
        d.text((bx + bw / 2 - (bb[2] - bb[0]) / 2, ty), ln, font=F_B, fill=BOX)
        ty += 26

    # --- cac nhanh ---
    tren = xuong[0::2]
    duoi = xuong[1::2]
    span = x1 - x0 - 200
    for nhom, phia in ((tren, -1), (duoi, +1)):
        n = len(nhom)
        for i, (ten, nguyen_nhan) in enumerate(nhom):
            # chan xuong nam tren song, ngon xuong cheo ra ngoai
            x_chan = x0 + 220 + i * (span / max(n, 1))
            x_ngon = x_chan - 150
            y_ngon = y_spine + phia * 285
            d.line([(x_chan, y_spine), (x_ngon, y_ngon)], fill=BONE, width=3)

            # nhan nhanh o dau xuong
            bb = d.textbbox((0, 0), ten, font=F_B)
            lx = x_ngon - (bb[2] - bb[0]) / 2
            ly = y_ngon + (-34 if phia < 0 else 12)
            d.rectangle([lx - 10, ly - 5, lx + (bb[2] - bb[0]) + 10, ly + 26],
                        fill=(238, 244, 255), outline=BONE)
            d.text((lx, ly), ten, font=F_B, fill=(40, 70, 130))

            # cac nguyen nhan bam vao xuong
            for j, nn in enumerate(nguyen_nhan):
                t = (j + 1) / (len(nguyen_nhan) + 1.0)
                px = x_chan + (x_ngon - x_chan) * t
                py = y_spine + (y_ngon - y_spine) * t
                d.line([(px, py), (px + 190, py)], fill=SUB, width=2)
                for k, ln in enumerate(wrap(d, nn, F_C, 300)):
                    d.text((px + 196, py - 9 + k * 17), ln, font=F_C, fill=INK)

    d.text((60, H - 34),
           "Nguồn: nhóm tự lập từ Issue Register v2 và mục 11 các hồ sơ quy trình. "
           "Mã IR trong ngoặc để đối chiếu.",
           font=F_N, fill=SUB)
    img.save(path)
    return img.size


# ============================================================ hinh 1: C4
XUONG_C4 = [
    ("Con người", [
        "Quầy bảo hành ít người trực hơn quầy bán (IR-09)",
        "KTV tại cửa hàng chỉ xử lý được lỗi nhẹ",
        "Phải hỏi lại khách nhiều lần khi thiếu dữ liệu (IR-11)",
    ]),
    ("Quy trình", [
        "Chưa tách luồng xử lý nhanh khỏi luồng gửi đi",
        "Kiểm tra điều kiện bảo hành đặt sau khi khách đã chờ",
        "Không có cơ chế ưu tiên ca đơn giản",
    ]),
    ("Hệ thống, thiết bị", [
        "Tra theo IMEI không phải lúc nào cũng ra dữ liệu (IR-11)",
        "Cửa hàng thiếu thiết bị chẩn đoán sâu nên phải gửi đi (IR-10)",
    ]),
    ("Thông tin, dữ liệu", [
        "Khách không giữ hóa đơn (ngoại lệ E1)",
        "Dữ liệu mua hàng chưa gắn đủ theo IMEI",
        "Dữ liệu lỗi về M2 chậm (IR-13)",
    ]),
    ("Chính sách, đối tác ngoài", [
        "Quyết định cuối thuộc trung tâm bảo hành (quy tắc R4)",
        "TopZone đi kênh ủy quyền Apple, thời gian khác (R5)",
        "Trung tâm trả kết quả trễ hẹn (ngoại lệ E3)",
    ]),
    ("Vật tư, linh kiện", [
        "Hết máy để đổi, phải điều chuyển (E2 → IR-22)",
        "Linh kiện thay thế không có sẵn tại cửa hàng",
    ]),
]

# =========================================== hinh 2: dieu chuyen gap
XUONG_DC = [
    ("Hoạch định nhu cầu (M1)", [
        "Model mới không có cơ sở lịch sử để dự báo (IR-16)",
        "Đề xuất từ cửa hàng về chậm (IR-14)",
        "Không hiệu chỉnh được dự báo giữa kỳ (IR-17)",
    ]),
    ("Phân bổ, tồn kho (M3)", [
        "Phân bổ theo kế hoạch, không theo tốc độ bán thực tế",
        "Cửa hàng nguồn phải giữ tồn tối thiểu (quy tắc R3)",
        "Hàng tới nơi chưa xác nhận nên chưa khả dụng (IR-26)",
    ]),
    ("Khâu bán (C1, C3)", [
        "Kiểm tra tồn diễn ra muộn trong quy trình (IR-02)",
        "Hồ sơ trả góp duyệt xong mới phát hiện hết hàng (IR-08)",
    ]),
    ("Khâu bảo hành (C4)", [
        "Hết máy để đổi khi đã có quyết định đổi (ngoại lệ E2)",
    ]),
    ("Thủ tục điều chuyển (M3)", [
        "Ca gấp vẫn phải qua dò nguồn và chuỗi duyệt (IR-23)",
        "Ngưỡng giá trị phải trình duyệt (G9, G10 — chưa xác minh)",
        "Không có nguồn thì công đã bỏ ra bị hủy (IR-24)",
    ]),
    ("Dữ liệu tồn kho", [
        "Tồn hệ thống lệch tồn thực tế (IR-25)",
        "Phát hiện lệch chỉ khi tới kỳ kiểm kê",
    ]),
]

if __name__ == "__main__":
    s1 = ve(D / "fishbone-C4.png",
            "Biểu đồ xương cá — C4 Bảo hành, đổi trả",
            "Thời gian từ khi khách mang máy tới quầy "
            "đến khi nhận lại máy kéo dài",
            XUONG_C4)
    print("fishbone-C4.png %s" % (s1,))

    s2 = ve(D / "fishbone-dieu-chuyen-gap.png",
            "Biểu đồ xương cá — điều chuyển gấp giữa các cửa hàng",
            "Phát sinh điều chuyển gấp để chữa "
            "tình trạng hết hàng cục bộ",
            XUONG_DC)
    print("fishbone-dieu-chuyen-gap.png %s" % (s2,))
