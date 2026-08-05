# C3 — Bán trả góp

**Lớp:** cốt lõi
**Người lập:** Nguyễn Ngọc Danh · **Phiên bản:** v1 (draft — actor và input/output)
**Có mô hình BPMN:** có

## 1. Mục đích

Cho phép khách sở hữu sản phẩm mà không phải trả toàn bộ giá trị ngay, thông qua một
công ty tài chính hoặc ngân hàng đứng ra cấp tín dụng. Với cửa hàng, đây là công cụ mở
rộng tệp khách cho các sản phẩm giá cao.

## 2. Phạm vi

- **Bắt đầu từ:** khách đã chọn được sản phẩm và chọn hình thức thanh toán trả góp.
- **Kết thúc khi:** hồ sơ được duyệt và hàng giao · hồ sơ bị từ chối và khách chuyển
  sang trả thẳng · hồ sơ bị từ chối và khách rời đi · khách tự hủy giữa chừng.
- **Không bao gồm:** khâu tư vấn chọn máy (thuộc C1), thu hồi nợ sau bán (thuộc công ty
  tài chính, ngoài phạm vi đề tài).

## 3. Actor và vai trò

| Actor | Loại | Trách nhiệm chính |
|---|---|---|
| Khách hàng | Bên ngoài | Cung cấp giấy tờ, ký hợp đồng, trả trước |
| Nhân viên tư vấn trả góp | Nội bộ | Tư vấn gói, kiểm tra điều kiện sơ bộ, nhập hồ sơ |
| Nhân viên thu ngân | Nội bộ | Thu khoản trả trước, xuất hóa đơn |
| Quản lý cửa hàng | Nội bộ | Duyệt ngoại lệ, xử lý tranh chấp tại chỗ |
| **Công ty tài chính / ngân hàng** | Bên ngoài | Thẩm định tín dụng, ra quyết định duyệt |
| Hệ thống POS | Hệ thống | Lập đơn, ghi nhận khoản trả trước |
| Cổng hồ sơ trả góp | Hệ thống | Truyền hồ sơ sang bên cấp tín dụng, nhận kết quả |

Actor **công ty tài chính** là actor bên ngoài duy nhất có quyền ra quyết định — đây là
nguồn gốc của phần lớn thời gian chờ trong quy trình này.

## 4. Đầu vào và đầu ra

| Loại | Tên | Từ đâu / đi đâu | Bắt buộc |
|---|---|---|---|
| Đầu vào | Sản phẩm đã chọn và giá bán | C1 | Có |
| Đầu vào | CMND/CCCD của khách | Khách hàng | Có |
| Đầu vào | Giấy tờ chứng minh thu nhập hoặc giấy tờ phụ | Khách hàng | Tùy gói |
| Đầu vào | Bảng gói trả góp hiện hành theo từng bên cấp tín dụng | Hệ thống giá | Có |
| Đầu vào | Khoản trả trước | Khách hàng | Tùy gói |
| Đầu ra | Hồ sơ trả góp | → Công ty tài chính | Có |
| Đầu ra | Kết quả thẩm định (duyệt / từ chối / yêu cầu bổ sung) | ← Công ty tài chính | Có |
| Đầu ra | Hợp đồng trả góp đã ký | → Khách, → Công ty tài chính | Chỉ khi duyệt |
| Đầu ra | Đơn hàng và hóa đơn | → ERP | Chỉ khi duyệt |
| Đầu ra | Phiếu bảo hành gắn IMEI | → C4 | Chỉ khi duyệt |

## 5. Các bước thực hiện

`(chưa hoàn thiện — bổ sung ở bản v2)`

## 6. Điểm ra quyết định

`(chưa hoàn thiện — bổ sung ở bản v2, cần > 7 điểm để phục vụ BPMN)`

## 7. Ngoại lệ và xử lý

`(chưa hoàn thiện — bổ sung ở bản v2)`

## 8. Quy tắc nghiệp vụ

`(chưa hoàn thiện — bổ sung ở bản v2)`

## 9. Chỉ số đo lường

`(chưa hoàn thiện — chờ dữ liệu phỏng vấn câu 3 và câu 4 trong buổi khảo sát)`

## 10. Hệ thống và biểu mẫu liên quan

| Tên | Loại | Ghi chú |
|---|---|---|
| Cổng hồ sơ trả góp | Hệ thống | Kênh trao đổi với bên cấp tín dụng |
| POS | Hệ thống | Ghi nhận đơn và khoản trả trước |
| Hợp đồng trả góp | Biểu mẫu | Ảnh mẫu cần chụp (che thông tin cá nhân) |
| Bảng gói trả góp niêm yết | Biểu mẫu | Ảnh mẫu cần chụp |

## 11. Điểm nghẽn quan sát được

`(chưa hoàn thiện — chờ buổi khảo sát 23/08)`

## 12. Nguồn tham chiếu

`(bổ sung sau khảo sát)`
