# C3 — Bán trả góp

**Lớp:** cốt lõi
**Người lập:** Nguyễn Ngọc Danh · **Phiên bản:** v2 (hoàn thiện)
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

| # | Bước | Actor | Đầu vào | Đầu ra | Ghi chú |
|---|---|---|---|---|---|
| 1 | Tiếp nhận yêu cầu trả góp | NV tư vấn trả góp | Sản phẩm đã chọn từ C1 | Yêu cầu được ghi nhận | Chuyển tiếp từ G3 của C1 |
| 2 | Kiểm tra điều kiện sơ bộ của khách | NV tư vấn trả góp | Độ tuổi, giấy tờ khách đang có | Kết luận đủ / không đủ điều kiện sơ bộ | → G1 |
| 3 | Tư vấn và so sánh các gói trả góp | NV tư vấn trả góp | Bảng gói của các bên cấp tín dụng | Khách chọn được gói | → G2 |
| 4 | Thu thập và kiểm tra giấy tờ | NV tư vấn trả góp | CCCD, giấy tờ phụ | Bộ hồ sơ | → G3 |
| 5 | Chụp, nhập hồ sơ lên cổng trả góp | NV tư vấn trả góp | Bộ hồ sơ | Hồ sơ điện tử đã gửi | |
| 6 | Chờ thẩm định tín dụng | Công ty tài chính | Hồ sơ điện tử | Kết quả thẩm định | **Khâu chờ dài nhất** → B1 |
| 7 | Nhận và thông báo kết quả cho khách | NV tư vấn trả góp | Kết quả thẩm định | Khách biết kết quả | → G4 |
| 8 | Bổ sung hồ sơ nếu bị yêu cầu | Khách + NV tư vấn | Yêu cầu bổ sung | Hồ sơ đã bổ sung | Quay lại bước 6 → G5 |
| 9 | Xác nhận điều khoản và số tiền trả trước | NV tư vấn + Khách | Thông báo duyệt | Khách đồng ý điều khoản | → G6 |
| 10 | Thu khoản trả trước | NV thu ngân | Số tiền trả trước | Biên nhận | → G7 |
| 11 | Ký hợp đồng trả góp | Khách + Công ty tài chính | Hợp đồng | Hợp đồng đã ký | Bản giấy hoặc ký điện tử |
| 12 | Lập đơn hàng trên POS | NV tư vấn | Hợp đồng đã ký | Đơn hàng | |
| 13 | Lấy hàng, khui hộp, kiểm tra cùng khách | NV kho + Khách | Đơn hàng | Máy được xác nhận | Giống bước 8–9 của C1 |
| 14 | Xuất hóa đơn, phiếu bảo hành, bàn giao máy | Thu ngân + NV tư vấn | Đơn hàng | Hóa đơn, phiếu bảo hành gắn IMEI | Đầu vào cho C4 |
| 15 | Đồng bộ dữ liệu sang ERP và bên cấp tín dụng | Hệ thống | Đơn hoàn tất | Tồn kho trừ, hợp đồng có hiệu lực | Tự động |

## 6. Điểm ra quyết định

