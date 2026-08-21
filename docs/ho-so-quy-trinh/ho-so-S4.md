# S4 — Quy trình đối soát công nợ nhà cung cấp

**Lớp:** hỗ trợ
**Người lập:** Nguyễn Thanh Phúc · **Ngày lập:** 21/08/2026 · **Phiên bản:** v1
**Có mô hình BPMN:** có

## 1. Mục đích

Quy trình đối soát công nợ nhà cung cấp tồn tại để xác minh lại tính chính xác của hóa đơn, chứng từ, và doanh số bán hàng so với dữ liệu hệ thống, để đảm bảo công nợ đối với nhà cung cấp được tính đúng. Nếu không có quy trình này, công ty sẽ bị lập hóa đơn sai, trả tiền nhiều hơn, hoặc bỏ sót công nợ, dẫn tới mất tiền hoặc mất uy tín với nhà cung cấp.

## 2. Phạm vi

- **Bắt đầu từ:** nhà cung cấp gửi hóa đơn hoặc cuối tháng khi cần đối soát định kỳ
- **Kết thúc khi:** công nợ được xác nhận chính xác, hóa đơn được phê duyệt thanh toán, hoặc lập phiếu điều chỉnh nếu có lỗi
- **Không bao gồm:** thương thảo hạn thanh toán, xin giãn nợ

## 3. Actor và vai trò

| Actor | Loại | Trách nhiệm chính |
|---|---|---|
| Nhà cung cấp | Bên ngoài | Gửi hóa đơn, hóa đơn điều chỉnh |
| Phòng Mua hàng | Nội bộ | Kiểm tra chứng từ nhập kho, so sánh với hóa đơn |
| Kho hàng | Nội bộ | Xác minh số lượng hàng thực tế, cấp phát hàng cho cửa hàng |
| Kế toán | Nội bộ | So sánh hóa đơn với doanh số bán hàng, đối soát tài chính |
| Hệ thống ERP | Hệ thống | Lưu trữ chứng từ nhập kho, giá bán, doanh số hàng |
| Giám đốc / Ban quản lý | Nội bộ | Phê duyệt thanh toán nếu có chênh lệch lớn |

## 4. Đầu vào và đầu ra

| Loại | Tên | Từ đâu / đi đâu | Bắt buộc |
|---|---|---|---|
| Đầu vào | Hóa đơn từ nhà cung cấp | Nhà cung cấp | Có |
| Đầu vào | Chứng từ nhập kho | Kho hàng | Có |
| Đầu vào | Doanh số bán hàng | ERP/POS | Có |
| Đầu ra | Biên bản đối soát | Kế toán | Có |
| Đầu ra | Phiếu thanh toán | Kế toán | Có |
| Đầu ra | Phiếu điều chỉnh (nếu có lỗi) | Kế toán | Không bắt buộc |

## 5. Các bước thực hiện

| # | Bước | Actor | Đầu vào | Đầu ra | Ghi chú |
|---|---|---|---|---|---|
| 1 | Tiếp nhận hóa đơn | Kế toán | Hóa đơn từ nhà cung cấp | Hóa đơn đầu vào | Ghi chép vào sổ hóa đơn đầu vào |
| 2 | Kiểm tra tính hợp lệ hóa đơn | Kế toán | Hóa đơn | Kết quả kiểm tra | Kiểm tra kỳ hạn, chữ ký, số tiếp nhận (G1) |
| 3 | Tra cứu chứng từ nhập kho | Phòng Mua hàng | Số hóa đơn | Chứng từ nhập kho | Tra cứu trong ERP hoặc sổ kho |
| 4 | So sánh số lượng và giá | Phòng Mua hàng | Hóa đơn + Chứng từ nhập kho | Báo cáo so sánh | Kiểm tra số lượng, đơn vị, giá khớp không (G2) |
| 5 | Kiểm tra doanh số bán hàng | Kho hàng + Kế toán | Chứng từ nhập + Doanh số ERP | Báo cáo bán hàng | Xác minh hàng được cấp phát cho cửa hàng nào, bán được bao nhiêu (G3) |
| 6 | Tính toán công nợ còn lại | Kế toán | Báo cáo bán hàng | Tính toán công nợ | Công nợ = Nhập - (Đã bán + Hàng còn tồn) |
| 7 | So sánh với dữ liệu hệ thống | Kế toán | Công nợ tính toán + Dữ liệu ERP | Báo cáo chênh lệch | Nếu lệch, xác định lý do (G4) |
| 8 | Xác định nguyên nhân chênh lệch | Kế toán + Phòng Mua hàng + Kho | Báo cáo chênh lệch | Nguyên nhân | Hàng tặng, hỏng, mất, hoặc lỗi nhập liệu (G5) |
| 9 | Lập phiếu điều chỉnh (nếu có lỗi) | Kế toán | Nguyên nhân + Chứng từ chứng minh | Phiếu điều chỉnh | Ghi rõ lý do điều chỉnh |
| 10 | Phê duyệt phiếu điều chỉnh (nếu lệch lớn) | Giám đốc | Phiếu điều chỉnh + Bằng chứng | Quyết định phê duyệt (G6) | Nếu lệch > 5% hoặc > 5 triệu đồng |
| 11 | Lập biên bản đối soát cuối cùng | Kế toán | Kết quả từ bước 7-10 | Biên bản đối soát | Tổng hợp kết luận |
| 12 | Lập phiếu thanh toán | Kế toán | Biên bản đối soát | Phiếu thanh toán | Công nợ cần trả = Công nợ chính xác |
| 13 | Phê duyệt thanh toán | Giám đốc / Ban quản lý | Phiếu thanh toán | Quyết định thanh toán | Ký duyệt |
| 14 | Thực hiện thanh toán | Kế toán | Phiếu thanh toán | Chứng từ thanh toán | Chuyển tiền hoặc trả tiền mặt |

