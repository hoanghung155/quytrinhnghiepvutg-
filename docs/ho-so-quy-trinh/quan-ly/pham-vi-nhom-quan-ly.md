# Phạm vi nhóm quy trình quản lý (M1–M4)

**Người lập:** Nguyễn Thị Hồng Phúc · **Phiên bản:** v1
**Liên quan:** [phân rã 12 quy trình](../../kien-truc-quy-trinh/phan-ra-12-quy-trinh.md)

Tài liệu này chốt ranh giới bốn quy trình lớp quản lý trước khi lập hồ sơ chi tiết. Mục
đích là tránh chuyện cùng một hoạt động bị mô tả ở hai hồ sơ, hoặc rơi vào khoảng trống
không hồ sơ nào nhận.

Lớp quản lý **không trực tiếp bán hàng cho khách**. Nó quyết định *bán cái gì, lấy từ
đâu, để ở đâu, và bán tại điểm nào* — bốn câu hỏi tương ứng bốn quy trình M1–M4.

---

## 1. Bốn quy trình và câu hỏi mà mỗi quy trình trả lời

| Mã | Tên | Câu hỏi quản trị | Nhịp chạy |
|---|---|---|---|
| **M1** | Hoạch định nhu cầu | Kỳ tới cần bao nhiêu hàng, nhóm nào? | Theo chu kỳ (tuần/tháng) + kích hoạt bất thường |
| **M2** | Quản lý nhà cung cấp | Mua của ai, giá và điều khoản nào? | Theo nhu cầu nhập + kỳ đánh giá định kỳ |
| **M3** | Kho và điều chuyển | Hàng nằm ở đâu, chuyển đi đâu? | Liên tục, theo sự kiện |
| **M4** | Mạng lưới cửa hàng | Mở, giữ, chuyển hay đóng điểm bán nào? | Chu kỳ dài (quý/năm) |

Bốn quy trình chạy ở bốn nhịp khác nhau. Đây là lý do không gộp chúng lại: M3 phản ứng
theo từng sự kiện trong ngày, còn M4 ra quyết định vài tháng một lần.

## 2. Ranh giới bắt đầu — kết thúc

| Mã | Bắt đầu từ | Kết thúc khi | Không bao gồm |
|---|---|---|---|
| M1 | Tới kỳ lập kế hoạch, hoặc tín hiệu tồn kho vượt ngưỡng | Kế hoạch nhu cầu được duyệt và chuyển sang M2 | Việc chọn nhà cung cấp cụ thể (M2); việc đặt hàng (M2) |
| M2 | Nhận yêu cầu nhập hàng từ M1, hoặc tới kỳ đánh giá NCC | Hợp đồng/PO được phát hành và hàng đã nhận đạt yêu cầu; hoặc kết quả đánh giá NCC được ghi nhận | Nhập kho vật lý (M3); đối soát công nợ và thanh toán (S4) |
| M3 | Có lệnh nhập từ M2, hoặc yêu cầu điều chuyển từ cửa hàng | Hàng nằm đúng vị trí và tồn kho hệ thống khớp tồn thực tế | Quyết định mua bao nhiêu (M1); xuất bán cho khách (C1–C3) |
| M4 | Kế hoạch mở rộng, hoặc tới kỳ rà soát hiệu quả điểm bán | Quyết định mở / giữ / chuyển / đóng được phê duyệt | Thi công và mua sắm thiết bị cho cửa hàng (S3); tuyển nhân sự cho cửa hàng mới (S1) |

## 3. Bốn chỗ dễ mô tả trùng — đã chốt cách tách

| Hoạt động dễ nhầm | Thuộc quy trình nào | Lý do |
|---|---|---|
| "Đặt bao nhiêu hàng cho cửa hàng A" | **M1** nếu là kế hoạch kỳ; **M3** nếu là điều chuyển bù gấp trong ngày | M1 quyết lượng mua vào từ ngoài; M3 chỉ phân bổ lượng đã có trong hệ thống |
| Kiểm tra chất lượng lô hàng về | **M2** | Đây là bước nghiệm thu đối với nhà cung cấp, gắn với PO, không phải nghiệp vụ kho |
| Nhập kho sau khi nghiệm thu | **M3** | Từ lúc hàng đạt và được ghi nhận tồn thì mới sang M3 |
| Đề xuất đóng cửa hàng vì tồn ứ kéo dài | **M4** | M3 chỉ báo tình trạng tồn; quyết định về điểm bán luôn thuộc M4 |

