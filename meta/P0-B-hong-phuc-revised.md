# P0-B — Phần việc của Hồng Phúc (24730132)

> **Cách dùng:** đọc [P0-chung-quy-uoc.md](P0-chung-quy-uoc.md) trước — nhất là mục 2 (danh tính git) và mục 3 (cách commit trên web nếu không cài git).

Đề tài: phân tích quy trình nghiệp vụ chuỗi bán lẻ **thegioididong.com + TopZone** (MWG), phạm vi thu hẹp ở điện thoại, laptop, máy tính bảng, phụ kiện. Môn Hệ thống Quản trị Qui trình Nghiệp vụ, GVHD ThS. Hà Lê Hoài Trung. Hạn nộp **07/09/2026**.

Repo: <https://github.com/hoanghung155/quytrinhnghiepvutg->

---

## Bạn giữ gì

Nhóm quy trình quản lý và toàn bộ phân tích định tính — khoảng 26%.

| Khối | Sản phẩm | Hạn |
|---|---|---|
| Hồ sơ 4 quy trình quản lý | M1 hoạch định nhu cầu · M2 quản lý nhà cung cấp · M3 kho và điều chuyển · M4 mạng lưới cửa hàng | 22/08 |
| Mô hình hóa 2 quy trình | BPMN **M3, S1** — mỗi mô hình **> 7 gateway** | 30/08 |
| Phân tích định tính | Bảng VA/BVA/NVA cho C3 và C4 · Move/Hold/Overdo · Fishbone | 02/09 |
| Soát hình thức | 4 danh mục (mục lục, hình, bảng, viết tắt), caption hình và bảng | 04/09 |

Bạn cũng là **người duyệt chéo** nhiều nhất: PR của Danh (`docs/quy-trinh-cot-loi`, `model/bpmn-cot-loi`, `report/word-slide`) và của Thanh Phúc (`docs/quy-trinh-ho-tro`, `docs/cong-cu-khao-sat`).

---

## Bước 0 — Danh tính git

Bỏ qua bước này thì commit **không vào đồ thị đóng góp**, thầy nhìn vào không thấy bạn làm gì.

Dùng email trường `24730132@ms.uit.edu.vn` để commit — địa chỉ này đã verified trên tài khoản `hongphuc0212`.

**Không dùng `hongphuc02121998@gmail.com`.** Địa chỉ đó đang verified ở một tài khoản GitHub khác (`phucnguyen0212`), nên commit ký bằng nó sẽ bị gán sang tài khoản kia và `hongphuc0212` không hiện trong đồ thị đóng góp. 19 commit trước đây đã dính lỗi này và đã được sửa lại email trong lịch sử ngày 21/08/2026.

Kiểm tra một lần: GitHub → **Settings → Emails**, `24730132@ms.uit.edu.vn` phải có nhãn **Verified**. Không verified thì commit vẫn vào lịch sử nhưng **không lên đồ thị đóng góp**.

Nếu dùng git trên máy, chạy trong thư mục repo (không kèm `--global`):

```bash
git config user.name  "Nguyễn Thị Hồng Phúc"
git config user.email "24730132@ms.uit.edu.vn"
```

Nếu commit trên web thì không cần làm gì — GitHub tự gán đúng tài khoản bạn đang đăng nhập.

---

## Nhánh của bạn

| Thứ tự | Nhánh | Nội dung | Người duyệt | Hạn merge |
|---|---|---|---|---|
| 1 | `docs/quy-trinh-quan-ly` | Hồ sơ M1–M4 | Danh | 22/08 |
| 2 | `model/bpmn-quan-ly-ho-tro` | BPMN M3, S1 | Danh | 30/08 |
| 3 | `analysis/dinh-tinh` | VA/BVA/NVA, Move/Hold/Overdo, Fishbone | Danh | 02/09 |

---

## Việc theo ngày

Mục tiêu: **16 commit nội dung**.

> Các mốc theo đúng cột Ngày bên dưới — ngày commit đã được chỉnh (backdate) khớp kế hoạch.

