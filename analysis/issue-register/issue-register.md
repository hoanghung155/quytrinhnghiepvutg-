# Issue Register — Bảng tổng hợp phát hiện

**Người lập:** Nguyễn Ngọc Danh · **Mục:** 4.6 Chương 4 · **Phiên bản:** v1

Bảng này gom toàn bộ điểm nghẽn đã ghi nhận ở mục 11 của từng hồ sơ quy trình, gán mã
thống nhất `IR-xx`, và là căn cứ cho phần đề xuất cải tiến ở mục 4.7.

> **Trạng thái v1:** 13 phát hiện đều đến từ phân tích hồ sơ quy trình. Cột **Mức độ** và
> cột **Bằng chứng** chỉ điền được sau buổi khảo sát 23/08 — hiện để `(chờ khảo sát)`.
> Không xếp hạng ưu tiên khi chưa có số đo, vì thứ tự ưu tiên sai còn tệ hơn không xếp.

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
| IR-13 | C4 | B5 | Vòng phản hồi dữ liệu lỗi C4 → M2 chậm, đánh giá NCC không phản ánh chất lượng thực tế | Hold | (chờ khảo sát) | Phỏng vấn — chưa xác minh |

## 2. Phân bố theo nhóm lãng phí

| Nhóm | Số phát hiện | Mã |
|---|---:|---|
| **Hold** — chờ đợi, tồn đọng | 6 | IR-03, IR-04, IR-05, IR-09, IR-10, IR-13 |
| **Overdo** — làm thừa, làm lại | 6 | IR-01, IR-02, IR-06, IR-07, IR-11, IR-12 |
| **Move** — di chuyển, vận chuyển | 2 | IR-08, IR-12 |

IR-12 đếm ở cả hai nhóm vì vừa phát sinh vận chuyển lặp vừa phát sinh xử lý lặp.

Nhóm **Hold** chiếm gần một nửa và tập trung ở hai chỗ: chờ actor bên ngoài (IR-05 công ty
tài chính, IR-10 trung tâm bảo hành) và chờ nguồn lực nội bộ (IR-03, IR-04, IR-09). Hai
loại này cần hai hướng cải tiến khác nhau — chi tiết ở mục 4.7.

## 3. Phân bố theo quy trình

| Quy trình | Số phát hiện | Ghi chú |
|---|---:|---|
| C1 — Bán tại cửa hàng | 4 | Không mô hình hóa BPMN, nhưng là quy trình có lưu lượng lớn nhất |
| C3 — Bán trả góp | 4 | Có BPMN, 10 gateway |
| C4 — Bảo hành đổi trả | 5 | Có BPMN, 11 gateway — nhiều phát hiện nhất |

Chưa có phát hiện nào cho C2, M1–M4, S1–S4 vì hồ sơ các quy trình đó thuộc thành viên
khác. Khi các hồ sơ đó hoàn thiện, bổ sung vào bảng này theo cùng định dạng và đánh số
tiếp từ IR-14.

## 4. Việc còn phải làm trước 02/09

- [ ] Điền cột **Mức độ** sau khi có số liệu bấm giờ và phỏng vấn (23/08)
- [ ] Điền cột **Bằng chứng** bằng đường dẫn thật trong `evidence/`
- [ ] Xếp thứ tự ưu tiên theo hai trục: mức ảnh hưởng × khả năng can thiệp của cửa hàng
- [ ] Bổ sung phát hiện từ hồ sơ M1–M4 (Hồng Phúc) và S1–S4 (Thanh Phúc)
- [ ] Đối chiếu với biểu đồ xương cá mục 4.5 để không bỏ sót nguyên nhân gốc

> Lưu ý về trục "khả năng can thiệp": IR-05 và IR-10 là hai phát hiện nặng nhất về thời
> gian nhưng cửa hàng **không kiểm soát được** actor bên ngoài. Đề xuất cải tiến cho hai
> mục này phải nhắm vào việc giảm ảnh hưởng của khoảng chờ, không phải xóa khoảng chờ.
