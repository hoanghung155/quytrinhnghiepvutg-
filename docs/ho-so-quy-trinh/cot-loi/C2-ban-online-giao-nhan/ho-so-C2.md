# C2 — Bán online, giao hàng và nhận tại cửa hàng

**Lớp:** cốt lõi
**Người lập:** Mai Hoàng Hưng · **Ngày lập:** 21/08/2026 · **Phiên bản:** v1 (draft khung)
**Có mô hình BPMN:** có (chưa vẽ — thuộc nhánh `model/bpmn-cot-loi`, phụ trách Danh)

> **Trạng thái:** draft khung, dựng từ chính sách công bố ở
> [nguon-khao-sat-cua-hang.md](../../../tai-lieu-tham-khao/nguon-khao-sat-cua-hang.md) và
> suy luận nghiệp vụ thông thường của mô hình đặt online + nhận tại cửa hàng (BOPIS).
> Mọi mục liên quan thao tác nội bộ, thời gian xử lý cụ thể tại một cửa hàng, hoặc tỷ lệ
> phát sinh vấn đề đều đánh dấu `(chờ khảo sát)` — **chưa có số nào là số đo thật**.

## 1. Mục đích

Cho khách đặt hàng qua website/app mà không cần tới cửa hàng trước, rồi chọn nhận hàng
tại một cửa hàng cụ thể thay vì chờ giao tận nơi — rút ngắn thời gian nhận hàng và giảm
tải khâu tư vấn tại quầy so với C1. Nếu không có quy trình này, khách ở xa cửa hàng hoặc
muốn tránh chờ đợi tại chỗ sẽ chuyển sang kênh khác.

## 2. Phạm vi

- **Bắt đầu từ:** khách đặt đơn trên website/app và chọn hình thức nhận tại cửa hàng.
- **Kết thúc khi:** một trong các trạng thái — khách nhận hàng tại cửa hàng và hoàn tất
  thanh toán (nếu chưa trả trước) · khách hủy đơn trước khi tới nhận · đơn quá hạn nhận
  không có người tới lấy.
- **Không bao gồm:** giao hàng tận nơi (kênh giao vận riêng, không phải nhận tại cửa
  hàng) · mua tại quầy trực tiếp (C1) · thẩm định trả góp (C3) · xử lý bảo hành/đổi trả
  sau khi đã nhận hàng (C4).

## 3. Actor và vai trò

| Actor | Loại | Trách nhiệm chính |
|---|---|---|
| Khách hàng | Bên ngoài | Đặt đơn online, chọn cửa hàng nhận, tới nhận và thanh toán |
| Hệ thống website/app bán hàng | Hệ thống | Ghi nhận đơn, kiểm tra tồn theo cửa hàng, gửi thông báo |
| Nhân viên xử lý đơn online tại cửa hàng | Nội bộ | Nhận thông báo đơn mới, chuẩn bị hàng, đối chiếu khi khách tới |
| Nhân viên thu ngân | Nội bộ | Thu phần còn lại (nếu có), xuất hóa đơn khi khách nhận hàng |
| Hệ thống ERP / tồn kho | Hệ thống | Giữ hàng cho đơn online, trừ tồn khi giao thành công |
| Cổng thanh toán online | Hệ thống | Xử lý thanh toán trước (nếu khách chọn trả trước) |

`(chưa xác minh)` — chưa rõ có vai trò riêng cho "nhân viên xử lý đơn online" hay việc
này do nhân viên tư vấn tại quầy kiêm nhiệm; cần hỏi khi khảo sát.

## 4. Đầu vào và đầu ra

| Loại | Tên | Từ đâu / đi đâu | Bắt buộc |
|---|---|---|---|
| Đầu vào | Đơn hàng online | Khách hàng qua website/app | Có |
| Đầu vào | Tồn kho theo từng cửa hàng | ERP (M3) | Có |
| Đầu vào | Xác nhận thanh toán trước (nếu có) | Cổng thanh toán online | Không — chỉ khi khách trả trước |
| Đầu ra | Thông báo đơn sẵn sàng nhận | → Khách hàng (SMS/app/email) | Có |
| Đầu ra | Hóa đơn bán hàng | → Khách hàng | Có |
| Đầu ra | Dữ liệu bảo hành gắn IMEI | → C4 | Có |
| Đầu ra | Bản ghi trừ tồn kho | → M3 | Có |

## 5. Các bước thực hiện

