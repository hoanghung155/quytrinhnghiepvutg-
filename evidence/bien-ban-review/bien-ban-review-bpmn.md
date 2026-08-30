# Biên bản review chéo mô hình BPMN

**Mục đích:** làm bằng chứng cho mục 2.5 Chương 2 — quy trình review chéo trong nhóm.
**Mốc khóa mô hình:** 30/08/2026.

> **TRẠNG THÁI: CHƯA HOÀN TẤT.** File này hiện chỉ có phần **tự kiểm của người vẽ**.
> Phần nhận xét của người duyệt để trống vì buổi review chéo chưa diễn ra — mô hình vừa
> được đẩy lên PR #2, người duyệt chưa comment. **Không điền hộ phần của người khác.**

---

## 1. Phạm vi review

| Mô hình | Người vẽ | Người duyệt | PR | Trạng thái |
|---|---|---|---|---|
| M2 — Quản lý nhà cung cấp | Danh | Hồng Phúc | #2 | ⏳ Chờ review |
| C3 — Bán trả góp | Danh | Hồng Phúc | #2 | ⏳ Chờ review |
| C4 — Bảo hành đổi trả | Danh | Hồng Phúc | #2 | ⏳ Chờ review |
| M3 — Kho và điều chuyển | Hồng Phúc | Danh | #4 | ⏳ Chờ review |
| S1 — Tuyển dụng và đào tạo | Hồng Phúc | Danh | #4 | ⏳ Chờ review |
| S4 — Đối soát công nợ NCC | Thanh Phúc | Hồng Phúc | — | ⏳ Chưa có mô hình |

## 2. Tự kiểm của người vẽ — Danh, 20/08/2026

Kiểm bằng script tự động trên file `.bpmn`, không đếm tay.

| Tiêu chí | M2 | C3 | C4 | Đạt? |
|---|---:|---:|---:|---|
| Số gateway (yêu cầu **> 7**) | 9 | 10 | 11 | ✅ |
| Số lane | 5 | 5 | 6 | ✅ |
| Số task | 15 | 15 | 16 | ✅ |
| Số sequence flow | 35 | 35 | 41 | ✅ |
| Sequence flow trỏ tới node không tồn tại | 0 | 0 | 0 | ✅ |
| Node mồ côi (không có luồng vào lẫn ra) | 0 | 0 | 0 | ✅ |
| Có đủ BPMNDI (mở được bằng bpmn.io) | ✅ | ✅ | ✅ | ✅ |
| XML parse hợp lệ | ✅ | ✅ | ✅ | ✅ |

Lệnh kiểm lại:

```bash
python -c "from lxml import etree; ..."   # xem lich su commit model: BPMN *
```

### Điểm người vẽ tự thấy còn yếu

1. **M2 dựng khi chưa có hồ sơ M2.** Hồ sơ M2 thuộc phần Hồng Phúc (hạn 22/08), tại thời
   điểm vẽ chưa có. Mô hình dựng từ bảng phân rã 12 quy trình và logic mua hàng phổ biến.
   **Đây là rủi ro lớn nhất trong ba mô hình** — cần đối chiếu lại toàn bộ trước 30/08.
2. **Ba mô hình đều rất rộng** (khoảng 20–24 cột). Ảnh xuất tỷ lệ gần 4:1, đưa vào Word
   phải để trang ngang hoặc đẩy xuống phụ lục.
3. **Chưa có mô hình nào được đối chiếu với thực tế.** Toàn bộ dựng từ hồ sơ quy trình,
   mà hồ sơ lại dựng từ quan sát bên ngoài. Buổi khảo sát 23/08 có thể làm đổi luồng.
4. **Gateway G2 của C3** (chọn bên cấp tín dụng) vẽ thành gateway hai nhánh cho gọn, thực
   tế có thể nhiều bên hơn — cần xác minh ở buổi khảo sát.

## 2b. Tự kiểm của người vẽ — Hồng Phúc

Kiểm bằng script [`model/bpmn/dem_gateway.py`](../../model/bpmn/dem_gateway.py), chạy trên
chính file `.bpmn` chứ không đếm từ script sinh — để con số báo cáo là con số thật nằm
trong file mà bpmn.io sẽ mở.

