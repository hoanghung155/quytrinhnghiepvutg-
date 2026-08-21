# S1 — Quy trình tuyển dụng

**Lớp:** hỗ trợ
**Người lập:** Nguyễn Thanh Phúc · **Ngày lập:** 21/08/2026 · **Phiên bản:** v1
**Có mô hình BPMN:** không

## 1. Mục đích

Quy trình tuyển dụng tồn tại để tìm kiếm, đánh giá và tuyển chọn ứng viên phù hợp với nhu cầu nhân sự của công ty. Nếu không có quy trình này, công ty sẽ không có đủ nhân lực để vận hành cửa hàng và kho, ảnh hưởng đến khả năng phục vụ khách hàng.

## 2. Phạm vi

- **Bắt đầu từ:** nhu cầu tuyển dụng được phê duyệt từ ban quản lý
- **Kết thúc khi:** ứng viên được chọn ký hợp đồng và bắt đầu làm việc, hoặc tất cả ứng viên dự tuyển bị từ chối
- **Không bao gồm:** đào tạo hướng dẫn việc làm, quản lý lương thưởng

## 3. Actor và vai trò

| Actor | Loại | Trách nhiệm chính |
|---|---|---|
| Phòng Nhân sự | Nội bộ | Đăng tuyên bố tuyển dụng, sàng lọc hồ sơ, phỏng vấn sơ bộ |
| Quản lý cửa hàng / kho | Nội bộ | Phỏng vấn chuyên môn, quyết định tuyển chọn |
| Ứng viên | Bên ngoài | Nộp hồ sơ, tham dự phỏng vấn |
| Hệ thống tuyển dụng | Hệ thống | Lưu trữ hồ sơ, gửi thông báo |

## 4. Đầu vào và đầu ra

| Loại | Tên | Từ đâu / đi đâu | Bắt buộc |
|---|---|---|---|
| Đầu vào | Nhu cầu tuyển dụng | Ban quản lý | Có |
| Đầu vào | Hồ sơ ứng viên | Website tuyển dụng / LinkedIn | Có |
| Đầu ra | Danh sách ứng viên sơ tuyển | Phòng Nhân sự | Có |
| Đầu ra | Quyết định tuyển chọn | Quản lý | Có |
| Đầu ra | Hợp đồng lao động | Phòng Nhân sự | Có |

## 5. Các bước thực hiện

| # | Bước | Actor | Đầu vào | Đầu ra | Ghi chú |
|---|---|---|---|---|---|
| 1 | Nhận nhu cầu tuyển dụng | Phòng Nhân sự | Thông báo nhu cầu | Phiếu tuyển dụng | Xác định số lượng, chức vụ, kỹ năng yêu cầu |
| 2 | Đăng tuyên bố tuyển dụng | Phòng Nhân sự | Phiếu tuyển dụng | Tuyên bố công khai | Đăng trên website công ty, LinkedIn, trang việc làm |
| 3 | Tiếp nhận hồ sơ | Hệ thống | Hồ sơ ứng viên | Danh sách hồ sơ | Kiểm tra đầy đủ thông tin cơ bản |
| 4 | Sàng lọc hồ sơ | Phòng Nhân sự | Danh sách hồ sơ | Danh sách sơ tuyển | Rút gọn theo tiêu chí học vấn, kinh nghiệm |
| 5 | Gửi thông báo phỏng vấn | Phòng Nhân sự | Danh sách sơ tuyển | Thư mời | Gửi email/SMS xác nhận lịch phỏng vấn |
| 6 | Phỏng vấn sơ bộ | Phòng Nhân sự | Hồ sơ ứng viên | Biên bản phỏng vấn | Đánh giá kỹ năng mềm, động lực |
| 7 | Chọn ứng viên vào vòng chuyên môn | Phòng Nhân sự | Biên bản phỏng vấn | Danh sách vòng 2 | Rút gọn xuống 2-3 ứng viên hàng đầu (G1) |
| 8 | Phỏng vấn chuyên môn | Quản lý cửa hàng / kho | Hồ sơ ứng viên | Báo cáo đánh giá | Đánh giá kiến thức chuyên môn, kỹ năng kỹ thuật |
| 9 | Quyết định tuyển chọn | Quản lý | Báo cáo đánh giá | Quyết định tuyển chọn | Phê duyệt ứng viên hoặc từ chối (G2) |
| 10 | Gửi thông báo kết quả | Phòng Nhân sự | Quyết định tuyển chọn | Thư thông báo | Gửi cho ứng viên trúng tuyển và không trúng |
| 11 | Ký hợp đồng lao động | Phòng Nhân sự | Giấy tờ lao động | Hợp đồng | Ứng viên trúng tuyển ký hợp đồng |
| 12 | Bàn giao cho phòng ban | Quản lý cửa hàng / kho | Hợp đồng | Danh sách nhân viên mới | Chuẩn bị công việc, định hướng ban đầu |

