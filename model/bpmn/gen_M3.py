# -*- coding: utf-8 -*-
"""BPMN M3 — Kho va dieu chuyen.

Ve theo dung bang muc 5 (19 buoc) va muc 6 (12 diem ra quyet dinh) cua ho so M3
o nhanh docs/quy-trinh-quan-ly. Ho so va mo hinh phai khop nhau: sua ho so truoc,
sua mo hinh sau.

Ba nhanh tach tu G1:
  - Nhap hang tu NCC   : G2, G3, G4, G5, G6
  - Dieu chuyen giua CH: G7, G8, G9, G10
  - Kiem ke dinh ky    : G11, G12

Yeu cau do phuc tap: HON 7 gateway. Dem bang dem_gateway.py tren file .bpmn.
"""
import sys
import pathlib

sys.path.insert(0, str(pathlib.Path(__file__).parent))
from bpmn_lib import Proc, render_png

D = pathlib.Path(__file__).parent
IMG = D.parent / "hinh-xuat"

DP = "Bộ phận điều phối tồn kho"
KT = "Kho tổng"
CH = "Cửa hàng (kho cửa hàng)"
VC = "Đơn vị vận chuyển (bên ngoài)"
HT = "Hệ thống ERP"

p = Proc("M3", "M3 — Kho và điều chuyển", [DP, KT, CH, VC, HT])

# ---------------------------------------------------------------- kich hoat
p.add("start", "s1", "Lệnh nhập từ M2 · yêu cầu\nđiều chuyển · tới kỳ kiểm kê", DP, 0)
p.add("gw", "G1", "G1: Loại sự kiện kích hoạt?", DP, 1)

# ------------------------------------------------- nhanh 1: nhap hang tu NCC
p.add("task", "t1", "Nhận hàng từ NCC tại điểm nhận", KT, 2)
p.add("task", "t2", "Đối chiếu chứng từ với PO", KT, 3)
p.add("gw", "G2", "G2: Chứng từ khớp PO?", KT, 4)
p.add("end", "e1", "Trả lại M2\nxử lý sai lệch", KT, 4, row=1)
p.add("task", "t3", "Kiểm đếm thực tế và ghi nhận tình trạng", KT, 5)
p.add("gw", "G3", "G3: Kiểm đếm có đạt?", KT, 6)
p.add("task", "t4", "Lập biên bản, chuyển M2 khiếu nại", KT, 7, row=1)
p.add("end", "e2", "Lô hàng không đạt,\nkhông nhập tồn", KT, 8, row=1)
p.add("task", "t5", "Nhập kho, gán vị trí lưu, cập nhật tồn", HT, 7)
p.add("task", "t6", "Phân bổ hàng về cửa hàng theo kế hoạch", DP, 8)
p.add("gw", "G4", "G4: Về kho tổng hay giao thẳng cửa hàng?", DP, 9)
p.add("gw", "G5", "G5: Cửa hàng đích còn sức chứa?", DP, 10)
p.add("task", "t7", "Phân bổ lại sang cửa hàng khác", DP, 11, row=1)
p.add("task", "t8", "Lập lệnh xuất chuyển và khóa tồn", HT, 11)
p.add("task", "t9", "Đóng gói, bàn giao đơn vị vận chuyển", KT, 12)
p.add("task", "t10", "Vận chuyển tới cửa hàng đích", VC, 13)
p.add("task", "t11", "Cửa hàng nhận, kiểm đếm, xác nhận", CH, 14)
p.add("gw", "G6", "G6: Xác nhận có khớp lệnh xuất?", CH, 15)
p.add("task", "t12", "Lập biên bản thiếu hụt vận chuyển", CH, 16, row=1)
p.add("end", "e3", "Chờ xử lý với\nđơn vị vận chuyển", CH, 17, row=1)
p.add("task", "t13", "Cập nhật tồn khả dụng tại cửa hàng", HT, 16)
p.add("end", "e4", "Hàng sẵn sàng bán\n(C1, C2, C3)", HT, 17)

