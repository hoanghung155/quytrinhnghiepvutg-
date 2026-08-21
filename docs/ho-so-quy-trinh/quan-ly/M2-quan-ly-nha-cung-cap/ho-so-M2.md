# M2 — Quản lý nhà cung cấp

**Lớp:** quản lý
**Người lập:** Nguyễn Thị Hồng Phúc · **Phiên bản:** v2 (hoàn thiện)
**Có mô hình BPMN:** có — [M2-quan-ly-nha-cung-cap.bpmn](../../../../model/bpmn/M2-quan-ly-nha-cung-cap.bpmn) (Danh dựng, 9 gateway)

> **Lưu ý phối hợp:** mô hình BPMN của M2 do Danh dựng **trước** khi có hồ sơ này, kèm ghi
> chú trong `gen_M2.py` là cần đối chiếu lại. Hồ sơ này viết bám đúng chín gateway G1–G9
> của mô hình đó — xem bảng đối chiếu ở mục 6. Nếu khảo sát 23/08 cho kết quả khác thì sửa
> hồ sơ trước, sửa mô hình sau, và ghi vào biên bản review trước khi khóa mô hình 30/08.

## 1. Mục đích

Chọn và duy trì tập nhà cung cấp đủ năng lực, chốt điều khoản mua, và theo dõi chất lượng
thực tế của hàng sau khi đã bán ra. Quy trình này quyết định hai thứ mà cửa hàng không tự
sửa được: giá vốn và tỷ lệ lỗi của hàng bày trên kệ.

Điểm đặc thù của ngành hàng điện thoại và laptop là phần lớn hàng đến từ hãng hoặc nhà
phân phối ủy quyền, nên "chọn nhà cung cấp" thiên về chốt điều khoản và theo dõi chất
lượng hơn là đấu thầu mở. Đây là giả định cần xác minh (xem R1 ở mục 8).

## 2. Phạm vi

- **Bắt đầu từ:** nhận yêu cầu nhập hàng từ M1, hoặc tới kỳ đánh giá nhà cung cấp định kỳ.
- **Kết thúc khi:** PO được phát hành và lô hàng đã nghiệm thu đạt · lô hàng không đạt và
  được trả lại · nhà cung cấp bị loại khỏi danh sách sau đánh giá · nhà cung cấp được giữ
  lại sau đánh giá.
- **Không bao gồm:** nhập kho vật lý và điều chuyển (M3); đối soát công nợ và thanh toán
  (S4); quyết định mua bao nhiêu (M1).

## 3. Actor và vai trò

| Actor | Loại | Trách nhiệm chính |
|---|---|---|
| Bộ phận thu mua | Nội bộ | Lập danh sách NCC, gửi RFQ, chấm điểm, đàm phán, phát hành PO |
| Ban lãnh đạo | Nội bộ | Phê duyệt hợp đồng vượt hạn mức |
| **Nhà cung cấp / hãng / nhà phân phối** | Bên ngoài | Gửi hồ sơ năng lực và báo giá, xác nhận PO, giao hàng |
| Bộ phận chất lượng / kho | Nội bộ | Thẩm định năng lực tại chỗ, kiểm tra chất lượng và số lượng lô hàng |
| Hệ thống ERP | Hệ thống | Phát hành PO, ghi nhận nhập kho và công nợ |

Nhà cung cấp là actor **bên ngoài** — trong BPMN được vẽ thành lane riêng. Hai khâu phụ
thuộc hoàn toàn vào actor này là xác nhận PO (G6) và giao hàng đúng hạn.

## 4. Đầu vào và đầu ra

| Loại | Tên | Từ đâu / đi đâu | Bắt buộc |
|---|---|---|---|
| Đầu vào | Yêu cầu nhập hàng theo kế hoạch nhu cầu | M1 | Có |
| Đầu vào | Hồ sơ năng lực và báo giá của NCC | Nhà cung cấp | Có |
| Đầu vào | Hạn mức phê duyệt theo giá trị hợp đồng | Ban lãnh đạo | Có |
| Đầu vào | Tỷ lệ lỗi theo model từ dữ liệu bảo hành | C4 | Có |
| Đầu vào | Lịch kỳ đánh giá NCC | Bộ phận thu mua | Có |
| Đầu ra | Hợp đồng đã ký | → NCC, → S4 | Có |
| Đầu ra | Đơn đặt hàng (PO) | → NCC, → M3, → S4 | Có |
| Đầu ra | Biên bản nghiệm thu lô hàng | → M3 | Có |
| Đầu ra | Kết quả đánh giá NCC | → danh sách NCC kỳ sau | Có |
| Đầu ra | Biên bản trả hàng hoặc khiếu nại | → NCC | Chỉ khi lô không đạt |