## 6. Điểm ra quyết định

| # | Câu hỏi quyết định | Điều kiện | Nhánh kết quả | Ai quyết |
|---|---|---|---|---|
| G1 | Hồ sơ có đạt tiêu chí sơ bộ không? | Bằng cấp, kinh nghiệm | Chuyển vòng chuyên môn / Từ chối | Phòng Nhân sự |
| G2 | Ứng viên có phù hợp chuyên môn không? | Kỹ năng kỹ thuật, kiến thức | Tuyển chọn / Từ chối | Quản lý cửa hàng / kho |

## 7. Ngoại lệ và xử lý

| Mã | Tình huống ngoại lệ | Cách xử lý | Ai xử lý |
|---|---|---|---|
| E1 | Không có ứng viên nào đạt tiêu chí | Kéo dài thời gian tuyển dụng, hạ tiêu chí | Phòng Nhân sự + Ban quản lý |
| E2 | Ứng viên từ chối lời mời | Chọn ứng viên kế tiếp từ danh sách | Phòng Nhân sự |
| E3 | Ứng viên không tới dự phỏng vấn | Gửi thư thông báo từ chối, chọn ứng viên khác | Phòng Nhân sự |

## 8. Quy tắc nghiệp vụ

| Mã | Quy tắc | Nguồn |
|---|---|---|
| R1 | Mỗi chức vụ cần xác định rõ kỹ năng bắt buộc và thời gian kinh nghiệm tối thiểu | Chính sách tuyển dụng |
| R2 | Phỏng vấn sơ bộ ưu tiên đánh giá kỹ năng mềm và độ trung thành | quan sát |
| R3 | Phòng Nhân sự phải hoàn thành sàng lọc hồ sơ trong vòng 2 ngày làm việc | (ước lượng) |

## 9. Chỉ số đo lường

| Chỉ số | Đơn vị | Cách đo | Giá trị ghi nhận | Nguồn |
|---|---|---|---|---|
| Thời gian tuyển dụng từ đăng tuyên bố đến ký hợp đồng | ngày | Tính từ ngày đăng đến ngày ký | (ước lượng) | (chưa xác minh) |
| Tỉ lệ ứng viên sơ tuyển trong tổng hồ sơ tiếp nhận | % | (sơ tuyển / tổng) × 100 | (ước lượng) | (chưa xác minh) |
| Tỉ lệ ứng viên trúng tuyển trong sơ tuyển | % | (trúng / sơ tuyển) × 100 | (ước lượng) | (chưa xác minh) |

## 10. Hệ thống và biểu mẫu liên quan

| Tên | Loại | Ghi chú |
|---|---|---|
| Hệ thống quản lý tuyển dụng | Hệ thống | Lưu trữ hồ sơ, gửi thông báo tự động |
| Phiếu tuyển dụng | Biểu mẫu | Xác định nhu cầu, chức vụ, yêu cầu |
| Biên bản phỏng vấn | Biểu mẫu | Đánh giá ứng viên |
| Hợp đồng lao động | Biểu mẫu | Ký kết với ứng viên trúng tuyển |

## 11. Điểm nghẽn quan sát được

- **Thời gian tuyển dụng quá dài:** Từ khi đăng tuyên bố đến ký hợp đồng thường mất 20-30 ngày, do sàng lọc hồ sơ chậm (hôm nay ghi 2 ngày nhưng thực tế rất lâu) hoặc ứng viên phỏng vấn chậm. Bằng chứng: quan sát tại phòng Nhân sự thegioididong.com Chi Nhánh Hà Nội, Phòng Mua hàng nhân sự mất 5-10 ngày chỉ để sàng lọc hồ sơ.
- **Tỉ lệ sơ tuyển rất thấp:** Thường chỉ 5-10% hồ sơ được qua sơ tuyển, do tiêu chí cao (bằng cấp cao, kinh nghiệm 2+ năm) nhưng tiền lương không cạnh tranh. Bằng chứ: phỏng vấn với Trưởng Phòng Nhân sự, tháng 7/2026.
- **Phỏng vấn chuyên môn không có chuẩn:** Mỗi quản lý có tiêu chí khác nhau, không có bảng đánh giá thống nhất, dẫn tới quyết định chủ quan. Bằng chứng: quan sát buổi phỏng vấn tại cửa hàng TopZone, tháng 8/2026.

## 12. Nguồn tham chiếu

- Phỏng vấn: Trưởng Phòng Nhân sự, thegioididong.com Hà Nội, 20/08/2026
- Quan sát: Quá trình tuyển dụng tại cửa hàng TopZone Landmark 81, tháng 7-8/2026
- Tài liệu: Chính sách tuyển dụng thegioididong.com (nội bộ)
