# M4 — Mạng lưới cửa hàng

**Lớp:** quản lý
**Người lập:** Nguyễn Thị Hồng Phúc · **Phiên bản:** v2 (hoàn thiện)
**Có mô hình BPMN:** không

## 1. Mục đích

Quyết định mở, giữ, chuyển địa điểm hay đóng từng điểm bán, dựa trên hiệu quả thực tế của
điểm bán đó và độ phủ của mạng lưới. Đây là quy trình có nhịp chậm nhất trong bốn quy
trình quản lý nhưng hệ quả lớn nhất: một quyết định sai về điểm bán kéo theo chi phí thuê
mặt bằng, chi phí hạ tầng và chi phí nhân sự trong nhiều tháng.

Với chuỗi bán lẻ điện thoại và laptop, mật độ điểm bán vừa là lợi thế cạnh tranh vừa là
rủi ro tự cạnh tranh nội bộ — hai cửa hàng cùng thương hiệu quá gần nhau sẽ chia sẻ cùng
một tệp khách. Cân bằng giữa độ phủ và hiệu quả từng điểm là bài toán trung tâm của M4.

## 2. Phạm vi

- **Bắt đầu từ:** có kế hoạch mở rộng mạng lưới, hoặc tới kỳ rà soát hiệu quả điểm bán,
  hoặc có tín hiệu bất thường từ một điểm bán cụ thể.
- **Kết thúc khi:** quyết định mở / giữ / chuyển / đóng được phê duyệt và chuyển sang các
  quy trình thực thi · đề xuất bị bác và điểm bán giữ nguyên hiện trạng.
- **Không bao gồm:** thi công và mua sắm thiết bị cho cửa hàng (S3); tuyển và đào tạo
  nhân sự (S1); nhập hàng ban đầu cho cửa hàng mới (M1 và M3).

## 3. Actor và vai trò

| Actor | Loại | Trách nhiệm chính |
|---|---|---|
| Bộ phận phát triển mạng lưới | Nội bộ | Khảo sát địa điểm, lập hồ sơ đề xuất, theo dõi hiệu quả điểm bán |
| Bộ phận tài chính | Nội bộ | Thẩm định hiệu quả tài chính, điểm hòa vốn, dòng tiền |
| Ban lãnh đạo | Nội bộ | Phê duyệt quyết định mở, chuyển, đóng |
| Quản lý vùng | Nội bộ | Cung cấp đánh giá thực địa, đề xuất từ tuyến dưới |
| Quản lý cửa hàng | Nội bộ | Báo cáo tình hình điểm bán, giải trình khi bị rà soát |
| **Chủ mặt bằng** | Bên ngoài | Đàm phán và ký hợp đồng thuê, gia hạn hoặc chấm dứt |
| Hệ thống báo cáo bán hàng | Hệ thống | Doanh thu, lưu lượng khách, hiệu quả theo điểm bán |

Chủ mặt bằng là actor bên ngoài quyết định phần lớn tiến độ: điều khoản thuê và thời điểm
hết hạn hợp đồng thường là ràng buộc cứng hơn cả kết quả kinh doanh của điểm bán.

## 4. Đầu vào và đầu ra

| Loại | Tên | Từ đâu / đi đâu | Bắt buộc |
|---|---|---|---|
| Đầu vào | Báo cáo hiệu quả theo điểm bán | Hệ thống báo cáo bán hàng | Có |
| Đầu vào | Bản đồ độ phủ mạng lưới hiện tại | Bộ phận phát triển mạng lưới | Có |
| Đầu vào | Hồ sơ mặt bằng ứng viên | Bộ phận phát triển mạng lưới | Chỉ khi mở mới |
| Đầu vào | Thời hạn và điều khoản hợp đồng thuê hiện hành | Chủ mặt bằng | Có |
| Đầu vào | Ngân sách đầu tư điểm bán của kỳ | Ban lãnh đạo | Có |
| Đầu ra | Quyết định mở / giữ / chuyển / đóng | → S1, S3, M1, M3 | Có |
| Đầu ra | Danh sách điểm bán đang hoạt động | → M1, M3 | Có |
| Đầu ra | Hồ sơ thẩm định điểm bán | → lưu nội bộ | Có |
| Đầu ra | Kế hoạch xử lý tồn kho và nhân sự khi đóng điểm | → M3, S1 | Chỉ khi đóng |

## 5. Các bước thực hiện

