# Phân nhóm lãng phí — Move / Hold / Overdo

**Người lập:** Nguyễn Thị Hồng Phúc · **Mục:** 4.4 Chương 4 · **Phiên bản:** v1
**Nguồn:** [Issue Register v2](../issue-register/issue-register.md) — 31 phát hiện IR-01 đến IR-31

---

## 1. Cách phân nhóm dùng trong báo cáo

Ba nhóm **Move**, **Hold**, **Overdo** là **cấp 1** — đây là tiêu đề của từng nhóm trong
Chương 4. Bảy loại lãng phí gốc trong Lean được gom vào ba nhóm này và chỉ xuất hiện ở
**cấp 2**, dùng để mô tả chi tiết bên trong mỗi nhóm.

| Cấp 1 | Câu hỏi nhận diện | Cấp 2 — dạng biểu hiện gặp trong đề tài |
|---|---|---|
| **Move** | Người, hàng hóa hoặc hồ sơ có phải di chuyển không? Việc di chuyển đó có làm nó tốt lên không? | Vận chuyển hàng giữa kho và cửa hàng · vận chuyển máy đi bảo hành · di chuyển thao tác của nhân viên trong cùng một ca |
| **Hold** | Có ai hoặc cái gì đang đứng yên chờ không? | Khách chờ tới lượt · hồ sơ chờ thẩm định · hàng nằm chờ xác nhận · dữ liệu chờ tới kỳ mới được dùng · tồn đọng ở một khâu |
| **Overdo** | Có việc nào đang làm thừa, làm lại, hoặc làm rồi bỏ đi không? | Nhập liệu thủ công lặp · bổ sung hồ sơ do kiểm chưa kỹ · kiểm đếm lại do lệch tồn · công đã bỏ ra bị hủy vì nhánh sau không thành |

> **Lý do không lấy tên bảy lãng phí gốc làm tiêu đề:** rubric của môn gom bảy loại thành
> ba nhóm này. Dùng "Vận chuyển", "Chờ đợi", "Khuyết tật"… làm tiêu đề cấp 1 là trình bày
> sai khung phân tích được yêu cầu, dù nội dung bên dưới có đúng.

## 2. Nhóm **Move** — 7 phát hiện

Di chuyển người, hàng hoặc hồ sơ mà bản thân việc di chuyển không làm chúng tốt lên.

| Mã | Quy trình | Phát hiện | Dạng biểu hiện (cấp 2) |
|---|---|---|---|
| IR-08 | C3 | Hết hàng sau khi hồ sơ trả góp đã duyệt, phải điều chuyển từ cửa hàng khác | Vận chuyển hàng phát sinh ngoài kế hoạch |
| IR-10 | C4 | Gửi máy lên trung tâm bảo hành | Vận chuyển sản phẩm đi và về |
| IR-12 | C4 | Máy nhận về không đạt, phải gửi lại trung tâm | Vận chuyển lặp lại |
| IR-16 | M1 | Sai số dự báo model mới, về sau phải chữa bằng điều chuyển ở M3 | Vận chuyển sinh ra từ một sai sót ở khâu trước |
| IR-20 | M2 | Lô hàng không đạt nghiệm thu phải giao lại | Vận chuyển lặp lại |
| IR-22 | M3 | Vận chuyển giữa kho tổng và cửa hàng, hoặc giữa hai cửa hàng | Vận chuyển là bản chất của quy trình |
| IR-30 | M4 | Đóng điểm bán, phải chuyển toàn bộ tồn sang điểm khác | Vận chuyển khối lượng lớn ngoài kế hoạch |

**Nhận xét.** Chỉ IR-22 là vận chuyển *thuộc bản chất* của quy trình — hàng phải đi từ kho
tới cửa hàng thì mới bán được. Sáu phát hiện còn lại đều là vận chuyển **sinh ra từ một
vấn đề ở chỗ khác**: dự báo sai (IR-16), kiểm chưa kỹ (IR-20), sửa không đạt (IR-12), hết
hàng cục bộ (IR-08), quyết định đóng điểm (IR-30). Đây là lý do Move không nên xử lý bằng
cách "tối ưu tuyến vận chuyển" mà phải truy ngược lên nguyên nhân sinh ra chuyến đi.

