# -*- coding: utf-8 -*-
"""Sinh diagram.png cho quy trình mua hàng Shopee.

Layout kiểu BPMN swimlane ngang: 4 pool xếp dọc (Buyer / Shopee / Seller /
Shipper), pool phụ Payment Gateway vẽ như collapsed pool ở góc.

Không dựng render BPMN thật (không có mmdc/graphviz local); chỉ vẽ hình
chữ nhật + diamond + đường mũi tên bằng PIL. Mục tiêu: thầy đọc được luồng
theo pool, phân biệt task / gateway / event / message flow.
"""
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

OUT = Path(__file__).parent / "diagram.png"

# ---------- canvas ----------
W, H = 2100, 1200
BG = (255, 255, 255)
BLACK = (0, 0, 0)
GREY = (120, 120, 120)
GREEN = (0, 140, 0)
RED = (180, 30, 30)
YELLOW_FILL = (255, 245, 200)
BLUE_FILL = (220, 235, 255)
LIGHT_GREY = (245, 245, 245)

img = Image.new("RGB", (W, H), BG)
d = ImageDraw.Draw(img)

# ---------- fonts ----------
def _font(size, bold=False):
    candidates = [
        "/System/Library/Fonts/Supplemental/Arial Bold.ttf" if bold else "/System/Library/Fonts/Supplemental/Arial.ttf",
        "/System/Library/Fonts/Helvetica.ttc",
        "/System/Library/Fonts/Supplemental/Times New Roman.ttf",
    ]
    for p in candidates:
        try:
            return ImageFont.truetype(p, size)
        except Exception:
            continue
    return ImageFont.load_default()

F_POOL = _font(20, bold=True)
F_TASK = _font(15, bold=True)
F_SMALL = _font(13)
F_LABEL = _font(12)

# ---------- pool bands ----------
POOL_LABEL_W = 110
POOL_LEFT = 20
POOL_RIGHT = W - 20
POOLS = [
    ("Buyer",             80,  240,  BLUE_FILL),
    ("Shopee marketplace", 240, 480, YELLOW_FILL),
    ("Seller",            480, 640,  BLUE_FILL),
    ("Shipper",           640, 800,  YELLOW_FILL),
]

for label, y1, y2, fill in POOLS:
    # outer rectangle
    d.rectangle([POOL_LEFT, y1, POOL_RIGHT, y2], outline=BLACK, width=2, fill=fill)
    # label strip
    d.rectangle([POOL_LEFT, y1, POOL_LEFT + POOL_LABEL_W, y2], outline=BLACK, width=2, fill=LIGHT_GREY)
    # rotated pool label (draw plain, rotated via temp image)
    tmp = Image.new("RGBA", (y2 - y1, POOL_LABEL_W), (0, 0, 0, 0))
    dt = ImageDraw.Draw(tmp)
    bbox = dt.textbbox((0, 0), label, font=F_POOL)
    tw, th = bbox[2] - bbox[0], bbox[3] - bbox[1]
    dt.text(((y2 - y1 - tw) / 2, (POOL_LABEL_W - th) / 2 - 4), label, fill=BLACK, font=F_POOL)
    tmp = tmp.rotate(90, expand=True)
    img.paste(tmp, (POOL_LEFT + 2, y1 + 2), tmp)

# Payment gateway collapsed pool (top-right, black box)
PG_X, PG_Y, PG_W, PG_H = W - 260, 20, 240, 50
d.rectangle([PG_X, PG_Y, PG_X + PG_W, PG_Y + PG_H], outline=BLACK, width=2, fill=LIGHT_GREY)
bbox = d.textbbox((0, 0), "Payment gateway (black box)", font=F_TASK)
tw = bbox[2] - bbox[0]
d.text((PG_X + (PG_W - tw) / 2, PG_Y + 15), "Payment gateway (black box)", fill=BLACK, font=F_TASK)

