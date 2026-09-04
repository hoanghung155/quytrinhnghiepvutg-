# Issue Register — Bảng tổng hợp phát hiện

**Người lập:** Nguyễn Ngọc Danh (v1, IR-01–IR-13) · Nguyễn Thị Hồng Phúc (v2, IR-14–IR-31)
**Mục:** 4.6 Chương 4 · **Phiên bản:** v2

Bảng này gom toàn bộ điểm nghẽn đã ghi nhận ở mục 11 của từng hồ sơ quy trình, gán mã
thống nhất `IR-xx`, và là căn cứ cho phần đề xuất cải tiến ở mục 4.7.

> **Trạng thái v2:** 31 phát hiện, đều đến từ phân tích hồ sơ quy trình. Cột **Mức độ** và
> cột **Bằng chứng** chỉ điền được sau buổi khảo sát 23/08 — hiện để `(chờ khảo sát)` với
> phần xác minh được tại cửa hàng, và `(chưa xác minh)` với phần thuộc khối văn phòng hoặc
> cấp tập đoàn mà nhóm không có kênh tiếp cận. Không xếp hạng ưu tiên khi chưa có số đo,
> vì thứ tự ưu tiên sai còn tệ hơn không xếp.

---

## 1. Bảng tổng hợp

| Mã | Quy trình | Nguồn | Phát hiện | Nhóm lãng phí | Mức độ | Bằng chứng |
|---|---|---|---|---|---|---|
| IR-01 | C1 | B1 | Khâu kích hoạt máy và chuyển dữ liệu chiếm phần lớn thời gian giao dịch, giữ chân nhân viên | Overdo | (chờ khảo sát) | Bấm giờ riêng bước 10 |
| IR-02 | C1 | B2 | Kiểm tra tồn kho diễn ra muộn (bước 4), công tư vấn trước đó bị bỏ phí khi hết hàng | Overdo | (chờ khảo sát) | Đếm lượt phải đổi model |
| IR-03 | C1 | B3 | Khách chờ tới lượt được tư vấn trong giờ cao điểm | Hold | (chờ khảo sát) | Bấm giờ thời gian chờ |
| IR-04 | C1 | B4 | Nhiều giao dịch song song nghẽn ở một quầy thu ngân | Hold | (chờ khảo sát) | Đếm quầy thu ngân / NV tư vấn |
| IR-05 | C3 | B1 | Chờ thẩm định tín dụng — toàn bộ quy trình dừng chờ actor bên ngoài | Hold | (chờ khảo sát) | Câu phỏng vấn 3 |
| IR-06 | C3 | B2 | Vòng lặp bổ sung hồ sơ quay lại thẩm định, nhân đôi thời gian chờ | Overdo | (chờ khảo sát) | Câu phỏng vấn 4 |
| IR-07 | C3 | B3 | Nhập liệu hồ sơ thủ công, dễ sai và phải làm lại | Overdo | (chờ khảo sát) | Quan sát tại quầy |
| IR-08 | C3 | B4 | Hết hàng sau khi hồ sơ đã duyệt, có nguy cơ phải làm lại toàn bộ hồ sơ | Move | (chờ khảo sát) | Câu phỏng vấn 5 |
| IR-09 | C4 | B1 | Khách chờ tới lượt tại quầy bảo hành, quầy ít người trực hơn quầy bán | Hold | (chờ khảo sát) | Bấm giờ thời gian chờ |
| IR-10 | C4 | B2 | Gửi máy lên trung tâm và chờ kết quả — khoảng chờ dài nhất, cửa hàng không kiểm soát | Hold | (chờ khảo sát) | Câu phỏng vấn 2 |
| IR-11 | C4 | B3 | Tra cứu thủ công khi khách không có hóa đơn | Overdo | (chờ khảo sát) | Quan sát tại quầy |
| IR-12 | C4 | B4 | Máy nhận về không đạt phải gửi lại, lặp toàn bộ chu kỳ vận chuyển | Move + Overdo | (chờ khảo sát) | Câu phỏng vấn 1 |
| IR-13 | C4, M2 | C4 B5 · M2 B5 | Vòng phản hồi dữ liệu lỗi C4 → M2 chậm, đánh giá NCC không phản ánh chất lượng thực tế | Hold | (chờ khảo sát) | Phỏng vấn — chưa xác minh |
| IR-14 | M1 | B1 | Chờ đề xuất điều chỉnh từ nhiều cửa hàng, tiến độ kế hoạch phụ thuộc điểm bán phản hồi chậm nhất | Hold | (chưa xác minh) | Câu hỏi Q1 |
| IR-15 | M1 | B2 | Kế hoạch bị trả lại ở khâu phê duyệt, phải lập lại từ bước dự báo | Overdo | (chưa xác minh) | Dữ liệu nội bộ — chưa có kênh |
| IR-16 | M1 | B3 | Dự báo model mới không có cơ sở lịch sử; sai số về sau phải chữa bằng điều chuyển ở M3 | Move | (chưa xác minh) | Đối chiếu tần suất điều chuyển ở M3 |
| IR-17 | M1 | B4 | Vòng phản hồi sai lệch dự báo chỉ dùng được cho kỳ sau, không hiệu chỉnh được trong kỳ đang chạy | Hold | (chưa xác minh) | Dữ liệu nội bộ — chưa có kênh |
| IR-18 | M2 | B1 | Chờ nhà cung cấp gửi hồ sơ năng lực và báo giá | Hold | (chưa xác minh) | Dữ liệu nội bộ — chưa có kênh |
| IR-19 | M2 | B2 | PO quá hạn xác nhận, vừa phát sinh chờ vừa phát sinh việc nhắc lại | Hold + Overdo | (chưa xác minh) | Dữ liệu nội bộ — chưa có kênh |
| IR-20 | M2 | B3 | Lô hàng không đạt nghiệm thu phải giao lại, lặp cả chu kỳ vận chuyển và kiểm tra | Move + Overdo | (chưa xác minh) | Dữ liệu nội bộ — chưa có kênh |
| IR-21 | M2 | B4 | Hồ sơ nằm chờ ở cấp duyệt khi giá trị hợp đồng vượt hạn mức | Hold | (chưa xác minh) | Dữ liệu nội bộ — chưa có kênh |
| IR-22 | M3 | B1 | Vận chuyển giữa kho tổng và cửa hàng, hoặc giữa hai cửa hàng — khách C3 và C4 chờ trực tiếp trên khoảng này | Move + Hold | (chờ khảo sát) | Câu hỏi Q3 |
| IR-23 | M3 | B2 | Yêu cầu điều chuyển gấp vẫn phải đi qua dò nguồn và chuỗi duyệt | Hold | (chờ khảo sát) | Câu hỏi Q2 |
| IR-24 | M3 | B3 | Không tìm được cửa hàng nguồn, công tư vấn và lập hồ sơ ở C3/C4 trước đó bỏ phí | Overdo | (chờ khảo sát) | Câu hỏi Q2 |
| IR-25 | M3 | B4 | Chênh lệch kiểm kê buộc kiểm đếm lại và truy nguyên nhân | Overdo | (chờ khảo sát) | Câu hỏi Q4 |
| IR-26 | M3 | B5 | Hàng đã nằm tại cửa hàng nhưng chưa xác nhận nhận nên chưa bán được | Hold | (chờ khảo sát) | Quan sát tại cửa hàng |
| IR-27 | M4 | B1 | Chờ đàm phán điều khoản thuê với chủ mặt bằng, không xác định thời hạn | Hold | (chưa xác minh) | Cấp tập đoàn — ngoài tầm khảo sát |
| IR-28 | M4 | B2 | Không thỏa thuận được mặt bằng, toàn bộ công khảo sát và thẩm định bỏ phí | Overdo | (chưa xác minh) | Cấp tập đoàn — ngoài tầm khảo sát |
| IR-29 | M4 | B3 | Chuỗi thu thập giải trình qua nhiều cấp kéo dài kỳ rà soát điểm bán | Hold | (chưa xác minh) | Cấp tập đoàn — ngoài tầm khảo sát |
| IR-30 | M4 | B4 | Đóng điểm bán phát sinh điều chuyển toàn bộ tồn sang điểm khác, ngoài kế hoạch điều chuyển thường | Move | (chưa xác minh) | Đối chiếu với M3 |
| IR-31 | M4 | B5 | Chỉ phát hiện điểm bán mới kém hiệu quả sau khi chi phí thuê và vận hành đã phát sinh | Hold | (chưa xác minh) | Cấp tập đoàn — ngoài tầm khảo sát |