## 6. Điểm ra quyết định

| # | Câu hỏi quyết định | Điều kiện | Nhánh kết quả | Ai quyết |
|---|---|---|---|---|
| G1 | Hóa đơn có hợp lệ không? | Đúng thời hạn, chữ ký, số tiếp nhận | Tiếp tục xử lý / Trả lại nhà cung cấp | Kế toán |
| G2 | Số lượng và giá có khớp không? | Số lượng trong hóa đơn = Chứng từ nhập, Giá = Đơn đặt hàng | Khớp / Lệch | Phòng Mua hàng |
| G3 | Hàng nhập có được bán hết không? | Tồn kho = 0 hoặc tồn kho từ hàng khác | Bán hết / Còn tồn / Mất/Hỏng | Kho hàng |
| G4 | Công nợ có khớp dữ liệu hệ thống không? | Công nợ tính = Công nợ ERP | Khớp / Lệch | Kế toán |
| G5 | Nguyên nhân lệch là gì? | Hàng tặng, hỏng, mất, lỗi nhập, hay cải giá? | Hàng tặng / Hỏng / Mất / Lỗi nhập / Cải giá / Lỗi khác | Kế toán + Phòng Mua hàng |
| G6 | Lệch lớn có cần phê duyệt không? | Lệch > 5% hoặc > 5 triệu đồng | Phê duyệt / Tự động chấp nhận | Giám đốc |

## 7. Ngoại lệ và xử lý

| Mã | Tình huống ngoại lệ | Cách xử lý | Ai xử lý |
|---|---|---|---|
| E1 | Không tìm thấy chứng từ nhập kho | Tra cứu sổ kho cũ, gọi nhà cung cấp xác nhận, lập phiếu điều chỉnh | Phòng Mua hàng + Kế toán |
| E2 | Hóa đơn bị hỏng hoặc không đủ thông tin | Yêu cầu nhà cung cấp gửi lại hoặc lập hóa đơn điều chỉnh | Kế toán |
| E3 | Hàng nhập nhưng không tìm thấy trong kho | Điều tra xem hàng được cấp phát cho cửa hàng nào, hay bị mất/hỏng | Kho hàng + Phòng Mua hàng |
| E4 | Lệch số lượng lớn (>10% số lượng nhập) | Báo cáo quản lý, điều tra chi tiết, lập phiếu điều chỉnh | Kho hàng + Giám đốc |
| E5 | Lệch tiền lớn (>5% giá trị nhập) | Báo cáo quản lý, điều tra tất cả giao dịch liên quan, yêu cầu phê duyệt | Kế toán + Giám đốc |
| E6 | Nhà cung cấp tranh cãi kết quả đối soát | Chuẩn bị hồ sơ chứng từ, gọi điện thoại thương thảo, lập biên bản cuộc gọi | Kế toán + Phòng Mua hàng |

## 8. Quy tắc nghiệp vụ

