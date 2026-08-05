# M3 — Kho và điều chuyển

**Lớp:** quản lý
**Người lập:** Nguyễn Thị Hồng Phúc · **Phiên bản:** v1 (draft)
**Có mô hình BPMN:** có — sẽ dựng ở nhánh `model/bpmn-quan-ly-ho-tro`

## 1. Mục đích

Đưa hàng về đúng nơi cần bán và giữ cho tồn kho trên hệ thống khớp tồn thực tế. Ba quy
trình bán C1, C2, C3 đều cam kết giao hàng cho khách dựa trên con số tồn khả dụng mà M3
chịu trách nhiệm — con số đó sai thì lời hứa với khách sai theo.

M3 cũng là nơi chữa cháy cho hai tình huống đã ghi nhận ở lớp cốt lõi: hết hàng sau khi
hồ sơ trả góp đã duyệt (C3, gateway G8) và hết máy để đổi bảo hành (C4, ngoại lệ E2). Cả
hai đều rơi vào nhánh điều chuyển gấp giữa cửa hàng.

## 2. Phạm vi

- **Bắt đầu từ:** có lệnh nhập từ M2, hoặc có yêu cầu điều chuyển phát sinh từ cửa hàng,
  hoặc tới kỳ kiểm kê.
- **Kết thúc khi:** hàng nằm đúng vị trí và tồn hệ thống khớp tồn thực tế · yêu cầu điều
  chuyển bị từ chối vì không có nguồn · chênh lệch kiểm kê đã được xử lý và đóng.
- **Không bao gồm:** quyết định mua bao nhiêu (M1); nghiệm thu chất lượng đối với nhà
  cung cấp (M2); xuất bán cho khách tại quầy (C1–C3).

## 3. Actor và vai trò

| Actor | Loại | Trách nhiệm chính |
|---|---|---|
| Nhân viên kho tổng | Nội bộ | Nhận hàng, kiểm đếm, nhập kho, lập lệnh xuất chuyển |
| Nhân viên kho cửa hàng | Nội bộ | Nhận hàng về cửa hàng, kiểm đếm, xác nhận, kiểm kê |
| Quản lý cửa hàng | Nội bộ | Tạo và duyệt yêu cầu điều chuyển ở cấp cửa hàng |
| Bộ phận điều phối tồn kho | Nội bộ | Phân bổ hàng về cửa hàng, chọn cửa hàng nguồn, duyệt điều chuyển |
| **Đơn vị vận chuyển** | Bên ngoài | Vận chuyển giữa kho tổng và cửa hàng, giữa hai cửa hàng |
| Hệ thống ERP | Hệ thống | Ghi nhận tồn, sinh lệnh xuất nhập, khóa tồn khi có lệnh |

Đơn vị vận chuyển là actor bên ngoài — thời gian vận chuyển nằm ngoài kiểm soát của cửa
hàng và là thành phần chính của thời gian chờ trong nhánh điều chuyển gấp.

## 4. Đầu vào và đầu ra

| Loại | Tên | Từ đâu / đi đâu | Bắt buộc |
|---|---|---|---|
| Đầu vào | Lô hàng đã nghiệm thu đạt kèm biên bản | M2 | Có |
| Đầu vào | Kế hoạch phân bổ hàng về cửa hàng | M1, bộ phận điều phối | Có |
| Đầu vào | Yêu cầu điều chuyển từ cửa hàng | Quản lý cửa hàng | Không |
| Đầu vào | Danh sách cửa hàng đang hoạt động | M4 | Có |
| Đầu vào | Lịch kiểm kê định kỳ | Bộ phận điều phối | Có |
| Đầu ra | Tồn kho khả dụng theo từng cửa hàng | → C1, C2, C3 | Có |
| Đầu ra | Phiếu nhập kho, phiếu xuất chuyển | → ERP | Có |
| Đầu ra | Hàng đã về đúng cửa hàng | → C1, C2, C3 | Có |
| Đầu ra | Biên bản chênh lệch kiểm kê | → bộ phận điều phối, ban lãnh đạo | Chỉ khi có chênh lệch |
| Đầu ra | Cảnh báo tồn ứ hoặc tồn thiếu theo cửa hàng | → M1 | Có |