# ---------- helper shapes ----------
def event_circle(cx, cy, r=22, thick=2, fill=(255, 255, 255), color=BLACK, label=None, label_pos="below"):
    d.ellipse([cx - r, cy - r, cx + r, cy + r], outline=color, width=thick, fill=fill)
    if label:
        bbox = d.textbbox((0, 0), label, font=F_LABEL)
        tw, th = bbox[2] - bbox[0], bbox[3] - bbox[1]
        if label_pos == "below":
            d.text((cx - tw / 2, cy + r + 4), label, fill=BLACK, font=F_LABEL)
        elif label_pos == "above":
            d.text((cx - tw / 2, cy - r - th - 4), label, fill=BLACK, font=F_LABEL)
    return (cx, cy, r)

def end_circle(cx, cy, label=None):
    return event_circle(cx, cy, r=22, thick=4, fill=(255, 255, 255), color=BLACK, label=label)

def start_circle(cx, cy, label=None):
    return event_circle(cx, cy, r=22, thick=2, fill=(230, 255, 230), color=GREEN, label=label)

def task_box(cx, cy, text, w=150, h=60, fill=(255, 255, 255)):
    x1, y1 = cx - w / 2, cy - h / 2
    x2, y2 = cx + w / 2, cy + h / 2
    d.rectangle([x1, y1, x2, y2], outline=BLACK, width=2, fill=fill)
    lines = text.split("\n")
    total_h = len(lines) * 18
    for i, ln in enumerate(lines):
        bbox = d.textbbox((0, 0), ln, font=F_TASK)
        tw = bbox[2] - bbox[0]
        d.text((cx - tw / 2, cy - total_h / 2 + i * 18), ln, fill=BLACK, font=F_TASK)
    return (cx, cy, w, h)

def gateway_diamond(cx, cy, symbol="X", size=32, label=None, label_pos="above"):
    pts = [(cx, cy - size), (cx + size, cy), (cx, cy + size), (cx - size, cy)]
    d.polygon(pts, outline=BLACK, fill=(255, 255, 255))
    # redraw outline thicker
    d.line([pts[0], pts[1], pts[2], pts[3], pts[0]], fill=BLACK, width=2)
    bbox = d.textbbox((0, 0), symbol, font=F_TASK)
    tw, th = bbox[2] - bbox[0], bbox[3] - bbox[1]
    d.text((cx - tw / 2, cy - th / 2 - 3), symbol, fill=BLACK, font=F_TASK)
    if label:
        bbox = d.textbbox((0, 0), label, font=F_LABEL)
        tw, th = bbox[2] - bbox[0], bbox[3] - bbox[1]
        if label_pos == "above":
            d.text((cx - tw / 2, cy - size - th - 4), label, fill=BLACK, font=F_LABEL)
        else:
            d.text((cx - tw / 2, cy + size + 4), label, fill=BLACK, font=F_LABEL)
    return (cx, cy, size)

def arrow(x1, y1, x2, y2, dashed=False, color=BLACK, label=None, thick=2):
    if dashed:
        # draw dashed
        import math
        dx, dy = x2 - x1, y2 - y1
        length = math.hypot(dx, dy)
        segs = max(1, int(length / 12))
        ux, uy = dx / length, dy / length
        for i in range(segs):
            if i % 2 == 0:
                sx = x1 + ux * i * 12
                sy = y1 + uy * i * 12
                ex = x1 + ux * min((i + 1) * 12, length)
                ey = y1 + uy * min((i + 1) * 12, length)
                d.line([(sx, sy), (ex, ey)], fill=color, width=thick)
    else:
        d.line([(x1, y1), (x2, y2)], fill=color, width=thick)
    # arrowhead
    import math
    ang = math.atan2(y2 - y1, x2 - x1)
    ah = 10
    p1 = (x2 - ah * math.cos(ang - math.pi / 6), y2 - ah * math.sin(ang - math.pi / 6))
    p2 = (x2 - ah * math.cos(ang + math.pi / 6), y2 - ah * math.sin(ang + math.pi / 6))
    d.polygon([(x2, y2), p1, p2], fill=color)
    if label:
        mx, my = (x1 + x2) / 2, (y1 + y2) / 2
        bbox = d.textbbox((0, 0), label, font=F_LABEL)
        tw, th = bbox[2] - bbox[0], bbox[3] - bbox[1]
        # small white background for readability
        d.rectangle([mx - tw / 2 - 3, my - th / 2 - 1, mx + tw / 2 + 3, my + th / 2 + 1], fill=(255, 255, 255))
        d.text((mx - tw / 2, my - th / 2), label, fill=color, font=F_LABEL)

