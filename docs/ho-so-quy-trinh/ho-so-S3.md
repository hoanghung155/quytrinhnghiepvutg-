# S3 — Quy trình mua sắm hạ tầng công nghệ

**Lớp:** hỗ trợ
**Người lập:** Nguyễn Thanh Phúc · **Ngày lập:** 21/08/2026 · **Phiên bản:** v1
**Có mô hình BPMN:** không

## 1. Mục đích

Quy trình mua sắm hạ tầng công nghệ tồn tại để cung cấp, nâng cấp, và bảo trì các thiết bị IT (máy tính, máy POS, máy quét mã vạch, router, máy chủ) cho cửa hàng và kho. Nếu không có quy trình này, công ty sẽ không theo dõi được chi phí hạ tầng, không biết được nhu cầu cần gì, dẫn tới mua hàng vô tổ chức hoặc hỏng máy không thể sửa chữa kịp thời.

## 2. Phạm vi

- **Bắt đầu từ:** nhu cầu thiết bị IT được phát sinh từ cửa hàng / kho
- **Kết thúc khi:** thiết bị được nhận, kiểm tra, đưa vào sử dụng, hoặc được từ chối do không đạt chất lượng
- **Không bao gồm:** bảo trì định kỳ sau khi đưa vào sử dụng, khấu hao tài sản

## 3. Actor và vai trò

| Actor | Loại | Trách nhiệm chính |
|---|---|---|
| Quản lý cửa hàng / kho | Nội bộ | Phát sinh nhu cầu, xác nhận nhu cầu |
| Phòng IT | Nội bộ | Đánh giá nhu cầu, lựa chọn nhà cung cấp, xác nhận thông số kỹ thuật |
| Phòng Mua hàng | Nội bộ | Thương thảo, đặt hàng, theo dõi nhà cung cấp |
| Nhà cung cấp | Bên ngoài | Báo giá, giao hàng, hỗ trợ kỹ thuật |
| Kho hàng | Nội bộ | Tiếp nhận, kiểm tra chất lượng |

## 4. Đầu vào và đầu ra

| Loại | Tên | Từ đâu / đi đâu | Bắt buộc |
|---|---|---|---|
| Đầu vào | Yêu cầu nhu cầu thiết bị | Quản lý cửa hàng / kho | Có |
| Đầu vào | Báo giá từ nhà cung cấp | Nhà cung cấp | Có |
| Đầu ra | Đơn đặt hàng | Phòng Mua hàng | Có |
| Đầu ra | Biên bản tiếp nhận hàng | Kho hàng | Có |
| Đầu ra | Báo cáo nhu cầu hạ tầng | Phòng IT | Có |

## 5. Các bước thực hiện

| # | Bước | Actor | Đầu vào | Đầu ra | Ghi chú |
|---|---|---|---|---|---|
| 1 | Ghi nhận nhu cầu thiết bị | Quản lý cửa hàng / kho | Thiết bị hỏng hoặc cần mới | Phiếu yêu cầu | Xác định loại, số lượng, mức độ ưu tiên |
| 2 | Đánh giá nhu cầu | Phòng IT | Phiếu yêu cầu | Thông số kỹ thuật | Xác nhận có cần mua, lựa chọn thông số phù hợp |
| 3 | Lựa chọn nhà cung cấp ứng cử | Phòng Mua hàng | Thông số kỹ thuật | Danh sách nhà cung cấp | Chọn 2-3 nhà cung cấp dựa trên lịch sử, uy tín |
| 4 | Gửi yêu cầu báo giá | Phòng Mua hàng | Danh sách nhà cung cấp | Yêu cầu báo giá | Gửi email hoặc gọi điện |
| 5 | Nhà cung cấp báo giá | Nhà cung cấp | Yêu cầu báo giá | Báo giá chi tiết | Gồm giá, thời gian giao, bảo hành |
| 6 | So sánh giá và điều kiện | Phòng Mua hàng | Báo giá từ nhà cung cấp | Báo cáo so sánh | Giá, thời gian giao, điều kiện bảo hành (G1) |
| 7 | Phê duyệt nhà cung cấp | Giám đốc / Ban quản lý | Báo cáo so sánh | Quyết định phê duyệt | Phê duyệt nhà cung cấp được chọn |
| 8 | Thương thảo với nhà cung cấp | Phòng Mua hàng | Quyết định phê duyệt | Điều kiện thỏa thuận | Nếu cần thương thảo giá hoặc thời gian (G2) |
| 9 | Phát hành đơn đặt hàng | Phòng Mua hàng | Điều kiện thỏa thuận | Đơn đặt hàng | Ghi rõ loại, số lượng, giá, thời hạn thanh toán |
| 10 | Nhà cung cấp xác nhận đơn hàng | Nhà cung cấp | Đơn đặt hàng | Thư xác nhận | Xác nhận thời gian giao hàng |
| 11 | Giao hàng | Nhà cung cấp | Đơn đặt hàng | Hàng hóa + Hóa đơn | Giao theo địa chỉ và thời gian đã thỏa thuận |
| 12 | Tiếp nhận hàng | Kho hàng | Hàng hóa + Hóa đơn | Biên bản tiếp nhận | Kiểm tra số lượng, nguyên vẹn |
| 13 | Kiểm tra chất lượng kỹ thuật | Phòng IT | Thiết bị | Biên bản kiểm tra | Kiểm tra chức năng, thông số kỹ thuật (G3) |
| 14 | Đưa vào sử dụng hoặc trả lại | Phòng IT + Kho | Kết quả kiểm tra | Báo cáo hoàn thành | Ghi chép bất thường vào báo cáo |

