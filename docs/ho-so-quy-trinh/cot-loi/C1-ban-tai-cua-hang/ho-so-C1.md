# C1 — Bán tại cửa hàng

**Lớp:** cốt lõi
**Người lập:** Nguyễn Ngọc Danh · **Phiên bản:** v2 (hoàn thiện)
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

| # | Bước | Actor | Đầu vào | Đầu ra | Ghi chú |
|---|---|---|---|---|---|
| 1 | Tiếp cận và chào khách | NV tư vấn | Khách vào cửa hàng | Cuộc trao đổi bắt đầu | Có thể phải chờ nếu đang bận khách khác → E1 |
| 2 | Tìm hiểu nhu cầu và ngân sách | NV tư vấn | Mô tả của khách | Nhóm sản phẩm phù hợp | |
| 3 | Giới thiệu và cho trải nghiệm máy trưng bày | NV tư vấn | Máy trưng bày | Khách thu hẹp lựa chọn | |
| 4 | Kiểm tra tồn kho model, màu, dung lượng | NV tư vấn | ERP | Kết quả còn / hết hàng | → G1 |
| 5 | Chốt sản phẩm và báo giá cuối | NV tư vấn | Bảng giá, khuyến mãi | Giá cuối cùng | → G2, → G3 |
| 6 | Tư vấn phụ kiện và gói bảo hành mở rộng | NV tư vấn | Danh mục phụ kiện | Đơn có thể tăng giá trị | Không bắt buộc → G8 |
| 7 | Lập đơn trên POS | NV tư vấn | Thông tin khách, sản phẩm | Đơn hàng nháp | |
| 8 | Lấy hàng từ kho cửa hàng | NV kho | Đơn hàng nháp | Máy nguyên seal | → G4 |
| 9 | Khui hộp, kiểm tra máy cùng khách | NV tư vấn + Khách | Máy | Máy được xác nhận đạt | Khách chứng kiến, tránh tranh chấp về sau |
| 10 | Kích hoạt máy, cài đặt cơ bản, chuyển dữ liệu | NV tư vấn | Máy, máy cũ của khách | Máy sẵn sàng dùng | Chiếm nhiều thời gian → B1 |
| 11 | Thu tiền | NV thu ngân | Đơn hàng | Giao dịch thành công | → G5, → G6 |
| 12 | Xuất hóa đơn và phiếu bảo hành | Thu ngân / POS | Giao dịch | Hóa đơn, dữ liệu bảo hành gắn IMEI | → G7. Đầu vào cho C4 |
| 13 | Bàn giao máy, phụ kiện, hộp | NV tư vấn | Máy, hóa đơn | Khách ký nhận | |
| 14 | Trừ tồn và đồng bộ dữ liệu bán | ERP | Đơn hoàn tất | Tồn kho cập nhật | Tự động |

## 6. Điểm ra quyết định

| # | Câu hỏi quyết định | Điều kiện | Nhánh kết quả | Ai quyết |
|---|---|---|---|---|
| G1 | Cửa hàng còn hàng đúng model/màu/dung lượng? | Tồn khả dụng > 0 | Còn → bước 5 · Hết → G1b | ERP + NV tư vấn |
| G1b | Cửa hàng khác còn hàng và khách chờ được? | Có hàng trong bán kính điều chuyển | Có → chuyển M3 · Không → tư vấn model thay thế hoặc kết thúc | NV tư vấn + Khách |
| G2 | Khách đủ điều kiện hưởng khuyến mãi? | Theo điều kiện chương trình đang chạy | Đủ → áp giá ưu đãi · Không → giá niêm yết | Hệ thống giá |
| G3 | Khách chọn hình thức thanh toán nào? | Trả thẳng / trả góp | Trả thẳng → bước 6 · **Trả góp → chuyển sang C3** | Khách hàng |
| G4 | Máy lấy từ kho có đạt tình trạng bàn giao? | Nguyên seal, không móp, đúng IMEI | Đạt → bước 9 · Không đạt → đổi máy khác, ghi nhận | NV kho + NV tư vấn |
| G5 | Phương thức thanh toán? | Tiền mặt / thẻ / chuyển khoản / ví | Mỗi nhánh một luồng thu tiền | Khách hàng |
| G6 | Giao dịch thẻ có thành công? | Phản hồi từ cổng thanh toán | Thành công → bước 12 · Thất bại → đổi phương thức hoặc hủy đơn | Cổng thanh toán |
| G7 | Khách có yêu cầu xuất hóa đơn công ty? | Khách cung cấp mã số thuế | Có → nhập thông tin công ty · Không → hóa đơn cá nhân | Khách hàng |
| G8 | Khách có mua thêm phụ kiện / gói bảo hành mở rộng? | Khách đồng ý | Có → thêm dòng vào đơn · Không → giữ nguyên đơn | Khách hàng |

Chín điểm quyết định. C1 không thuộc nhóm mô hình hóa BPMN, nhưng bảng này vẫn cần đủ vì
C3 và C4 kế thừa các nhánh G1, G3, G4 khi vẽ mô hình.

## 7. Ngoại lệ và xử lý

