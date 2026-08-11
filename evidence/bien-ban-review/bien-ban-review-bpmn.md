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
| M3 — Kho và điều chuyển | Hồng Phúc | Danh | — | ⏳ Chưa có mô hình |
| S1 — Tuyển dụng và đào tạo | Hồng Phúc | Danh | — | ⏳ Chưa có mô hình |
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

## 3. Nhận xét của người duyệt

### 3.1 Hồng Phúc — duyệt M2, C3, C4

> *(chưa có — điền sau khi Hồng Phúc comment trên PR #2)*

| Mô hình | Đếm lại gateway | Nhận xét | Kết luận |
|---|---:|---|---|
| M2 | | | ⏳ |
| C3 | | | ⏳ |
| C4 | | | ⏳ |

### 3.2 Danh — duyệt M3, S1 của Hồng Phúc

> *(chưa có — chờ Hồng Phúc đẩy mô hình)*

### 3.3 Hồng Phúc — duyệt S4 của Thanh Phúc

> *(chưa có — chờ Thanh Phúc đẩy mô hình)*

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