> **Bổ sung v2 — Hồng Phúc, 20/08/2026.** IR-14 đến IR-31 lấy từ mục 11 của bốn hồ sơ
> M1–M4. Hai điều chỉnh so với v1:
>
> 1. **IR-13 nay có hai nguồn.** Điểm nghẽn B5 của hồ sơ M2 chính là IR-13 nhìn từ phía
>    M2. Cột "Quy trình" và "Nguồn" đã ghi cả hai thay vì tạo mã mới — tránh đếm một vấn
>    đề thành hai.
> 2. **IR-10 được đếm thêm ở nhóm Move.** Phát hiện này gồm hai phần: gửi máy đi (vận
>    chuyển, Move) và chờ kết quả (Hold). Xem ghi chú 1 ở
>    [bảng VA/BVA/NVA của C4](../dinh-tinh/va-bva-nva-C4.md) mục 4. Mã IR-10 giữ nguyên,
>    chỉ bổ sung cách đếm.
>
> **Mức độ tin cậy không đồng đều.** IR-22 đến IR-26 (M3) có thể xác minh ở buổi khảo sát
> 23/08. IR-27 đến IR-31 (M4) là quy trình cấp tập đoàn, gần như chắc chắn sẽ ở lại trạng
> thái `(chưa xác minh)` trong bản nộp — **không xếp ngang hàng với các phát hiện đã có
> quan sát** khi xếp ưu tiên ở mục 4.7.