# ---------- coordinate baseline (X for each column) ----------
COL_LEFT = POOL_LEFT + POOL_LABEL_W + 30
# X positions for main flow (Buyer row uses many)
X = [COL_LEFT + i * 150 for i in range(13)]

# Y centers for each pool row
Y_BUYER = 160
Y_SHOPEE = 360
Y_SELLER = 560
Y_SHIPPER = 720

# ============= BUYER POOL =============
# Start event
sB = start_circle(X[0], Y_BUYER, label="Nhu cầu\nmua hàng")
# Task: Search product
tB1 = task_box(X[1], Y_BUYER, "Search\nproduct")
# Task: View + compare
tB2 = task_box(X[2], Y_BUYER, "Compare +\nread reviews")
# Task: Add to cart
tB3 = task_box(X[3], Y_BUYER, "Add\nto cart")
# Task: Checkout (chọn address, voucher, payment method)
tB4 = task_box(X[4], Y_BUYER, "Checkout &\npick payment")
# XOR gateway 1: online payment or COD
gB1 = gateway_diamond(X[5], Y_BUYER, symbol="×", label="Payment\nmethod?")
# Path online: Pay online (send to payment gateway)
tB5a = task_box(X[6], Y_BUYER - 55, "Pay online", h=45)
# Path COD: (no task, just wait — jumps to receive)
# XOR-join before wait
gB2 = gateway_diamond(X[7], Y_BUYER, symbol="×")
# Task: Wait for delivery (intermediate wait)
tB6 = task_box(X[8], Y_BUYER, "Wait for\ndelivery")
# Task: Receive & inspect
tB7 = task_box(X[9], Y_BUYER, "Receive &\ninspect item")
# XOR gateway 2: satisfied?
gB3 = gateway_diamond(X[10], Y_BUYER, symbol="×", label="Satisfied?")
# Path yes: Confirm receipt
tB8y = task_box(X[11], Y_BUYER - 55, "Confirm\nreceipt", h=45)
# Path no: Request return
tB8n = task_box(X[11], Y_BUYER + 55, "Request\nreturn", h=45)
# End events
eB_ok = end_circle(X[12] - 30, Y_BUYER - 55, label="Order\nfulfilled")
eB_ret = end_circle(X[12] - 30, Y_BUYER + 55, label="Order\nreturned")

# arrows in Buyer pool
arrow(sB[0] + sB[2], sB[1], tB1[0] - tB1[2] / 2, Y_BUYER)
arrow(tB1[0] + tB1[2] / 2, Y_BUYER, tB2[0] - tB2[2] / 2, Y_BUYER)
arrow(tB2[0] + tB2[2] / 2, Y_BUYER, tB3[0] - tB3[2] / 2, Y_BUYER)
arrow(tB3[0] + tB3[2] / 2, Y_BUYER, tB4[0] - tB4[2] / 2, Y_BUYER)
arrow(tB4[0] + tB4[2] / 2, Y_BUYER, gB1[0] - gB1[2], Y_BUYER)
# gB1 split
arrow(gB1[0], gB1[1] - gB1[2], tB5a[0], tB5a[1] + tB5a[3] / 2, label="online")
arrow(gB1[0] + gB1[2], gB1[1], gB2[0] - gB2[2], gB2[1], label="COD")
arrow(tB5a[0] + tB5a[2] / 2, tB5a[1], gB2[0], gB2[1] - gB2[2])
# gB2 join → wait
arrow(gB2[0] + gB2[2], gB2[1], tB6[0] - tB6[2] / 2, Y_BUYER)
arrow(tB6[0] + tB6[2] / 2, Y_BUYER, tB7[0] - tB7[2] / 2, Y_BUYER)
arrow(tB7[0] + tB7[2] / 2, Y_BUYER, gB3[0] - gB3[2], Y_BUYER)
# gB3 split
arrow(gB3[0], gB3[1] - gB3[2], tB8y[0], tB8y[1] + tB8y[3] / 2, label="yes")
arrow(gB3[0], gB3[1] + gB3[2], tB8n[0], tB8n[1] - tB8n[3] / 2, label="no")
arrow(tB8y[0] + tB8y[2] / 2, tB8y[1], eB_ok[0] - eB_ok[2], eB_ok[1])
arrow(tB8n[0] + tB8n[2] / 2, tB8n[1], eB_ret[0] - eB_ret[2], eB_ret[1])

