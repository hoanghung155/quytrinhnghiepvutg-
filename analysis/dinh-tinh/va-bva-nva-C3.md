# Phân tích VA / BVA / NVA — C3 Bán trả góp

**Người lập:** Nguyễn Thị Hồng Phúc · **Mục:** 4.3 Chương 4 · **Phiên bản:** v1
**Nguồn:** [hồ sơ C3](../../docs/ho-so-quy-trinh/cot-loi/C3-ban-tra-gop/ho-so-C3.md) mục 5
(15 bước) và mục 11 (4 điểm nghẽn) · [Issue Register](../issue-register/issue-register.md)

---

## 1. Tiêu chí xếp loại

Ba loại theo cách phân loại hoạt động trong phân tích quy trình:

| Loại | Định nghĩa dùng trong báo cáo này | Câu hỏi kiểm |
|---|---|---|
| **VA** — Value Adding | Hoạt động làm thay đổi sản phẩm hoặc dịch vụ theo hướng khách hàng mong muốn, và khách hàng sẵn sàng trả tiền cho nó | Nếu bỏ bước này, khách có thấy mình mất đi thứ mình đang trả tiền để có không? |
| **BVA** — Business Value Adding | Không tạo giá trị trực tiếp cho khách, nhưng bắt buộc phải có vì quy định pháp lý, yêu cầu của bên cấp tín dụng, hoặc để kiểm soát rủi ro | Nếu bỏ, doanh nghiệp có vi phạm quy định hoặc gánh rủi ro không chấp nhận được không? |
| **NVA** — Non Value Adding | Không tạo giá trị cho khách, cũng không bắt buộc; là chờ đợi, làm lại, hoặc thao tác có thể loại bỏ | Nếu bỏ, có ai mất gì không? |

Quy ước áp dụng cho bảng dưới:

- Một bước có phần vừa VA vừa BVA thì ghi cả hai và tách rõ phần nào là phần nào.
- **Thời gian chờ tách khỏi hành động.** Bước 6 là ví dụ: bản thân việc thẩm định tín dụng
  là BVA (bắt buộc, do bên cấp tín dụng thực hiện), nhưng **khoảng thời gian khách ngồi
  chờ** là NVA. Gộp hai thứ này lại sẽ che mất điểm nghẽn lớn nhất của C3.

## 2. Bảng xếp loại 15 bước

