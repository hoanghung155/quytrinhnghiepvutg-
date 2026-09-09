# Phân tích quy trình nghiệp vụ chuỗi bán lẻ thegioididong.com + TopZone

Đồ án môn **Hệ thống Quản trị Qui trình Nghiệp vụ** — GVHD: ThS. Hà Lê Hoài Trung.
Trường Đại học Công nghệ Thông tin, ĐHQG-HCM — Khoa Hệ thống Thông tin.

**Phạm vi:** chuỗi bán lẻ thegioididong.com và TopZone (Công ty CP Đầu tư Thế Giới
Di Động — MWG), thu hẹp ở bốn nhóm sản phẩm: điện thoại, laptop, máy tính bảng và
phụ kiện.

**Hạn nộp:** 07/09/2026.

---

## Thành viên

| MSSV | Họ và tên | GitHub | Phần phụ trách |
|---|---|---|---|
| 24730090 | Nguyễn Ngọc Danh (nhóm trưởng) | `24730090` | Kiến trúc quy trình, hồ sơ C1/C3/C4, BPMN M2/C3/C4, Issue Register, báo cáo Word, slide |
| 24730132 | Nguyễn Thị Hồng Phúc | `hongphuc0212` | Hồ sơ M1–M4, BPMN M3/S1, phân tích định tính, soát hình thức |
| 24730131 | Nguyễn Thanh Phúc | `phucnguyen24730131` | Hồ sơ S1–S4, bộ câu hỏi phỏng vấn, bảng thuật ngữ, BPMN S4, tài liệu tham khảo |
| 24730099 | Mai Hoàng Hưng | `hoanghung155` | Quản trị repo, khảo sát thực địa, hồ sơ C2, bằng chứng, phân tích định lượng |

---

## Mười hai quy trình theo ba lớp

| Lớp | Mã | Quy trình |
|---|---|---|
| **Cốt lõi** | C1 | Bán tại cửa hàng |
| | C2 | Bán online, giao hàng và nhận tại cửa hàng |
| | C3 | Bán trả góp |
| | C4 | Bảo hành, đổi trả |
| **Quản lý** | M1 | Hoạch định nhu cầu |
| | M2 | Quản lý nhà cung cấp |
| | M3 | Kho và điều chuyển |
| | M4 | Mạng lưới cửa hàng |
| **Hỗ trợ** | S1 | Tuyển dụng và đào tạo |
| | S2 | ERP / POS |
| | S3 | Mua sắm hạ tầng |
| | S4 | Đối soát công nợ nhà cung cấp |

Sáu quy trình được mô hình hóa BPMN: **M2, C3, C4, M3, S1, S4** — mỗi mô hình phải có
**hơn 7 gateway**.

---

## Cấu trúc thư mục

| Thư mục | Chứa gì | Số file |
|---|---|---:|
| [`docs/`](docs/) | Hồ sơ 12 quy trình, kiến trúc quy trình, bộ câu hỏi phỏng vấn, bảng thuật ngữ | 47 |
| [`model/`](model/) | Sáu mô hình BPMN và ảnh xuất | 20 |
| [`analysis/`](analysis/) | Phân tích định tính, định lượng, Issue Register | 12 |
| [`evidence/`](evidence/) | Ảnh biểu mẫu, biên bản review, kết quả khảo sát cửa hàng | 5 |
| [`report/`](report/) | Báo cáo Word và công cụ soát | 8 |
| [`slide/`](slide/) | Slide trình bày | 3 |
| [`bai-tap-tuan/`](bai-tap-tuan/) | 11 bài tập từng buổi, mỗi bài một thư mục `YYYY-MM-DD-<slug>/` | 31 |
| [`nop/`](nop/) | Gói nộp cuối kỳ — bản đúng như đã nộp cho thầy | 77 |
| [`meta/`](meta/) | Quy ước làm việc nhóm, phân công, checklist quản trị repo | 7 |

Tên thư mục và tên file theo [docs/quy-uoc-dat-ten-file.md](docs/quy-uoc-dat-ten-file.md):
không dấu, chữ thường, nối bằng `-`.

Thư mục [`nop/do-an-cuoi-ky/`](nop/do-an-cuoi-ky/) trên repo đã đổi tên cho hợp quy ước.
Tên thư mục **thật sự nộp** lên Drive lớp và e-learning là:

```
24730090_Nguyễn Ngọc Danh;24730099_Mai Hoàng Hưng;24730131_Nguyễn Thanh Phúc;24730132_Nguyễn Thị Hồng Phúc
```

---

Quy ước làm việc nhóm, phân công và nhịp commit xem
[meta/P0-chung-quy-uoc-revised.md](meta/P0-chung-quy-uoc-revised.md).