# ============= SHOPEE POOL =============
# Task: Validate order + place hold
sS_start = start_circle(X[4] - 60, Y_SHOPEE - 40, label="Order\nreceived")
tS1 = task_box(X[5], Y_SHOPEE - 40, "Validate\norder")
# AND-split: fanout notify seller / hold payment
gS1 = gateway_diamond(X[6] - 40, Y_SHOPEE - 40, symbol="+")
# Task: Notify seller (upward branch)
tS2 = task_box(X[6] + 90, Y_SHOPEE - 60, "Route order\nto seller", w=140, h=45)
# Task: Hold buyer money (downward branch)
tS3 = task_box(X[6] + 90, Y_SHOPEE + 30, "Hold buyer\npayment (escrow)", w=180, h=45)
# AND-join
gS2 = gateway_diamond(X[8] - 20, Y_SHOPEE - 40, symbol="+")
# Task: Track shipping
tS4 = task_box(X[9] - 15, Y_SHOPEE - 40, "Track\nshipping")
# XOR: buyer confirms or auto-confirm
gS3 = gateway_diamond(X[10] - 20, Y_SHOPEE - 40, symbol="×", label="Buyer\nreaction?")
# Task: Release payment to seller
tS5a = task_box(X[11] - 25, Y_SHOPEE - 90, "Release payment\nto seller", w=170, h=45)
# Task: Freeze payment + handle return
tS5b = task_box(X[11] - 25, Y_SHOPEE + 10, "Freeze payment,\nhandle return", w=170, h=45)
# End events
eS_ok = end_circle(X[12] - 30, Y_SHOPEE - 90, label="Order\nclosed")
eS_ret = end_circle(X[12] - 30, Y_SHOPEE + 10, label="Return\nresolved")

# Sequence flows in Shopee pool
arrow(sS_start[0] + sS_start[2], sS_start[1], tS1[0] - tS1[2] / 2, tS1[1])
arrow(tS1[0] + tS1[2] / 2, tS1[1], gS1[0] - gS1[2], gS1[1])
arrow(gS1[0], gS1[1] - gS1[2], tS2[0] - tS2[2] / 2, tS2[1])
arrow(gS1[0], gS1[1] + gS1[2], tS3[0] - tS3[2] / 2, tS3[1])
arrow(tS2[0] + tS2[2] / 2, tS2[1], gS2[0], gS2[1] - gS2[2])
arrow(tS3[0] + tS3[2] / 2, tS3[1], gS2[0], gS2[1] + gS2[2])
arrow(gS2[0] + gS2[2], gS2[1], tS4[0] - tS4[2] / 2, tS4[1])
arrow(tS4[0] + tS4[2] / 2, tS4[1], gS3[0] - gS3[2], gS3[1])
arrow(gS3[0], gS3[1] - gS3[2], tS5a[0], tS5a[1] + tS5a[3] / 2, label="confirm")
arrow(gS3[0], gS3[1] + gS3[2], tS5b[0], tS5b[1] - tS5b[3] / 2, label="return")
arrow(tS5a[0] + tS5a[2] / 2, tS5a[1], eS_ok[0] - eS_ok[2], eS_ok[1])
arrow(tS5b[0] + tS5b[2] / 2, tS5b[1], eS_ret[0] - eS_ret[2], eS_ret[1])

