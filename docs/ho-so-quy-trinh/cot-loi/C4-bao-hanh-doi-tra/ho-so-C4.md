# C4 — Bảo hành, đổi trả

**Lớp:** cốt lõi
**Người lập:** Nguyễn Ngọc Danh · **Phiên bản:** v2 (hoàn thiện)
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

| # | Bước | Actor | Đầu vào | Đầu ra | Ghi chú |
|---|---|---|---|---|---|
| 1 | Khách tới quầy bảo hành, nêu yêu cầu | Khách hàng | Máy lỗi, mô tả lỗi | Yêu cầu được ghi nhận | Có thể phải chờ tới lượt → B1 |
| 2 | Tra cứu thông tin mua hàng theo IMEI | NV tiếp nhận | IMEI hoặc hóa đơn | Ngày mua, hạn bảo hành, lịch sử máy | Dữ liệu từ C1/C2/C3 |
| 3 | Xác định máy còn trong hạn bảo hành không | NV tiếp nhận | Ngày mua, chính sách | Kết luận còn / hết hạn | → G1 |
| 4 | Xác định khách muốn bảo hành hay đổi trả | NV tiếp nhận | Yêu cầu của khách | Hướng xử lý | → G2 |
| 5 | Kiểm tra ngoại quan và điều kiện bảo hành | NV tiếp nhận + KTV | Máy | Kết luận đủ / không đủ điều kiện | → G3 |
| 6 | Kiểm tra sơ bộ để phân loại lỗi | KTV tại cửa hàng | Máy | Lỗi phần mềm / phần cứng / không tái hiện | → G4 |
| 7 | Xử lý tại chỗ nếu là lỗi phần mềm hoặc lỗi nhẹ | KTV tại cửa hàng | Máy | Máy đã xử lý | → G5 |
| 8 | Lập phiếu tiếp nhận, bàn giao máy cho khách giữ liên hệ | NV tiếp nhận | Máy, thông tin khách | Phiếu tiếp nhận | Khách giữ một liên |
| 9 | Đóng gói và gửi máy lên trung tâm bảo hành | NV tiếp nhận + NV kho | Máy, phiếu | Máy đã gửi đi | Bắt đầu khoảng chờ dài → B2 |
| 10 | Trung tâm bảo hành kiểm định và xử lý | Trung tâm bảo hành / hãng | Máy | Kết luận và máy đã xử lý | → G6 |
| 11 | Nhận máy về, đối chiếu kết luận | NV tiếp nhận | Máy, kết luận | Máy sẵn sàng trả khách | → G7 |
| 12 | Thông báo và hẹn khách tới nhận | NV tiếp nhận | Kết quả | Khách được thông báo | |
| 13 | Bàn giao máy, khách kiểm tra và ký nhận | NV tiếp nhận + Khách | Máy | Phiếu đã tất toán | → G8 |
| 14 | Trường hợp đổi máy — xuất máy mới, thu hồi máy lỗi | NV kho + Thu ngân | Quyết định đổi | Máy mới giao khách, máy lỗi nhập kho lỗi | Nhánh từ G6 |
| 15 | Trường hợp hoàn tiền — lập chứng từ hoàn | Thu ngân + Quản lý | Quyết định hoàn | Tiền hoàn cho khách | Nhánh từ G2/G6 |
| 16 | Ghi nhận vào hệ thống, cập nhật thống kê lỗi theo model | Hệ thống | Hồ sơ đã đóng | Dữ liệu lỗi → M2 | Vòng phản hồi C4 → M2 |

## 6. Điểm ra quyết định