| # | Bước | Actor | Đầu vào | Đầu ra | Ghi chú |
|---|---|---|---|---|---|
| 1 | Xác định loại việc trong kỳ | Bộ phận phát triển mạng lưới | Kế hoạch mở rộng, lịch rà soát, tín hiệu bất thường | Loại việc đã xác định | → G1 |
| 2 | Trích báo cáo hiệu quả theo điểm bán | Hệ thống | Dữ liệu bán theo điểm | Bảng xếp hạng hiệu quả | Tự động |
| 3 | Lọc các điểm bán dưới ngưỡng hiệu quả | Bộ phận phát triển mạng lưới | Bảng xếp hạng | Danh sách điểm cần rà soát | → G2 |
| 4 | Thu thập giải trình từ quản lý cửa hàng và quản lý vùng | Quản lý cửa hàng, quản lý vùng | Danh sách điểm cần rà soát | Giải trình nguyên nhân | |
| 5 | Phân loại nguyên nhân kém hiệu quả | Bộ phận phát triển mạng lưới | Giải trình, số liệu | Nguyên nhân do vận hành hay do địa điểm | → G3 |
| 6 | Khảo sát mặt bằng ứng viên | Bộ phận phát triển mạng lưới | Yêu cầu mở mới hoặc chuyển địa điểm | Hồ sơ mặt bằng | |
| 7 | Đánh giá độ phủ và mức tự cạnh tranh nội bộ | Bộ phận phát triển mạng lưới | Bản đồ mạng lưới, hồ sơ mặt bằng | Kết luận về độ phủ | → G4 |
| 8 | Thẩm định hiệu quả tài chính dự kiến | Bộ phận tài chính | Hồ sơ mặt bằng, giả định doanh thu | Điểm hòa vốn dự kiến | → G5 |
| 9 | Đàm phán điều khoản thuê với chủ mặt bằng | Bộ phận phát triển mạng lưới | Hồ sơ mặt bằng | Điều khoản dự kiến | → G6 |
| 10 | Lập hồ sơ trình phê duyệt | Bộ phận phát triển mạng lưới | Toàn bộ kết quả thẩm định | Hồ sơ trình | → G7 |
| 11 | Phê duyệt quyết định | Ban lãnh đạo | Hồ sơ trình | Quyết định | → G8 |
| 12 | Chuyển quyết định sang các quy trình thực thi | Bộ phận phát triển mạng lưới | Quyết định đã duyệt | Yêu cầu tới S1, S3, M1, M3 | Kích hoạt lớp hỗ trợ |
| 13 | Lập kế hoạch xử lý tồn kho và nhân sự khi đóng điểm | Bộ phận phát triển mạng lưới | Quyết định đóng | Kế hoạch chuyển tồn và bố trí lại nhân sự | Chỉ nhánh đóng, → M3 và S1 |
| 14 | Theo dõi điểm bán mới sau khai trương | Bộ phận phát triển mạng lưới | Số liệu bán sau khai trương | Đánh giá so với dự kiến | → G9 |

## 6. Điểm ra quyết định

| # | Câu hỏi quyết định | Điều kiện | Nhánh kết quả | Ai quyết |
|---|---|---|---|---|
| G1 | Loại việc trong kỳ là gì? | Mở mới / rà soát định kỳ / xử lý tín hiệu bất thường | Mở mới → bước 6 · Rà soát → bước 2 · Bất thường → bước 4 | Bộ phận phát triển mạng lưới |
| G2 | Điểm bán có dưới ngưỡng hiệu quả? | So với ngưỡng theo nhóm điểm bán | Dưới → bước 4 · Đạt → giữ nguyên, đóng kỳ rà soát | Bộ phận phát triển mạng lưới |
| G3 | Nguyên nhân kém hiệu quả do vận hành hay do địa điểm? | Đối chiếu giải trình với số liệu lưu lượng khách | Vận hành → chuyển quản lý vùng xử lý, giữ điểm · Địa điểm → xét chuyển hoặc đóng | Bộ phận phát triển mạng lưới |
| G4 | Địa điểm có gây tự cạnh tranh với điểm bán hiện có? | Khoảng cách và mức chồng lấn tệp khách | Có → cân nhắc lại hoặc loại · Không → bước 8 | Bộ phận phát triển mạng lưới |
| G5 | Hiệu quả tài chính dự kiến có đạt ngưỡng? | Điểm hòa vốn trong thời hạn chấp nhận được | Đạt → bước 9 · Không đạt → loại hồ sơ mặt bằng | Bộ phận tài chính |
| G6 | Chủ mặt bằng có chấp nhận điều khoản? | Kết quả đàm phán | Chấp nhận → bước 10 · Không → tìm mặt bằng khác, quay lại bước 6 | **Chủ mặt bằng** |
| G7 | Đề xuất có vượt ngân sách đầu tư kỳ? | So với ngân sách kỳ | Vượt → hoãn sang kỳ sau hoặc trình ngoại lệ · Không → bước 11 | Bộ phận tài chính |
| G8 | Ban lãnh đạo quyết định thế nào? | Đánh giá tổng thể | Mở → bước 12 · Giữ → đóng hồ sơ · Chuyển → bước 12 và 13 · Đóng → bước 13 | **Ban lãnh đạo** |
| G9 | Điểm bán mới có đạt kỳ vọng sau thời gian theo dõi? | So sánh thực tế với dự kiến ở bước 8 | Đạt → đưa vào rà soát định kỳ bình thường · Không → kích hoạt rà soát sớm | Bộ phận phát triển mạng lưới |