## 4. Giao diện với lớp cốt lõi và lớp hỗ trợ

Sáu liên kết đã chốt ở Hình 1.1, phần liên quan tới nhóm quản lý:

| Từ | Đến | Nội dung trao đổi | Ghi chú |
|---|---|---|---|
| M1 | M2 | Kế hoạch nhu cầu → yêu cầu đặt hàng | Đầu ra chính của M1 |
| M2 | M3 | PO đã duyệt → lệnh nhập kho | Điểm chuyển giao ở khâu nghiệm thu |
| M3 | C1, C2, C3 | Tồn khả dụng tại cửa hàng → điều kiện xuất hàng | M3 là ràng buộc của cả ba quy trình bán |
| C4 | M2 | Tỷ lệ lỗi theo model → đầu vào đánh giá NCC | Vòng phản hồi, xem IR-13 |
| M2 | S4 | Hợp đồng và PO → căn cứ đối soát công nợ | Sang lớp hỗ trợ |
| M4 | S1, S3 | Quyết định mở điểm bán → nhu cầu nhân sự và hạ tầng | Kích hoạt hai quy trình hỗ trợ |

Hai giao diện đáng chú ý nhất:

- **M3 → C3 và C4.** Cả hai quy trình cốt lõi này đều có nhánh phụ thuộc điều chuyển:
  C3 ở G8 (hết hàng sau khi hồ sơ trả góp đã duyệt) và C4 ở E2 (hết máy để đổi). Hồ sơ M3
  phải mô tả được nhánh điều chuyển gấp phục vụ hai tình huống đó.
- **C4 → M2.** Độ trễ của vòng phản hồi này đã được ghi nhận là phát hiện IR-13. Hồ sơ M2
  phải nói rõ dữ liệu lỗi đi vào bước đánh giá nào.

## 5. Những gì nhóm quản lý *không* bao gồm

- Bán hàng, tư vấn, thu tiền, giao máy — thuộc C1–C3.
- Bảo hành, đổi trả — thuộc C4.
- Tuyển và đào tạo nhân viên — thuộc S1, kể cả khi phát sinh do M4 mở cửa hàng mới.
- Vận hành ERP/POS và mua sắm hạ tầng — thuộc S2, S3.
- Đối soát và thanh toán công nợ nhà cung cấp — thuộc S4, dù chứng từ gốc sinh ra ở M2.

## 6. Câu hỏi còn mở — cần xác minh ở buổi khảo sát 23/08

| # | Câu hỏi | Ảnh hưởng tới hồ sơ nào |
|---|---|---|
| Q1 | Kế hoạch nhu cầu lập theo chu kỳ nào, và cửa hàng có quyền đề xuất điều chỉnh không? | M1 mục 5, mục 6 |
| Q2 | Điều chuyển giữa hai cửa hàng do ai duyệt, có ngưỡng giá trị nào không? | M3 mục 6 |
| Q3 | Cửa hàng mất bao lâu để nhận hàng điều chuyển từ cửa hàng khác? | M3 mục 9 — liên quan C3 G8 và C4 E2 |
| Q4 | Kiểm kê tồn kho tại cửa hàng thực hiện theo tần suất nào? | M3 mục 5 |

Bốn câu này bổ sung vào bộ câu hỏi khảo sát của Hưng. Trước khi có trả lời, các mục tương
ứng trong hồ sơ ghi `(chờ khảo sát)`, không điền số cho đủ bảng.

## 7. Nguồn tham chiếu

| Nguồn | Loại | Trạng thái |
|---|---|---|
| Phân rã 12 quy trình theo ba lớp | Tài liệu nội bộ nhóm | Đã có — bản của Danh |
| Hồ sơ C3, C4 (mục 6, mục 11) | Tài liệu nội bộ nhóm | Đã có — dùng để chốt giao diện M3 |
| Buổi khảo sát tại cửa hàng | Phỏng vấn | Dự kiến 23/08, phụ trách Hưng |

> Tài liệu này dựng từ mô hình phân lớp quy trình và quan sát bên ngoài, **không phải cơ
> cấu quản trị do MWG ban hành**. Mọi phát biểu về thẩm quyền phê duyệt trong hồ sơ M1–M4
> đều phải kiểm chứng lại ở buổi khảo sát trước khi đưa vào Chương 3.
