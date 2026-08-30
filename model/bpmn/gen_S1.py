# -*- coding: utf-8 -*-
"""BPMN S1 — Tuyen dung va dao tao.

LUU Y QUAN TRONG — mo hinh nay dung TRUOC khi co ho so S1.

Ho so S1 thuoc phan Thanh Phuc (nhanh docs/quy-trinh-ho-tro), tai thoi diem dung
mo hinh nay CHUA CO. Mo hinh duoc dung tu:
  - bang phan ra 12 quy trinh: S1 kich hoat boi "thieu nhan su, mo cua hang moi",
    ket qua "nhan vien duoc tuyen va dao tao du chuan quay";
  - ly do chon S1 de mo hinh hoa: "nhieu vong sang loc va diem quyet dinh dat/khong dat";
  - lien ket M4 -> S1: quyet dinh mo diem ban keo theo nhu cau nhan su.

CAN DOI CHIEU LAI voi ho so S1 cua Thanh Phuc truoc khi khoa mo hinh ngay 30/08.
Neu ho so cho ket qua khac thi sua ho so truoc, sua mo hinh sau, va ghi vao bien
ban review. Nguoi dung mo hinh (Hong Phuc) khong tu viet ho so thay Thanh Phuc.

Yeu cau do phuc tap: HON 7 gateway. Dem bang dem_gateway.py tren file .bpmn.
"""
import sys
import pathlib

sys.path.insert(0, str(pathlib.Path(__file__).parent))
from bpmn_lib import Proc, render_png

D = pathlib.Path(__file__).parent
IMG = D.parent / "hinh-xuat"

TD = "Bộ phận tuyển dụng"
QL = "Quản lý cửa hàng / quản lý vùng"
UV = "Ứng viên (bên ngoài)"
DT = "Bộ phận đào tạo"
NS = "Hệ thống quản lý nhân sự"

p = Proc("S1", "S1 — Tuyển dụng và đào tạo", [TD, QL, UV, DT, NS])

p.add("start", "s1", "Thiếu nhân sự · mở\ncửa hàng mới (M4)", TD, 0)
p.add("gw", "G1", "G1: Nguồn nội bộ hay tuyển ngoài?", TD, 1)
p.add("task", "t0", "Điều chuyển nhân sự nội bộ giữa cửa hàng", QL, 2, row=1)

p.add("task", "t1", "Xác nhận nhu cầu và chỉ tiêu tuyển", TD, 2)
p.add("gw", "G2", "G2: Chỉ tiêu vượt định biên đã duyệt?", TD, 3)
p.add("task", "t2", "Trình duyệt bổ sung định biên", QL, 4, row=1)
p.add("task", "t3", "Đăng tuyển và tìm nguồn ứng viên", TD, 4)
p.add("task", "t4", "Nộp hồ sơ ứng tuyển", UV, 5)

p.add("gw", "G3", "G3: Hồ sơ đạt sàng lọc?", TD, 6)
p.add("end", "e1", "Hồ sơ không đạt,\ntừ chối", TD, 6, row=1)
p.add("task", "t5", "Phỏng vấn vòng 1 — sàng lọc năng lực", TD, 7)
p.add("gw", "G4", "G4: Vòng 1 có đạt?", TD, 8)
p.add("end", "e2", "Dừng sau vòng 1", TD, 8, row=1)

p.add("task", "t6", "Phỏng vấn vòng 2 với quản lý cửa hàng", QL, 9)
p.add("gw", "G5", "G5: Vòng 2 có đạt?", QL, 10)
p.add("end", "e3", "Đưa vào nguồn\nứng viên dự phòng", QL, 10, row=1)

p.add("task", "t7", "Gửi đề nghị nhận việc", TD, 11)
p.add("gw", "G6", "G6: Ứng viên chấp nhận đề nghị?", UV, 12)
p.add("end", "e4", "Ứng viên từ chối,\nmở lại nguồn tuyển", UV, 12, row=1)

p.add("task", "t8", "Hoàn tất hồ sơ, ký hợp đồng thử việc", NS, 13)
p.add("task", "t9", "Đào tạo hội nhập và nghiệp vụ quầy", DT, 14)
p.add("gw", "G7", "G7: Kiểm tra cuối khóa đạt?", DT, 15)
p.add("gw", "G8", "G8: Đã đào tạo lại lần nào chưa?", DT, 16)
p.add("end", "e5", "Không đạt sau khi\nđã đào tạo lại", DT, 16, row=1)

p.add("task", "t10", "Thực tập tại quầy có người kèm cặp", QL, 17)
p.add("gw", "G9", "G9: Đánh giá kết thúc thử việc đạt?", QL, 18)
p.add("end", "e6", "Không đạt thử việc,\nkhông ký chính thức", QL, 18, row=1)

p.add("task", "t11", "Ký hợp đồng chính thức, cập nhật hệ thống", NS, 19)
p.add("gw", "G10", "G10: Nhân sự cho cửa hàng mới khai trương?", TD, 20)
p.add("task", "t12", "Bố trí theo lịch khai trương (M4)", QL, 21, row=1)
p.add("task", "t13", "Bố trí vào ca làm việc tại cửa hàng", QL, 21)
p.add("end", "e7", "Nhân viên đủ chuẩn quầy,\nsẵn sàng nhận ca", NS, 22)

FLOWS = [
    ("s1", "G1", ""),
    ("G1", "t0", "nội bộ"), ("t0", "t9", "vào thẳng đào tạo"),
    ("G1", "t1", "tuyển ngoài"),
    ("t1", "G2", ""),
    ("G2", "t2", "vượt định biên"), ("t2", "t3", ""),
    ("G2", "t3", "trong định biên"),
    ("t3", "t4", ""), ("t4", "G3", ""),
    ("G3", "e1", "không đạt"), ("G3", "t5", "đạt"),
    ("t5", "G4", ""),
    ("G4", "e2", "không đạt"), ("G4", "t6", "đạt"),
    ("t6", "G5", ""),
    ("G5", "e3", "không đạt"), ("G5", "t7", "đạt"),
    ("t7", "G6", ""),
    ("G6", "e4", "từ chối"), ("G6", "t8", "chấp nhận"),
    ("t8", "t9", ""), ("t9", "G7", ""),
    ("G7", "t10", "đạt"),
    ("G7", "G8", "không đạt"),
    ("G8", "t9", "chưa — đào tạo lại"),
    ("G8", "e5", "đã đào tạo lại"),
    ("t10", "G9", ""),
    ("G9", "e6", "không đạt"), ("G9", "t11", "đạt"),
    ("t11", "G10", ""),
    ("G10", "t12", "cửa hàng mới"), ("t12", "e7", ""),
    ("G10", "t13", "cửa hàng đang hoạt động"), ("t13", "e7", ""),
]
for a, b, n in FLOWS:
    p.flow(a, b, n)

(D / "S1-tuyen-dung-dao-tao.bpmn").write_text(p.to_bpmn(), encoding="utf-8")
sz = render_png(p, IMG / "S1-tuyen-dung-dao-tao.png", "BPMN S1 — Tuyển dụng và đào tạo")
print("S1: %d gateway, %d phan tu, %d luong | PNG %s"
      % (p.n_gateway(), len(p.el), len(p.fl), sz))