M4 **không được chọn để mô hình hóa BPMN**, nên bảng này không cần vượt mốc 7 dòng. Chín
điểm quyết định ở trên mô tả trong Chương 3 bằng lời và bằng bảng.

## 7. Ngoại lệ và xử lý

| Mã | Tình huống ngoại lệ | Cách xử lý | Ai xử lý |
|---|---|---|---|
| E1 | Chủ mặt bằng đơn phương chấm dứt hoặc tăng giá thuê đột ngột | Kích hoạt tìm mặt bằng thay thế trong cùng khu vực, ưu tiên giữ độ phủ | Bộ phận phát triển mạng lưới |
| E2 | Điểm bán mới không đạt kỳ vọng ngay trong giai đoạn đầu | Rà soát sớm trước kỳ, phân biệt nguyên nhân vận hành và địa điểm | Bộ phận phát triển mạng lưới |
| E3 | Quyết định đóng điểm nhưng tồn kho còn lớn | Điều chuyển tồn sang điểm bán lân cận trước ngày đóng (M3) | Bộ phận điều phối tồn kho |
| E4 | Nhân sự của điểm bán đóng cửa chưa có nơi bố trí | Phối hợp S1 bố trí lại sang điểm bán khác trong vùng | S1, quản lý vùng |
| E5 | Khu vực có thay đổi quy hoạch ảnh hưởng lưu lượng khách | Đưa vào diện rà soát bất thường, không đợi tới kỳ | Bộ phận phát triển mạng lưới |

## 8. Quy tắc nghiệp vụ

| Mã | Quy tắc | Nguồn |
|---|---|---|
| R1 | Quyết định mở, chuyển hoặc đóng điểm bán thuộc thẩm quyền ban lãnh đạo, không phân cấp xuống vùng | (ước lượng) — cần xác minh |
| R2 | Điểm bán kém hiệu quả do nguyên nhân vận hành thì xử lý vận hành trước, chưa xét đóng | (ước lượng) — cần xác minh |
| R3 | Tồn kho phải được xử lý xong trước ngày đóng điểm bán | (ước lượng) — cần xác minh |
| R4 | Mở điểm bán mới phải kích hoạt S1 và S3 trước ngày khai trương một khoảng đủ dài | (ước lượng) — cần xác minh |

Bốn quy tắc đều chưa có nguồn công khai, đưa vào bảng giả định Chương 4. M4 là quy trình
cấp tập đoàn nên buổi khảo sát tại một cửa hàng gần như không xác minh được — cần nói rõ
giới hạn này trong Chương 3.

## 9. Chỉ số đo lường

| Chỉ số | Đơn vị | Cách đo | Giá trị ghi nhận | Nguồn |
|---|---|---|---|---|
| Số điểm bán đang hoạt động của chuỗi | cửa hàng | Số công bố trong báo cáo thường niên MWG | (chờ bổ sung — kèm ngày truy cập) | tài liệu công khai |
| Thời gian từ khi duyệt mở điểm bán tới ngày khai trương | tháng | Hỏi bộ phận phát triển mạng lưới | (chưa xác minh — không có kênh tiếp cận) | ngoài tầm khảo sát |
| Thời gian đạt điểm hòa vốn của điểm bán mới | tháng | Dữ liệu tài chính nội bộ | (chưa xác minh) | ngoài tầm khảo sát |
| Tỷ lệ điểm bán bị đưa vào diện rà soát mỗi kỳ | % | Dữ liệu nội bộ | (chưa xác minh) | ngoài tầm khảo sát |
| Số điểm ra quyết định trong quy trình | điểm | Đếm từ bảng mục 6 | 9 | phân tích hồ sơ |