## 5. Các bước thực hiện

| # | Bước | Actor | Đầu vào | Đầu ra | Ghi chú |
|---|---|---|---|---|---|
| 1 | Tiếp nhận và phân loại sự kiện kích hoạt | Bộ phận điều phối | Lệnh nhập / yêu cầu điều chuyển / lịch kiểm kê | Loại luồng đã xác định | → G1, ba nhánh |
| 2 | Nhận hàng từ nhà cung cấp tại điểm nhận | NV kho tổng | Lô hàng, biên bản nghiệm thu từ M2 | Hàng đã tiếp nhận | |
| 3 | Đối chiếu chứng từ với PO | NV kho tổng | Chứng từ giao hàng, PO | Kết luận khớp / lệch | → G2 |
| 4 | Kiểm đếm thực tế và ghi nhận tình trạng | NV kho tổng | Lô hàng | Số lượng thực nhận | → G3 |
| 5 | Nhập kho, gán vị trí lưu, cập nhật tồn | NV kho tổng, ERP | Hàng đạt | Tồn kho tổng cập nhật | |
| 6 | Phân bổ hàng về cửa hàng theo kế hoạch | Bộ phận điều phối | Tồn kho tổng, kế hoạch phân bổ | Danh sách phân bổ | → G4 |
| 7 | Lập lệnh xuất chuyển và khóa tồn | ERP | Danh sách phân bổ | Lệnh xuất, tồn bị khóa | Tránh bán trùng phần đã cam kết |
| 8 | Đóng gói và bàn giao cho đơn vị vận chuyển | NV kho tổng | Lệnh xuất | Kiện hàng đã bàn giao | |
| 9 | Vận chuyển tới cửa hàng đích | Đơn vị vận chuyển | Kiện hàng | Hàng tới cửa hàng | Khâu chờ, ngoài kiểm soát cửa hàng |
| 10 | Cửa hàng nhận, kiểm đếm, xác nhận trên hệ thống | NV kho cửa hàng | Kiện hàng, lệnh xuất | Xác nhận nhận đủ | → G6 |
| 11 | Cập nhật tồn khả dụng tại cửa hàng | ERP | Xác nhận nhận | Tồn cửa hàng cập nhật | Đầu vào cho C1–C3 |
| 12 | Tiếp nhận yêu cầu điều chuyển giữa cửa hàng | Bộ phận điều phối | Yêu cầu từ quản lý cửa hàng | Yêu cầu đã ghi nhận | → G7 |
| 13 | Dò tìm cửa hàng nguồn còn tồn khả dụng | ERP, bộ phận điều phối | Tồn theo cửa hàng | Danh sách cửa hàng nguồn | → G8 |
| 14 | Trình duyệt điều chuyển | Bộ phận điều phối | Yêu cầu, cửa hàng nguồn | Quyết định duyệt | → G9, G10 |
| 15 | Xuất chuyển từ cửa hàng nguồn | NV kho cửa hàng nguồn | Lệnh điều chuyển | Hàng rời cửa hàng nguồn | Quay về bước 9 |
| 16 | Thực hiện kiểm kê theo lịch | NV kho cửa hàng | Lịch kiểm kê | Số liệu kiểm kê thực tế | → G11 |
| 17 | Đối chiếu và xử lý chênh lệch | Bộ phận điều phối | Kiểm kê so với tồn hệ thống | Kết luận chênh lệch | → G12 |
| 18 | Lập biên bản chênh lệch và điều chỉnh tồn | Bộ phận điều phối, ERP | Biên bản | Tồn hệ thống đã điều chỉnh | |
| 19 | Tổng hợp cảnh báo tồn ứ và tồn thiếu | Bộ phận điều phối | Tồn theo cửa hàng | Cảnh báo | → M1 kỳ sau |