## 3. Nhóm **Hold** — 17 phát hiện

Người, hàng, hồ sơ hoặc dữ liệu đứng yên chờ.

| Mã | Quy trình | Phát hiện | Dạng biểu hiện (cấp 2) | Cửa hàng can thiệp được? |
|---|---|---|---|---|
| IR-03 | C1 | Khách chờ tới lượt được tư vấn giờ cao điểm | Khách chờ nguồn lực nội bộ | Có |
| IR-04 | C1 | Nghẽn ở một quầy thu ngân | Khách chờ nguồn lực nội bộ | Có |
| IR-05 | C3 | Chờ thẩm định tín dụng | Chờ actor bên ngoài | Không |
| IR-09 | C4 | Khách chờ tới lượt tại quầy bảo hành | Khách chờ nguồn lực nội bộ | Có |
| IR-10 | C4 | Chờ kết quả từ trung tâm bảo hành | Chờ actor bên ngoài | Không |
| IR-13 | C4, M2 | Dữ liệu lỗi về tới khâu đánh giá NCC chậm | Dữ liệu chờ tới kỳ mới được dùng | Một phần |
| IR-14 | M1 | Chờ đề xuất điều chỉnh từ nhiều cửa hàng | Chờ phản hồi nội bộ nhiều đầu mối | Một phần |
| IR-17 | M1 | Sai lệch dự báo chỉ hiệu chỉnh được ở kỳ sau | Dữ liệu chờ tới kỳ mới được dùng | Một phần |
| IR-18 | M2 | Chờ NCC gửi hồ sơ năng lực và báo giá | Chờ actor bên ngoài | Không |
| IR-19 | M2 | PO quá hạn xác nhận | Chờ actor bên ngoài | Không |
| IR-21 | M2 | Hồ sơ chờ ở cấp duyệt khi vượt hạn mức | Chờ quyết định cấp trên | Một phần |
| IR-22 | M3 | Thời gian hàng đi đường khi điều chuyển | Hàng và khách cùng chờ | Không |
| IR-23 | M3 | Yêu cầu gấp vẫn phải qua dò nguồn và duyệt | Chờ thủ tục nội bộ | Một phần |
| IR-26 | M3 | Hàng đã tới cửa hàng nhưng chưa xác nhận nên chưa bán được | Tồn đọng do thủ tục | Có |
| IR-27 | M4 | Chờ đàm phán với chủ mặt bằng | Chờ actor bên ngoài | Không |
| IR-29 | M4 | Chuỗi thu thập giải trình qua nhiều cấp | Chờ phản hồi nội bộ nhiều đầu mối | Một phần |
| IR-31 | M4 | Chỉ phát hiện điểm bán kém hiệu quả sau khi chi phí đã phát sinh | Dữ liệu chờ tới kỳ mới được dùng | Một phần |

**Nhận xét.** Hold là nhóm lớn nhất, nhưng con số 17 tự nó không dùng được vì ba loại chờ
bên trong đòi hỏi ba hướng cải tiến hoàn toàn khác nhau:

| Loại chờ | Số phát hiện | Hướng cải tiến khả dĩ |
|---|---:|---|
| Chờ actor bên ngoài | 6 | Không xóa được khoảng chờ. Chỉ giảm ảnh hưởng: cho khách về và báo kết quả sau (C3 ngoại lệ E2), báo trước thời gian dự kiến, chuẩn bị sẵn phương án thay thế |
| Chờ nguồn lực nội bộ | 4 | Xóa được: bố trí người theo giờ cao điểm, gộp quầy, sửa thủ tục xác nhận |
| Chờ quyết định hoặc dữ liệu | 7 | Rút ngắn được: hạ ngưỡng phải trình duyệt, tăng tần suất đưa dữ liệu về, cho phép hiệu chỉnh giữa kỳ |

## 4. Nhóm **Overdo** — 12 phát hiện

Làm thừa, làm lại, hoặc làm rồi bỏ đi.