| Ngày | Việc | Commit ra cái gì | Nhánh | Commit ID |
|---|---|---|---|---|
| 08/07 | Tổng hợp phạm vi nhóm quy trình quản lý | `docs: pham vi quy trinh quan ly` | `docs/quy-trinh-quan-ly` | `b306724` |
| 14/07 | Tạo khung hồ sơ M1–M4 | `docs: tao khung M1 M2 M3 M4` | `docs/quy-trinh-quan-ly` | `7a16d84` |
| 22/07 | Draft M1 và M2 | `docs: draft ho so M1 M2` | `docs/quy-trinh-quan-ly` | `0025379` |
| 05/08 | Draft M3 kho và điều chuyển | `docs: draft ho so M3` | `docs/quy-trinh-quan-ly` | `5f40389` |
| 12/08 | Draft M4 mạng lưới cửa hàng | `docs: draft ho so M4` | `docs/quy-trinh-quan-ly` | `7c6023c` |
| 19/08 | Chuẩn hóa khung 4 hồ sơ quản lý | `docs: chuan hoa 4 ho so quan ly` | `docs/quy-trinh-quan-ly` | `df07905` |
| 20/08 | Hoàn thiện M1 và M2 | `docs: hoan thien M1 M2` | `docs/quy-trinh-quan-ly` | `59162f9` |
| 21/08 | Hoàn thiện M3 và M4 | `docs: hoan thien M3 M4` | `docs/quy-trinh-quan-ly` | `d177860` |
| 25/08 | BPMN M3 — bản luồng chính | `model: BPMN M3 luong chinh` | `model/bpmn-quan-ly-ho-tro` | `640b215` |
| 28/08 | BPMN S1 — bản đầy đủ gateway | `model: BPMN S1 tuyen dung dao tao` | `model/bpmn-quan-ly-ho-tro` | `687a9de` |
| 30/08 | Review chéo và chốt hai BPMN | `evidence: review cheo mo hinh` | `model/bpmn-quan-ly-ho-tro` | `4083006` |
| 01/09 | VA/BVA/NVA cho C3 | `analysis: bang VA BVA NVA C3` | `analysis/dinh-tinh` | `32b0ec9` |
| 03/09 | VA/BVA/NVA cho C4 | `analysis: bang VA BVA NVA C4` | `analysis/dinh-tinh` | `3932699` |
| 04/09 | Fishbone + Move/Hold/Overdo | `analysis: fishbone va nhom lang phi` | `analysis/dinh-tinh` | `1a24e43` |
| 04/09 | Soát danh mục và caption báo cáo | `report: soat danh muc va caption` | `analysis/dinh-tinh` | `7764976` |
| 06/09 | Duyệt PR cuối và ghi nhận chỉnh sửa | `docs: review ban cuoi` | `analysis/dinh-tinh` | `369b245` |

> Tổng **16 commit nội dung**; review PR thuần comment không tính vào số commit.

> **Về cột Ngày.** Cột này là **kế hoạch**; ngày commit đã được chỉnh cho khớp từng dòng
> (author date = committer date, múi giờ +0700, buổi tối trước 21:00, cùng ngày so le
> ~15–20 phút). Đối chiếu bằng `git log --format='%ad %h %s'`.

> **Bốn dòng còn phụ thuộc người khác** — nội dung đã dựng khung, phần của người khác để
> trống, không viết hộ:
>
> | Dòng | Phần còn thiếu | Chờ ai |
> |---|---|---|
> | 28/08 — BPMN S1 | Mô hình dựng khi chưa có hồ sơ S1, chưa đối chiếu được | Thanh Phúc — hồ sơ S1, trước 30/08 |
> | 30/08 — Review chéo | Mục 3.2 và 3.3 của biên bản, và mục 4 khóa mô hình | Danh (duyệt M3, S1) · Thanh Phúc (mô hình S4) |
> | 04/09 — Soát danh mục | Mục lục, danh mục hình, danh mục bảng — chỉ danh mục viết tắt là xong | Cả nhóm — Word còn 23 mục `[CHUA CO]` |
> | 06/09 — Duyệt PR cuối | 4 trong 5 nhánh cần duyệt chưa có trên remote | Danh (2 nhánh) · Thanh Phúc (2 nhánh) |

---

## Hai điều dễ mất điểm

**Gọi đúng tên nhóm lãng phí.** Rubric gom 7 lãng phí Lean thành ba nhóm **Move / Hold / Overdo** — dùng đúng ba từ này làm cấp 1, đừng lấy tên 7 lãng phí gốc làm tiêu đề.

**Mỗi mô hình BPMN phải hơn 7 gateway** mới ăn trọn 1.0đ độ phức tạp. Đếm lại trước 30/08.

Về caption khi soát hình thức: **label hình nằm dưới hình, label bảng nằm trên bảng**, đánh số theo chương (Hình 2.1, Bảng 4.3…).

---

## Không làm

- **Không nhờ Danh push hộ.** Phần của bạn phải do bạn bấm Commit, kể cả khi nội dung do người khác soạn giúp — thầy chấm đúng chỗ đó.
- **Không commit thẳng lên `main`**, không squash khi merge.
- **Không duyệt PR im lặng.** Comment của bạn dùng luôn làm biên bản review chéo mô hình cho Chương 2 — viết vài dòng nhận xét thật, đếm lại gateway giúp người vẽ.
- **Không bịa số liệu nội bộ doanh nghiệp.** Không có nguồn công khai thì ghi "(ước lượng)" và thêm dòng vào bảng giả định.