| Tiêu chí | M3 | S1 | Đạt? |
|---|---:|---:|---|
| Số gateway (yêu cầu **> 7**) | 12 | 10 | ✅ |
| Số lane | 5 | 5 | ✅ |
| Số task | 26 | 14 | ✅ |
| Số sự kiện bắt đầu / kết thúc | 1 / 8 | 1 / 7 | ✅ |
| Số sequence flow | 52 | 35 | ✅ |
| Sequence flow trỏ tới node không tồn tại | 0 | 0 | ✅ |
| Node không thuộc lane nào | 0 | 0 | ✅ |
| Có đủ BPMNDI (mở được bằng bpmn.io) | ✅ | ✅ | ✅ |
| XML parse hợp lệ | ✅ | ✅ | ✅ |

Lệnh kiểm lại:

```bash
python model/bpmn/dem_gateway.py
```

Script kiểm cả năm file `.bpmn` hiện có và thoát với mã 1 nếu có file nào chưa đủ hơn 7
gateway hoặc thiếu BPMNDI. Kết quả lần chạy gần nhất: **5/5 file đạt**.

### Điểm người vẽ tự thấy còn yếu

1. **S1 dựng khi chưa có hồ sơ S1.** Hồ sơ S1 thuộc phần Thanh Phúc (nhánh
   `docs/quy-trinh-ho-tro`), tại thời điểm vẽ chưa có. Mô hình dựng từ bảng phân rã 12 quy
   trình, từ lý do chọn S1 để mô hình hóa ("nhiều vòng sàng lọc và điểm quyết định
   đạt/không đạt"), và từ liên kết M4 → S1. **Đây là rủi ro lớn nhất trong hai mô hình** —
   đúng kiểu rủi ro mà Danh đã gặp với M2. Người vẽ **không tự viết hồ sơ S1 thay Thanh
   Phúc**; phải đối chiếu lại khi hồ sơ có, trước 30/08.
2. **M3 ban đầu rộng 7516px**, gấp rưỡi ba mô hình của Danh. Đã nén còn 6316px bằng cách
   cho nhánh điều chuyển dùng lại các cột mà nhánh nhập hàng để trống ở lane khác. Vẫn là
   mô hình rộng nhất trong năm mô hình — xem điểm 3.
3. **M3 có ba nhánh tách từ G1** (nhập hàng, điều chuyển, kiểm kê) nên tỷ lệ ảnh gần 4,6:1.
   Đưa vào Word nên **tách thành ba hình con theo ba nhánh**, hoặc để trang ngang cả trang.
   Đây là việc của khâu soát hình thức, không phải sửa mô hình.
4. **Chưa mô hình nào được đối chiếu với thực tế.** M3 dựng từ hồ sơ M3, mà hồ sơ M3 dựng
   từ quan sát bên ngoài. Ba chỉ số của M3 đang chờ khảo sát 23/08 và có thể làm đổi luồng
   nhánh điều chuyển (G7, G8).
5. **G9 và G10 của M3** (ngưỡng giá trị phải trình duyệt điều chuyển) là suy đoán — quy tắc
   R3 và R4 của hồ sơ M3 đều ở trạng thái `(ước lượng)`. Nếu khảo sát cho biết cửa hàng tự
   duyệt điều chuyển thì hai gateway này phải bỏ, còn **10 gateway — vẫn đạt mốc hơn 7**.

## 3. Nhận xét của người duyệt

### 3.1 Hồng Phúc — duyệt M2, C3, C4

**Ngày:** 20/08/2026 · **Cách kiểm:** chạy `dem_gateway.py` trên file `.bpmn` và đối chiếu
mô hình với bảng mục 5, mục 6 của hồ sơ tương ứng.

| Mô hình | Đếm lại gateway | Nhận xét | Kết luận |
|---|---:|---|---|
| M2 | 9 — khớp | Đối chiếu G1–G9 với hồ sơ M2 vừa lập: khớp cả chín. Hồ sơ M2 đã viết bám theo mô hình này, xem mục 6 của `ho-so-M2.md`. | ✅ Đạt |
| C3 | 10 — khớp | Đối chiếu với mục 6 hồ sơ C3 (G1–G9 và G4b): đủ, không thiếu nhánh. | ✅ Đạt |
| C4 | 11 — khớp | Đối chiếu với mục 6 hồ sơ C4 (G1–G8, G1b, G2b, G4b): đủ. | ✅ Đạt |

**Ba điểm nhận xét:**

1. **M2 — rủi ro người vẽ tự nêu đã được xử lý.** Danh ghi trong `gen_M2.py` là mô hình
   dựng trước hồ sơ và cần đối chiếu lại. Hồ sơ M2 nay đã có (PR #3) và mục 6 viết bám
   đúng chín gateway của mô hình, nên rủi ro này **đã đóng** — trừ khi khảo sát 23/08 cho
   kết quả khác. Không phải sửa mô hình M2.

2. **C3 gateway G2 — đồng ý với điểm tự kiểm số 4 của người vẽ.** Việc vẽ "chọn bên cấp
   tín dụng" thành gateway hai nhánh là chấp nhận được cho bản hiện tại. Nhưng nếu khảo
   sát cho biết cửa hàng làm việc với nhiều hơn hai bên, nên đổi tên nhánh thay vì thêm
   nhánh — thêm nhánh làm hình rộng thêm mà không tăng giá trị phân tích.

3. **C4 — vòng phản hồi C4 → M2 chưa thấy trên mô hình.** Hồ sơ C4 có bước 16 "cập nhật
   thống kê lỗi theo model → M2", và đây là phát hiện IR-13. Trên BPMN C4 thì bước này kết
   thúc trong pool C4, không có message flow sang M2. **Không đề nghị sửa mô hình** — vẽ
   message flow giữa hai pool của hai mô hình khác nhau sẽ làm hình rối. Nhưng Chương 2
   khi mô tả C4 nên nói rõ vòng phản hồi này tồn tại ngoài phạm vi hình.

> **Ghi nhận về quy trình:** PR #2 đã được merge lúc 07:02 ngày 20/08 **trước khi** có
> comment review chéo này. P0-chung mục 4 yêu cầu không merge im lặng vì comment PR chính
> là bằng chứng cho mục 2.5 Chương 2. Nhận xét ở trên được ghi bổ sung vào biên bản sau khi
> merge — vẫn dùng làm bằng chứng được, nhưng ba PR còn lại (#3, #4, và PR nhánh phân tích)
> nên có comment trước khi merge để không lặp lại.

### 3.2 Danh — duyệt M3, S1 của Hồng Phúc

> *(chưa có — mô hình đã đẩy lên PR #4 ngày 20/08, chờ Danh comment. **Không điền hộ.**)*

| Mô hình | Đếm lại gateway | Nhận xét | Kết luận |
|---|---:|---|---|
| M3 | | | ⏳ |
| S1 | | | ⏳ |

Hai chỗ người vẽ mong người duyệt soi kỹ:

- **M3 gateway G9 và G10** — ngưỡng giá trị phải trình duyệt điều chuyển là suy đoán. Nếu
  Danh thấy vô lý thì bỏ, mô hình còn 10 gateway, vẫn đạt mốc.
- **S1 toàn bộ** — dựng khi chưa có hồ sơ S1 của Thanh Phúc. Cần soi ở mức "luồng này có
  hợp lý không", chưa soi được ở mức "có khớp hồ sơ không".

### 3.3 Hồng Phúc — duyệt S4 của Thanh Phúc

> *(chưa có — chờ Thanh Phúc đẩy mô hình. Tính tới 20/08, thư mục
> `docs/ho-so-quy-trinh/ho-tro/S4-doi-soat-cong-no-ncc/` mới chỉ có `.gitkeep`.)*

## 4. Kết luận khóa mô hình

> *(điền ngày 30/08 sau khi cả sáu mô hình đã được review chéo)*

| Mô hình | Ngày khóa | Phiên bản khóa | Người xác nhận |
|---|---|---|---|
| M2 | | | |
| C3 | | | |
| C4 | | | |
| M3 | | | |
| S1 | | | |
| S4 | | | |

---

## Cách dùng file này

Comment trong pull request là nguồn gốc của biên bản. Sau mỗi lượt review:

1. Người duyệt comment trực tiếp trên PR — đếm lại gateway, chỉ ra chỗ sai luồng.
2. Người vẽ sửa và trả lời trong PR.
3. Chép lại phần kết luận vào mục 3 của file này, ghi ngày.

Không merge PR trước khi mục 3 tương ứng đã có nội dung — merge im lặng là mất bằng chứng
cho mục 2.5 Chương 2.