# ============= SELLER POOL =============
sSel_start = start_circle(X[6] + 60, Y_SELLER - 40, label="Order\nnotified")
gSel1 = gateway_diamond(X[7], Y_SELLER - 40, symbol="×", label="Stock?")
# in-stock branch
tSel1 = task_box(X[8] - 15, Y_SELLER - 75, "Pack & hand\nto shipper", w=170, h=45)
# out-of-stock branch
tSel2 = task_box(X[8] - 15, Y_SELLER + 20, "Cancel order,\nnotify Shopee", w=180, h=45)
eSel_ok = end_circle(X[12] - 30, Y_SELLER - 75, label="Handed\nover")
eSel_cx = end_circle(X[12] - 30, Y_SELLER + 20, label="Order\ncancelled")

arrow(sSel_start[0] + sSel_start[2], sSel_start[1], gSel1[0] - gSel1[2], gSel1[1])
arrow(gSel1[0], gSel1[1] - gSel1[2], tSel1[0], tSel1[1] + tSel1[3] / 2, label="in-stock")
arrow(gSel1[0], gSel1[1] + gSel1[2], tSel2[0], tSel2[1] - tSel2[3] / 2, label="out-of-stock")
arrow(tSel1[0] + tSel1[2] / 2, tSel1[1], eSel_ok[0] - eSel_ok[2], eSel_ok[1])
arrow(tSel2[0] + tSel2[2] / 2, tSel2[1], eSel_cx[0] - eSel_cx[2], eSel_cx[1])

# ============= SHIPPER POOL =============
sShip_start = start_circle(X[8] + 80, Y_SHIPPER - 30, label="Pickup\nready")
tShip1 = task_box(X[9] + 40, Y_SHIPPER - 30, "Pick up\nparcel")
tShip2 = task_box(X[10] + 20, Y_SHIPPER - 30, "Deliver\nto buyer")
eShip = end_circle(X[12] - 30, Y_SHIPPER - 30, label="Delivered")

arrow(sShip_start[0] + sShip_start[2], sShip_start[1], tShip1[0] - tShip1[2] / 2, tShip1[1])
arrow(tShip1[0] + tShip1[2] / 2, tShip1[1], tShip2[0] - tShip2[2] / 2, tShip2[1])
arrow(tShip2[0] + tShip2[2] / 2, tShip2[1], eShip[0] - eShip[2], eShip[1])

