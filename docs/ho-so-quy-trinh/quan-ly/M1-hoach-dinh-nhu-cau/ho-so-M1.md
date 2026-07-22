# M1 — Hoạch định nhu cầu

**Lớp:** quản lý
**Người lập:** Nguyễn Thị Hồng Phúc · **Phiên bản:** v1 (draft)
**Có mô hình BPMN:** không

## 1. Mục đích

Xác định trước lượng hàng cần có theo từng nhóm sản phẩm cho kỳ tới, để chuỗi không rơi
vào hai trạng thái cùng tốn tiền: hết hàng khi khách hỏi, và tồn ứ hàng bán chậm. Với
ngành hàng điện thoại và laptop, sai số dự báo tốn kém hơn nhiều ngành khác vì giá trị
đơn vị cao và sản phẩm mất giá nhanh theo vòng đời model.

Không có M1 thì M2 không biết đặt bao nhiêu, và M3 chỉ còn cách chữa cháy bằng điều
chuyển giữa các cửa hàng — vốn là hoạt động tốn chi phí mà không tạo thêm giá trị.

## 2. Phạm vi

- **Bắt đầu từ:** tới kỳ lập kế hoạch, hoặc có tín hiệu tồn kho vượt ngưỡng.
- **Kết thúc khi:** kế hoạch nhu cầu được duyệt và chuyển sang M2 · kế hoạch bị trả lại
  để lập lại · kỳ kế hoạch bị hủy do thay đổi định hướng kinh doanh.
- **Không bao gồm:** chọn nhà cung cấp cụ thể và đặt hàng (M2); phân bổ hàng đã có giữa
  các cửa hàng (M3); quyết định mở hay đóng điểm bán (M4).

## 3. Actor và vai trò

| Actor | Loại | Trách nhiệm chính |
|---|---|---|
| Bộ phận kế hoạch / phân tích kinh doanh | Nội bộ | Lập dự báo, tính lượng cần mua, trình duyệt |
| Bộ phận ngành hàng | Nội bộ | Cung cấp thông tin model mới, vòng đời sản phẩm, chương trình của hãng |
| Quản lý cửa hàng | Nội bộ | Đề xuất điều chỉnh theo tình hình bán tại điểm |
| Bộ phận thu mua | Nội bộ | Nhận kế hoạch đã duyệt, phản hồi về khả năng cung ứng |
| Ban lãnh đạo | Nội bộ | Phê duyệt kế hoạch và ngân sách nhập hàng |
| Hệ thống ERP | Hệ thống | Cung cấp dữ liệu bán, tồn, hàng đang về |
| Hệ thống báo cáo bán hàng | Hệ thống | Số liệu bán theo model, theo cửa hàng, theo kỳ |

Bộ phận ngành hàng là actor dễ bị bỏ sót khi vẽ sơ đồ, nhưng chính họ nắm thông tin về
model sắp ra mắt — yếu tố làm dự báo theo lịch sử bán trở nên vô nghĩa.

## 4. Đầu vào và đầu ra

| Loại | Tên | Từ đâu / đi đâu | Bắt buộc |
|---|---|---|---|
| Đầu vào | Dữ liệu bán kỳ trước theo model và theo cửa hàng | ERP / báo cáo bán hàng | Có |
| Đầu vào | Tồn kho hiện có và hàng đang về | ERP, M3 | Có |
| Đầu vào | Lịch ra mắt model mới và chương trình của hãng | Bộ phận ngành hàng | Có |
| Đầu vào | Đề xuất điều chỉnh từ cửa hàng | Quản lý cửa hàng | Không |
| Đầu vào | Ngân sách nhập hàng của kỳ | Ban lãnh đạo | Có |
| Đầu vào | Danh sách điểm bán đang hoạt động và điểm bán mới | M4 | Có |
| Đầu ra | Kế hoạch nhu cầu theo nhóm sản phẩm | → M2 | Có |
| Đầu ra | Cảnh báo nhóm hàng tồn ứ | → M2, M3 | Có |
| Đầu ra | Báo cáo sai lệch dự báo kỳ trước | → nội bộ M1 kỳ sau | Có |

## 5. Các bước thực hiện