## 6. Điểm ra quyết định

| # | Câu hỏi quyết định | Điều kiện | Nhánh kết quả | Ai quyết |
|---|---|---|---|---|
| G1 | Sự kiện kích hoạt thuộc loại nào? | Nhập từ NCC / điều chuyển giữa cửa hàng / kiểm kê định kỳ | Nhập → bước 2 · Điều chuyển → bước 12 · Kiểm kê → bước 16 | Bộ phận điều phối |
| G2 | Chứng từ giao hàng có khớp PO? | Đối chiếu model, số lượng, đơn giá | Khớp → bước 4 · Lệch → trả lại M2 xử lý, dừng luồng nhập | NV kho tổng |
| G3 | Kiểm đếm thực tế có đạt? | Số lượng và tình trạng đúng chứng từ | Đạt → bước 5 · Không đạt → lập biên bản, chuyển M2 khiếu nại | NV kho tổng |
| G4 | Hàng đi về kho tổng hay giao thẳng cửa hàng? | Theo nhóm hàng và khoảng cách điểm bán | Kho tổng → bước 7 · Giao thẳng → bỏ qua bước 7, sang bước 9 | Bộ phận điều phối |
| G5 | Cửa hàng đích còn sức chứa trưng bày và lưu trữ? | Sức chứa so với lượng phân bổ | Còn → giữ nguyên phân bổ · Không → phân bổ lại sang cửa hàng khác | Bộ phận điều phối |
| G6 | Cửa hàng nhận xác nhận có khớp lệnh xuất? | Đối chiếu số lượng và IMEI | Khớp → bước 11 · Lệch → lập biên bản thiếu hụt vận chuyển | NV kho cửa hàng |
| G7 | Yêu cầu điều chuyển có phải hàng gấp cho đơn đã chốt? | Gắn với đơn C3 đã duyệt hoặc ca đổi máy C4 | Gấp → ưu tiên xử lý trước · Thường → xếp theo lịch điều chuyển | Bộ phận điều phối |
| G8 | Có cửa hàng nguồn nào còn tồn khả dụng? | Tồn khả dụng lớn hơn mức tồn tối thiểu của cửa hàng nguồn | Có → bước 14 · Không → từ chối yêu cầu, báo cửa hàng và báo M1 | ERP, bộ phận điều phối |
| G9 | Giá trị lô điều chuyển có vượt ngưỡng phải duyệt? | So với ngưỡng phân quyền | Vượt → trình cấp trên · Không → điều phối tự duyệt | Bộ phận điều phối |
| G10 | Cấp duyệt có chấp thuận điều chuyển? | Cân nhắc tồn của cửa hàng nguồn | Duyệt → bước 15 · Không → từ chối, phản hồi lý do | Cấp duyệt theo ngưỡng |
| G11 | Kiểm kê có phát hiện chênh lệch? | Tồn thực tế so với tồn hệ thống | Có chênh → bước 17 · Không → đóng kỳ kiểm kê | NV kho cửa hàng |
| G12 | Chênh lệch có vượt ngưỡng phải lập biên bản? | So với ngưỡng cho phép | Vượt → bước 18, lập biên bản và truy nguyên nhân · Không → điều chỉnh tồn trực tiếp | Bộ phận điều phối |

**Mười hai điểm quyết định — vượt xa mốc 7 gateway** yêu cầu cho mô hình BPMN. Khi vẽ, G1
là gateway ba nhánh; đơn vị vận chuyển vẽ thành lane riêng vì là bên ngoài.

## 7. Ngoại lệ và xử lý