| # | Bước | Actor | Đầu vào | Đầu ra | Ghi chú |
|---|---|---|---|---|---|
| 1 | Khách đặt đơn trên website/app, chọn cửa hàng nhận | Khách hàng | Nhu cầu, tồn kho hiển thị theo cửa hàng | Đơn online | |
| 2 | Hệ thống kiểm tra tồn tại cửa hàng đã chọn | Hệ thống | Đơn online | Kết quả còn/hết hàng tại điểm nhận | → G1 |
| 3 | Khách chọn thanh toán trước hoặc thanh toán khi nhận | Khách hàng | Đơn online | Phương thức thanh toán | → G2 |
| 4 | Cửa hàng nhận thông báo đơn mới | NV xử lý đơn online | Đơn đã xác nhận | Đơn vào hàng chờ xử lý | |
| 5 | Chuẩn bị hàng, giữ riêng cho đơn | NV xử lý đơn online | Đơn, tồn kho | Hàng được giữ | (chờ khảo sát) thời gian chuẩn bị |
| 6 | Gửi thông báo hàng sẵn sàng cho khách | Hệ thống | Hàng đã chuẩn bị xong | Thông báo tới khách | |
| 7 | Khách tới cửa hàng, xuất trình mã đơn/giấy tờ | Khách hàng | Thông báo, giấy tờ | Đối chiếu đơn | → G3 |
| 8 | Kiểm tra máy cùng khách | NV xử lý đơn online + Khách | Máy đã giữ | Máy được xác nhận đạt | Tương tự bước 9 của C1 |
| 9 | Thu phần còn lại (nếu chưa trả đủ) | NV thu ngân | Đơn, số tiền còn lại | Giao dịch hoàn tất | → G2 nhánh chưa trả trước |
| 10 | Xuất hóa đơn và phiếu bảo hành | Thu ngân / POS | Giao dịch | Hóa đơn, dữ liệu bảo hành gắn IMEI | Đầu vào cho C4 |
| 11 | Bàn giao máy, phụ kiện, hộp | NV xử lý đơn online | Máy, hóa đơn | Khách ký nhận | |
| 12 | Trừ tồn và đồng bộ dữ liệu bán | ERP | Đơn hoàn tất | Tồn kho cập nhật | Tự động |

`(chưa xác minh)` — thứ tự bước 8–9 (kiểm tra máy trước hay thu tiền trước) suy theo
logic thông thường, cần đối chiếu thực tế.

## 6. Điểm ra quyết định

| # | Câu hỏi quyết định | Điều kiện | Nhánh kết quả | Ai quyết |
|---|---|---|---|---|
| G1 | Cửa hàng đã chọn còn hàng đúng model/màu? | Tồn khả dụng tại điểm nhận | Còn → bước 3 · Hết → gợi ý cửa hàng khác hoặc hủy đơn | Hệ thống + Khách hàng |
| G2 | Khách thanh toán trước hay khi nhận? | Lựa chọn của khách lúc đặt đơn | Trả trước → bỏ qua bước 9 · Trả khi nhận → thực hiện bước 9 | Khách hàng |
| G3 | Đơn còn hiệu lực khi khách tới nhận? | Trong hạn giữ hàng | Còn hạn → bước 8 · Quá hạn → hủy đơn, hoàn tiền nếu đã trả trước | Hệ thống + NV xử lý đơn online |
| G4 | Máy chuẩn bị sẵn có đạt tình trạng bàn giao? | Nguyên seal, đúng IMEI | Đạt → bước 9 · Không đạt → chuẩn bị lại hoặc đổi model, báo khách | NV xử lý đơn online |

`(chờ khảo sát)` — thời hạn giữ hàng cụ thể (bao nhiêu ngày) trước khi đơn bị hủy tự
động, cần hỏi khi khảo sát.

## 7. Ngoại lệ và xử lý

| Mã | Tình huống ngoại lệ | Cách xử lý | Ai xử lý |
|---|---|---|---|
| E1 | Hết hàng tại cửa hàng đã chọn sau khi đặt đơn | Gợi ý điều chuyển từ cửa hàng khác (liên quan M3) hoặc đổi điểm nhận | NV xử lý đơn online |
| E2 | Khách không tới nhận trong thời hạn giữ hàng | Hủy đơn, hoàn tiền nếu đã trả trước, trả hàng về tồn chung | NV xử lý đơn online + Hệ thống |
| E3 | Khách hủy đơn trước khi tới nhận | Hủy trên hệ thống, hoàn tiền nếu đã thanh toán trước | Hệ thống |
| E4 | Máy chuẩn bị sẵn bị lỗi ngoại quan khi kiểm tra cùng khách | Đổi máy khác cùng model nếu còn hàng, không thì hủy đơn | NV xử lý đơn online |

