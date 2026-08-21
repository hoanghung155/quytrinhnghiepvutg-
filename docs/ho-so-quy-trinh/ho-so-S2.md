# S2 — Quy trình vận hành ERP/POS

**Lớp:** hỗ trợ
**Người lập:** Nguyễn Thanh Phúc · **Ngày lập:** 21/08/2026 · **Phiên bản:** v1
**Có mô hình BPMN:** không

## 1. Mục đích

Quy trình vận hành ERP/POS tồn tại để quản lý các hệ thống thông tin bán hàng, kho hàng, và tài chính. Nếu không có quy trình này, công ty sẽ không theo dõi được tồn kho, doanh thu, chi phí, dẫn tới sai sót tài chính và mất kiểm soát hàng hóa.

## 2. Phạm vi

- **Bắt đầu từ:** nhân viên bán hàng quẹt hàng hoặc nhập kho
- **Kết thúc khi:** hóa đơn được lưu vào ERP, dữ liệu kho được cập nhật, báo cáo hàng ngày được phát hành
- **Không bao gồm:** bảo trì công nghệ, nâng cấp hệ thống

## 3. Actor và vai trò

| Actor | Loại | Trách nhiệm chính |
|---|---|---|
| Nhân viên bán hàng (POS) | Nội bộ | Quẹt hàng, nhập giỏ, thanh toán |
| Nhân viên kho | Nội bộ | Nhập/xuất kho, cập nhật tồn kho |
| Quản lý ca | Nội bộ | Kiểm tra đóng ca, đối chiếu tiền mặt |
| Kế toán | Nội bộ | Đối chiếu doanh thu, báo cáo tài chính |
| Hệ thống ERP/POS | Hệ thống | Lưu trữ giao dịch, cập nhật kho, tính toán báo cáo |

## 4. Đầu vào và đầu ra

| Loại | Tên | Từ đâu / đi đâu | Bắt buộc |
|---|---|---|---|
| Đầu vào | Giao dịch bán hàng | Máy POS | Có |
| Đầu vào | Phiếu nhập/xuất kho | Nhân viên kho | Có |
| Đầu ra | Hóa đơn điện tử | ERP | Có |
| Đầu ra | Báo cáo tồn kho | ERP | Có |
| Đầu ra | Báo cáo doanh thu hàng ngày | ERP | Có |

## 5. Các bước thực hiện

| # | Bước | Actor | Đầu vào | Đầu ra | Ghi chú |
|---|---|---|---|---|---|
| 1 | Quẹt mã hàng tại POS | Nhân viên bán hàng | Hàng hóa, mã vạch | Giỏ hàng | Sử dụng máy quét mã vạch hoặc nhập tay |
| 2 | Xác nhận số lượng và giá | Nhân viên bán hàng | Giỏ hàng | Giỏ hàng xác nhận | Kiểm tra tính đúng đắn của giá bán |
| 3 | Xử lý thanh toán | Nhân viên bán hàng | Giỏ hàng | Hóa đơn tạm | Tiền mặt, thẻ, ví điện tử (G1) |
| 4 | In hóa đơn | Máy POS | Hóa đơn tạm | Hóa đơn in | Hóa đơn được lưu trong bộ nhớ POS |
| 5 | Trao hàng và hóa đơn | Nhân viên bán hàng | Hóa đơn | Giao dịch kết thúc | Khách hàng ký xác nhận nếu cần |
| 6 | Nhập/xuất kho | Nhân viên kho | Phiếu nhập/xuất | Kho hàng cập nhật | Quẹt mã vạch hoặc nhập tay vào hệ thống kho |
| 7 | Đối soát ca làm việc | Quản lý ca | Danh sách giao dịch POS | Biên bản đóng ca | So sánh tiền mặt với hóa đơn (G2) |
| 8 | Gửi dữ liệu lên ERP | Hệ thống POS | Dữ liệu giao dịch | Báo cáo tạm | Tự động sau mỗi giao dịch hoặc theo lịch |
| 9 | Xử lý hóa đơn không lệch | Hệ thống ERP | Hóa đơn | Báo cáo tồn kho | Cập nhật doanh thu, chi phí, tồn kho |
| 10 | Báo cáo lệch | Kế toán | Báo cáo tạm | Yêu cầu xác minh (G3) | Kế toán điều tra lý do lệch tiền/hàng |
| 11 | Phát hành báo cáo hàng ngày | Hệ thống ERP | Dữ liệu tổng hợp | Báo cáo cuối ngày | Doanh thu, tồn kho, chi phí |

