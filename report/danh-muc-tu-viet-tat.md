# Danh mục từ viết tắt

**Người lập:** Nguyễn Thị Hồng Phúc · **Vị trí trong báo cáo:** sau Danh mục bảng biểu
**Phiên bản:** v1 · **Trạng thái:** sẵn sàng chèn vào Word

Danh mục lập bằng cách quét toàn bộ file `.md` trong repo và toàn bộ nội dung file Word
hiện có, không liệt kê theo trí nhớ. Sắp theo thứ tự chữ cái.

> **Cần rà lại một lần nữa trước khi nộp.** Các chương 2, 3.3, 4.1, 4.2 hiện chưa có nội
> dung, nên có thể phát sinh thêm từ viết tắt. Chạy lại bước quét sau khi các chương đó
> hoàn tất — xem [soat-danh-muc-va-caption.md](soat-danh-muc-va-caption.md) mục 4.

---

## 1. Từ viết tắt chuyên ngành

| Viết tắt | Dạng đầy đủ | Nghĩa tiếng Việt |
|---|---|---|
| **BPM** | Business Process Management | Quản trị quy trình nghiệp vụ |
| **BPMN** | Business Process Model and Notation | Ký hiệu và mô hình hóa quy trình nghiệp vụ, phiên bản 2.0 |
| **BPMNDI** | BPMN Diagram Interchange | Phần mô tả hình vẽ trong file `.bpmn`; thiếu phần này thì mở file ra không thấy sơ đồ |
| **BVA** | Business Value Adding | Hoạt động không tạo giá trị trực tiếp cho khách nhưng bắt buộc phải có |
| **CTE** | Cycle Time Efficiency | Hiệu suất thời gian chu kỳ — tỷ lệ thời gian tạo giá trị trên tổng thời gian |
| **NVA** | Non Value Adding | Hoạt động không tạo giá trị và không bắt buộc |
| **VA** | Value Adding | Hoạt động tạo giá trị cho khách hàng |

## 2. Từ viết tắt về hệ thống và nghiệp vụ

| Viết tắt | Dạng đầy đủ | Nghĩa tiếng Việt |
|---|---|---|
| **ERP** | Enterprise Resource Planning | Hệ thống hoạch định nguồn lực doanh nghiệp |
| **IMEI** | International Mobile Equipment Identity | Số định danh thiết bị di động, dùng làm căn cứ bảo hành |
| **PO** | Purchase Order | Đơn đặt hàng gửi nhà cung cấp |
| **POS** | Point of Sale | Hệ thống bán hàng tại quầy |
| **RFQ** | Request for Quotation | Yêu cầu báo giá gửi nhà cung cấp |
| **SIM** | Subscriber Identity Module | Thẻ định danh thuê bao di động |

## 3. Từ viết tắt tiếng Việt

| Viết tắt | Dạng đầy đủ |
|---|---|
| **KTV** | Kỹ thuật viên |
| **NCC** | Nhà cung cấp |
| **NV** | Nhân viên |
| **TGDĐ** | thegioididong.com — chuỗi bán lẻ thiết bị công nghệ của MWG |

## 4. Tên riêng viết tắt

| Viết tắt | Dạng đầy đủ |
|---|---|
| **GVHD** | Giảng viên hướng dẫn |
| **HTTT** | Hệ thống Thông tin (khoa) |
| **MSSV** | Mã số sinh viên |
| **MWG** | Công ty Cổ phần Đầu tư Thế Giới Di Động |
| **UIT** | Trường Đại học Công nghệ Thông tin, ĐHQG-HCM |

## 5. Mã ký hiệu dùng trong hồ sơ quy trình

Đây **không phải từ viết tắt** mà là hệ thống mã nội bộ của nhóm. Đặt thành mục riêng để
người đọc tra được khi gặp trong Chương 3 và Chương 4.

| Mã | Ý nghĩa | Ví dụ |
|---|---|---|
| **C1–C4** | Quy trình lớp cốt lõi | C3 — Bán trả góp |
| **M1–M4** | Quy trình lớp quản lý | M3 — Kho và điều chuyển |
| **S1–S4** | Quy trình lớp hỗ trợ | S1 — Tuyển dụng và đào tạo |
| **Gn** | Điểm ra quyết định trong hồ sơ, tương ứng gateway trong BPMN | G8 của C3 — sản phẩm còn tồn không |
| **En** | Tình huống ngoại lệ ở mục 7 hồ sơ quy trình | E2 của C4 — hết máy để đổi |
| **Rn** | Quy tắc nghiệp vụ ở mục 8 hồ sơ quy trình | R4 của C4 — quyết định cuối thuộc trung tâm bảo hành |
| **Bn** | Điểm nghẽn quan sát được ở mục 11 hồ sơ quy trình | B2 của C4 — chờ kết quả từ trung tâm |
| **IR-xx** | Mã phát hiện trong Issue Register, mục 4.6 | IR-10 — chờ kết quả bảo hành |
| **Qn** | Câu hỏi cần xác minh ở buổi khảo sát | Q3 — thời gian nhận hàng điều chuyển |

## 6. Ba trạng thái dữ liệu dùng thống nhất trong báo cáo

Ba nhãn này xuất hiện nhiều lần trong Chương 3 và Chương 4. Chúng có nghĩa khác nhau và
**không được dùng thay thế cho nhau**:

| Nhãn | Nghĩa | Khi nào dùng |
|---|---|---|
| **(chờ khảo sát)** | Số liệu sẽ có sau buổi khảo sát tại cửa hàng | Chỉ số đo được tại cửa hàng, ví dụ thời gian chờ tại quầy |
| **(chưa xác minh)** | Không có kênh tiếp cận, nhiều khả năng ở lại trạng thái này tới khi nộp | Dữ liệu khối văn phòng hoặc cấp tập đoàn |
| **(ước lượng)** | Nhóm tự suy ra từ quan sát, chưa có nguồn công khai xác nhận | Quy tắc nghiệp vụ suy từ quan sát bên ngoài |

Mọi dòng mang một trong ba nhãn trên đều phải có mặt trong **bảng giả định ở mục 4.1**.