| Mã | Quy trình | Phát hiện | Dạng biểu hiện (cấp 2) |
|---|---|---|---|
| IR-01 | C1 | Kích hoạt máy và chuyển dữ liệu chiếm phần lớn thời gian giao dịch | Xử lý thừa tại quầy |
| IR-02 | C1 | Kiểm tra tồn kho diễn ra muộn, công tư vấn trước đó bỏ phí | Công đã bỏ ra bị hủy |
| IR-06 | C3 | Vòng lặp bổ sung hồ sơ | Làm lại do kiểm chưa kỹ |
| IR-07 | C3 | Nhập liệu hồ sơ thủ công | Nhập liệu lặp, dễ sai |
| IR-11 | C4 | Tra cứu thủ công khi khách không có hóa đơn | Xử lý thừa do thiếu dữ liệu |
| IR-12 | C4 | Máy nhận về không đạt, phải xử lý lại | Làm lại toàn chu kỳ |
| IR-15 | M1 | Kế hoạch bị trả lại, lập lại từ khâu dự báo | Làm lại do bị bác ở khâu duyệt |
| IR-19 | M2 | Phát sinh việc nhắc PO quá hạn | Việc sinh ra chỉ để chữa một khoảng chờ |
| IR-20 | M2 | Lô không đạt phải kiểm tra lại từ đầu | Làm lại do kiểm chưa kỹ |
| IR-24 | M3 | Không tìm được cửa hàng nguồn, công tư vấn và lập hồ sơ ở C3/C4 bỏ phí | Công đã bỏ ra bị hủy |
| IR-25 | M3 | Chênh lệch kiểm kê phải kiểm đếm lại và truy nguyên nhân | Làm lại do dữ liệu không khớp |
| IR-28 | M4 | Không thỏa thuận được mặt bằng, công khảo sát và thẩm định bỏ phí | Công đã bỏ ra bị hủy |

**Nhận xét.** Overdo chia thành hai dạng có cách xử lý khác hẳn nhau:

- **Làm lại vì khâu trước làm chưa kỹ** — IR-06, IR-20, IR-25, IR-12. Xử lý bằng cách siết
  chất lượng ở khâu trước, và đây là dạng dễ cải tiến nhất trong toàn bộ 31 phát hiện.
- **Công đã bỏ ra bị hủy vì một nhánh sau không thành** — IR-02, IR-24, IR-28. Xử lý bằng
  cách **đưa điểm kiểm tra lên sớm hơn**: kiểm tồn trước khi tư vấn (IR-02), dò nguồn
  trước khi hứa với khách (IR-24), sàng lọc mặt bằng trước khi thẩm định tài chính (IR-28).
  Ba phát hiện ở ba quy trình khác nhau nhưng cùng một dạng và cùng một cách chữa.

## 5. Tổng hợp ba nhóm

| Nhóm | Số phát hiện | Tỷ trọng | Đặc điểm nổi bật |
|---|---:|---:|---|
| **Hold** | 17 | 47% | Nhóm lớn nhất, nhưng 6 phát hiện cửa hàng không can thiệp được |
| **Overdo** | 12 | 33% | Nhóm dễ cải tiến nhất; có 3 phát hiện cùng chung một cách chữa |
| **Move** | 7 | 20% | Chỉ 1 phát hiện là vận chuyển thuộc bản chất, 6 còn lại sinh ra từ vấn đề ở chỗ khác |

Tỷ trọng tính trên 36 lượt đếm (31 phát hiện, 5 mã đếm ở hai nhóm: IR-10, IR-12, IR-19,
IR-20, IR-22).

> **Cảnh báo khi đọc bảng này.** Tỷ trọng ở trên tính theo **số phát hiện**, không theo
> **mức độ ảnh hưởng**. Một phát hiện Hold kéo dài nhiều ngày (IR-10) và một phát hiện
> Overdo tốn vài phút (IR-11) đang được đếm ngang nhau. Sau khi có số liệu khảo sát 23/08,
> phải bổ sung cột mức độ trước khi dùng tỷ trọng này để xếp ưu tiên cải tiến ở mục 4.7.
> Hiện tại bảng chỉ dùng để **mô tả phân bố**, không dùng để kết luận cái nào quan trọng hơn.