| # | Bước | Actor | Đầu vào | Đầu ra | Ghi chú |
|---|---|---|---|---|---|
| 1 | Chốt kỳ kế hoạch và phạm vi nhóm sản phẩm | Bộ phận kế hoạch | Lịch kỳ | Phạm vi kỳ này | |
| 2 | Trích dữ liệu bán và tồn từ ERP | Hệ thống | Dữ liệu kỳ trước | Bộ số liệu nền | Tự động |
| 3 | Phân loại nhóm sản phẩm theo mức biến động | Bộ phận kế hoạch | Bộ số liệu nền | Nhóm ổn định / nhóm biến động cao | → G1 |
| 4 | Thu thập thông tin model mới và chương trình hãng | Bộ phận ngành hàng | Lịch ra mắt | Danh mục model mới trong kỳ | → G2 |
| 5 | Lập dự báo nhu cầu sơ bộ theo nhóm | Bộ phận kế hoạch | Số liệu nền, thông tin model mới | Dự báo sơ bộ | Nhóm mới ra mắt không dự báo theo lịch sử bán |
| 6 | Đối chiếu dự báo với tồn hiện có và hàng đang về | Bộ phận kế hoạch | Dự báo, tồn, hàng đang về | Lượng thiếu / thừa theo nhóm | → G3 |
| 7 | Thu thập đề xuất điều chỉnh từ cửa hàng | Quản lý cửa hàng | Dự báo sơ bộ | Danh sách đề xuất | → G4 |
| 8 | Hiệu chỉnh dự báo theo đề xuất được chấp nhận | Bộ phận kế hoạch | Đề xuất | Dự báo đã hiệu chỉnh | |
| 9 | Rà soát ràng buộc ngân sách và sức chứa kho | Bộ phận kế hoạch | Ngân sách kỳ, sức chứa | Kết luận khả thi / phải cắt giảm | → G5 |
| 10 | Trình phê duyệt kế hoạch nhu cầu | Bộ phận kế hoạch | Kế hoạch | Kế hoạch trình duyệt | → G6 |
| 11 | Chuyển kế hoạch đã duyệt sang M2 | Bộ phận kế hoạch | Kế hoạch đã duyệt | Yêu cầu nhập hàng | Đầu vào của M2 |
| 12 | Theo dõi sai lệch dự báo trong kỳ | Bộ phận kế hoạch | Bán thực tế so với dự báo | Báo cáo sai lệch | → G7 |

## 6. Điểm ra quyết định

| # | Câu hỏi quyết định | Điều kiện | Nhánh kết quả | Ai quyết |
|---|---|---|---|---|
| G1 | Nhóm sản phẩm thuộc loại biến động cao hay ổn định? | Độ lệch bán giữa các kỳ gần nhất | Ổn định → dự báo theo lịch sử · Biến động cao → dự báo theo thông tin ngành hàng | Bộ phận kế hoạch |
| G2 | Trong kỳ có model mới ra mắt không? | Lịch ra mắt của hãng | Có → tách riêng, không dùng lịch sử bán · Không → bước 5 bình thường | Bộ phận ngành hàng |
| G3 | Tồn hiện có và hàng đang về đã đủ đáp ứng dự báo? | Tồn cộng hàng đang về so với dự báo | Đủ → không đề xuất mua thêm nhóm đó · Thiếu → tính lượng cần mua | Bộ phận kế hoạch |
| G4 | Đề xuất từ cửa hàng có được chấp nhận? | Mức chênh so với dự báo và lý do kèm theo | Chấp nhận → bước 8 · Không → giữ dự báo, phản hồi lý do cho cửa hàng | Bộ phận kế hoạch |
| G5 | Kế hoạch có vượt ngân sách hoặc sức chứa? | Giá trị kế hoạch so với ngân sách kỳ | Vượt → cắt giảm theo thứ tự ưu tiên rồi quay lại bước 9 · Không → bước 10 | Bộ phận kế hoạch |
| G6 | Ban lãnh đạo duyệt kế hoạch? | Đánh giá của ban lãnh đạo | Duyệt → bước 11 · Trả lại → quay lại bước 5 kèm lý do · Hủy kỳ → kết thúc | Ban lãnh đạo |
| G7 | Sai lệch dự báo có vượt ngưỡng chấp nhận? | So sánh bán thực tế với dự báo | Vượt → ghi nhận nguyên nhân, hiệu chỉnh phương pháp kỳ sau · Không → đóng kỳ | Bộ phận kế hoạch |

