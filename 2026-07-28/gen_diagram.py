# -*- coding: utf-8 -*-
"""Sinh diagram.png — mo hinh BPMN CHI TIET quy trinh nhap hoc Newtown
University, tong hop tu 3 phong van (Mary Adams, Louise Smith, Peter
Capello) + quan sat truc tiep vai ung vien. 3 pool: Applicant / Student
Admission Officer / Academic Committee (khong co Enrollment Office).
Ve bang PIL, tieng Viet co dau.
"""
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont
import math

OUT = Path(__file__).parent / "diagram.png"

W, H = 2650, 1300
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
F_TASK = _font(13, bold=True)
F_SMALL = _font(11)

POOL_LABEL_W = 120
POOL_LEFT, POOL_RIGHT = 20, W - 20
POOLS = [
    ("Applicant", 90, 340, BLUE_FILL),
    ("Student Admission Officer", 340, 730, YELLOW_FILL),
    ("Academic Committee", 730, 1080, PINK_FILL),
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


def event_circle(cx, cy, r=18, thick=2, fill=(255, 255, 255), color=BLACK, label=None, below=True):
    d.ellipse([cx - r, cy - r, cx + r, cy + r], outline=color, width=thick, fill=fill)
    if label:
        for i, ln in enumerate(label.split("\n")):
            bbox = d.textbbox((0, 0), ln, font=F_SMALL)
            tw, th = bbox[2] - bbox[0], bbox[3] - bbox[1]
            y = cy + r + 4 + i * 14 if below else cy - r - 14 * (label.count(chr(10)) + 1 - i) - 4
            d.text((cx - tw / 2, y), ln, fill=BLACK, font=F_SMALL)
    return (cx, cy, r)


def start_circle(cx, cy, label=None, below=True):
    return event_circle(cx, cy, r=18, thick=2, fill=(230, 255, 230), color=GREEN, label=label, below=below)


def end_circle(cx, cy, label=None, below=True):
    return event_circle(cx, cy, r=18, thick=4, fill=(255, 235, 235), color=RED, label=label, below=below)


def task_box(cx, cy, text, w=175, h=58):
    x1, y1, x2, y2 = cx - w / 2, cy - h / 2, cx + w / 2, cy + h / 2
    d.rounded_rectangle([x1, y1, x2, y2], radius=8, outline=BLACK, width=2, fill=(255, 255, 255))
    lines = text.split("\n")
    total_h = len(lines) * 15
    for i, ln in enumerate(lines):
        bbox = d.textbbox((0, 0), ln, font=F_TASK)
        tw = bbox[2] - bbox[0]
        d.text((cx - tw / 2, cy - total_h / 2 + i * 15), ln, fill=BLACK, font=F_TASK)
    return (cx, cy, w, h)


def gateway(cx, cy, size=24, label=None, above=True):
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
            y = cy - size - (len(lines) - i) * 14 - 4 if above else cy + size + 4 + i * 14
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
    ah = 9
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


# ============================================================
# APPLICANT POOL (Y ~ 90-340)
# ============================================================
sA = start_circle(160, 210, "Chuẩn bị hồ sơ\n(bảng điểm, essay,\n2 thư giới thiệu)")
tA1 = task_box(420, 210, "Nộp hồ sơ qua\nWeb portal")
gA = gateway(720, 210, label="Phản hồi từ\nAdmission Officer?")
tA_offer = task_box(1000, 130, "Ký & gửi lại offer\nqua post (≤ 4 tuần)")
eA_rej = end_circle(1000, 290, "Bị từ chối,\nkhông làm gì thêm")
tA_clarify = task_box(950, 210, "Nộp lại hồ sơ đã\ncập nhật (cùng portal)")
eA_ok = end_circle(1260, 130, "Đã gửi offer\nký tên")

arrow(sA[0] + sA[2], sA[1], tA1[0] - tA1[2] / 2, tA1[1])
arrow(tA1[0] + tA1[2] / 2, tA1[1], gA[0] - gA[2], gA[1], label="nộp hồ sơ")
arrow(gA[0], gA[1] - gA[2], tA_offer[0] - tA_offer[2] / 2, tA_offer[1], label="letter of offer\n(post)")
arrow(gA[0], gA[1] + gA[2], eA_rej[0] - eA_rej[2], eA_rej[1], label="rejection letter\n(post)")
arrow(gA[0] + 10, gA[1] + gA[2] - 5, tA_clarify[0] - tA_clarify[2] / 2, tA_clarify[1] + 20, label="request\nclarification (email)")
arrow(tA_clarify[0], tA_clarify[1] - tA_clarify[3] / 2, gA[0] + 15, gA[1] - gA[2] + 5, label="hồ sơ mới")
arrow(tA_offer[0] + tA_offer[2] / 2, tA_offer[1], eA_ok[0] - eA_ok[2], eA_ok[1])

# ============================================================
# STUDENT ADMISSION OFFICER POOL (Y ~ 340-730)
# ============================================================
sAO = start_circle(420, 400, "Nhận hồ sơ")
tAO1 = task_box(650, 400, "Kiểm tra hồ sơ đầy đủ\n(tên, địa chỉ, SĐT, email)")
gAO1 = gateway(880, 400, label="Hồ sơ\nđầy đủ?")
tAO_req = task_box(880, 490, "Gửi yêu cầu bổ sung\n(email)")
tAO2 = task_box(1130, 400, "Chuyển hồ sơ cho\nAcademic Committee\n(hệ thống nội bộ)")
sAO2 = start_circle(1400, 400, "Nhận phản hồi từ\nAcademic Committee")
gAO2 = gateway(1620, 400, label="Phản hồi từ\nAcademic Committee?")
tAO_offer = task_box(1850, 320, "Soạn & gửi thư mời\nqua post")
gAO_deadline = gateway(2080, 320, label="Nhận offer ký tên\ntrong 4 tuần?")
eAO_ok = end_circle(2300, 250, "Hoàn tất\nnhập học")
eAO_expired = end_circle(2300, 390, "Hết hạn, nhường suất\ncho người khác")
tAO_reject = task_box(1850, 500, "Soạn & gửi thư\ntừ chối qua post")
eAO_done = end_circle(2080, 500, "Đã xử lý -\ntừ chối")

arrow(tA1[0], tA1[1] + tA1[3] / 2, sAO[0], sAO[1] - sAO[2], dashed=True, color=GREY, label="hồ sơ (portal)")
arrow(tA_clarify[0], tA_clarify[1] + tA_clarify[3] / 2, sAO[0] + 40, sAO[1] - sAO[2] - 5, dashed=True, color=GREY)
arrow(sAO[0] + sAO[2], sAO[1], tAO1[0] - tAO1[2] / 2, tAO1[1])
arrow(tAO1[0] + tAO1[2] / 2, tAO1[1], gAO1[0] - gAO1[2], gAO1[1])
arrow(gAO1[0], gAO1[1] + gAO1[2], tAO_req[0], tAO_req[1] - tAO_req[3] / 2, label="thiếu")
arrow(tAO_req[0] - 30, tAO_req[1] + tAO_req[3] / 2, tA_clarify[0] - 60, tA_clarify[1] + tA_clarify[3] / 2 + 20,
      dashed=True, color=GREY, label="yêu cầu bổ sung\n(email)")
arrow(gAO1[0] + gAO1[2], gAO1[1], tAO2[0] - tAO2[2] / 2, tAO2[1], label="đầy đủ")
arrow(tAO2[0] + tAO2[2] / 2, tAO2[1], sAO2[0] - sAO2[2] - 40, sAO2[1] + 40, dashed=True, color=GREY,
      label="chuyển hồ sơ")
arrow(sAO2[0] + sAO2[2], sAO2[1], gAO2[0] - gAO2[2], gAO2[1])
arrow(gAO2[0], gAO2[1] - gAO2[2], tAO_offer[0] - tAO_offer[2] / 2, tAO_offer[1], label="acceptance")
arrow(gAO2[0], gAO2[1] + gAO2[2], tAO_reject[0] - tAO_reject[2] / 2, tAO_reject[1], label="rejection")
arrow(tAO_offer[0] + tAO_offer[2] / 2, tAO_offer[1], gAO_deadline[0] - gAO_deadline[2], gAO_deadline[1])
arrow(gAO_deadline[0], gAO_deadline[1] - gAO_deadline[2], eAO_ok[0] - eAO_ok[2], eAO_ok[1], label="có, ≤4 tuần")
arrow(gAO_deadline[0] + 5, gAO_deadline[1] + gAO_deadline[2], eAO_expired[0] - eAO_expired[2], eAO_expired[1] - 10,
      label="quá hạn")
arrow(tAO_reject[0] + tAO_reject[2] / 2, tAO_reject[1], eAO_done[0] - eAO_done[2], eAO_done[1])
# message flows to applicant
arrow(tAO_offer[0] - 20, tAO_offer[1] - tAO_offer[3] / 2, tA_offer[0] - 30, tA_offer[1] + tA_offer[3] / 2,
      dashed=True, color=GREY, label="letter of offer")
arrow(tAO_reject[0] - 20, tAO_reject[1] - tAO_reject[3] / 2 - 5, eA_rej[0], eA_rej[1] + eA_rej[2] + 45,
      dashed=True, color=GREY, label="rejection letter")
arrow(tA_offer[0] + 10, tA_offer[1] + tA_offer[3] / 2, gAO_deadline[0] - 20, gAO_deadline[1] - gAO_deadline[2] - 20,
      dashed=True, color=GREY, label="offer ký tên")

# ============================================================
# ACADEMIC COMMITTEE POOL (Y ~ 730-1080)
# ============================================================
sAC = start_circle(1200, 800, "Nhận hồ sơ")
tAC1 = task_box(1400, 800, "Quy đổi điểm bằng\ntrước (bảng chuẩn)")
gAC1 = gateway(1610, 800, label="Điểm quy đổi\n≥ 70%?")
tAC_rejA = task_box(1610, 900, "Gửi thông báo từ chối\n(điểm dưới 70%)")
tAC2 = task_box(1830, 800, "Kiểm tra đạo văn +\nđọc, chấm bài luận")
tAC3 = task_box(2040, 800, "Đọc 2 thư\ngiới thiệu")
gAC2 = gateway(2240, 800, label="Đủ điều kiện\ntuyển sinh?")
tAC_acc = task_box(2240, 900, "Gửi thông báo\nchấp nhận")
tAC_rejB = task_box(2440, 900, "Gửi thông báo từ chối\n(không đạt vòng cuối)")
tAC_archive = task_box(2340, 1010, "Lưu kết quả đánh giá\n(database)")
eAC = end_circle(2340, 1050 + 30, "Hoàn tất\nthẩm định")

arrow(tAO2[0] + 30, tAO2[1] + tAO2[3] / 2, sAC[0] - 40, sAC[1] - sAC[2] - 5, dashed=True, color=GREY,
      label="hồ sơ hợp lệ")
arrow(sAC[0] + sAC[2], sAC[1], tAC1[0] - tAC1[2] / 2, tAC1[1])
arrow(tAC1[0] + tAC1[2] / 2, tAC1[1], gAC1[0] - gAC1[2], gAC1[1])
arrow(gAC1[0], gAC1[1] + gAC1[2], tAC_rejA[0], tAC_rejA[1] - tAC_rejA[3] / 2, label="dưới 70%")
arrow(gAC1[0] + gAC1[2], gAC1[1], tAC2[0] - tAC2[2] / 2, tAC2[1], label="≥ 70%")
arrow(tAC2[0] + tAC2[2] / 2, tAC2[1], tAC3[0] - tAC3[2] / 2, tAC3[1])
arrow(tAC3[0] + tAC3[2] / 2, tAC3[1], gAC2[0] - gAC2[2], gAC2[1])
arrow(gAC2[0], gAC2[1] + gAC2[2] - 10, tAC_acc[0] - tAC_acc[2] / 2, tAC_acc[1] - 10, label="đạt")
arrow(gAC2[0] + gAC2[2], gAC2[1] + 10, tAC_rejB[0] - tAC_rejB[2] / 2, tAC_rejB[1] - 20, label="không đạt")
arrow(tAC_rejA[0] + 10, tAC_rejA[1] + tAC_rejA[3] / 2, tAC_archive[0] - tAC_archive[2] / 2 - 10,
      tAC_archive[1] - tAC_archive[3] / 2, dashed=False)
arrow(tAC_acc[0] + tAC_acc[2] / 2, tAC_acc[1], tAC_archive[0] - tAC_archive[2] / 2, tAC_archive[1] - 5)
arrow(tAC_rejB[0], tAC_rejB[1] + tAC_rejB[3] / 2, tAC_archive[0] + tAC_archive[2] / 2 - 10, tAC_archive[1] - tAC_archive[3] / 2)
arrow(tAC_archive[0], tAC_archive[1] + tAC_archive[3] / 2, eAC[0] - eAC[2], eAC[1] - eAC[2])
# message flows back to AO
arrow(tAC_rejA[0] + tAC_rejA[2] / 2, tAC_rejA[1], sAO2[0] - 30, sAO2[1] + sAO2[2] + 15, dashed=True, color=GREY,
      label="rejection")
arrow(tAC_acc[0], tAC_acc[1] - tAC_acc[3] / 2, gAO2[0] + 10, gAO2[1] + gAO2[2] + 10, dashed=True, color=GREY,
      label="acceptance")
arrow(tAC_rejB[0], tAC_rejB[1] - tAC_rejB[3] / 2, gAO2[0] + 60, gAO2[1] + gAO2[2] + 40, dashed=True, color=GREY)

# ---------- title ----------
title = "Quy trình nhập học Newtown University — mô hình chi tiết từ phỏng vấn (BPMN)"
bbox = d.textbbox((0, 0), title, font=F_TITLE)
d.text(((W - (bbox[2] - bbox[0])) / 2, 20), title, fill=BLACK, font=F_TITLE)
sub = "Tổng hợp từ phỏng vấn Mary Adams, Louise Smith, Peter Capello + quan sát trực tiếp vai ứng viên"
bbox = d.textbbox((0, 0), sub, font=F_SMALL)
d.text(((W - (bbox[2] - bbox[0])) / 2, 52), sub, fill=GREY, font=F_SMALL)

# ---------- legend ----------
LX, LY = 20, H - 170
d.rectangle([LX, LY, LX + 700, LY + 150], outline=BLACK, width=2, fill=(252, 252, 252))
d.text((LX + 10, LY + 8), "Chú thích:", fill=BLACK, font=F_TASK)
d.line([(LX + 20, LY + 38), (LX + 100, LY + 38)], fill=BLACK, width=2)
d.polygon([(LX + 100, LY + 38), (LX + 92, LY + 34), (LX + 92, LY + 42)], fill=BLACK)
d.text((LX + 110, LY + 30), "Sequence flow (trong cùng pool)", fill=BLACK, font=F_SMALL)
arrow(LX + 20, LY + 62, LX + 100, LY + 62, dashed=True, color=GREY)
d.text((LX + 110, LY + 54), "Message flow (post / email / web portal / hệ thống nội bộ)", fill=BLACK, font=F_SMALL)
gateway(LX + 420, LY + 40, size=13)
d.text((LX + 445, LY + 32), "XOR gateway", fill=BLACK, font=F_SMALL)
event_circle(LX + 420, LY + 75, r=12, thick=2, fill=(230, 255, 230), color=GREEN)
d.text((LX + 445, LY + 67), "Start / End event", fill=BLACK, font=F_SMALL)
d.text((LX + 10, LY + 108), "Ghi chú: hệ thống nội bộ Admission↔Committee đôi khi thất lạc thông điệp (theo P. Capello);", fill=GREY, font=F_SMALL)
d.text((LX + 10, LY + 126), "kết quả khi bài luận bị phát hiện đạo văn chưa được xác nhận rõ trong phỏng vấn.", fill=GREY, font=F_SMALL)

img.save(OUT, "PNG")
print("Saved:", OUT)