Chỉ số đầu tiên là chỉ số duy nhất có khả năng lấy được **từ nguồn công khai** — báo cáo
thường niên của MWG có công bố số lượng điểm bán theo chuỗi. Cần bổ sung kèm ngày truy
cập trước khi nộp. Ba chỉ số giữa cần dữ liệu nội bộ cấp tập đoàn, giữ `(chưa xác minh)`.

M4 là hồ sơ có ít chỉ số đo được nhất trong bốn hồ sơ quản lý — đây là hệ quả trực tiếp
của việc chọn phạm vi khảo sát ở cấp cửa hàng, và cần nêu thẳng ở Chương 3.

## 10. Hệ thống và biểu mẫu liên quan

| Tên | Loại | Ghi chú |
|---|---|---|
| Hệ thống báo cáo bán hàng | Hệ thống | Hiệu quả theo điểm bán |
| Hồ sơ thẩm định mặt bằng | Biểu mẫu | Chưa quan sát được — (chưa xác minh) |
| Hợp đồng thuê mặt bằng | Biểu mẫu | Không tiếp cận được — (chưa xác minh) |
| Tờ trình phê duyệt điểm bán | Biểu mẫu | Chưa quan sát được — (chưa xác minh) |

## 11. Điểm nghẽn quan sát được

| # | Điểm nghẽn | Vì sao là nghẽn | Nhóm lãng phí | Bằng chứng cần có |
|---|---|---|---|---|
| B1 | Bước 9 — đàm phán điều khoản thuê với chủ mặt bằng | Phụ thuộc hoàn toàn actor bên ngoài; hồ sơ mặt bằng nằm chờ không xác định thời hạn | **Hold** | (chưa xác minh) |
| B2 | G6 — không thỏa thuận được, phải quay lại bước 6 tìm mặt bằng khác | Toàn bộ công khảo sát, đánh giá độ phủ và thẩm định tài chính đã làm bị bỏ phí | **Overdo** | (chưa xác minh) |
| B3 | Bước 4 — thu thập giải trình từ nhiều cấp trước khi kết luận | Chuỗi hỏi qua quản lý cửa hàng rồi quản lý vùng kéo dài kỳ rà soát | **Hold** | (chưa xác minh) |
| B4 | Bước 13 — xử lý tồn kho khi đóng điểm bán | Phát sinh điều chuyển toàn bộ tồn sang điểm khác, là vận chuyển thuần túy không tạo giá trị | **Move** | Đối chiếu với M3 |
| B5 | Bước 14 — chỉ phát hiện điểm bán mới kém hiệu quả sau một thời gian theo dõi | Chi phí thuê và vận hành đã phát sinh trước khi có tín hiệu để can thiệp | **Hold** | (chưa xác minh) |

Toàn bộ năm điểm đều ở trạng thái `(chưa xác minh)` trừ B4 — đây là hồ sơ có mức chắc
chắn thấp nhất trong bốn hồ sơ quản lý. Khi đưa vào Issue Register, **phải ghi rõ mức độ
tin cậy thấp** thay vì xếp ngang hàng với các phát hiện đã có bằng chứng quan sát.

B4 liên thông trực tiếp với M3: quyết định đóng điểm bán ở M4 tạo ra một đợt điều chuyển
lớn ở M3, nhưng khối lượng đó không nằm trong kế hoạch điều chuyển thông thường.

Năm điểm B1–B5 đánh số tiếp từ IR-14 ở nhánh `analysis/dinh-tinh`, kèm ghi chú mức tin cậy.

## 12. Nguồn tham chiếu

| Nguồn | Loại | Trạng thái |
|---|---|---|
| Phạm vi nhóm quy trình quản lý | Tài liệu nội bộ nhóm | Đã có |
| Phân rã 12 quy trình theo ba lớp | Tài liệu nội bộ nhóm | Đã có |
| Báo cáo thường niên MWG về số lượng điểm bán | Tài liệu công khai | Chờ bổ sung kèm ngày truy cập |

> Hồ sơ này dựng từ thực hành phát triển mạng lưới bán lẻ phổ biến và quan sát bên ngoài,
> **không phải quy trình chuẩn do MWG ban hành**. M4 là quy trình cấp tập đoàn — đây là hồ
> sơ có tỷ lệ nội dung (ước lượng) cao nhất trong bốn quy trình quản lý, và Chương 3 phải
> nêu rõ giới hạn đó thay vì trình bày như quy trình đã xác minh.