M1 **không được chọn để mô hình hóa BPMN**, nên bảng này không cần vượt mốc 7 dòng. Bảy
điểm quyết định ở trên đủ để mô tả trong Chương 3 bằng lời và bằng bảng.

## 7. Ngoại lệ và xử lý

| Mã | Tình huống ngoại lệ | Cách xử lý | Ai xử lý |
|---|---|---|---|
| E1 | Hãng thay đổi lịch ra mắt model sau khi kế hoạch đã duyệt | Lập kế hoạch bổ sung ngoài kỳ cho nhóm bị ảnh hưởng | Bộ phận kế hoạch, bộ phận ngành hàng |
| E2 | Dữ liệu bán trong ERP không đầy đủ do sự cố hệ thống | Dùng số liệu kỳ liền trước và ghi rõ giới hạn trong kế hoạch | Bộ phận kế hoạch |
| E3 | Nhu cầu tăng đột biến giữa kỳ do khuyến mại lớn hoặc sự kiện | Kích hoạt lập kế hoạch bất thường, không đợi hết kỳ | Bộ phận kế hoạch |
| E4 | Ngân sách bị cắt sau khi kế hoạch đã duyệt | Rà soát lại theo thứ tự ưu tiên nhóm hàng, trình duyệt lại | Ban lãnh đạo |
| E5 | Cửa hàng mới khai trương giữa kỳ theo quyết định của M4 | Bổ sung nhu cầu hàng trưng bày và tồn ban đầu ngoài kế hoạch kỳ | Bộ phận kế hoạch |

## 8. Quy tắc nghiệp vụ

| Mã | Quy tắc | Nguồn |
|---|---|---|
| R1 | Model mới ra mắt không dự báo theo lịch sử bán của model cũ cùng dòng | (ước lượng) — cần xác minh |
| R2 | Kế hoạch nhu cầu chỉ có hiệu lực với M2 sau khi được phê duyệt | (ước lượng) — cần xác minh |
| R3 | Cửa hàng được đề xuất điều chỉnh nhưng không có quyền tự quyết lượng nhập | (ước lượng) — cần xác minh |
| R4 | Nhu cầu hàng trưng bày của cửa hàng mới tính tách khỏi nhu cầu bán | (ước lượng) — cần xác minh |

Bốn quy tắc đều chưa có nguồn công khai. Toàn bộ đưa vào bảng giả định Chương 4 và hỏi
lại ở buổi khảo sát 23/08 (câu Q1 trong danh sách câu hỏi mở của nhóm quản lý).

## 9. Chỉ số đo lường

(chưa hoàn thiện — chốt cách đo ở bản v2)

## 10. Hệ thống và biểu mẫu liên quan

| Tên | Loại | Ghi chú |
|---|---|---|
| ERP | Hệ thống | Nguồn dữ liệu bán, tồn, hàng đang về |
| Hệ thống báo cáo bán hàng | Hệ thống | Số liệu theo model và theo cửa hàng |
| Biểu mẫu kế hoạch nhu cầu kỳ | Biểu mẫu | Chưa quan sát được — (chưa xác minh) |
| Biểu mẫu đề xuất điều chỉnh của cửa hàng | Biểu mẫu | Chưa quan sát được — (chưa xác minh) |

## 11. Điểm nghẽn quan sát được

(chưa hoàn thiện — điền ở bản v2 sau khi rà lại bảng bước)

## 12. Nguồn tham chiếu

| Nguồn | Loại | Trạng thái |
|---|---|---|
| Phân rã 12 quy trình theo ba lớp | Tài liệu nội bộ nhóm | Đã có |
| Phạm vi nhóm quy trình quản lý | Tài liệu nội bộ nhóm | Đã có |
| Buổi khảo sát tại cửa hàng — câu Q1 | Phỏng vấn | Dự kiến 23/08, phụ trách Hưng |

> Hồ sơ này dựng từ mô hình hoạch định nhu cầu bán lẻ phổ biến và quan sát bên ngoài,
> **không phải quy trình chuẩn do MWG ban hành**. M1 là quy trình nội bộ khối văn phòng
> nên khảo sát tại cửa hàng chỉ xác minh được phần giao diện với cửa hàng (bước 7 và G4).