| # | Câu hỏi quyết định | Điều kiện | Nhánh kết quả | Ai quyết |
|---|---|---|---|---|
| G1 | Khách có đủ điều kiện sơ bộ? | Đủ tuổi, có giấy tờ tùy thân hợp lệ | Đủ → bước 3 · Không → tư vấn trả thẳng hoặc kết thúc | NV tư vấn |
| G2 | Khách chọn bên cấp tín dụng nào? | Mỗi bên có điều kiện và lãi suất riêng | Mỗi nhánh gửi hồ sơ tới một bên khác nhau | Khách hàng |
| G3 | Bộ hồ sơ đã đủ giấy tờ theo gói đã chọn? | Đối chiếu danh mục giấy tờ của gói | Đủ → bước 5 · Thiếu → yêu cầu khách bổ sung tại chỗ | NV tư vấn |
| G4 | Kết quả thẩm định là gì? | Duyệt / Từ chối / Yêu cầu bổ sung | Duyệt → bước 9 · Từ chối → G4b · Bổ sung → bước 8 | **Công ty tài chính** |
| G4b | Khách có chuyển sang trả thẳng khi bị từ chối? | Khách quyết định | Có → quay về C1 · Không → kết thúc, khách rời đi | Khách hàng |
| G5 | Hồ sơ bổ sung có được chấp nhận? | Thẩm định lại | Được → bước 9 · Không → G4b | Công ty tài chính |
| G6 | Khách có đồng ý điều khoản cuối (lãi suất, kỳ hạn, phí)? | Khách đọc và xác nhận | Đồng ý → bước 10 · Không → hủy, kết thúc | Khách hàng |
| G7 | Khoản trả trước đã thu đủ? | Số tiền thực thu = số tiền theo gói | Đủ → bước 11 · Chưa đủ → xử lý theo E4 | NV thu ngân |
| G8 | Sản phẩm còn tồn tại cửa hàng ở thời điểm duyệt? | Tồn khả dụng > 0 | Còn → bước 13 · Hết → điều chuyển M3 hoặc đổi model, thẩm định lại nếu đổi giá | ERP + NV tư vấn |
| G9 | Máy lấy ra có đạt tình trạng bàn giao? | Nguyên seal, đúng IMEI | Đạt → bước 14 · Không → đổi máy khác | NV kho |

**Mười điểm quyết định — vượt mốc 7 gateway** yêu cầu cho mô hình BPMN. Khi vẽ, G4 là
gateway ba nhánh, G2 là gateway nhiều nhánh theo số bên cấp tín dụng.

## 7. Ngoại lệ và xử lý

| Mã | Tình huống ngoại lệ | Cách xử lý | Ai xử lý |
|---|---|---|---|
| E1 | Cổng hồ sơ trả góp gián đoạn, không gửi được hồ sơ | Hẹn khách quay lại hoặc gọi báo kết quả sau | NV tư vấn + Quản lý |
| E2 | Thẩm định kéo dài quá thời gian khách chờ được | Khách về, nhận kết quả qua điện thoại, quay lại hoàn tất | NV tư vấn |
| E3 | Khách tự hủy giữa chừng sau khi đã gửi hồ sơ | Hủy hồ sơ trên cổng, không thu phí | NV tư vấn |
| E4 | Khách không đủ tiền trả trước tại thời điểm ký | Đổi sang gói có mức trả trước thấp hơn, thẩm định lại | NV tư vấn + Công ty tài chính |
| E5 | Giấy tờ nghi ngờ không hợp lệ | Từ chối tiếp nhận, không tự ý xác minh | NV tư vấn + Quản lý |
| E6 | Hết hàng sau khi hồ sơ đã duyệt | Điều chuyển từ cửa hàng khác (M3); nếu đổi model khác giá thì phải làm lại hồ sơ | NV tư vấn |
| E7 | Khách đã ký hợp đồng nhưng đổi ý trước khi nhận máy | Hủy hợp đồng theo quy định của bên cấp tín dụng | Công ty tài chính |

## 8. Quy tắc nghiệp vụ

| Mã | Quy tắc | Nguồn |
|---|---|---|
| R1 | Quyết định duyệt hay từ chối thuộc **bên cấp tín dụng**, cửa hàng không có quyền can thiệp | Quan sát |
| R2 | Máy chỉ được bàn giao sau khi hợp đồng đã ký và khoản trả trước đã thu đủ | Quan sát |
| R3 | Mỗi bộ hồ sơ chỉ gửi tới một bên cấp tín dụng tại một thời điểm | (chưa xác minh) |
| R4 | Đổi model sau khi duyệt mà thay đổi giá trị khoản vay thì phải thẩm định lại | (ước lượng) — cần xác minh |
| R5 | Nhân viên cửa hàng không được giữ bản gốc giấy tờ tùy thân của khách | Quan sát |
| R6 | Hợp đồng trả góp là hợp đồng giữa khách và bên cấp tín dụng; cửa hàng chỉ là điểm giới thiệu và giao hàng | Chính sách công bố |