## 8. Quy tắc nghiệp vụ

| Mã | Quy tắc | Nguồn |
|---|---|---|
| R1 | Sản phẩm được giữ riêng cho đơn online trong một khoảng thời gian nhất định trước khi trả về tồn chung | (ước lượng) — cần xác minh thời hạn cụ thể khi khảo sát |
| R2 | Giao trễ hoặc không đúng cam kết, khách có quyền từ chối nhận và được hoàn tiền đã trả trước trong 7 ngày | Chính sách công bố — [Chính sách giao hàng](https://www.thegioididong.com/giao-hang), truy cập 21/08/2026 |
| R3 | Mỗi máy bán ra gắn với một IMEI duy nhất, là căn cứ bảo hành ở C4 | Suy theo R3 của C1 — quan sát |

## 9. Chỉ số đo lường

| Chỉ số | Đơn vị | Cách đo | Giá trị ghi nhận | Nguồn |
|---|---|---|---|---|
| Thời gian từ lúc cửa hàng nhận thông báo đơn đến lúc hàng sẵn sàng | phút/giờ | Đối chiếu thời gian đơn vào hệ thống và thời gian gửi thông báo sẵn sàng | (chờ khảo sát) | phỏng vấn — không quan sát trực tiếp được vì diễn ra hậu trường |
| Thời gian giao dịch khi khách tới nhận | phút | Bấm giờ từ lúc khách xuất trình mã đơn đến lúc rời quầy | (chờ khảo sát) | bấm giờ, n = … |
| Tỷ lệ đơn quá hạn không ai tới nhận | % | Hỏi nhân viên ước lượng theo kinh nghiệm | (chờ khảo sát) | phỏng vấn |

## 10. Hệ thống và biểu mẫu liên quan

| Tên | Loại | Ghi chú |
|---|---|---|
| Website/app bán hàng online | Hệ thống | Đặt đơn, chọn cửa hàng nhận |
| POS | Hệ thống | Xuất hóa đơn khi khách nhận hàng |
| ERP / hệ thống tồn kho | Hệ thống | Giữ hàng theo đơn, trừ tồn |
| Mã đơn hàng / thông báo nhận hàng | Biểu mẫu | Ảnh mẫu cần chụp trong buổi khảo sát nếu nhân viên đồng ý cho xem |

## 11. Điểm nghẽn quan sát được

`(chưa xác minh)` — mục này cần dữ liệu khảo sát mới viết được, hiện chỉ nêu giả thuyết
cần kiểm chứng:

| # | Điểm nghẽn giả thuyết | Vì sao nghi ngờ là nghẽn | Bằng chứng cần có |
|---|---|---|---|
| B1 (giả thuyết) | Khâu chuẩn bị hàng hậu trường trước khi khách tới | Không quan sát trực tiếp được, có thể chiếm nhiều thời gian nhưng khách không thấy | Hỏi nhân viên thời gian chuẩn bị trung bình |
| B2 (giả thuyết) | Đối chiếu đơn khi khách tới nhận nếu hệ thống chậm | Tương tự E4/G6 của C1 — phụ thuộc hệ thống | Bấm giờ bước 7–8, ghi lại nếu có gián đoạn hệ thống |

## 12. Nguồn tham chiếu

| Nguồn | Loại | Trạng thái |
|---|---|---|
| [Chính sách về đặt hàng và đơn hàng online](https://www.thegioididong.com/tin-tuc/chinh-sach-ve-dat-hang-va-don-hang-online-25620) | Tài liệu công khai | Đã dùng, truy cập 21/08/2026 |
| [Chính sách giao hàng](https://www.thegioididong.com/giao-hang) | Tài liệu công khai | Đã dùng, truy cập 21/08/2026 |
| Buổi khảo sát tại cửa hàng TGDĐ | Quan sát + phỏng vấn | Dự kiến 23/08, chót 26/08, phụ trách Hưng |
| Ảnh mã đơn/thông báo nhận hàng | Evidence | Chờ chụp — `evidence/anh-bieu-mau/` |

> Hồ sơ này là **draft khung**, dựng từ chính sách công bố và suy luận nghiệp vụ thông
> thường, chưa đối chiếu với cửa hàng thật. Toàn bộ mục đánh dấu `(chờ khảo sát)`,
> `(chưa xác minh)`, `(ước lượng)` phải được xác minh lại sau buổi khảo sát trước khi
> đưa vào bản Word.
