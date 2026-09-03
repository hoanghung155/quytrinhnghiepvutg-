# Phân tích VA / BVA / NVA — C4 Bảo hành, đổi trả

**Người lập:** Nguyễn Thị Hồng Phúc · **Mục:** 4.3 Chương 4 · **Phiên bản:** v1
**Nguồn:** [hồ sơ C4](../../docs/ho-so-quy-trinh/cot-loi/C4-bao-hanh-doi-tra/ho-so-C4.md)
mục 5 (16 bước) và mục 11 (5 điểm nghẽn) · [Issue Register](../issue-register/issue-register.md)

Tiêu chí xếp loại và quy ước tách bước dùng chung với
[bảng VA/BVA/NVA của C3](va-bva-nva-C3.md) mục 1 — không lặp lại ở đây.

---

## 1. Điểm khác biệt khi phân tích C4 so với C3

C4 là quy trình **dịch vụ sau bán**, không phải quy trình bán. Hai hệ quả cho cách xếp loại:

1. **Khách đã trả tiền rồi.** Câu hỏi "khách có sẵn sàng trả tiền cho bước này không" phải
   đọc lại thành "bước này có nằm trong thứ khách đã trả tiền để có khi mua máy không" —
   vì bảo hành là cam kết đi kèm sản phẩm.

2. **Chẩn đoán lỗi được xếp VA.** Khách mang máy tới quầy chính là để biết máy bị gì và
   được xử lý. Việc kiểm tra phân loại lỗi (bước 6) vì thế là một phần của dịch vụ khách
   đang tìm kiếm, khác với các bước kiểm tra thuần túy để kiểm soát rủi ro của doanh
   nghiệp (bước 5) — bước sau là BVA.

## 2. Bảng xếp loại 16 bước

