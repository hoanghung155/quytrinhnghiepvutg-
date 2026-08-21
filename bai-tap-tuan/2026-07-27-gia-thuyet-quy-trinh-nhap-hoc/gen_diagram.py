# -*- coding: utf-8 -*-
"""Sinh diagram.png — mo hinh BPMN gia thuyet (don gian) quy trinh nhap hoc
sinh vien Newtown University, suy tu so do to chuc + so do lop UML + chinh
sach tuyen sinh (chap04.pdf slide 18-20). Ve bang PIL, tieng Viet co dau.
"""
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont
import math

OUT = Path(__file__).parent / "diagram.png"

W, H = 2000, 1050
BG = (255, 255, 255)
BLACK = (0, 0, 0)
GREY = (120, 120, 120)
GREEN = (0, 140, 0)
RED = (180, 30, 30)
YELLOW_FILL = (255, 245, 200)
BLUE_FILL = (220, 235, 255)
PINK_FILL = (255, 228, 235)
LIGHT_GREY = (245, 245, 245)

img = Image.new("RGB", (W, H), BG)
d = ImageDraw.Draw(img)


def _font(size, bold=False):
    for p in (
        "/System/Library/Fonts/Supplemental/Arial Bold.ttf" if bold else "/System/Library/Fonts/Supplemental/Arial.ttf",
        "/System/Library/Fonts/Helvetica.ttc",
    ):
        try:
            return ImageFont.truetype(p, size)
        except Exception:
            continue
    return ImageFont.load_default()


F_TITLE = _font(22, bold=True)
F_POOL = _font(18, bold=True)
F_TASK = _font(14, bold=True)
F_SMALL = _font(12)

POOL_LABEL_W = 120
POOL_LEFT, POOL_RIGHT = 20, W - 20
POOLS = [
    ("Ứng viên", 90, 330, BLUE_FILL),
    ("Phòng Tuyển sinh", 330, 590, YELLOW_FILL),
    ("Hội đồng Học thuật", 590, 830, PINK_FILL),
]
for label, y1, y2, fill in POOLS:
    d.rectangle([POOL_LEFT, y1, POOL_RIGHT, y2], outline=BLACK, width=2, fill=fill)
    d.rectangle([POOL_LEFT, y1, POOL_LEFT + POOL_LABEL_W, y2], outline=BLACK, width=2, fill=LIGHT_GREY)
    tmp = Image.new("RGBA", (y2 - y1, POOL_LABEL_W), (0, 0, 0, 0))
    dt = ImageDraw.Draw(tmp)
    bbox = dt.textbbox((0, 0), label, font=F_POOL)
    tw, th = bbox[2] - bbox[0], bbox[3] - bbox[1]
    dt.text(((y2 - y1 - tw) / 2, (POOL_LABEL_W - th) / 2 - 4), label, fill=BLACK, font=F_POOL)
    tmp = tmp.rotate(90, expand=True)
    img.paste(tmp, (POOL_LEFT + 2, y1 + 2), tmp)


def event_circle(cx, cy, r=20, thick=2, fill=(255, 255, 255), color=BLACK, label=None, below=True):
    d.ellipse([cx - r, cy - r, cx + r, cy + r], outline=color, width=thick, fill=fill)
    if label:
        for i, ln in enumerate(label.split("\n")):
            bbox = d.textbbox((0, 0), ln, font=F_SMALL)
            tw, th = bbox[2] - bbox[0], bbox[3] - bbox[1]
            y = cy + r + 4 + i * 15 if below else cy - r - 15 * (label.count(chr(10)) + 1 - i) - 4
            d.text((cx - tw / 2, y), ln, fill=BLACK, font=F_SMALL)
    return (cx, cy, r)


def start_circle(cx, cy, label=None, below=True):
    return event_circle(cx, cy, r=20, thick=2, fill=(230, 255, 230), color=GREEN, label=label, below=below)


def end_circle(cx, cy, label=None, below=True):
    return event_circle(cx, cy, r=20, thick=4, fill=(255, 235, 235), color=RED, label=label, below=below)


def task_box(cx, cy, text, w=190, h=64):
    x1, y1, x2, y2 = cx - w / 2, cy - h / 2, cx + w / 2, cy + h / 2
    d.rounded_rectangle([x1, y1, x2, y2], radius=8, outline=BLACK, width=2, fill=(255, 255, 255))
    lines = text.split("\n")
    total_h = len(lines) * 17
    for i, ln in enumerate(lines):
        bbox = d.textbbox((0, 0), ln, font=F_TASK)
        tw = bbox[2] - bbox[0]
        d.text((cx - tw / 2, cy - total_h / 2 + i * 17), ln, fill=BLACK, font=F_TASK)
    return (cx, cy, w, h)