## 6. Điểm ra quyết định

| # | Câu hỏi quyết định | Điều kiện | Nhánh kết quả | Ai quyết |
|---|---|---|---|---|
| G1 | Phương thức thanh toán nào? | Tiền mặt / Thẻ / Ví | Xử lý theo từng kênh | Nhân viên bán hàng |
| G2 | Tiền mặt có khớp với hóa đơn không? | Tiền thực = Tiền hóa đơn | Đóng ca / Điều tra (chênh lệch) | Quản lý ca |
| G3 | Lý do lệch được tìm thấy không? | Kiểm tra chứng từ, hóa đơn | Ghi nhận / Điều chỉnh hóa đơn | Kế toán |

## 7. Ngoại lệ và xử lý

| Mã | Tình huống ngoại lệ | Cách xử lý | Ai xử lý |
|---|---|---|---|
| E1 | Mã vạch không quét được | Nhập tay mã sản phẩm | Nhân viên bán hàng |
| E2 | Không đủ tiền / số dư thẻ | Yêu cầu khách hàng bổ sung tiền hoặc dùng phương thức khác | Nhân viên bán hàng |
| E3 | POS bị mất kết nối mạng | Lưu giao dịch cục bộ, đồng bộ khi có kết nối | Quản lý ca |
| E4 | Chênh lệch tiền mặt quá lớn | Điều tra chi tiết, báo cáo quản lý | Quản lý ca + Kế toán |
| E5 | Hàng hóa bị đăng ký sai giá | Sử dụng hóa đơn điều chỉnh | Kế toán |

## 8. Quy tắc nghiệp vụ

| Mã | Quy tắc | Nguồn |
|---|---|---|
| R1 | Mỗi sản phẩm phải có mã vạch duy nhất trong hệ thống | Chính sách quản lý hàng hóa |
| R2 | Giá bán tại POS phải đồng bộ với giá trong ERP | Quy định kiểm soát nội bộ |
| R3 | Quản lý ca phải đóng ca và đối chiếu trong vòng 30 phút sau khi ca kết thúc | quan sát |
| R4 | Nhân viên kho phải cập nhật tồn kho trong vòng 1 giờ sau khi nhập/xuất | (ước lượng) |

## 9. Chỉ số đo lường

| Chỉ số | Đơn vị | Cách đo | Giá trị ghi nhận | Nguồn |
|---|---|---|---|---|
| Thời gian từ giao dịch đến cập nhật ERP | giây | Bấm giờ từ quẹt mã đến lưu vào ERP | (ước lượng) | (chưa xác minh) |
| Tỉ lệ ca đóng không lệch tiền | % | (ca khớp / tổng ca) × 100 | (ước lượng) | (chưa xác minh) |
| Tỉ lệ lỗi quẹt hàng (mã vạch không đọc được) | % | (lần quẹt lỗi / tổng lần quẹt) × 100 | (ước lượng) | (chưa xác minh) |

## 10. Hệ thống và biểu mẫu liên quan

| Tên | Loại | Ghi chú |
|---|---|---|
| Hệ thống POS | Hệ thống | Xử lý giao dịch bán hàng tại quầy |
| Hệ thống ERP | Hệ thống | Quản lý tồn kho, doanh thu, tài chính |
| Phiếu nhập/xuất kho | Biểu mẫu | Ghi chép thay đổi tồn kho |
| Biên bản đóng ca | Biểu mẫu | Xác nhận tiền mặt và giao dịch hàng ngày |

## 11. Điểm nghẽn quan sát được

- (chưa xác minh)

## 12. Nguồn tham chiếu

- (chưa xác minh)