| # | Bước | Actor | Loại | Lý do xếp loại | Mã IR |
|---|---|---|---|---|---|
| 1a | Chờ tới lượt tại quầy bảo hành | Khách hàng | **NVA** | Khách đứng chờ, không có gì xảy ra. Quầy bảo hành thường ít người trực hơn quầy bán nên chờ ngay từ đầu. | **IR-09** |
| 1b | Nêu yêu cầu và ghi nhận | Khách + NV tiếp nhận | **BVA** | Bắt buộc để mở hồ sơ, nhưng bản thân việc ghi nhận không thay đổi gì cho khách. | — |
| 2a | Tra cứu thông tin mua hàng theo IMEI | NV tiếp nhận | **BVA** | Bắt buộc để xác định điều kiện bảo hành. Khi có dữ liệu, đây là thao tác nhanh và cần thiết. | — |
| 2b | Dò tìm thủ công khi khách không có hóa đơn | NV tiếp nhận | **NVA** | Mất thời gian dò, phải hỏi lại khách nhiều lần. Loại bỏ được nếu tra theo IMEI luôn cho kết quả (quy tắc R1 của hồ sơ C4 nói căn cứ là IMEI, không phụ thuộc hóa đơn giấy). | **IR-11** |
| 3 | Xác định máy còn trong hạn bảo hành | NV tiếp nhận | **BVA** | Bắt buộc theo chính sách. Là điều kiện để đi tiếp, không tạo giá trị. | — |
| 4 | Xác định khách muốn bảo hành hay đổi trả | NV tiếp nhận | **BVA** | Phân luồng bắt buộc, khách không hưởng gì thêm từ bước này. | — |
| 5 | Kiểm tra ngoại quan và điều kiện bảo hành | NV tiếp nhận + KTV | **BVA** | Kiểm soát rủi ro cho doanh nghiệp — loại các ca rơi vỡ, vào nước, tự tháo theo quy tắc R2. Không phải thứ khách tìm kiếm. | — |
| 6 | Kiểm tra sơ bộ để phân loại lỗi | KTV tại cửa hàng | **VA** | Chẩn đoán là một phần của dịch vụ khách đang tìm. Xem mục 1 điểm 2. | — |
| 7 | Xử lý tại chỗ nếu là lỗi phần mềm hoặc lỗi nhẹ | KTV tại cửa hàng | **VA** | Máy được sửa và trả ngay — khách nhận đúng thứ mình cần, trong thời gian ngắn nhất. Đây là nhánh tốt nhất của C4. | — |
| 8 | Lập phiếu tiếp nhận, bàn giao máy cho khách giữ liên | NV tiếp nhận | **BVA** | Chứng từ bắt buộc, là căn cứ khi có tranh chấp. Khách giữ một liên nhưng không phải thứ khách muốn có. | — |
| 9 | Đóng gói và gửi máy lên trung tâm bảo hành | NV tiếp nhận + NV kho | **NVA** | Vận chuyển thuần túy. Máy không tốt lên vì được vận chuyển; đây là hệ quả của việc cửa hàng không tự sửa được lỗi phần cứng. | **IR-10** |
| 10a | Trung tâm bảo hành sửa chữa (hành động) | Trung tâm bảo hành | **VA** | Máy thực sự được sửa. Đây là bước tạo giá trị chính của nhánh gửi đi. | — |
| 10b | Khoảng chờ kết quả từ trung tâm | — | **NVA** | Khoảng chờ dài nhất toàn quy trình; khách không có máy dùng trong suốt thời gian này. Cửa hàng không kiểm soát được. | **IR-10** |
| 11 | Nhận máy về, đối chiếu kết luận | NV tiếp nhận | **BVA** | Kiểm soát chất lượng đầu vào — đối chiếu IMEI và kết luận. Cần thiết nhưng không tạo giá trị. | — |
| 12 | Thông báo và hẹn khách tới nhận | NV tiếp nhận | **BVA** | Bắt buộc để khách biết, nhưng bản thân cuộc gọi không thay đổi gì. | — |
| 13 | Bàn giao máy, khách kiểm tra và ký nhận | NV tiếp nhận + Khách | **VA** | Khách nhận lại máy hoạt động được — thời điểm nhận giá trị. | — |
| 14 | Đổi máy — xuất máy mới, thu hồi máy lỗi | NV kho + Thu ngân | **VA** | Khách nhận máy thay thế, giải quyết được vấn đề của khách. | — |
| 15a | Hoàn tiền cho khách | Thu ngân | **VA** | Trong nhánh không sửa và không đổi được, hoàn tiền là kết quả khách mong muốn. | — |
| 15b | Lập chứng từ hoàn | Thu ngân + Quản lý | **BVA** | Thủ tục kế toán bắt buộc, khách không hưởng. | — |
| 16a | Ghi nhận hồ sơ vào hệ thống | Hệ thống | **BVA** | Cần cho vận hành và cho thống kê lỗi. Tự động. | — |
| 16b | Độ trễ của vòng phản hồi dữ liệu lỗi sang M2 | — | **NVA** | Dữ liệu có sẵn nhưng về tới khâu đánh giá nhà cung cấp chậm, làm quyết định giữ hay loại NCC dựa trên dữ liệu cũ. | **IR-13** |

## 3. Tổng hợp

| Loại | Số dòng | Danh sách |
|---|---:|---|
| **VA** | 6 | 6, 7, 10a, 13, 14, 15a |
| **BVA** | 10 | 1b, 2a, 3, 4, 5, 8, 11, 12, 15b, 16a |
| **NVA** | 5 | 1a, 2b, 9, 10b, 16b |

Tổng 21 dòng vì năm bước của hồ sơ gốc được tách đôi (1, 2, 10, 15, 16).

### Ba nhận xét từ bảng

1. **C4 có nhiều VA hơn C3** (6 so với 3) nhưng cũng nhiều NVA hơn (5 so với 3). Lý do là
   C4 có nhiều nhánh kết thúc khác nhau — sửa, đổi, hoàn tiền đều là kết quả tạo giá trị.
   Không nên so trực tiếp hai con số này vì hai quy trình có số bước khác nhau.

2. **Nhánh xử lý tại chỗ (bước 7) là nhánh duy nhất không có NVA nào đáng kể.** Khách chờ
   tới lượt, được chẩn đoán, được sửa, nhận máy về. Mọi NVA nặng của C4 — bước 9, 10b —
   chỉ xuất hiện khi phải gửi máy đi. Điều này làm cho chỉ số "tỷ lệ ca xử lý xong tại cửa
   hàng" ở mục 9 hồ sơ C4 trở thành **con số quan trọng nhất của cả quy trình**: nó quyết
   định bao nhiêu phần trăm ca đi vào nhánh nhiều NVA.