| # | Bước | Actor | Loại | Lý do xếp loại | Mã IR |
|---|---|---|---|---|---|
| 1 | Tiếp nhận yêu cầu trả góp | NV tư vấn trả góp | **BVA** | Khách không trả tiền riêng cho việc được tiếp nhận, nhưng không có bước này thì không mở được hồ sơ. Là bước chuyển giao bắt buộc từ C1. | — |
| 2 | Kiểm tra điều kiện sơ bộ của khách | NV tư vấn trả góp | **BVA** | Không thay đổi gì cho khách, nhưng lọc sớm hồ sơ chắc chắn trượt, tránh lãng phí cả chuỗi phía sau. Là kiểm soát rủi ro. | — |
| 3 | Tư vấn và so sánh các gói trả góp | NV tư vấn trả góp | **VA** | Khách đến cửa hàng thay vì mua online chính vì bước này. So sánh lãi suất và kỳ hạn giúp khách chọn được gói phù hợp — đây là giá trị khách thực sự nhận. | — |
| 4 | Thu thập và kiểm tra giấy tờ | NV tư vấn trả góp | **BVA** | Bắt buộc theo yêu cầu của bên cấp tín dụng. Làm kỹ ở bước này giảm vòng lặp ở bước 8. | — |
| 5 | Chụp, nhập hồ sơ lên cổng trả góp | NV tư vấn trả góp | **NVA** | Nhập tay lại thông tin đã có trên giấy tờ. Không tạo giá trị, dễ sai, và loại bỏ được nếu số hóa khâu nhập liệu. | **IR-07** |
| 6a | Thẩm định tín dụng (hành động) | Công ty tài chính | **BVA** | Bắt buộc — bên cấp tín dụng phải đánh giá rủi ro trước khi cho vay. Không bỏ được. | — |
| 6b | Khoảng chờ kết quả thẩm định | — | **NVA** | Khách ngồi chờ, nhân viên bị giữ chân, không có gì thay đổi trong suốt khoảng này. Là khoảng chờ dài nhất của C3. | **IR-05** |
| 7 | Nhận và thông báo kết quả cho khách | NV tư vấn trả góp | **BVA** | Bắt buộc để khách biết đường đi tiếp, nhưng bản thân việc thông báo không thay đổi gì cho khách. | — |
| 8 | Bổ sung hồ sơ nếu bị yêu cầu | Khách + NV tư vấn | **NVA** | Làm lại việc đã làm ở bước 4. Nguyên nhân gốc là bước 4 kiểm chưa kỹ. Kéo theo lặp lại cả khoảng chờ 6b. | **IR-06** |
| 9 | Xác nhận điều khoản và số tiền trả trước | NV tư vấn + Khách | **BVA** | Bắt buộc về mặt pháp lý — khách phải được biết lãi suất, kỳ hạn, phí trước khi ký. Không phải thứ khách trả tiền để có, nhưng không bỏ được. | — |
| 10 | Thu khoản trả trước | NV thu ngân | **BVA** | Điều kiện của bên cấp tín dụng để giải ngân. Là giao dịch tiền, không tạo giá trị cho khách. | — |
| 11 | Ký hợp đồng trả góp | Khách + Công ty tài chính | **BVA** | Bắt buộc pháp lý. Đây là thứ tạo ra ràng buộc, không tạo ra giá trị sử dụng. | — |
| 12 | Lập đơn hàng trên POS | NV tư vấn | **BVA** | Cần cho vận hành và cho khâu bảo hành sau này, khách không hưởng trực tiếp. | — |
| 13 | Lấy hàng, khui hộp, kiểm tra cùng khách | NV kho + Khách | **VA** | Khách trực tiếp hưởng: xác nhận máy đúng model, nguyên seal, đúng IMEI. Đây là lý do khách chọn mua tại cửa hàng thay vì đặt giao. | — |
| 14a | Bàn giao máy cho khách | NV tư vấn | **VA** | Là thời điểm khách nhận được thứ mình trả tiền để có. Bước tạo giá trị rõ ràng nhất của toàn quy trình. | — |
| 14b | Xuất hóa đơn và phiếu bảo hành | Thu ngân | **BVA** | Bắt buộc pháp lý và là căn cứ cho C4 về sau. Khách không trả tiền riêng cho tờ hóa đơn. | — |
| 15 | Đồng bộ dữ liệu sang ERP và bên cấp tín dụng | Hệ thống | **BVA** | Tự động, cần cho vận hành và đối soát. Không ảnh hưởng trải nghiệm khách. | — |

## 3. Tổng hợp

| Loại | Số bước | Danh sách |
|---|---:|---|
| **VA** | 3 | 3, 13, 14a |
| **BVA** | 11 | 1, 2, 4, 6a, 7, 9, 10, 11, 12, 14b, 15 |
| **NVA** | 3 | 5, 6b, 8 |

Tổng 17 dòng vì ba bước được tách đôi (6a/6b, 14a/14b — bước 6 và 14 của hồ sơ gốc).

### Ba nhận xét từ bảng

1. **Chỉ 3 trên 17 dòng là VA.** Tỷ lệ này bản thân nó chưa nói lên vấn đề — quy trình tín
   dụng vốn nhiều bước bắt buộc. Điều đáng nói là cả ba bước VA đều nằm ở **hai đầu** của
   quy trình (bước 3 ở đầu, bước 13–14a ở cuối), còn toàn bộ phần giữa là BVA và NVA.
   Khách trải qua một khoảng dài không nhận được gì.

