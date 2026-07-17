# C1 — Bán tại cửa hàng

**Lớp:** cốt lõi
**Người lập:** Nguyễn Ngọc Danh · **Phiên bản:** v1 (draft — actor và input/output)
**Có mô hình BPMN:** không

## 1. Mục đích

Chuyển một khách có nhu cầu thành một đơn hàng hoàn tất ngay tại cửa hàng, đồng thời ghi
nhận đầy đủ dữ liệu bán hàng để phục vụ bảo hành về sau. Đây là quy trình sinh doanh thu
chính và cũng là nơi phát sinh dữ liệu gốc cho C4.

## 2. Phạm vi

- **Bắt đầu từ:** khách bước vào cửa hàng hoặc được nhân viên tiếp cận tại khu trưng bày.
- **Kết thúc khi:** một trong các trạng thái — khách nhận hàng và rời quầy · khách chuyển
  sang C3 (trả góp) · khách rời đi không mua · đơn chuyển thành đặt hàng do hết tồn.
- **Không bao gồm:** đặt hàng online (C2), thẩm định tín dụng trả góp (C3), tiếp nhận
  máy lỗi (C4), điều chuyển hàng giữa cửa hàng (M3).

## 3. Actor và vai trò

| Actor | Loại | Trách nhiệm chính |
|---|---|---|
| Khách hàng | Bên ngoài | Nêu nhu cầu, chọn sản phẩm, thanh toán, ký nhận |
| Nhân viên tư vấn | Nội bộ | Tiếp cận, tư vấn, kiểm tra tồn kho, lập đơn |
| Nhân viên kho tại cửa hàng | Nội bộ | Lấy hàng, kiểm tra tình trạng máy trước khi giao |
| Nhân viên thu ngân | Nội bộ | Thu tiền, xuất hóa đơn |
| Quản lý cửa hàng | Nội bộ | Duyệt trường hợp ngoại lệ: giảm giá, đổi máy trưng bày |
| Hệ thống POS | Hệ thống | Ghi nhận đơn, tính tiền, xuất hóa đơn |
| Hệ thống ERP / tồn kho | Hệ thống | Tra tồn kho, trừ tồn, đồng bộ dữ liệu bán |
| Cổng thanh toán thẻ | Hệ thống | Xử lý giao dịch thẻ |

Ở nhiều cửa hàng, **một nhân viên kiêm cả tư vấn và thu ngân** trong giờ vắng khách. Khi
mô hình hóa vẫn tách hai vai trò vì trách nhiệm khác nhau.

## 4. Đầu vào và đầu ra

| Loại | Tên | Từ đâu / đi đâu | Bắt buộc |
|---|---|---|---|
| Đầu vào | Nhu cầu của khách | Khách hàng | Có |
| Đầu vào | Thông tin tồn kho theo model và màu | ERP (M3) | Có |
| Đầu vào | Bảng giá và chương trình khuyến mãi hiện hành | Hệ thống giá | Có |
| Đầu vào | Giấy tờ tùy thân của khách | Khách hàng | Không — chỉ khi xuất hóa đơn công ty hoặc trả góp |
| Đầu ra | Đơn hàng trên POS | → ERP | Có |
| Đầu ra | Hóa đơn bán hàng | → Khách hàng | Có |
| Đầu ra | Phiếu bảo hành / dữ liệu bảo hành gắn IMEI | → C4 | Có |
| Đầu ra | Bản ghi trừ tồn kho | → M3 | Có |
| Đầu ra | Dữ liệu doanh số theo nhân viên | → M4, hệ thống lương | Có |

## 5. Các bước thực hiện

`(chưa hoàn thiện — bổ sung ở bản v2)`

## 6. Điểm ra quyết định

`(chưa hoàn thiện — bổ sung ở bản v2)`

## 7. Ngoại lệ và xử lý

`(chưa hoàn thiện — bổ sung ở bản v2)`

## 8. Quy tắc nghiệp vụ

`(chưa hoàn thiện — bổ sung ở bản v2)`

## 9. Chỉ số đo lường

`(chưa hoàn thiện — chờ dữ liệu bấm giờ từ buổi khảo sát 23/08)`

## 10. Hệ thống và biểu mẫu liên quan

| Tên | Loại | Ghi chú |
|---|---|---|
| POS | Hệ thống | Lập đơn, thu tiền |
| ERP / hệ thống tồn kho | Hệ thống | Tra và trừ tồn |
| Hóa đơn bán hàng | Biểu mẫu | Ảnh mẫu cần chụp trong buổi khảo sát |
| Phiếu bảo hành | Biểu mẫu | Ảnh mẫu cần chụp trong buổi khảo sát |

## 11. Điểm nghẽn quan sát được

`(chưa hoàn thiện — chờ buổi khảo sát 23/08)`

## 12. Nguồn tham chiếu

`(bổ sung sau khảo sát)`