## 2. Phân bố theo nhóm lãng phí

Chi tiết cấp 2 của từng nhóm ở
[bảng phân nhóm Move / Hold / Overdo](../dinh-tinh/nhom-lang-phi-move-hold-overdo.md).

| Nhóm | Số phát hiện | Mã |
|---|---:|---|
| **Hold** — chờ đợi, tồn đọng | 17 | IR-03, IR-04, IR-05, IR-09, IR-10, IR-13, IR-14, IR-17, IR-18, IR-19, IR-21, IR-22, IR-23, IR-26, IR-27, IR-29, IR-31 |
| **Overdo** — làm thừa, làm lại | 12 | IR-01, IR-02, IR-06, IR-07, IR-11, IR-12, IR-15, IR-19, IR-20, IR-24, IR-25, IR-28 |
| **Move** — di chuyển, vận chuyển | 7 | IR-08, IR-10, IR-12, IR-16, IR-20, IR-22, IR-30 |

Tổng 31 phát hiện. Năm mã được đếm ở hai nhóm vì bản thân chúng có hai thành phần khác
nhau: IR-10, IR-12, IR-19, IR-20, IR-22. Cộng theo nhóm ra 36 = 31 + 5.

Nhóm **Hold** chiếm hơn một nửa. Chia tiếp thành ba loại cần ba hướng cải tiến khác nhau:

| Loại chờ | Mã | Cửa hàng can thiệp được? |
|---|---|---|
| Chờ **actor bên ngoài** | IR-05, IR-10, IR-18, IR-22, IR-27 | Không — chỉ giảm được ảnh hưởng |
| Chờ **nguồn lực nội bộ** | IR-03, IR-04, IR-09, IR-26 | Có — bố trí người, sửa thủ tục |
| Chờ **quyết định hoặc dữ liệu từ cấp trên** | IR-13, IR-14, IR-17, IR-19, IR-21, IR-23, IR-29, IR-31 | Một phần — thuộc thẩm quyền khối văn phòng |

Phân loại này quan trọng hơn con số tổng: một đề xuất "giảm thời gian chờ" chung chung sẽ
vô nghĩa với nhóm thứ nhất.

## 3. Phân bố theo quy trình

| Quy trình | Số phát hiện | Ghi chú |
|---|---:|---|
| C1 — Bán tại cửa hàng | 4 | Không mô hình hóa BPMN, nhưng là quy trình có lưu lượng lớn nhất |
| C3 — Bán trả góp | 4 | Có BPMN, 10 gateway |
| C4 — Bảo hành đổi trả | 5 | Có BPMN, 11 gateway |
| M1 — Hoạch định nhu cầu | 4 | Không BPMN; phát hiện chủ yếu `(chưa xác minh)` |
| M2 — Quản lý nhà cung cấp | 4 | Có BPMN, 9 gateway; IR-13 dùng chung với C4 |
| M3 — Kho và điều chuyển | 5 | Có BPMN, 12 gateway — nhóm quản lý xác minh được nhiều nhất |
| M4 — Mạng lưới cửa hàng | 5 | Không BPMN; **toàn bộ `(chưa xác minh)`**, độ tin cậy thấp nhất |

Chưa có phát hiện nào cho C2 và S1–S4 vì hồ sơ các quy trình đó thuộc Hưng và Thanh Phúc.
Khi các hồ sơ đó hoàn thiện, bổ sung theo cùng định dạng và đánh số tiếp từ **IR-32**.

## 4. Việc còn phải làm trước 02/09

- [ ] Điền cột **Mức độ** sau khi có số liệu bấm giờ và phỏng vấn (23/08)
- [ ] Điền cột **Bằng chứng** bằng đường dẫn thật trong `evidence/`
- [ ] Xếp thứ tự ưu tiên theo hai trục: mức ảnh hưởng × khả năng can thiệp của cửa hàng
- [x] Bổ sung phát hiện từ hồ sơ M1–M4 (Hồng Phúc) — xong 20/08, IR-14 đến IR-31
- [ ] Bổ sung phát hiện từ hồ sơ C2 (Hưng) và S1–S4 (Thanh Phúc), đánh số từ IR-32
- [x] Đối chiếu với biểu đồ xương cá mục 4.5 — xem
      [fishbone C4](../dinh-tinh/fishbone-C4.md) và
      [fishbone điều chuyển gấp](../dinh-tinh/fishbone-dieu-chuyen-gap.md)

> Lưu ý về trục "khả năng can thiệp": IR-05 và IR-10 là hai phát hiện nặng nhất về thời
> gian nhưng cửa hàng **không kiểm soát được** actor bên ngoài. Đề xuất cải tiến cho hai
> mục này phải nhắm vào việc giảm ảnh hưởng của khoảng chờ, không phải xóa khoảng chờ.