## 5. Các bước thực hiện

Bảng này ánh xạ một-một với các task `t1`–`t15` trong mô hình BPMN M2.

| # | Bước | Actor | Đầu vào | Đầu ra | Ghi chú |
|---|---|---|---|---|---|
| 1 | Tiếp nhận và phân loại yêu cầu | Bộ phận thu mua | Yêu cầu từ M1 hoặc lịch đánh giá | Loại yêu cầu đã xác định | → G1, ba nhánh |
| 2 | Lập danh sách NCC tiềm năng | Bộ phận thu mua | Nhóm hàng cần mua | Danh sách NCC | `t1` |
| 3 | Gửi yêu cầu báo giá (RFQ) | Bộ phận thu mua | Danh sách NCC | RFQ đã gửi | `t2` |
| 4 | Gửi hồ sơ năng lực và báo giá | Nhà cung cấp | RFQ | Hồ sơ và báo giá | `t3` — khâu chờ actor bên ngoài |
| 5 | Sàng lọc điều kiện dự thầu | Bộ phận thu mua | Hồ sơ NCC | Kết luận đủ / không đủ | → G2 |
| 6 | So sánh và chấm điểm NCC | Bộ phận thu mua | Hồ sơ đạt sàng lọc | Bảng chấm điểm | `t4` → G3 |
| 7 | Thẩm định năng lực tại chỗ | Bộ phận chất lượng / kho | Danh sách NCC vào vòng trong | Kết quả thẩm định | `t5` — chỉ khi G3 yêu cầu |
| 8 | Trình phê duyệt cấp cao | Ban lãnh đạo | Hồ sơ NCC được chọn | Quyết định duyệt | `t6` — chỉ khi vượt hạn mức, → G4, G5 |
| 9 | Đàm phán điều khoản và ký hợp đồng | Bộ phận thu mua | Kết quả chọn NCC | Hợp đồng đã ký | `t7` |
| 10 | Phát hành đơn đặt hàng (PO) | Hệ thống ERP | Hợp đồng, nhu cầu | PO | `t8` — cũng là điểm vào cho NCC hiện có |
| 11 | Xác nhận PO | Nhà cung cấp | PO | PO đã xác nhận | → G6 |
| 12 | Nhắc và xử lý PO quá hạn xác nhận | Bộ phận thu mua | PO chưa xác nhận | PO được xác nhận hoặc hủy | `t9` |
| 13 | Giao hàng theo PO | Nhà cung cấp | PO đã xác nhận | Lô hàng tại điểm nhận | `t10` |
| 14 | Kiểm tra chất lượng và số lượng | Bộ phận chất lượng / kho | Lô hàng | Kết luận đạt / không đạt | `t11` → G7 |
| 15 | Lập biên bản và trả hàng hoặc khiếu nại | Bộ phận chất lượng / kho | Lô không đạt | Biên bản, yêu cầu giao lại | `t12` — quay lại bước 13 |
| 16 | Nhập kho và ghi nhận công nợ | Hệ thống ERP | Lô hàng đạt | Tồn kho cập nhật, công nợ ghi nhận | `t13` — bàn giao sang M3 và S4 |
| 17 | Đánh giá NCC kèm tỷ lệ lỗi từ C4 | Bộ phận thu mua | Dữ liệu giao hàng, tỷ lệ lỗi | Kết quả đánh giá | `t14` → G8, G9 |
| 18 | Cảnh báo và yêu cầu khắc phục | Nhà cung cấp | Kết quả đánh giá | Cam kết khắc phục | `t15` |

## 6. Điểm ra quyết định

