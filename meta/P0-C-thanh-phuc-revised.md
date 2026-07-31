# P0-C — Phần việc của Thanh Phúc (24730131)

> **Cách dùng:** đọc [P0-chung-quy-uoc.md](P0-chung-quy-uoc.md) trước — nhất là mục 2 (danh tính git) và mục 3 (cách commit trên web nếu không cài git).

Đề tài: phân tích quy trình nghiệp vụ chuỗi bán lẻ **thegioididong.com + TopZone** (MWG), phạm vi thu hẹp ở điện thoại, laptop, máy tính bảng, phụ kiện. Môn Hệ thống Quản trị Qui trình Nghiệp vụ, GVHD ThS. Hà Lê Hoài Trung. Hạn nộp **07/09/2026**.

Repo: <https://github.com/hoanghung155/quytrinhnghiepvutg->

---

## Bạn giữ gì

Nhóm quy trình hỗ trợ và bộ công cụ khảo sát — khoảng 22%. Đặc điểm phần của bạn: **các việc rời nhau**, mỗi cái làm gọn trong một buổi, không phụ thuộc ai.

| Khối | Sản phẩm | Hạn |
|---|---|---|
| Hồ sơ 4 quy trình hỗ trợ | S1 tuyển dụng · S2 ERP/POS · S3 mua sắm hạ tầng · S4 đối soát công nợ NCC | 22/08 |
| Bộ câu hỏi phỏng vấn | **24 câu**, chia 4 nhóm | 26/08 |
| Bảng thuật ngữ | 25–30 mục | 28/08 |
| Mô hình hóa 1 quy trình | BPMN **S4** — **> 7 gateway** | 30/08 |
| Tài liệu tham khảo | Danh mục IEEE, tách riêng tiếng Việt / tiếng Anh | 02/09 |
| Soát chính tả | Toàn báo cáo | 04/09 |

Bạn **duyệt chéo** cho: `docs/quy-trinh-cot-loi` (Danh) và `model/bpmn-quan-ly-ho-tro` (Hồng Phúc).

---

## Bước 0 — Danh tính git

Bỏ qua bước này thì commit **không vào đồ thị đóng góp**, thầy nhìn vào không thấy bạn làm gì.

Tài khoản `phucnguyen24730131` của bạn đăng ký bằng `phucnguyen.winn@gmail.com` — dùng đúng địa chỉ đó để commit.

Kiểm tra một lần: GitHub → **Settings → Emails**, địa chỉ đó phải có nhãn **Verified**. Không verified thì commit vẫn vào lịch sử nhưng **không lên đồ thị đóng góp**.

Nếu dùng git trên máy, chạy trong thư mục repo (không kèm `--global`):

```bash
git config user.name  "Nguyễn Thanh Phúc"
git config user.email "phucnguyen.winn@gmail.com"
```

Nếu commit trên web thì không cần làm gì — GitHub tự gán đúng tài khoản bạn đang đăng nhập.

---

## Nhánh của bạn

| Thứ tự | Nhánh | Nội dung | Người duyệt | Hạn merge |
|---|---|---|---|---|
| 1 | `docs/quy-trinh-ho-tro` | Hồ sơ S1–S4 | Hồng Phúc | 22/08 |
| 2 | `docs/cong-cu-khao-sat` | 24 câu hỏi, bảng thuật ngữ, BPMN S4 | Hồng Phúc | 30/08 |

---

## Việc theo ngày

Mục tiêu: **14 commit nội dung**.

> Các mốc trước 19/08 chỉ dùng nếu đúng với tiến độ thực tế đã làm. Nếu một đầu việc được làm muộn hơn, commit ở ngày thực tế.

| Ngày | Việc | Commit ra cái gì |
|---|---|---|
| 09/07 | Chốt phạm vi nhóm quy trình hỗ trợ | `docs: pham vi quy trinh ho tro` |
| 16/07 | Tạo khung hồ sơ S1–S4 | `docs: tao khung S1 S2 S3 S4` |
| 24/07 | Draft hồ sơ S1–S4 | `docs: draft ho so S1 S2 S3 S4` |
| 07/08 | Tạo khung bộ câu hỏi khảo sát | `docs: khung cau hoi khao sat` |
| 14/08 | Khởi tạo bảng thuật ngữ | `docs: khoi tao bang thuat ngu` |
| 19/08 | Chuẩn hóa 4 hồ sơ hỗ trợ | `docs: chuan hoa 4 ho so ho tro` |
| 20/08 | Hoàn thiện S1 và S2 | `docs: hoan thien S1 S2` |
| 21/08 | Hoàn thiện S3 và S4 | `docs: hoan thien S3 S4` |
| 25/08 | 12 câu hỏi phỏng vấn định tính | `docs: 12 cau hoi phong van dinh tinh` |
| 26/08 | Hoàn thiện đủ 24 câu hỏi | `docs: hoan thien 24 cau hoi phong van` |
| 28/08 | Hoàn thiện bảng thuật ngữ 25–30 mục | `docs: hoan thien bang thuat ngu` |
| 29/08 | BPMN S4 đối soát công nợ | `model: BPMN S4 doi soat cong no` |
| 02/09 | Danh mục tài liệu tham khảo IEEE | `docs: tai lieu tham khao IEEE` |
| 04/09 | Soát chính tả toàn báo cáo | `report: soat chinh ta` |

> Tổng **14 commit nội dung**.

---

## Hai con số cứng đừng để hụt

**Bộ câu hỏi phải từ 20 câu trở lên** mới ăn 0.5đ — nhóm chốt làm **24 câu** để có đệm. Chia 4 nhóm, ví dụ: bối cảnh cửa hàng · quy trình bán và trả góp · quy trình bảo hành đổi trả · điểm nghẽn và thời gian.

**BPMN S4 phải hơn 7 gateway** mới ăn trọn 1.0đ độ phức tạp. Quy trình đối soát công nợ có sẵn nhiều nhánh rẽ (khớp/lệch số liệu, quá hạn, thiếu chứng từ, duyệt vượt hạn mức) — khai thác đúng chỗ đó là đủ gateway.

Tài liệu tham khảo chuẩn **IEEE**, **tách riêng tiếng Việt và tiếng Anh** thành hai danh sách.

---

## Không làm

- **Không nhờ người khác push hộ.** Phần của bạn phải do bạn bấm Commit, kể cả khi nội dung do người khác soạn giúp — thầy chấm đúng chỗ đó.
- **Không commit thẳng lên `main`**, không squash khi merge.
- **Không duyệt PR im lặng.** Comment của bạn dùng luôn làm biên bản review chéo mô hình cho Chương 2.
- **Không bịa số liệu nội bộ doanh nghiệp.** Không có nguồn công khai thì ghi "(ước lượng)" và thêm dòng vào bảng giả định.
