# -*- coding: utf-8 -*-
"""BPMN C3 — Ban tra gop. Nguon: ho-so-C3.md muc 5 (15 buoc) va muc 6 (10 gateway)."""
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).parent))
from bpmn_lib import Proc, render_png

D = pathlib.Path(__file__).parent
IMG = D.parent / "hinh-xuat"

KH = "Khách hàng"
TV = "Nhân viên tư vấn trả góp"
TN = "Nhân viên thu ngân / kho"
CT = "Công ty tài chính (bên ngoài)"
HT = "Hệ thống POS / ERP / cổng trả góp"

p = Proc("C3", "C3 — Bán trả góp", [KH, TV, TN, CT, HT])

p.add("start", "s1", "Khách chọn\nhình thức trả góp", KH, 0)
p.add("task", "t1", "Tiếp nhận yêu cầu trả góp", TV, 1)
p.add("task", "t2", "Kiểm tra điều kiện sơ bộ", TV, 2)
p.add("gw", "G1", "G1: Đủ điều kiện sơ bộ?", TV, 3)
p.add("end", "e1", "Chuyển trả thẳng (C1)\nhoặc khách rời đi", KH, 3)

p.add("task", "t3", "Tư vấn và so sánh các gói", TV, 4)
p.add("gw", "G2", "G2: Chọn bên cấp tín dụng nào?", TV, 5)
p.add("task", "t4", "Thu thập và kiểm tra giấy tờ", TV, 6)
p.add("gw", "G3", "G3: Hồ sơ đủ giấy tờ?", TV, 7)
p.add("task", "t5", "Chụp và nhập hồ sơ lên cổng", TV, 8)
p.add("task", "t6", "Thẩm định tín dụng", CT, 9)
p.add("gw", "G4", "G4: Kết quả thẩm định?", CT, 10)

p.add("task", "t7", "Bổ sung hồ sơ theo yêu cầu", KH, 11)
p.add("gw", "G5", "G5: Hồ sơ bổ sung được chấp nhận?", CT, 12)
p.add("gw", "G4b", "G4b: Khách chuyển sang trả thẳng?", KH, 13)
p.add("end", "e2", "Quay về C1\nhoặc kết thúc", KH, 14)

p.add("task", "t8", "Xác nhận điều khoản và trả trước", TV, 13)
p.add("gw", "G6", "G6: Khách đồng ý điều khoản?", KH, 14)
p.add("end", "e3", "Khách hủy,\nkết thúc", KH, 15)
p.add("task", "t9", "Thu khoản trả trước", TN, 15)
p.add("gw", "G7", "G7: Trả trước đã thu đủ?", TN, 16)
p.add("gw", "G8", "G8: Sản phẩm còn tồn tại cửa hàng?", HT, 17)
p.add("task", "t10", "Điều chuyển hàng (M3)", TN, 18, row=1)
p.add("task", "t11", "Ký hợp đồng trả góp", CT, 18)
p.add("task", "t12", "Lập đơn hàng trên POS", TV, 19)
p.add("task", "t13", "Lấy hàng, khui hộp, kiểm tra", TN, 20)
p.add("gw", "G9", "G9: Máy đạt tình trạng bàn giao?", TN, 21)
p.add("task", "t14", "Xuất hóa đơn, phiếu BH, bàn giao", TN, 22)
p.add("task", "t15", "Đồng bộ ERP và bên cấp tín dụng", HT, 23)
p.add("end", "e4", "Hàng đã giao,\nhợp đồng có hiệu lực", HT, 24)

for a, b, n in [("s1", "t1", ""), ("t1", "t2", ""), ("t2", "G1", ""),
                ("G1", "e1", "không đủ"), ("G1", "t3", "đủ"), ("t3", "G2", ""),
                ("G2", "t4", "đã chọn bên"), ("t4", "G3", ""), ("G3", "t4", "thiếu — bổ sung tại chỗ"),
                ("G3", "t5", "đủ"), ("t5", "t6", ""), ("t6", "G4", ""),
                ("G4", "t7", "yêu cầu bổ sung"), ("t7", "G5", ""), ("G5", "t8", "chấp nhận"),
                ("G5", "G4b", "không"), ("G4", "G4b", "từ chối"), ("G4b", "e2", "quyết định"),
                ("G4", "t8", "duyệt"), ("t8", "G6", ""), ("G6", "e3", "không đồng ý"),
                ("G6", "t9", "đồng ý"), ("t9", "G7", ""), ("G7", "t9", "chưa đủ (E4)"),
                ("G7", "G8", "đủ"), ("G8", "t10", "hết hàng"), ("t10", "t11", ""),
                ("G8", "t11", "còn hàng"), ("t11", "t12", ""), ("t12", "t13", ""),
                ("t13", "G9", ""), ("G9", "t13", "không đạt — đổi máy"),
                ("G9", "t14", "đạt"), ("t14", "t15", ""), ("t15", "e4", "")]:
    p.flow(a, b, n)

(D / "C3-ban-tra-gop.bpmn").write_text(p.to_bpmn(), encoding="utf-8")
sz = render_png(p, IMG / "C3-ban-tra-gop.png", "BPMN C3 — Bán trả góp")
print("C3: %d gateway, %d phan tu, %d luong | PNG %s" % (p.n_gateway(), len(p.el), len(p.fl), sz))