| # | Câu hỏi quyết định | Điều kiện | Nhánh kết quả | Ai quyết |
|---|---|---|---|---|
| G1 | Loại yêu cầu là gì? | Tìm NCC mới / đặt hàng NCC hiện có / tới kỳ đánh giá | Mới → bước 2 · Hiện có → bước 10 · Đánh giá → bước 17 | Bộ phận thu mua |
| G2 | Hồ sơ NCC đủ điều kiện dự thầu? | Đối chiếu tiêu chí năng lực tối thiểu | Đủ → bước 6 · Không → loại khỏi vòng xét, kết thúc | Bộ phận thu mua |
| G3 | Có cần thẩm định năng lực tại chỗ? | Theo nhóm hàng và giá trị dự kiến | Cần → bước 7 · Không cần → G4 | Bộ phận thu mua |
| G4 | Giá trị hợp đồng có vượt hạn mức? | So với hạn mức phê duyệt | Vượt → bước 8 · Trong hạn mức → bước 9 | Bộ phận thu mua |
| G5 | Ban lãnh đạo có duyệt? | Đánh giá của ban lãnh đạo | Duyệt → bước 9 · Không duyệt → đàm phán lại hoặc dừng | **Ban lãnh đạo** |
| G6 | NCC xác nhận PO đúng hạn? | Thời hạn xác nhận theo hợp đồng | Xác nhận → bước 13 · Quá hạn → bước 12 | **Nhà cung cấp** |
| G7 | Lô hàng có đạt yêu cầu? | Đối chiếu số lượng, chất lượng, chứng từ | Đạt → bước 16 · Không đạt → bước 15, giao lại | Bộ phận chất lượng / kho |
| G8 | Đã đến kỳ đánh giá định kỳ NCC? | Lịch đánh giá | Tới kỳ → bước 17 · Chưa tới → kết thúc chu kỳ nhập hàng | Bộ phận thu mua |
| G9 | Kết quả đánh giá là gì? | Điểm đánh giá và tỷ lệ lỗi từ C4 | Đạt → giữ NCC · Cần cải thiện → bước 18 · Không đạt → loại khỏi danh sách | Bộ phận thu mua |

**Chín điểm quyết định — vượt mốc 7 gateway** yêu cầu cho mô hình BPMN. Bảng này khớp
một-một với chín gateway `G1`–`G9` trong file `M2-quan-ly-nha-cung-cap.bpmn`; G1 và G9 là
gateway ba nhánh.

## 7. Ngoại lệ và xử lý

| Mã | Tình huống ngoại lệ | Cách xử lý | Ai xử lý |
|---|---|---|---|
| E1 | NCC không phản hồi RFQ trong thời hạn | Loại khỏi vòng xét kỳ này, ghi nhận vào hồ sơ NCC | Bộ phận thu mua |
| E2 | NCC giao thiếu so với PO | Nhận phần đạt, lập biên bản phần thiếu, chốt lịch giao bù | Bộ phận chất lượng / kho |
| E3 | Hàng đúng số lượng nhưng sai model hoặc sai cấu hình | Trả toàn bộ lô, không nhập kho một phần | Bộ phận chất lượng / kho |
| E4 | NCC tăng giá sau khi PO đã phát hành | Giữ giá theo PO đã xác nhận; nếu chưa xác nhận thì đàm phán lại | Bộ phận thu mua |
| E5 | Phát hiện tỷ lệ lỗi cao đột biến giữa kỳ đánh giá | Kích hoạt đánh giá bất thường, không đợi tới kỳ | Bộ phận thu mua |
| E6 | NCC dừng cung cấp giữa chừng | Kích hoạt lại nhánh tìm NCC mới, báo M1 điều chỉnh kế hoạch | Bộ phận thu mua |

## 8. Quy tắc nghiệp vụ

| Mã | Quy tắc | Nguồn |
|---|---|---|
| R1 | Hàng chính hãng đến từ hãng hoặc nhà phân phối ủy quyền, không mua trôi nổi | Chính sách công bố |
| R2 | Hợp đồng vượt hạn mức phải có phê duyệt cấp cao trước khi ký | (ước lượng) — cần xác minh |
| R3 | Lô hàng chưa nghiệm thu đạt thì chưa được ghi nhận tồn khả dụng để bán | (ước lượng) — cần xác minh |
| R4 | Tỷ lệ lỗi theo model từ C4 là một tiêu chí bắt buộc trong đánh giá NCC | (ước lượng) — cần xác minh |
| R5 | Mỗi PO chỉ gắn với một nhà cung cấp | (chưa xác minh) |

R2, R3, R4 đưa vào bảng giả định Chương 4. R4 đặc biệt quan trọng vì nó là căn cứ để nói
vòng phản hồi C4 → M2 có thật — nếu khảo sát bác bỏ, phát hiện IR-13 phải viết lại.

## 9. Chỉ số đo lường

| Chỉ số | Đơn vị | Cách đo | Giá trị ghi nhận | Nguồn |
|---|---|---|---|---|
| Thời gian từ phát hành PO tới khi NCC xác nhận | ngày | Đo trên dữ liệu PO | (chưa xác minh — dữ liệu nội bộ khối thu mua) | ngoài tầm khảo sát cửa hàng |
| Tỷ lệ lô hàng không đạt nghiệm thu phải giao lại | % | Đếm số lần rẽ nhánh "không đạt" ở G7 | (chưa xác minh) | dữ liệu nội bộ |
| Độ trễ của dữ liệu tỷ lệ lỗi từ C4 về tới bước đánh giá NCC | ngày | Khoảng cách giữa thời điểm ghi nhận lỗi ở C4 và kỳ đánh giá gần nhất | (chưa xác minh) | liên quan IR-13 |
| Chu kỳ đánh giá nhà cung cấp | tháng | Hỏi bộ phận thu mua | (chưa xác minh) | phỏng vấn khối văn phòng — chưa có kênh tiếp cận |
| Số điểm ra quyết định trong quy trình | điểm | Đếm từ bảng mục 6 | 9 | phân tích hồ sơ |

