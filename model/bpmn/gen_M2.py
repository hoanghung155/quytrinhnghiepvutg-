# -*- coding: utf-8 -*-
"""BPMN M2 — Quan ly nha cung cap.

LUU Y: ho so M2 thuoc phan Hong Phuc (han 22/08), tai thoi diem dung mo hinh nay
chua co. Mo hinh dung tu bang phan ra 12 quy trinh va logic mua hang pho bien,
CAN DOI CHIEU LAI voi ho so M2 truoc khi khoa mo hinh ngay 30/08.
"""
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).parent))
from bpmn_lib import Proc, render_png

D = pathlib.Path(__file__).parent
IMG = D.parent / "hinh-xuat"

TM = "Bộ phận thu mua"
LD = "Ban lãnh đạo (phê duyệt)"
NCC = "Nhà cung cấp (bên ngoài)"
QC = "Bộ phận chất lượng / kho"
HT = "Hệ thống ERP"

p = Proc("M2", "M2 — Quản lý nhà cung cấp", [TM, LD, NCC, QC, HT])

p.add("start", "s1", "Nhu cầu nhập hàng (M1)\nhoặc kỳ đánh giá định kỳ", TM, 0)
p.add("gw", "G1", "G1: Loại yêu cầu?", TM, 1)

p.add("task", "t1", "Lập danh sách NCC tiềm năng", TM, 2)
p.add("task", "t2", "Gửi yêu cầu báo giá (RFQ)", TM, 3)
p.add("task", "t3", "Gửi hồ sơ năng lực và báo giá", NCC, 4)
p.add("gw", "G2", "G2: Hồ sơ đủ điều kiện dự thầu?", TM, 5)
p.add("end", "e1", "Loại NCC khỏi\nvòng xét", TM, 5, row=1)
p.add("task", "t4", "So sánh và chấm điểm NCC", TM, 6)
p.add("gw", "G3", "G3: Cần thẩm định năng lực tại chỗ?", TM, 7)
p.add("task", "t5", "Thẩm định năng lực tại chỗ", QC, 8)

p.add("gw", "G4", "G4: Giá trị hợp đồng vượt hạn mức?", TM, 9)
p.add("task", "t6", "Trình phê duyệt cấp cao", LD, 10)
p.add("gw", "G5", "G5: Ban lãnh đạo duyệt?", LD, 11)
p.add("end", "e2", "Không duyệt,\nđàm phán lại hoặc dừng", LD, 11, row=1)
p.add("task", "t7", "Đàm phán điều khoản và ký hợp đồng", TM, 12)
p.add("task", "t8", "Phát hành đơn đặt hàng (PO)", HT, 13)
p.add("gw", "G6", "G6: NCC xác nhận PO đúng hạn?", NCC, 14)
p.add("task", "t9", "Nhắc và xử lý PO quá hạn xác nhận", TM, 15, row=1)
p.add("task", "t10", "Giao hàng theo PO", NCC, 15)
p.add("task", "t11", "Kiểm tra chất lượng và số lượng", QC, 16)
p.add("gw", "G7", "G7: Lô hàng đạt yêu cầu?", QC, 17)
p.add("task", "t12", "Lập biên bản và trả hàng / khiếu nại", QC, 18, row=1)
p.add("task", "t13", "Nhập kho (M3) và ghi nhận công nợ (S4)", HT, 18)

p.add("gw", "G8", "G8: Đến kỳ đánh giá định kỳ NCC?", TM, 19)
p.add("task", "t14", "Đánh giá NCC (kèm tỷ lệ lỗi từ C4)", TM, 20)
p.add("gw", "G9", "G9: Kết quả đánh giá?", TM, 21)
p.add("task", "t15", "Cảnh báo và yêu cầu khắc phục", NCC, 22, row=1)
p.add("end", "e3", "Giữ NCC trong\ndanh sách", TM, 22)
p.add("end", "e4", "Loại NCC khỏi\ndanh sách", TM, 22, row=1)
p.add("end", "e5", "Kết thúc chu kỳ\nnhập hàng", HT, 20)

for a, b, n in [("s1", "G1", ""), ("G1", "t1", "tìm NCC mới"), ("G1", "t8", "NCC hiện có"),
                ("G1", "t14", "đánh giá định kỳ"),
                ("t1", "t2", ""), ("t2", "t3", ""), ("t3", "G2", ""),
                ("G2", "e1", "không đủ"), ("G2", "t4", "đủ"), ("t4", "G3", ""),
                ("G3", "t5", "cần"), ("t5", "G4", ""), ("G3", "G4", "không cần"),
                ("G4", "t6", "vượt hạn mức"), ("t6", "G5", ""), ("G5", "e2", "không duyệt"),
                ("G5", "t7", "duyệt"), ("G4", "t7", "trong hạn mức"),
                ("t7", "t8", ""), ("t8", "G6", ""), ("G6", "t9", "quá hạn"),
                ("t9", "t10", ""), ("G6", "t10", "xác nhận"), ("t10", "t11", ""),
                ("t11", "G7", ""), ("G7", "t12", "không đạt"), ("t12", "t10", "giao lại"),
                ("G7", "t13", "đạt"), ("t13", "G8", ""), ("G8", "e5", "chưa tới kỳ"),
                ("G8", "t14", "tới kỳ"), ("t14", "G9", ""), ("G9", "e3", "đạt — giữ"),
                ("G9", "t15", "cảnh báo"), ("G9", "e4", "loại")]:
    p.flow(a, b, n)

(D / "M2-quan-ly-nha-cung-cap.bpmn").write_text(p.to_bpmn(), encoding="utf-8")
sz = render_png(p, IMG / "M2-quan-ly-nha-cung-cap.png", "BPMN M2 — Quản lý nhà cung cấp")
print("M2: %d gateway, %d phan tu, %d luong | PNG %s" % (p.n_gateway(), len(p.el), len(p.fl), sz))