| Mã | Tình huống ngoại lệ | Cách xử lý | Ai xử lý |
|---|---|---|---|
| E1 | Hàng hư hại trong quá trình vận chuyển | Lập biên bản với đơn vị vận chuyển, không nhập tồn khả dụng | NV kho cửa hàng |
| E2 | Cửa hàng nguồn từ chối xuất vì sắp có khách chốt đơn | Điều phối chọn cửa hàng nguồn khác; nếu không còn thì từ chối yêu cầu | Bộ phận điều phối |
| E3 | Hàng điều chuyển tới nơi thì đơn gốc đã hủy | Giữ hàng tại cửa hàng đích, cập nhật tồn bình thường | Quản lý cửa hàng |
| E4 | Lệch IMEI giữa lệnh xuất và hàng thực nhận | Truy lại từ cửa hàng nguồn, không xác nhận cho tới khi khớp | NV kho cửa hàng |
| E5 | ERP gián đoạn, không khóa được tồn khi lập lệnh xuất | Ghi nhận thủ công và đối chiếu bù khi hệ thống hoạt động lại | Bộ phận điều phối |
| E6 | Chênh lệch kiểm kê lặp lại nhiều kỳ tại cùng một cửa hàng | Kiểm kê đột xuất và rà soát quy trình xuất nhập tại cửa hàng đó | Bộ phận điều phối |

## 8. Quy tắc nghiệp vụ

| Mã | Quy tắc | Nguồn |
|---|---|---|
| R1 | Tồn đã bị khóa theo lệnh xuất không được tính vào tồn khả dụng để bán | (ước lượng) — cần xác minh |
| R2 | Hàng chưa được cửa hàng xác nhận nhận thì chưa tính vào tồn khả dụng của cửa hàng đó | (ước lượng) — cần xác minh |
| R3 | Cửa hàng nguồn phải giữ lại mức tồn tối thiểu, không xuất hết cho điều chuyển | (ước lượng) — cần xác minh |
| R4 | Điều chuyển phục vụ đơn đã chốt được ưu tiên hơn điều chuyển cân bằng tồn | (ước lượng) — cần xác minh |
| R5 | Mỗi máy quản lý theo IMEI, không quản lý theo số lượng gộp | Quan sát — suy ra từ C1 và C4 |

R1–R4 đưa vào bảng giả định Chương 4, hỏi ở câu Q2 và Q3 trong danh sách câu hỏi mở.

## 9. Chỉ số đo lường

(chưa hoàn thiện — chốt cách đo ở bản v2)

## 10. Hệ thống và biểu mẫu liên quan

| Tên | Loại | Ghi chú |
|---|---|---|
| ERP | Hệ thống | Tồn kho, lệnh xuất nhập, khóa tồn |
| Phiếu nhập kho | Biểu mẫu | Chưa quan sát được — (chưa xác minh) |
| Phiếu xuất chuyển kho | Biểu mẫu | Ảnh mẫu nên chụp nếu quan sát được tại cửa hàng |
| Biên bản kiểm kê | Biểu mẫu | Chưa quan sát được — (chưa xác minh) |
| Biên bản chênh lệch | Biểu mẫu | Chỉ phát sinh khi kiểm kê lệch |

## 11. Điểm nghẽn quan sát được

(chưa hoàn thiện — điền ở bản v2 sau khi rà lại bảng bước)

## 12. Nguồn tham chiếu

| Nguồn | Loại | Trạng thái |
|---|---|---|
| Phạm vi nhóm quy trình quản lý | Tài liệu nội bộ nhóm | Đã có |
| Hồ sơ C3 — gateway G8 và ngoại lệ E6 | Tài liệu nội bộ nhóm | Đã có |
| Hồ sơ C4 — ngoại lệ E2 | Tài liệu nội bộ nhóm | Đã có |
| Buổi khảo sát tại cửa hàng — câu Q2, Q3, Q4 | Phỏng vấn | Dự kiến 23/08, phụ trách Hưng |

> Hồ sơ này dựng từ nghiệp vụ kho bán lẻ phổ biến và quan sát bên ngoài, **không phải quy
> trình chuẩn do MWG ban hành**. Phần cửa hàng (bước 10, 12, 16) có thể xác minh trực tiếp
> ở buổi khảo sát; phần kho tổng và điều phối thì không, và sẽ ở lại trạng thái (ước lượng).