Dòng R3 và R4 đưa vào bảng giả định Chương 4, cần hỏi lại ở câu phỏng vấn 3 và 4.

## 9. Chỉ số đo lường

| Chỉ số | Đơn vị | Cách đo | Giá trị ghi nhận | Nguồn |
|---|---|---|---|---|
| Tổng thời gian từ nộp giấy tờ đến có kết quả duyệt | phút | Hỏi nhân viên (câu phỏng vấn 3) | (chờ khảo sát 23/08) | phỏng vấn |
| Thời gian chờ thẩm định thuần (bước 6) | phút | Tách riêng khỏi tổng | (chờ khảo sát) | phỏng vấn / bấm giờ |
| Tỷ lệ hồ sơ bị yêu cầu bổ sung | % | Hỏi nhân viên (câu phỏng vấn 4) | (chờ khảo sát) | phỏng vấn |
| Số lượt chạm giữa nhân viên và khách trong toàn quy trình | lần | Đếm từ bảng bước | 15 bước, tối thiểu 8 lượt chạm | phân tích hồ sơ |

Chỉ số 2 là trọng tâm phân tích CTE ở Chương 4: đây là thời gian chờ thuần, không tạo
giá trị, và cửa hàng không kiểm soát được.

## 10. Hệ thống và biểu mẫu liên quan

| Tên | Loại | Ghi chú |
|---|---|---|
| Cổng hồ sơ trả góp | Hệ thống | Kênh trao đổi với bên cấp tín dụng |
| POS | Hệ thống | Ghi nhận đơn và khoản trả trước |
| ERP | Hệ thống | Trừ tồn, đồng bộ dữ liệu bán |
| Hợp đồng trả góp | Biểu mẫu | Ảnh mẫu cần chụp — che thông tin cá nhân |
| Bảng gói trả góp niêm yết | Biểu mẫu | Ảnh mẫu cần chụp |

## 11. Điểm nghẽn quan sát được

| # | Điểm nghẽn | Vì sao là nghẽn | Nhóm lãng phí | Bằng chứng cần có |
|---|---|---|---|---|
| B1 | Bước 6 — chờ thẩm định tín dụng | Toàn bộ quy trình dừng lại chờ actor bên ngoài; khách ngồi chờ tại cửa hàng, nhân viên bị giữ chân | **Hold** | Câu phỏng vấn 3 |
| B2 | Bước 8 — vòng lặp bổ sung hồ sơ | Quay lại bước 6, nhân đôi thời gian chờ; nguyên nhân thường do bước 4 kiểm tra chưa kỹ | **Overdo** | Câu phỏng vấn 4 |
| B3 | Bước 4–5 — nhập liệu thủ công | Chụp và nhập tay từng giấy tờ, dễ sai, phải làm lại | **Overdo** | Quan sát tại quầy |
| B4 | G8 — hết hàng sau khi đã duyệt | Toàn bộ hồ sơ có nguy cơ phải làm lại nếu đổi model khác giá | **Move** | Câu phỏng vấn 5 |

Bốn điểm này là đầu vào chính cho bảng VA/BVA/NVA của C3 (Hồng Phúc phụ trách, mục 4.3).

## 12. Nguồn tham chiếu

| Nguồn | Loại | Trạng thái |
|---|---|---|
| Buổi khảo sát tại cửa hàng TGDĐ — câu hỏi 3, 4 | Phỏng vấn | Dự kiến 23/08, phụ trách Hưng |
| Ảnh hợp đồng và bảng gói trả góp | Evidence | Chờ chụp — `evidence/anh-bieu-mau/` |
| Trang thông tin trả góp trên website TGDĐ | Tài liệu công khai | Chờ bổ sung kèm ngày truy cập |

> Hồ sơ này dựng từ quan sát bên ngoài và suy luận, **không phải quy trình chuẩn do MWG
> ban hành**. Mô hình BPMN của C3 vẽ theo đúng bảng mục 5 và mục 6 — nếu khảo sát cho kết
> quả khác thì sửa hồ sơ trước, sửa mô hình sau, và ghi vào biên bản review.