def gateway(cx, cy, size=26, label=None, above=True):
    pts = [(cx, cy - size), (cx + size, cy), (cx, cy + size), (cx - size, cy)]
    d.polygon(pts, outline=BLACK, fill=(255, 255, 255))
    d.line(pts + [pts[0]], fill=BLACK, width=2)
    bbox = d.textbbox((0, 0), "X", font=F_TASK)
    tw, th = bbox[2] - bbox[0], bbox[3] - bbox[1]
    d.text((cx - tw / 2, cy - th / 2 - 3), "X", fill=BLACK, font=F_TASK)
    if label:
        lines = label.split("\n")
        for i, ln in enumerate(lines):
            bbox = d.textbbox((0, 0), ln, font=F_SMALL)
            tw, th = bbox[2] - bbox[0], bbox[3] - bbox[1]
            y = cy - size - (len(lines) - i) * 15 - 4 if above else cy + size + 4 + i * 15
            d.text((cx - tw / 2, y), ln, fill=BLACK, font=F_SMALL)
    return (cx, cy, size)


def arrow(x1, y1, x2, y2, dashed=False, color=BLACK, label=None, off=(0, 0)):
    if dashed:
        dx, dy = x2 - x1, y2 - y1
        length = math.hypot(dx, dy) or 1
        ux, uy = dx / length, dy / length
        segs = max(1, int(length / 12))
        for i in range(0, segs, 2):
            sx, sy = x1 + ux * i * 12, y1 + uy * i * 12
            ex, ey = x1 + ux * min((i + 1) * 12, length), y1 + uy * min((i + 1) * 12, length)
            d.line([(sx, sy), (ex, ey)], fill=color, width=2)
    else:
        d.line([(x1, y1), (x2, y2)], fill=color, width=2)
    ang = math.atan2(y2 - y1, x2 - x1)
    ah = 10
    p1 = (x2 - ah * math.cos(ang - math.pi / 6), y2 - ah * math.sin(ang - math.pi / 6))
    p2 = (x2 - ah * math.cos(ang + math.pi / 6), y2 - ah * math.sin(ang + math.pi / 6))
    d.polygon([(x2, y2), p1, p2], fill=color)
    if label:
        mx, my = (x1 + x2) / 2 + off[0], (y1 + y2) / 2 + off[1]
        for i, ln in enumerate(label.split("\n")):
            bbox = d.textbbox((0, 0), ln, font=F_SMALL)
            tw, th = bbox[2] - bbox[0], bbox[3] - bbox[1]
            yy = my + i * (th + 2)
            d.rectangle([mx - tw / 2 - 3, yy - 1, mx + tw / 2 + 3, yy + th + 1], fill=(255, 255, 255))
            d.text((mx - tw / 2, yy), ln, fill=color, font=F_SMALL)


COL = 40 + POOL_LEFT + POOL_LABEL_W
X = [COL + i * 230 for i in range(8)]
Y_AP, Y_AO, Y_AC = 190, 460, 710

# ---- Ứng viên ----
sA = start_circle(X[0], Y_AP, "Có nhu cầu\nnhập học")
tA1 = task_box(X[1], Y_AP, "Nộp hồ sơ\n(hoàn tất + đóng lệ phí)")
gA = gateway(X[3] + 20, Y_AP, label="Kết quả\nxét tuyển?")
tA2 = task_box(X[5], Y_AP - 70, "Xác nhận nhập học\n(trong 4 tuần)")
eA_ok = end_circle(X[6] + 30, Y_AP - 70, "Nhập học\nthành công")
eA_rej = end_circle(X[5], Y_AP + 70, "Bị từ chối")

arrow(sA[0] + sA[2], sA[1], tA1[0] - tA1[2] / 2, Y_AP)
arrow(tA1[0] + tA1[2] / 2, Y_AP, gA[0] - gA[2], Y_AP, label="nộp hồ sơ")
arrow(gA[0], gA[1] - gA[2], tA2[0] - tA2[2] / 2, tA2[1], label="đạt")
arrow(gA[0], gA[1] + gA[2], eA_rej[0] - eA_rej[2], eA_rej[1], label="không đạt")
arrow(tA2[0] + tA2[2] / 2, tA2[1], eA_ok[0] - eA_ok[2], eA_ok[1])

# ---- Phòng Tuyển sinh ----
sAO = start_circle(X[2], Y_AO, "Nhận\nhồ sơ")
tAO1 = task_box(X[3], Y_AO, "Kiểm tra\nhồ sơ")
gAO = gateway(X[4] + 10, Y_AO, label="Hồ sơ\nhợp lệ?")
tAO_req = task_box(X[4] + 10, Y_AO + 100, "Yêu cầu\nbổ sung", h=50)
tAO2 = task_box(X[6] - 20, Y_AO, "Thông báo kết quả\ncho ứng viên")
eAO = end_circle(X[7] - 10, Y_AO, "Đã xử lý\nhồ sơ")

