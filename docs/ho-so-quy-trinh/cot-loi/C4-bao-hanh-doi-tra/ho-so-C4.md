# C4 — Bảo hành, đổi trả

**Lớp:** cốt lõi
**Người lập:** Nguyễn Ngọc Danh · **Phiên bản:** v1 (draft — actor và input/output)
**Có mô hình BPMN:** có

## 1. Mục đích

Xử lý yêu cầu của khách khi sản phẩm đã bán gặp lỗi hoặc khách muốn đổi trả, theo đúng
chính sách công bố. Quy trình này quyết định trải nghiệm sau bán, và là nơi phát sinh
chi phí mà Chương 4 sẽ phân tích kỹ.

## 2. Phạm vi

- **Bắt đầu từ:** khách mang sản phẩm tới cửa hàng và nêu yêu cầu bảo hành hoặc đổi trả.
- **Kết thúc khi:** máy được sửa và trả lại khách · máy được đổi máy khác · khách được
  hoàn tiền · yêu cầu bị từ chối kèm lý do · khách rút lại yêu cầu.
- **Không bao gồm:** sửa chữa thu phí ngoài điều kiện bảo hành sau khi khách đã đồng ý
  báo giá (tách thành luồng dịch vụ riêng), thu hồi hàng lỗi hàng loạt từ nhà sản xuất.

## 3. Actor và vai trò

| Actor | Loại | Trách nhiệm chính |
|---|---|---|
| Khách hàng | Bên ngoài | Mang máy tới, mô tả lỗi, cung cấp chứng từ mua hàng |
| Nhân viên tiếp nhận bảo hành | Nội bộ | Tiếp nhận, kiểm tra điều kiện, lập phiếu |
| Kỹ thuật viên tại cửa hàng | Nội bộ | Kiểm tra sơ bộ, xử lý lỗi phần mềm và lỗi nhẹ |
| Quản lý cửa hàng | Nội bộ | Duyệt đổi máy, duyệt hoàn tiền, xử lý khiếu nại |
| **Trung tâm bảo hành / hãng** | Bên ngoài | Sửa chữa lỗi phần cứng, ra kết luận bảo hành |
| Nhân viên kho | Nội bộ | Xuất máy đổi, nhập máy lỗi |
| Hệ thống quản lý bảo hành | Hệ thống | Tra cứu IMEI, hạn bảo hành, lịch sử máy |
| Hệ thống ERP | Hệ thống | Ghi nhận đổi trả, điều chỉnh tồn và công nợ |

Với **TopZone**, khâu sửa chữa đi theo kênh ủy quyền của Apple nên điều kiện tiếp nhận và
thời gian phản hồi khác TGDĐ. Điểm khác biệt này được ghi riêng ở mục 8.

## 4. Đầu vào và đầu ra

| Loại | Tên | Từ đâu / đi đâu | Bắt buộc |
|---|---|---|---|
| Đầu vào | Sản phẩm lỗi | Khách hàng | Có |
| Đầu vào | Mô tả lỗi của khách | Khách hàng | Có |
| Đầu vào | Hóa đơn hoặc dữ liệu mua hàng theo IMEI | Khách / hệ thống (từ C1, C2, C3) | Có |
| Đầu vào | Phụ kiện đi kèm và hộp | Khách hàng | Tùy trường hợp đổi trả |
| Đầu vào | Chính sách bảo hành và đổi trả hiện hành | Tài liệu công bố | Có |
| Đầu ra | Phiếu tiếp nhận bảo hành | → Khách hàng | Có |
| Đầu ra | Kết luận tình trạng máy | ← Kỹ thuật / trung tâm bảo hành | Có |
| Đầu ra | Máy đã sửa, máy đổi, hoặc khoản hoàn tiền | → Khách hàng | Tùy nhánh |
| Đầu ra | Bản ghi đổi trả | → ERP | Có |
| Đầu ra | Thống kê lỗi theo model | → M2 (đánh giá nhà cung cấp) | Có |

## 5. Các bước thực hiện

`(chưa hoàn thiện — bổ sung ở bản v2)`

## 6. Điểm ra quyết định

`(chưa hoàn thiện — bổ sung ở bản v2, cần > 7 điểm để phục vụ BPMN)`

## 7. Ngoại lệ và xử lý

`(chưa hoàn thiện — bổ sung ở bản v2)`

## 8. Quy tắc nghiệp vụ

`(chưa hoàn thiện — cần đối chiếu chính sách công bố của TGDĐ và TopZone)`

## 9. Chỉ số đo lường

`(chưa hoàn thiện — chờ bảng bấm giờ khâu bảo hành và câu hỏi 1, 2 buổi khảo sát)`

## 10. Hệ thống và biểu mẫu liên quan

| Tên | Loại | Ghi chú |
|---|---|---|
| Hệ thống quản lý bảo hành | Hệ thống | Tra IMEI, hạn bảo hành |
| ERP | Hệ thống | Ghi nhận đổi trả |
| Phiếu tiếp nhận bảo hành | Biểu mẫu | Ảnh mẫu cần chụp — ưu tiên cao |
| Bảng niêm yết chính sách đổi trả | Biểu mẫu | Ảnh mẫu cần chụp |

## 11. Điểm nghẽn quan sát được

`(chưa hoàn thiện — chờ buổi khảo sát 23/08)`

## 12. Nguồn tham chiếu

`(bổ sung sau khảo sát)`