3. **Hai NVA ở hai đầu quy trình có bản chất khác nhau.** Bước 1a là chờ do **nguồn lực nội
   bộ** — cửa hàng tự giải quyết được bằng cách bố trí người. Bước 10b là chờ do **actor bên
   ngoài** — cửa hàng chỉ giảm được ảnh hưởng chứ không xóa được. Đề xuất ở mục 4.7 phải
   tách hai loại này, đúng như Issue Register đã lưu ý.

## 4. Đối chiếu với Issue Register

Năm điểm nghẽn ở mục 11 hồ sơ C4 tương ứng IR-09 đến IR-13:

| Mã IR | Điểm nghẽn (hồ sơ C4) | Dòng tương ứng | Loại | Nhóm lãng phí (Issue Register) | Khớp? |
|---|---|---|---|---|---|
| IR-09 | B1 — chờ tới lượt tại quầy bảo hành | 1a | NVA | Hold | ✅ |
| IR-10 | B2 — gửi máy lên trung tâm và chờ kết quả | 9 và 10b | NVA | Hold | ⚠️ xem ghi chú 1 |
| IR-11 | B3 — tra cứu thủ công khi không có hóa đơn | 2b | NVA | Overdo | ✅ |
| IR-12 | B4 — máy nhận về không đạt, phải gửi lại | *(không có bước riêng)* | — | Move + Overdo | ⚠️ xem ghi chú 2 |
| IR-13 | B5 — dữ liệu lỗi về M2 chậm | 16b | NVA | Hold | ✅ |

**Ghi chú 1 — IR-10 trải trên hai dòng.** Issue Register xếp IR-10 vào nhóm **Hold**, nhưng
phát hiện này gồm hai phần khác nhau: bước 9 là **vận chuyển** (thuộc Move) và bước 10b là
**chờ** (thuộc Hold). Bảng phân nhóm lãng phí ở mục 4.4 sẽ đếm IR-10 ở cả hai nhóm, giống
cách Issue Register đã làm với IR-12. Đây là **bổ sung cách đếm, không phải sửa mã** — mã
IR-10 giữ nguyên.

**Ghi chú 2 — IR-12 gắn với gateway, không gắn với bước.** Giống trường hợp IR-08 của C3.
Phát hiện này gắn với **gateway G7** ("máy nhận về có đúng máy và đã xử lý đạt?"), khi
nhánh "không đạt" được kích hoạt thì lặp lại bước 9 và 10b. Vì vậy IR-12 không có dòng
riêng trong bảng xếp loại bước, mà thể hiện dưới dạng **lặp lại hai dòng đã có**. Giữ
nguyên mã IR-12, ghi rõ trong Chương 4.

Không có mâu thuẫn nào giữa bảng này và Issue Register. Một đề nghị bổ sung duy nhất là
cách đếm IR-10 ở ghi chú 1.

## 5. Giới hạn — chưa tính được tỷ lệ theo thời gian

Giống C3, bảng này xếp loại theo **số bước** chứ chưa theo **thời gian**. Với C4 thì khoảng
cách giữa hai cách tính còn lớn hơn C3: bước 10b tính bằng **ngày** trong khi phần lớn các
bước còn lại tính bằng **phút**. Một bảng tỷ lệ theo số bước vì thế sẽ đánh giá thấp nghiêm
trọng mức độ của IR-10.

| Số liệu cần | Trạng thái |
|---|---|
| Thời gian chờ tới lượt tại quầy bảo hành (1a) | (chờ khảo sát 23/08 — bấm giờ) |
| Thời gian tiếp nhận tại quầy (1b–8) | (chờ khảo sát — bấm giờ theo chặng) |
| Thời gian chờ kết quả từ trung tâm (10b) | (chờ khảo sát — câu phỏng vấn 2) |
| Tỷ lệ ca xử lý xong tại cửa hàng (nhánh bước 7) | (chờ khảo sát — câu phỏng vấn 1) |

Hai dòng cuối là hai con số quan trọng nhất của C4, đúng như hồ sơ C4 đã ghi ở mục 9. Sau
buổi khảo sát của Hưng, bổ sung bảng tỷ lệ thời gian vào file này. **Không điền số ước
lượng** — với C4 thì một con số sai ở dòng 10b sẽ kéo lệch toàn bộ kết luận mục 4.7.