arrow(tA1[0] + 20, tA1[1] + tA1[3] / 2, sAO[0], sAO[1] - sAO[2], dashed=True, color=GREY, label="hồ sơ")
arrow(sAO[0] + sAO[2], sAO[1], tAO1[0] - tAO1[2] / 2, Y_AO)
arrow(tAO1[0] + tAO1[2] / 2, Y_AO, gAO[0] - gAO[2], Y_AO)
arrow(gAO[0], gAO[1] + gAO[2], tAO_req[0], tAO_req[1] - tAO_req[3] / 2, label="thiếu")
arrow(tAO_req[0] - 60, tAO_req[1] - 15, tA1[0] + 10, tA1[1] + tA1[3] / 2 + 30, dashed=True, color=GREY, label="yêu cầu\nbổ sung")
arrow(gAO[0] + gAO[2], gAO[1], X[5] + 40, Y_AO - 90, label="hợp lệ")
arrow(tAO2[0] - 30, tAO2[1] - tAO2[3] / 2, gA[0] + 10, gA[1] + gA[2] + 10, dashed=True, color=GREY, label="kết quả\nxét tuyển")
arrow(tAO2[0] + tAO2[2] / 2, Y_AO, eAO[0] - eAO[2], Y_AO)

# ---- Hội đồng Học thuật ----
sAC = start_circle(X[5] + 40, Y_AC - 90)
d.text((sAC[0] - 45, sAC[1] + 26), "Nhận hồ sơ\nthẩm định", fill=BLACK, font=F_SMALL)
tAC1 = task_box(X[5] + 40, Y_AC, "Thẩm định hồ sơ\n(2-3 thành viên,\ntheo 4 tiêu chí)", h=76)
gAC = gateway(X[6] + 60, Y_AC, label="Đạt tiêu chí\ntuyển sinh?")
tAC2 = task_box(X[7] + 60, Y_AC - 60, "Chấp nhận", w=150, h=44)
tAC3 = task_box(X[7] + 60, Y_AC + 60, "Từ chối", w=150, h=44)

arrow(X[5] + 40, Y_AO + 15, sAC[0], sAC[1] - sAC[2], dashed=True, color=GREY)
arrow(sAC[0], sAC[1] + sAC[2], tAC1[0], tAC1[1] - tAC1[3] / 2)
arrow(tAC1[0] + tAC1[2] / 2, Y_AC, gAC[0] - gAC[2], Y_AC)
arrow(gAC[0], gAC[1] - gAC[2], tAC2[0] - tAC2[2] / 2, tAC2[1], label="đạt")
arrow(gAC[0], gAC[1] + gAC[2], tAC3[0] - tAC3[2] / 2, tAC3[1], label="không đạt")
arrow(tAC2[0] + tAC2[2] / 2, tAC2[1], tAO2[0] - 10, tAO2[1] - tAO2[3] / 2 - 10, dashed=True, color=GREY, label="kết quả\nthẩm định")
arrow(tAC3[0] + tAC3[2] / 2, tAC3[1], tAO2[0] - 10, tAO2[1] + tAO2[3] / 2 + 10, dashed=True, color=GREY)

# ---------- title ----------
title = "Giả thuyết ban đầu: quy trình nhập học sinh viên Newtown University (BPMN)"
bbox = d.textbbox((0, 0), title, font=F_TITLE)
d.text(((W - (bbox[2] - bbox[0])) / 2, 20), title, fill=BLACK, font=F_TITLE)
sub = "Suy từ sơ đồ tổ chức + sơ đồ lớp UML + chính sách tuyển sinh — chưa xác thực qua phỏng vấn"
bbox = d.textbbox((0, 0), sub, font=F_SMALL)
d.text(((W - (bbox[2] - bbox[0])) / 2, 52), sub, fill=GREY, font=F_SMALL)

# ---------- legend ----------
LX, LY = 20, H - 130
d.rectangle([LX, LY, LX + 620, LY + 110], outline=BLACK, width=2, fill=(252, 252, 252))
d.text((LX + 10, LY + 8), "Chú thích:", fill=BLACK, font=F_TASK)
d.line([(LX + 20, LY + 38), (LX + 100, LY + 38)], fill=BLACK, width=2)
d.polygon([(LX + 100, LY + 38), (LX + 92, LY + 34), (LX + 92, LY + 42)], fill=BLACK)
d.text((LX + 110, LY + 30), "Sequence flow (trong cùng pool)", fill=BLACK, font=F_SMALL)
arrow(LX + 20, LY + 62, LX + 100, LY + 62, dashed=True, color=GREY)
d.text((LX + 110, LY + 54), "Message flow (giữa 2 pool khác nhau)", fill=BLACK, font=F_SMALL)
gateway(LX + 400, LY + 40, size=15)
d.text((LX + 425, LY + 32), "XOR gateway", fill=BLACK, font=F_SMALL)
event_circle(LX + 400, LY + 75, r=13, thick=2, fill=(230, 255, 230), color=GREEN)
d.text((LX + 425, LY + 67), "Start / End event", fill=BLACK, font=F_SMALL)

img.save(OUT, "PNG")
print("Saved:", OUT)