| # | Câu hỏi quyết định | Điều kiện | Nhánh kết quả | Ai quyết |
|---|---|---|---|---|
| G1 | Máy còn trong hạn bảo hành? | Ngày hiện tại ≤ ngày hết hạn theo chính sách | Còn → G2 · Hết → báo giá sửa thu phí, khách quyết định → G1b | NV tiếp nhận + hệ thống |
| G1b | Khách có đồng ý sửa thu phí? | Khách xác nhận báo giá | Đồng ý → chuyển luồng dịch vụ thu phí (ngoài phạm vi) · Không → trả máy, kết thúc | Khách hàng |
| G2 | Khách yêu cầu bảo hành hay đổi trả? | Còn trong thời hạn đổi trả hay không | Đổi trả → G2b · Bảo hành → bước 5 | Khách + chính sách |
| G2b | Đủ điều kiện đổi trả (còn hạn đổi, đủ hộp và phụ kiện, máy không hư hại do người dùng)? | Đối chiếu chính sách đổi trả | Đủ → đổi máy hoặc hoàn tiền (bước 14/15) · Không → chuyển sang luồng bảo hành | NV tiếp nhận + Quản lý |
| G3 | Máy có đủ điều kiện bảo hành? | Không rơi vỡ, vào nước, không tự tháo, tem còn nguyên | Đủ → bước 6 · Không → từ chối bảo hành, báo giá sửa thu phí → G1b | NV tiếp nhận + KTV |
| G4 | Lỗi thuộc loại nào? | Phần mềm / phần cứng / không tái hiện được | Phần mềm → bước 7 · Phần cứng → bước 8 · Không tái hiện → G4b | KTV |
| G4b | Khách có đồng ý để lại máy theo dõi? | Khách quyết định | Có → bước 8 · Không → trả máy kèm ghi chú, kết thúc | Khách hàng |
| G5 | Xử lý tại chỗ có thành công? | Máy hoạt động bình thường sau xử lý | Thành công → bước 13 · Không → bước 8 | KTV |
| G6 | Kết luận của trung tâm bảo hành? | Sửa được / phải đổi máy / từ chối bảo hành | Sửa → bước 11 · Đổi → bước 14 · Từ chối → thông báo lý do, G1b | **Trung tâm bảo hành** |
| G7 | Máy nhận về có đúng máy và đã xử lý đạt? | Đối chiếu IMEI và kết luận | Đạt → bước 12 · Không đạt → gửi lại trung tâm | NV tiếp nhận |
| G8 | Khách có đồng ý với kết quả khi nhận máy? | Khách kiểm tra tại chỗ | Đồng ý → đóng hồ sơ · Không → mở khiếu nại, chuyển quản lý | Khách hàng |

**Mười một điểm quyết định — vượt xa mốc 7 gateway.** Khi vẽ BPMN, G4 và G6 là gateway
ba nhánh; trung tâm bảo hành vẽ thành pool riêng vì là tổ chức bên ngoài.

## 7. Ngoại lệ và xử lý

| Mã | Tình huống ngoại lệ | Cách xử lý | Ai xử lý |
|---|---|---|---|
| E1 | Khách không có hóa đơn, không nhớ nơi mua | Tra theo IMEI trong hệ thống; không có dữ liệu thì từ chối bảo hành theo chính sách | NV tiếp nhận |
| E2 | Máy hết hàng để đổi khi đã có quyết định đổi máy | Điều chuyển từ cửa hàng khác (M3), hoặc thỏa thuận đổi model tương đương | Quản lý cửa hàng |
| E3 | Trung tâm bảo hành trả kết quả trễ hơn hẹn | Thông báo khách, gia hạn, ghi nhận vào hồ sơ khiếu nại | NV tiếp nhận |
| E4 | Khách khiếu nại kết luận từ chối bảo hành | Chuyển quản lý cửa hàng, lập biên bản, có thể gửi kiểm định lại | Quản lý cửa hàng |
| E5 | Máy mất hoặc hư hại thêm trong quá trình vận chuyển | Lập biên bản, đền bù theo quy định | Quản lý + Trung tâm bảo hành |
| E6 | Khách không quay lại nhận máy sau nhiều lần thông báo | Lưu kho theo thời hạn quy định, ghi nhận vào hồ sơ | NV tiếp nhận |
| E7 | Dữ liệu cá nhân còn trong máy gửi đi bảo hành | Nhắc khách sao lưu và xóa dữ liệu trước khi gửi; ghi vào phiếu tiếp nhận | NV tiếp nhận |

## 8. Quy tắc nghiệp vụ

| Mã | Quy tắc | Nguồn |
|---|---|---|
| R1 | Căn cứ bảo hành là IMEI gắn với đơn hàng trong hệ thống, không phụ thuộc việc khách còn giữ hóa đơn giấy | Quan sát + chính sách công bố |
| R2 | Máy có dấu hiệu rơi vỡ, vào nước, tự tháo thì không thuộc điều kiện bảo hành | Chính sách công bố |
| R3 | Thời hạn đổi trả ngắn hơn thời hạn bảo hành và có điều kiện riêng về hộp, phụ kiện | Chính sách công bố |
| R4 | Quyết định cuối về lỗi phần cứng thuộc **trung tâm bảo hành / hãng**, không thuộc cửa hàng | Quan sát |
| R5 | Với TopZone, khâu sửa chữa đi theo kênh ủy quyền của Apple — điều kiện tiếp nhận và thời gian phản hồi khác TGDĐ | Chính sách công bố — (chưa xác minh chi tiết) |
| R6 | Khách phải tự sao lưu và xóa dữ liệu trước khi gửi máy đi bảo hành | Quan sát |
| R7 | Máy lỗi thu hồi nhập vào kho hàng lỗi, không quay lại kho bán | (ước lượng) — cần xác minh |