# ============= MESSAGE FLOWS (dashed, cross-pool) =============
# Buyer -> Shopee: place order (from checkout to Shopee start)
arrow(tB4[0], tB4[1] + tB4[3] / 2 + 5, sS_start[0], sS_start[1] - sS_start[2], dashed=True, color=GREY, label="place order")
# Buyer -> Payment gateway: Pay online (upward from tB5a)
arrow(tB5a[0], tB5a[1] - tB5a[3] / 2, PG_X + PG_W / 2, PG_Y + PG_H, dashed=True, color=GREY, label="charge card / e-wallet")
# Payment gateway -> Shopee: confirm settlement (down to Shopee "hold" task)
arrow(PG_X + 30, PG_Y + PG_H, tS3[0] - 40, tS3[1] - tS3[3] / 2, dashed=True, color=GREY, label="settlement ok")
# Shopee -> Seller: route order
arrow(tS2[0] + 20, tS2[1] + tS2[3] / 2, sSel_start[0], sSel_start[1] - sSel_start[2], dashed=True, color=GREY, label="order")
# Seller -> Shipper: hand parcel (route from right of tSel1 down to sShip_start)
arrow(tSel1[0] + tSel1[2] / 2 - 10, tSel1[1] + tSel1[3] / 2, sShip_start[0], sShip_start[1] - sShip_start[2], dashed=True, color=GREY, label="parcel")
# Shipper -> Buyer: deliver
arrow(tShip2[0], tShip2[1] - tShip2[3] / 2 - 5, tB6[0], tB6[1] + tB6[3] / 2, dashed=True, color=GREY, label="deliver")
# Shipper -> Shopee: delivered signal
arrow(eShip[0], eShip[1] - eShip[2], tS4[0] + 20, tS4[1] + tS4[3] / 2, dashed=True, color=GREY, label="delivered")
# Buyer -> Shopee: confirm receipt or return
arrow(tB8y[0] - 30, tB8y[1] + tB8y[3] / 2, gS3[0] - 10, gS3[1] - gS3[2] - 5, dashed=True, color=GREY, label="confirm")
arrow(tB8n[0] - 30, tB8n[1] + tB8n[3] / 2, gS3[0] + 10, gS3[1] + gS3[2] + 5, dashed=True, color=GREY, label="return req.")
# Shopee -> Payment gateway: payout to seller (via PG). Route from top-left of tS5a
# to avoid overlapping the "Order fulfilled" end-event label on Buyer row.
arrow(tS5a[0] - tS5a[2] / 2 + 20, tS5a[1] - tS5a[3] / 2, PG_X + PG_W - 90, PG_Y + PG_H, dashed=True, color=GREY, label="payout")

# ---------- title ----------
title = "Quy trinh mua hang tren san TMDT (Shopee) — BPMN collaboration"
bbox = d.textbbox((0, 0), title, font=F_POOL)
tw = bbox[2] - bbox[0]
d.text(((W - tw) / 2, 25), title, fill=BLACK, font=F_POOL)

# ---------- legend ----------
LEG_X, LEG_Y = 20, H - 130
d.rectangle([LEG_X, LEG_Y, LEG_X + 620, LEG_Y + 110], outline=BLACK, width=2, fill=(252, 252, 252))
d.text((LEG_X + 10, LEG_Y + 8), "Chu thich (Legend):", fill=BLACK, font=F_TASK)
# solid arrow
d.line([(LEG_X + 20, LEG_Y + 38), (LEG_X + 100, LEG_Y + 38)], fill=BLACK, width=2)
d.polygon([(LEG_X + 100, LEG_Y + 38), (LEG_X + 92, LEG_Y + 34), (LEG_X + 92, LEG_Y + 42)], fill=BLACK)
d.text((LEG_X + 110, LEG_Y + 30), "Sequence flow (trong cung pool)", fill=BLACK, font=F_SMALL)
# dashed arrow
arrow(LEG_X + 20, LEG_Y + 62, LEG_X + 100, LEG_Y + 62, dashed=True, color=GREY)
d.text((LEG_X + 110, LEG_Y + 54), "Message flow (giua 2 pool khac nhau)", fill=BLACK, font=F_SMALL)
# gateway
gateway_diamond(LEG_X + 350, LEG_Y + 40, symbol="×", size=15)
d.text((LEG_X + 375, LEG_Y + 32), "XOR gateway", fill=BLACK, font=F_SMALL)
gateway_diamond(LEG_X + 350, LEG_Y + 72, symbol="+", size=15)
d.text((LEG_X + 375, LEG_Y + 64), "AND gateway", fill=BLACK, font=F_SMALL)
# events
event_circle(LEG_X + 510, LEG_Y + 40, r=15, thick=2, fill=(230, 255, 230), color=GREEN)
d.text((LEG_X + 535, LEG_Y + 32), "Start event", fill=BLACK, font=F_SMALL)
event_circle(LEG_X + 510, LEG_Y + 72, r=15, thick=4)
d.text((LEG_X + 535, LEG_Y + 64), "End event", fill=BLACK, font=F_SMALL)

img.save(OUT, "PNG")
print(f"Saved: {OUT}")