Chỉ dòng cuối là số đo được trong phạm vi đề tài. Bốn dòng còn lại cần dữ liệu khối thu
mua mà nhóm không tiếp cận được — giữ `(chưa xác minh)`, **không điền số ước lượng**.
Chỉ số thứ ba là con số đáng giá nhất nếu sau này có kênh hỏi, vì nó định lượng trực tiếp
phát hiện IR-13.

## 10. Hệ thống và biểu mẫu liên quan

| Tên | Loại | Ghi chú |
|---|---|---|
| ERP | Hệ thống | Phát hành PO, ghi nhận nhập kho và công nợ |
| Đơn đặt hàng (PO) | Biểu mẫu | Chưa quan sát được — (chưa xác minh) |
| Biên bản nghiệm thu lô hàng | Biểu mẫu | Chưa quan sát được — (chưa xác minh) |
| Phiếu đánh giá nhà cung cấp | Biểu mẫu | Chưa quan sát được — (chưa xác minh) |

## 11. Điểm nghẽn quan sát được

| # | Điểm nghẽn | Vì sao là nghẽn | Nhóm lãng phí | Bằng chứng cần có |
|---|---|---|---|---|
| B1 | Bước 4 — chờ NCC gửi hồ sơ năng lực và báo giá | Toàn bộ nhánh tìm NCC mới dừng chờ actor bên ngoài, cửa hàng và thu mua không tác động được | **Hold** | (chưa xác minh) |
| B2 | G6 — PO quá hạn xác nhận, phải nhắc lại | Vừa phát sinh chờ, vừa phát sinh công việc nhắc vốn không tạo giá trị | **Hold** + **Overdo** | (chưa xác minh) |
| B3 | Bước 15 — lô hàng không đạt phải giao lại | Lặp lại toàn bộ chu kỳ vận chuyển và kiểm tra đã làm một lần | **Move** + **Overdo** | (chưa xác minh) |
| B4 | Bước 8 — trình phê duyệt cấp cao khi vượt hạn mức | Hồ sơ nằm chờ ở cấp duyệt, thời gian phụ thuộc lịch của ban lãnh đạo | **Hold** | (chưa xác minh) |
| B5 | Bước 17 — dữ liệu tỷ lệ lỗi từ C4 về chậm | Đánh giá NCC dựa trên dữ liệu cũ, quyết định giữ hay loại NCC không phản ánh chất lượng thực tế | **Hold** | Đã ghi nhận là IR-13 |

B5 chính là phát hiện **IR-13** đã có trong Issue Register, nhìn từ phía M2 thay vì từ
phía C4. Khi bổ sung phát hiện M1–M4 vào Issue Register, **không tạo mã mới cho B5** —
giữ nguyên IR-13 và thêm M2 vào cột nguồn để tránh đếm trùng một vấn đề thành hai.

Bốn điểm B1–B4 là phát hiện mới, đánh số tiếp từ IR-14 ở nhánh `analysis/dinh-tinh`.

## 12. Nguồn tham chiếu

| Nguồn | Loại | Trạng thái |
|---|---|---|
| Mô hình BPMN M2 và `gen_M2.py` | Tài liệu nội bộ nhóm | Đã có — bản của Danh, đã đối chiếu G1–G9 |
| Hồ sơ C4 mục 4 và mục 11 (vòng phản hồi tỷ lệ lỗi) | Tài liệu nội bộ nhóm | Đã có |
| Issue Register — IR-13 | Tài liệu nội bộ nhóm | Đã có |
| Buổi khảo sát tại cửa hàng | Phỏng vấn | Dự kiến 23/08, phụ trách Hưng |

> Hồ sơ này dựng từ logic mua hàng bán lẻ phổ biến và quan sát bên ngoài, **không phải quy
> trình chuẩn do MWG ban hành**. M2 là quy trình khối văn phòng, khảo sát tại cửa hàng
> gần như không xác minh được trực tiếp — phần lớn quy tắc ở mục 8 sẽ ở lại trạng thái
> (ước lượng) trong bản nộp, và cần nói rõ điều đó ở Chương 4.