2. **Ba bước NVA liên kết với nhau thành một vòng.** Bước 5 nhập liệu ẩu → bước 8 phải bổ
   sung → quay lại khoảng chờ 6b lần thứ hai. Đây không phải ba vấn đề rời rạc mà là **một
   chuỗi nhân quả**, và là nội dung chính của biểu đồ xương cá ở mục 4.5.

3. **Khoảng chờ 6b là NVA nhưng cửa hàng không xóa được.** Quyết định thuộc bên cấp tín
   dụng (quy tắc R1 của hồ sơ C3). Đề xuất cải tiến ở mục 4.7 phải nhắm vào **giảm ảnh
   hưởng** của khoảng chờ — ví dụ cho khách về và nhận kết quả qua điện thoại như ngoại lệ
   E2 đã mô tả — chứ không nhắm vào xóa khoảng chờ.

## 4. Đối chiếu với Issue Register

Bốn điểm nghẽn ở mục 11 hồ sơ C3 tương ứng IR-05 đến IR-08. Bảng trên khớp như sau:

| Mã IR | Điểm nghẽn (hồ sơ C3) | Bước tương ứng trong bảng | Loại | Nhóm lãng phí (Issue Register) | Khớp? |
|---|---|---|---|---|---|
| IR-05 | B1 — chờ thẩm định tín dụng | 6b | NVA | Hold | ✅ |
| IR-06 | B2 — vòng lặp bổ sung hồ sơ | 8 | NVA | Overdo | ✅ |
| IR-07 | B3 — nhập liệu thủ công | 5 | NVA | Overdo | ✅ |
| IR-08 | B4 — hết hàng sau khi hồ sơ đã duyệt | *(không có bước riêng)* | — | Move | ⚠️ xem ghi chú |

**Ghi chú về IR-08.** Đây là phát hiện gắn với **gateway G8** chứ không gắn với một bước
nào trong bảng mục 5. G8 hỏi "sản phẩm còn tồn tại cửa hàng ở thời điểm duyệt không" — khi
nhánh "hết" được kích hoạt, việc phát sinh là điều chuyển, mà điều chuyển thuộc quy trình
**M3** chứ không thuộc C3. Vì vậy IR-08 không xuất hiện trong bảng xếp loại bước của C3.

Cách xử lý: giữ nguyên mã IR-08, ghi rõ trong Chương 4 rằng phát hiện này nằm ở điểm ra
quyết định chứ không nằm ở bước, và phần thời gian chờ của nó thuộc M3 (xem điểm nghẽn B1
của hồ sơ M3). **Không tạo mã IR mới cho phần M3 của cùng một vấn đề.**

Không có mâu thuẫn nào giữa bảng này và Issue Register.

## 5. Giới hạn — chưa tính được tỷ lệ theo thời gian

Bảng trên xếp loại theo **số bước**, không theo **thời gian**. Phân tích VA/BVA/NVA có giá
trị hơn nhiều khi tính theo thời gian, vì một bước NVA kéo dài 40 phút nặng hơn năm bước
BVA mỗi bước 1 phút.

Chưa tính được vì mục 9 của hồ sơ C3 đang ở trạng thái `(chờ khảo sát 23/08)`:

| Số liệu cần | Trạng thái |
|---|---|
| Tổng thời gian từ nộp giấy tờ đến có kết quả duyệt | (chờ khảo sát — câu phỏng vấn 3) |
| Thời gian chờ thẩm định thuần, bước 6b | (chờ khảo sát — câu phỏng vấn 3) |
| Tỷ lệ hồ sơ bị yêu cầu bổ sung, bước 8 | (chờ khảo sát — câu phỏng vấn 4) |

Sau buổi khảo sát của Hưng, bổ sung một bảng "tỷ lệ thời gian VA/BVA/NVA" vào file này.
**Không điền số ước lượng vào chỗ trống** — tỷ lệ sai còn tệ hơn không có tỷ lệ, vì nó
đi thẳng vào kết luận của Chương 4.
