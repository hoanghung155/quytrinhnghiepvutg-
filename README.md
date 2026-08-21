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

| Thư mục | Nội dung |
|---|---|
| [docs/](docs/) | Hồ sơ 12 quy trình, đề cương, quy ước, công cụ khảo sát |
| [model/](model/) | Mô hình BPMN và hình xuất |
| [analysis/](analysis/) | Phân tích định tính, định lượng, Issue Register |
| [evidence/](evidence/) | Bằng chứng khảo sát, biên bản review |
| [report/](report/) | Báo cáo Word bản nộp |
| [slide/](slide/) | Slide trình bày |
| [bai-tap-tuan/](bai-tap-tuan/) | Bài tập trên lớp — **không thuộc đồ án**, loại trừ khi đóng gói nộp |

---

Quy ước đặt tên file và thư mục xem
[docs/quy-uoc-dat-ten-file.md](docs/quy-uoc-dat-ten-file.md).