| Mã | Quy tắc | Nguồn |
|---|---|---|
| R1 | Hóa đơn phải được xác nhận nhập kho trong vòng 48 giờ, nếu không báo cáo quản lý | Quy định kiểm soát nội bộ |
| R2 | Đối soát định kỳ phải thực hiện hàng tháng, trước ngày 5 của tháng sau | Chính sách kế toán |
| R3 | Nếu lệch số lượng hoặc tiền > 5%, phải lập phiếu điều chỉnh và báo cáo quản lý | Quy định chi tiêu |
| R4 | Chênh lệch từ hàng tặng, hỏng, mất phải ghi rõ lý do và được phê duyệt | quan sát |
| R5 | Dữ liệu ERP phải được cập nhật đầy đủ trước khi đối soát | Quy định hệ thống |

## 9. Chỉ số đo lường

| Chỉ số | Đơn vị | Cách đo | Giá trị ghi nhận | Nguồn |
|---|---|---|---|---|
| Thời gian đối soát từ tiếp nhận hóa đơn đến phê duyệt thanh toán | ngày | Tính từ ngày nhận hóa đơn đến ngày phê duyệt | (ước lượng) | (chưa xác minh) |
| Tỉ lệ hóa đơn khớp lần đầu (không cần điều chỉnh) | % | (Hóa đơn khớp / Tổng hóa đơn) × 100 | (ước lượng) | (chưa xác minh) |
| Tỉ lệ chênh lệch trung bình khi có lệch | % | ((Lệch) / Giá trị nhập) × 100 | (ước lượng) | (chưa xác minh) |
| Số lần chênh lệch > 5% | lần/tháng | Đếm số hóa đơn có chênh lệch > 5% | (ước lượng) | (chưa xác minh) |

## 10. Hệ thống và biểu mẫu liên quan

| Tên | Loại | Ghi chú |
|---|---|---|
| Hệ thống ERP | Hệ thống | Lưu trữ chứng từ nhập kho, giá bán, doanh số |
| Hệ thống POS | Hệ thống | Cung cấp doanh số bán hàng hàng ngày |
| Phiếu nhập kho | Biểu mẫu | Ghi chép hàng nhập từ nhà cung cấp |
| Hóa đơn từ nhà cung cấp | Biểu mẫu | Chứng từ hóa đơn điều chỉnh |
| Biên bản đối soát | Biểu mẫu | Ghi kết quả so sánh, quyết định thanh toán |
| Phiếu điều chỉnh công nợ | Biểu mẫu | Ghi chép điều chỉnh nếu có lỗi |
| Phiếu thanh toán | Biểu mẫu | Ghi rõ công nợ cần trả, hạn thanh toán |

## 11. Điểm nghẽn quan sát được

- **Thời gian đối soát kéo dài:** Đối soát từ khi tiếp nhận hóa đơn đến khi phê duyệt thanh toán thường mất 3-5 ngày, do chờ kho hàng xác minh, chờ ERP cập nhật dữ liệu. Bằng chứng: theo dõi 10 hóa đơn từ 7/8 đến 21/8/2026, trung bình 4.2 ngày.
- **Chênh lệch số lượng hoặc tiền thường xuyên xảy ra:** Khoảng 20-30% hóa đơn có chênh lệch, chủ yếu do lỗi nhập liệu, hàng bị mất, hỏng, hoặc cải giá. Bằng chứng: quan sát tại Phòng Kế toán, tháng 8/2026.
- **Hàng nhập không được tìm thấy trong kho:** Có những lần hàng ghi nhập trong hóa đơn nhưng không tìm thấy trong kho, do nhân viên kho quên cập nhật hoặc hàng bị mất. Bằng chứng: phỏng vấn Trưởng kho, cho biết "mỗi tháng có 2-3 lần như thế".
- **Tranh cãi với nhà cung cấp:** Khi phát hiện lệch, đôi khi nhà cung cấp không chấp nhận điều chỉnh, yêu cầu chứng từ chi tiết, kéo dài thời gian giải quyết. Bằng chứng: quan sát tranh cãi về hóa đơn Samsung trong tháng 7/2026, mất 10 ngày để giải quyết.

## 12. Nguồn tham chiếu

- Phỏng vấn: Trưởng kho hàng, thegioididong.com Hà Nội, 21/08/2026
- Phỏng vấn: Kế toán trưởng, thegioididong.com Hà Nội, 20/08/2026
- Quan sát: Quá trình đối soát công nợ tại Phòng Kế toán, tháng 7-8/2026
- Dữ liệu: Biên bản đối soát tháng 7-8/2026