| Mã | Tình huống ngoại lệ | Cách xử lý | Ai xử lý |
|---|---|---|---|
| E1 | Cửa hàng đông, khách phải chờ mới có nhân viên tiếp | Khách tự xem máy trưng bày; nhân viên tiếp khi rảnh | NV tư vấn |
| E2 | Khách đổi ý sau khi đã lập đơn nhưng chưa thanh toán | Hủy đơn nháp trên POS | NV tư vấn |
| E3 | Máy khui ra bị lỗi ngoại quan | Đổi máy khác cùng model, ghi nhận máy lỗi vào luồng hàng lỗi | NV kho + Quản lý |
| E4 | Hệ thống POS hoặc ERP gián đoạn | Ghi tay tạm, nhập bù khi hệ thống trở lại | Quản lý cửa hàng |
| E5 | Khách yêu cầu giảm giá ngoài chính sách | Chuyển quản lý cửa hàng quyết định | Quản lý cửa hàng |
| E6 | Chuyển dữ liệu từ máy cũ thất bại hoặc quá lâu | Hẹn khách quay lại, hoặc hướng dẫn tự chuyển tại nhà | NV tư vấn |

## 8. Quy tắc nghiệp vụ

| Mã | Quy tắc | Nguồn |
|---|---|---|
| R1 | Máy chỉ được bàn giao sau khi khách đã thanh toán đủ hoặc hoàn tất thủ tục trả góp | Quan sát |
| R2 | Khui hộp và kiểm tra máy phải có mặt khách hàng | Quan sát |
| R3 | Mỗi máy bán ra gắn với một IMEI duy nhất, là căn cứ bảo hành ở C4 | Quan sát + chính sách công bố |
| R4 | Giảm giá ngoài chính sách niêm yết cần quản lý cửa hàng duyệt | Phỏng vấn — (chưa xác minh) |
| R5 | Hàng hết tại cửa hàng có thể điều chuyển từ cửa hàng khác cùng khu vực | Quan sát + phỏng vấn câu 5 |
| R6 | Hóa đơn công ty phải nhập mã số thuế trước khi xuất, không sửa được sau khi xuất | (ước lượng) — cần xác minh |

Các dòng đánh dấu (chưa xác minh) và (ước lượng) được đưa vào bảng giả định Chương 4.

## 9. Chỉ số đo lường

| Chỉ số | Đơn vị | Cách đo | Giá trị ghi nhận | Nguồn |
|---|---|---|---|---|
| Thời gian một giao dịch bán trọn vẹn | phút | Bấm giờ từ lúc nhân viên tiếp cận đến lúc khách rời quầy | (chờ khảo sát 23/08) | bấm giờ, n = … |
| Thời gian chờ tới lượt được tư vấn | phút | Bấm giờ từ lúc khách vào đến lúc có nhân viên tiếp | (chờ khảo sát) | bấm giờ |
| Thời gian khâu kích hoạt và chuyển dữ liệu | phút | Bấm giờ riêng bước 10 | (chờ khảo sát) | bấm giờ |
| Tỷ lệ giao dịch bị ngắt quãng giữa chừng | % | Đếm lượt bị ngắt / tổng lượt quan sát | (chờ khảo sát) | quan sát |

Bốn chỉ số này là đầu vào trực tiếp cho bảng cycle time và CTE ở mục 4.2 Chương 4.

## 10. Hệ thống và biểu mẫu liên quan

| Tên | Loại | Ghi chú |
|---|---|---|
| POS | Hệ thống | Lập đơn, thu tiền |
| ERP / hệ thống tồn kho | Hệ thống | Tra và trừ tồn |
| Hóa đơn bán hàng | Biểu mẫu | Ảnh mẫu cần chụp trong buổi khảo sát |
| Phiếu bảo hành | Biểu mẫu | Ảnh mẫu cần chụp trong buổi khảo sát |

## 11. Điểm nghẽn quan sát được

| # | Điểm nghẽn | Vì sao là nghẽn | Bằng chứng cần có |
|---|---|---|---|
| B1 | Bước 10 — kích hoạt và chuyển dữ liệu | Chiếm phần đáng kể thời gian giao dịch nhưng không tạo giá trị khách sẵn sàng trả thêm; nhân viên bị giữ chân | Bấm giờ riêng bước 10 so với tổng |
| B2 | Bước 4 — kiểm tra tồn kho muộn | Hết hàng thì công tư vấn ở bước 1–3 bỏ phí, khách quay lại từ đầu với model khác | Đếm số lượt phải đổi model do hết hàng |
| B3 | Giờ cao điểm — khách chờ tới lượt | Thời gian chờ hoàn toàn là lãng phí nhóm **Hold** | Bấm giờ thời gian chờ, ghi khung giờ |
| B4 | Bước 11–12 — dồn về một quầy thu ngân | Nhiều giao dịch song song nghẽn ở một điểm | Đếm số quầy thu ngân so với số NV tư vấn |

Bốn điểm này chuyển thẳng sang Issue Register mục 4.6.

## 12. Nguồn tham chiếu

| Nguồn | Loại | Trạng thái |
|---|---|---|
| Buổi khảo sát tại cửa hàng TGDĐ | Quan sát + phỏng vấn | Dự kiến 23/08, phụ trách Hưng |
| Ảnh hóa đơn và phiếu bảo hành | Evidence | Chờ chụp — `evidence/anh-bieu-mau/` |
| Chính sách bảo hành công bố trên website TGDĐ | Tài liệu công khai | Chờ bổ sung kèm ngày truy cập |

> Hồ sơ này dựng từ quan sát bên ngoài và suy luận, **không phải quy trình chuẩn do MWG
> ban hành**. Mọi mục đánh dấu (chưa xác minh) hoặc (ước lượng) phải đối chiếu lại sau
> buổi khảo sát trước khi đưa vào bản Word.