R5 và R7 đưa vào bảng giả định Chương 4.

## 9. Chỉ số đo lường

| Chỉ số | Đơn vị | Cách đo | Giá trị ghi nhận | Nguồn |
|---|---|---|---|---|
| Thời gian tiếp nhận tại quầy (bước 1–8) | phút | Bấm giờ theo chặng | (chờ khảo sát 23/08) | bấm giờ, n = … |
| Thời gian chờ tới lượt tại quầy bảo hành | phút | Bấm giờ | (chờ khảo sát) | bấm giờ |
| Thời gian chờ kết quả từ trung tâm bảo hành | ngày | Hỏi nhân viên (câu phỏng vấn 2) | (chờ khảo sát) | phỏng vấn |
| Tỷ lệ ca xử lý xong tại cửa hàng, không phải gửi đi | % | Hỏi nhân viên (câu phỏng vấn 1) | (chờ khảo sát) | phỏng vấn |

Chỉ số 3 và 4 là hai con số quan trọng nhất của C4: chúng quyết định phần lớn cycle time
và là căn cứ cho đề xuất cải tiến ở mục 4.7.

## 10. Hệ thống và biểu mẫu liên quan

| Tên | Loại | Ghi chú |
|---|---|---|
| Hệ thống quản lý bảo hành | Hệ thống | Tra IMEI, hạn bảo hành, lịch sử máy |
| ERP | Hệ thống | Ghi nhận đổi trả, điều chỉnh tồn và công nợ |
| Phiếu tiếp nhận bảo hành | Biểu mẫu | Ảnh mẫu cần chụp — **ưu tiên cao nhất** |
| Bảng niêm yết chính sách đổi trả | Biểu mẫu | Ảnh mẫu cần chụp |
| Biên bản khiếu nại | Biểu mẫu | Chỉ phát sinh khi có tranh chấp |

## 11. Điểm nghẽn quan sát được

| # | Điểm nghẽn | Vì sao là nghẽn | Nhóm lãng phí | Bằng chứng cần có |
|---|---|---|---|---|
| B1 | Bước 1 — chờ tới lượt tại quầy bảo hành | Quầy bảo hành thường ít người trực hơn quầy bán; khách chờ lâu ngay từ đầu | **Hold** | Bấm giờ thời gian chờ |
| B2 | Bước 9–10 — gửi máy lên trung tâm và chờ kết quả | Khoảng chờ dài nhất toàn quy trình, cửa hàng không kiểm soát được; khách không có máy dùng trong suốt thời gian này | **Hold** | Câu phỏng vấn 2 |
| B3 | Bước 2 — tra cứu thủ công khi khách không có hóa đơn | Mất thời gian dò tìm, đôi khi phải hỏi lại khách nhiều lần | **Overdo** | Quan sát tại quầy |
| B4 | G7 — máy nhận về không đạt, phải gửi lại | Lặp lại toàn bộ chu kỳ vận chuyển và chờ | **Move** + **Overdo** | Câu phỏng vấn 1 |
| B5 | Bước 16 — dữ liệu lỗi về M2 chậm | Vòng phản hồi C4 → M2 trễ thì việc đánh giá nhà cung cấp không kịp phản ánh chất lượng thực tế | **Hold** | Phỏng vấn — (chưa xác minh) |

Năm điểm này là đầu vào cho bảng VA/BVA/NVA của C4 (mục 4.3) và cho biểu đồ xương cá
(mục 4.5).

## 12. Nguồn tham chiếu

| Nguồn | Loại | Trạng thái |
|---|---|---|
| Buổi khảo sát tại cửa hàng TGDĐ — câu hỏi 1, 2 | Phỏng vấn | Dự kiến 23/08, phụ trách Hưng |
| Ảnh phiếu tiếp nhận bảo hành | Evidence | Chờ chụp — ưu tiên cao |
| Chính sách bảo hành TGDĐ | Tài liệu công khai | Chờ bổ sung kèm ngày truy cập |
| Chính sách bảo hành TopZone / Apple ủy quyền | Tài liệu công khai | Chờ bổ sung — dùng cho R5 |

> Hồ sơ này dựng từ quan sát bên ngoài và suy luận, **không phải quy trình chuẩn do MWG
> ban hành**. C4 là quy trình có nhiều nhánh nhất trong ba quy trình cốt lõi được giao —
> đếm lại 11 điểm quyết định ở mục 6 trước khi khóa mô hình BPMN ngày 30/08.
