# -*- coding: utf-8 -*-
"""BPMN C4 — Bao hanh, doi tra. Nguon: ho-so-C4.md muc 5 (16 buoc) va muc 6 (11 gateway)."""
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).parent))
from bpmn_lib import Proc, render_png

D = pathlib.Path(__file__).parent
IMG = D.parent / "hinh-xuat"

KH = "Khách hàng"
TN = "NV tiếp nhận bảo hành"
KT = "Kỹ thuật viên / kho"
QL = "Quản lý cửa hàng"
TT = "Trung tâm bảo hành (bên ngoài)"
HT = "Hệ thống bảo hành / ERP"

p = Proc("C4", "C4 — Bảo hành, đổi trả", [KH, TN, KT, QL, TT, HT])

p.add("start", "s1", "Khách mang máy tới,\nnêu yêu cầu", KH, 0)
p.add("task", "t1", "Tiếp nhận và ghi nhận yêu cầu", TN, 1)
p.add("task", "t2", "Tra cứu IMEI, ngày mua, hạn bảo hành", HT, 2)
p.add("gw", "G1", "G1: Máy còn trong hạn bảo hành?", TN, 3)

p.add("task", "t3", "Báo giá sửa chữa thu phí", TN, 4, row=1)
p.add("gw", "G1b", "G1b: Khách đồng ý sửa thu phí?", KH, 5, row=1)
p.add("end", "e1", "Chuyển luồng dịch vụ\nthu phí (ngoài phạm vi)", KH, 6, row=1)
p.add("end", "e2", "Trả máy,\nkết thúc", KH, 6)

p.add("gw", "G2", "G2: Bảo hành hay đổi trả?", TN, 4)
p.add("gw", "G2b", "G2b: Đủ điều kiện đổi trả?", QL, 5)
p.add("task", "t4", "Đổi máy hoặc lập chứng từ hoàn tiền", QL, 6)
p.add("task", "t5", "Kiểm tra ngoại quan và điều kiện", TN, 6, row=1)
p.add("gw", "G3", "G3: Đủ điều kiện bảo hành?", TN, 7)
p.add("task", "t6", "Kiểm tra sơ bộ, phân loại lỗi", KT, 8)
p.add("gw", "G4", "G4: Lỗi thuộc loại nào?", KT, 9)

p.add("gw", "G4b", "G4b: Khách để lại máy theo dõi?", KH, 10, row=1)
p.add("task", "t7", "Xử lý tại chỗ (lỗi phần mềm)", KT, 10)
p.add("gw", "G5", "G5: Xử lý tại chỗ thành công?", KT, 11)
p.add("task", "t8", "Lập phiếu tiếp nhận, giao liên cho khách", TN, 12)
p.add("task", "t9", "Đóng gói và gửi lên trung tâm bảo hành", KT, 13)
p.add("task", "t10", "Kiểm định và xử lý tại trung tâm", TT, 14)
p.add("gw", "G6", "G6: Kết luận của trung tâm?", TT, 15)
p.add("task", "t11", "Xuất máy đổi, thu hồi máy lỗi", KT, 16, row=1)
p.add("task", "t12", "Nhận máy về, đối chiếu kết luận", TN, 16)
p.add("gw", "G7", "G7: Máy nhận về đúng và đạt?", TN, 17)
p.add("task", "t13", "Thông báo và hẹn khách tới nhận", TN, 18)
p.add("task", "t14", "Bàn giao, khách kiểm tra và ký nhận", KH, 19)
p.add("gw", "G8", "G8: Khách đồng ý với kết quả?", KH, 20)
p.add("task", "t15", "Mở khiếu nại, chuyển quản lý xử lý", QL, 21, row=1)
p.add("task", "t16", "Ghi nhận và cập nhật thống kê lỗi → M2", HT, 21)
p.add("end", "e3", "Hồ sơ đóng,\ndữ liệu lỗi về M2", HT, 22)

for a, b, n in [("s1", "t1", ""), ("t1", "t2", ""), ("t2", "G1", ""),
                ("G1", "t3", "hết hạn"), ("t3", "G1b", ""), ("G1b", "e1", "đồng ý"),
                ("G1b", "e2", "không đồng ý"), ("G1", "G2", "còn hạn"),
                ("G2", "G2b", "đổi trả"), ("G2b", "t4", "đủ điều kiện"), ("t4", "t16", ""),
                ("G2b", "t5", "không đủ — chuyển bảo hành"), ("G2", "t5", "bảo hành"),
                ("t5", "G3", ""), ("G3", "t3", "không đủ điều kiện"), ("G3", "t6", "đủ"),
                ("t6", "G4", ""), ("G4", "G4b", "không tái hiện"), ("G4b", "e2", "không để lại"),
                ("G4b", "t8", "để lại"), ("G4", "t7", "lỗi phần mềm"), ("t7", "G5", ""),
                ("G5", "t14", "thành công"), ("G5", "t8", "không thành công"),
                ("G4", "t8", "lỗi phần cứng"), ("t8", "t9", ""), ("t9", "t10", ""),
                ("t10", "G6", ""), ("G6", "t11", "phải đổi máy"), ("t11", "t13", ""),
                ("G6", "t12", "sửa được"), ("G6", "t3", "từ chối bảo hành"),
                ("t12", "G7", ""), ("G7", "t9", "không đạt — gửi lại"), ("G7", "t13", "đạt"),
                ("t13", "t14", ""), ("t14", "G8", ""), ("G8", "t15", "không đồng ý"),
                ("t15", "t16", ""), ("G8", "t16", "đồng ý"), ("t16", "e3", "")]:
    p.flow(a, b, n)

(D / "C4-bao-hanh-doi-tra.bpmn").write_text(p.to_bpmn(), encoding="utf-8")
sz = render_png(p, IMG / "C4-bao-hanh-doi-tra.png", "BPMN C4 — Bảo hành, đổi trả")
print("C4: %d gateway, %d phan tu, %d luong | PNG %s" % (p.n_gateway(), len(p.el), len(p.fl), sz))