# --------------------------------------- nhanh 2: dieu chuyen giua cua hang
# Nhanh 2 bat dau tu cot 12: lane DP da trong tu cot 12 tro di (nhanh 1 dung
# DP toi cot 11), nen xep lai vao day thay vi noi tiep sau nhanh 1 — bot ~1100px
# chieu ngang ma khong gay chong lan.
p.add("task", "t14", "Tiếp nhận yêu cầu điều chuyển từ cửa hàng", DP, 12)
p.add("gw", "G7", "G7: Hàng gấp cho đơn đã chốt?", DP, 13)
p.add("task", "t15", "Xếp vào lịch điều chuyển định kỳ", DP, 14, row=1)
p.add("task", "t16", "Dò tìm cửa hàng nguồn còn tồn khả dụng", HT, 14)
p.add("gw", "G8", "G8: Có cửa hàng nguồn khả dụng?", DP, 15)
p.add("end", "e5", "Từ chối yêu cầu,\nbáo cửa hàng và M1", DP, 15, row=1)
p.add("gw", "G9", "G9: Giá trị vượt ngưỡng phải duyệt?", DP, 16)
p.add("task", "t17", "Trình cấp trên duyệt điều chuyển", DP, 17, row=1)
p.add("gw", "G10", "G10: Cấp duyệt có chấp thuận?", DP, 18)
p.add("end", "e6", "Không duyệt,\nphản hồi lý do", DP, 18, row=1)
p.add("task", "t18", "Xuất chuyển từ cửa hàng nguồn", CH, 19)
p.add("task", "t19", "Vận chuyển giữa hai cửa hàng", VC, 20)
p.add("task", "t20", "Cửa hàng đích nhận và xác nhận", CH, 21)
p.add("end", "e7", "Hàng về đúng cửa hàng,\ntồn đã cập nhật", HT, 22)

# ---------------------------------------------- nhanh 3: kiem ke dinh ky
p.add("task", "t21", "Thực hiện kiểm kê theo lịch", CH, 23)
p.add("gw", "G11", "G11: Có chênh lệch tồn?", CH, 24)
p.add("task", "t22", "Đối chiếu và xác định mức chênh lệch", DP, 25)
p.add("gw", "G12", "G12: Chênh vượt ngưỡng lập biên bản?", DP, 26)
p.add("task", "t23", "Điều chỉnh tồn trực tiếp", HT, 27, row=1)
p.add("task", "t24", "Lập biên bản chênh lệch, truy nguyên nhân", DP, 27)
p.add("task", "t25", "Điều chỉnh tồn hệ thống", HT, 28)
p.add("task", "t26", "Tổng hợp cảnh báo tồn ứ và tồn thiếu", DP, 29)
p.add("end", "e8", "Tồn hệ thống khớp tồn\nthực tế · cảnh báo → M1", DP, 30)

FLOWS = [
    ("s1", "G1", ""),
    ("G1", "t1", "nhập từ NCC"),
    ("G1", "t14", "điều chuyển"),
    ("G1", "t21", "kiểm kê"),
    # nhanh nhap
    ("t1", "t2", ""), ("t2", "G2", ""),
    ("G2", "e1", "lệch"), ("G2", "t3", "khớp"),
    ("t3", "G3", ""),
    ("G3", "t4", "không đạt"), ("t4", "e2", ""),
    ("G3", "t5", "đạt"),
    ("t5", "t6", ""), ("t6", "G4", ""),
    ("G4", "G5", "về kho tổng"),
    ("G4", "t10", "giao thẳng cửa hàng"),
    ("G5", "t7", "hết sức chứa"), ("t7", "G5", "phân bổ lại"),
    ("G5", "t8", "còn sức chứa"),
    ("t8", "t9", ""), ("t9", "t10", ""), ("t10", "t11", ""), ("t11", "G6", ""),
    ("G6", "t12", "lệch"), ("t12", "e3", ""),
    ("G6", "t13", "khớp"), ("t13", "e4", ""),
    # nhanh dieu chuyen
    ("t14", "G7", ""),
    ("G7", "t15", "thường"), ("t15", "t16", ""),
    ("G7", "t16", "gấp — ưu tiên"),
    ("t16", "G8", ""),
    ("G8", "e5", "không có nguồn"),
    ("G8", "G9", "có nguồn"),
    ("G9", "t17", "vượt ngưỡng"), ("t17", "G10", ""),
    ("G10", "e6", "không duyệt"), ("G10", "t18", "duyệt"),
    ("G9", "t18", "trong ngưỡng"),
    ("t18", "t19", ""), ("t19", "t20", ""), ("t20", "e7", ""),
    # nhanh kiem ke
    ("t21", "G11", ""),
    ("G11", "t26", "không chênh"),
    ("G11", "t22", "có chênh"),
    ("t22", "G12", ""),
    ("G12", "t23", "trong ngưỡng"), ("t23", "t26", ""),
    ("G12", "t24", "vượt ngưỡng"),
    ("t24", "t25", ""), ("t25", "t26", ""), ("t26", "e8", ""),
]
for a, b, n in FLOWS:
    p.flow(a, b, n)

(D / "M3-kho-va-dieu-chuyen.bpmn").write_text(p.to_bpmn(), encoding="utf-8")
sz = render_png(p, IMG / "M3-kho-va-dieu-chuyen.png", "BPMN M3 — Kho và điều chuyển")
print("M3: %d gateway, %d phan tu, %d luong | PNG %s"
      % (p.n_gateway(), len(p.el), len(p.fl), sz))