## 6. Điểm ra quyết định

| # | Câu hỏi quyết định | Điều kiện | Nhánh kết quả | Ai quyết |
|---|---|---|---|---|
| G1 | Chọn nhà cung cấp nào? | Giá tốt, thời gian giao nhanh, bảo hành tốt | Phê duyệt nhà cung cấp / Lựa chọn lại | Ban quản lý |
| G2 | Có cần thương thảo tiếp không? | Giá cao hơn dự toán, thời gian chưa phù hợp | Thương thảo / Chấp nhận điều kiện | Phòng Mua hàng + Giám đốc |
| G3 | Hàng có đạt chất lượng không? | Chức năng hoạt động, thông số khớp | Nhận hàng / Trả lại nhà cung cấp | Phòng IT |

## 7. Ngoại lệ và xử lý

| Mã | Tình huống ngoại lệ | Cách xử lý | Ai xử lý |
|---|---|---|---|
| E1 | Nhà cung cấp trễ giao hàng | Gọi điện xác nhận, yêu cầu giảm giá hoặc thay nhà cung cấp | Phòng Mua hàng |
| E2 | Hàng giao không đúng số lượng / loại | Liên hệ nhà cung cấp yêu cầu bổ sung hoặc trả lại | Kho hàng + Phòng Mua hàng |
| E3 | Thiết bị hỏng hoặc không hoạt động | Yêu cầu nhà cung cấp thay thế hoặc sửa chữa trong thời gian bảo hành | Phòng IT |
| E4 | Nhu cầu bị hủy bỏ | Liên hệ nhà cung cấp hủy hoặc trì hoãn đơn hàng | Phòng Mua hàng + Quản lý cửa hàng |

## 8. Quy tắc nghiệp vụ

| Mã | Quy tắc | Nguồn |
|---|---|---|
| R1 | Yêu cầu nhu cầu thiết bị phải được phê duyệt bởi Phòng IT trước khi mua | Chính sách kiểm soát chi phí |
| R2 | Đơn đặt hàng giá trị > 10 triệu đồng phải được phê duyệt bởi Giám đốc | Quy định chi tiêu |
| R3 | Phòng Mua hàng phải luôn so sánh giá từ ít nhất 2 nhà cung cấp | Chính sách mua sắm |
| R4 | Nhà cung cấp phải có thời gian bảo hành tối thiểu 12 tháng cho thiết bị | Quy định chất lượng |

## 9. Chỉ số đo lường

| Chỉ số | Đơn vị | Cách đo | Giá trị ghi nhận | Nguồn |
|---|---|---|---|---|
| Thời gian từ yêu cầu đến nhận hàng | ngày | Tính từ ngày phát sinh nhu cầu đến ngày tiếp nhận | (ước lượng) | (chưa xác minh) |
| Tỉ lệ lệch giá so với dự toán | % | ((Giá thực tế - Dự toán) / Dự toán) × 100 | (ước lượng) | (chưa xác minh) |
| Tỉ lệ hàng giao không đúng chất lượng | % | (Thiết bị lỗi / Tổng thiết bị giao) × 100 | (ước lượng) | (chưa xác minh) |

## 10. Hệ thống và biểu mẫu liên quan

| Tên | Loại | Ghi chú |
|---|---|---|
| Hệ thống quản lý mua sắm | Hệ thống | Lưu trữ nhu cầu, đơn hàng, nhà cung cấp |
| Phiếu yêu cầu thiết bị | Biểu mẫu | Ghi nhu cầu từ cửa hàng / kho |
| Đơn đặt hàng | Biểu mẫu | Ghi rõ loại, số lượng, giá, thời hạn |
| Biên bản tiếp nhận hàng | Biểu mẫu | Xác nhận số lượng, nguyên vẹn |
| Biên bản kiểm tra kỹ thuật | Biểu mẫu | Xác nhận chất lượng, thông số kỹ thuật |

## 11. Điểm nghẽn quan sát được

- (chưa xác minh)

## 12. Nguồn tham chiếu

- (chưa xác minh)
