# Sổ duyệt pull request — Hồng Phúc

**Người lập:** Nguyễn Thị Hồng Phúc · **Phiên bản:** v1 · **Cập nhật:** 20/08/2026

Theo bảng phân công ở P0-chung mục 4 (giữ ngoài repo), Hồng Phúc là
người duyệt của **5 nhánh** — nhiều nhất nhóm. File này ghi lại từng lượt duyệt để dùng
làm bằng chứng cho mục 2.5 Chương 2, cùng với comment trực tiếp trên pull request.

> **TRẠNG THÁI: MỚI DUYỆT ĐƯỢC 1 TRONG 5.** Bốn nhánh còn lại chưa được đẩy lên hoặc chưa
> mở PR. **Không điền hộ phần của người khác** — các dòng để trống là thật, không phải
> quên.

---

## 1. Năm nhánh Hồng Phúc phụ trách duyệt

| # | Nhánh | Người làm | Hạn merge | PR | Trạng thái duyệt |
|---|---|---|---|---|---|
| 1 | `docs/quy-trinh-cot-loi` | Danh | 22/08 | #2 | ✅ Đã duyệt — xem mục 2 |
| 2 | `model/bpmn-cot-loi` | Danh | 30/08 | — | ⏳ Chưa có nhánh trên remote |
| 3 | `report/word-slide` | Danh | 05/09 | — | ⏳ Chưa có nhánh trên remote |
| 4 | `docs/quy-trinh-ho-tro` | Thanh Phúc | 22/08 | — | ⏳ Chưa có nhánh trên remote |
| 5 | `docs/cong-cu-khao-sat` | Thanh Phúc | 30/08 | — | ⏳ Chưa có nhánh trên remote |

Nhánh có trên remote tính tới 20/08: `bai-tap-qua-trinh`, `setup/khung-repo`,
`docs/quy-trinh-cot-loi`, `docs/quy-trinh-quan-ly`, `model/bpmn-quan-ly-ho-tro`,
`revert-4-model/bpmn-quan-ly-ho-tro`.

**Ghi chú về nhánh 2 và 3.** Mô hình BPMN M2, C3, C4 của Danh không nằm ở nhánh
`model/bpmn-cot-loi` như bảng phân công dự kiến, mà đã đi chung trong PR #2 của nhánh
`docs/quy-trinh-cot-loi`. Vì vậy phần duyệt mô hình đã làm luôn ở mục 2 dưới đây. Nếu sau
này nhánh `model/bpmn-cot-loi` vẫn được mở thì cần thống nhất lại với Danh để tránh duyệt
trùng.

## 2. PR #2 — `docs/quy-trinh-cot-loi` của Danh

**Ngày duyệt:** 20/08/2026 · **Kết luận: đạt, không yêu cầu sửa.**

Nội dung nhận xét đầy đủ nằm ở
[biên bản review chéo BPMN](../evidence/bien-ban-review/bien-ban-review-bpmn.md) mục 3.1.
Tóm tắt:

| Hạng mục | Cách kiểm | Kết quả |
|---|---|---|
| Gateway M2, C3, C4 | Chạy `dem_gateway.py` trên file `.bpmn` | 9 / 10 / 11 — khớp con số Danh tự kiểm |
| BPMNDI | Script kiểm mọi node có `BPMNShape`, mọi flow có `BPMNEdge` | Đủ cả ba |
| Hồ sơ C1, C3, C4 đủ 12 mục | Chạy `kiem-tra-cau-truc-ho-so.py` | Khớp template |
| Mô hình khớp hồ sơ | Đối chiếu mục 6 của từng hồ sơ với gateway trong `.bpmn` | Khớp |

Ba nhận xét nội dung đã ghi trong biên bản: rủi ro M2 dựng trước hồ sơ (nay đã đóng),
gateway G2 của C3 nên đổi tên nhánh thay vì thêm nhánh nếu khảo sát cho kết quả khác, và
vòng phản hồi C4 → M2 không thể hiện được trên hình nên phải nói bằng lời ở Chương 2.

**Vấn đề về quy trình:** PR #2 được merge lúc 07:02 ngày 20/08, **trước khi** có nhận xét
duyệt. P0-chung mục 4 yêu cầu không merge im lặng vì comment PR chính là bằng chứng cho
mục 2.5. Nhận xét đã được ghi bổ sung sau merge — vẫn dùng làm bằng chứng được, nhưng
không nên lặp lại ở các PR sau.

## 3. Bốn nhánh còn lại — chưa duyệt được

### 3.1 `model/bpmn-cot-loi` — Danh

> *(chưa có — nhánh chưa xuất hiện trên remote. Xem ghi chú ở mục 1: nội dung có thể đã
> đi chung trong PR #2.)*

### 3.2 `report/word-slide` — Danh

> *(chưa có — hạn 05/09. File `report/bao-cao-...docx` và `slide/slide-trinh-bay.pptx`
> hiện đã nằm trên nhánh chính qua PR #2, chưa tách nhánh riêng.)*

Khi duyệt nhánh này cần soi hai điểm đã phát hiện trong lúc soát hình thức:

- File Word dùng toàn bộ style `Normal` cho 106 đoạn, kể cả tiêu đề chương và mục. Word
  không sinh được mục lục tự động khi tiêu đề không dùng style `Heading`.
- Bảng 4.1 đang là Issue Register 13 phát hiện; nay đã lên v2 với 31 phát hiện, phải cập
  nhật cả nội dung bảng lẫn caption.

Chi tiết ở [soat-danh-muc-va-caption.md](../report/soat-danh-muc-va-caption.md).

### 3.3 `docs/quy-trinh-ho-tro` — Thanh Phúc

> *(chưa có — hạn 22/08. Bốn thư mục `S1` đến `S4` trong `docs/ho-so-quy-trinh/ho-tro/`
> hiện mới chỉ có `.gitkeep`.)*

**Việc này đang chặn phần của Hồng Phúc.** Mô hình BPMN S1 đã dựng nhưng **chưa đối chiếu
được với hồ sơ S1** vì hồ sơ chưa tồn tại — mô hình hiện dựng từ bảng phân rã 12 quy trình
và liên kết M4 → S1. Cần hồ sơ S1 trước mốc khóa mô hình **30/08**.

Khi duyệt, dùng `kiem-tra-cau-truc-ho-so.py` để kiểm 12 mục — script đã hỗ trợ sẵn mã S1–S4
và tự cảnh báo nếu S1, S4 không đủ hơn 7 điểm ra quyết định.

### 3.4 `docs/cong-cu-khao-sat` — Thanh Phúc

> *(chưa có — hạn 30/08. Bộ 24 câu phỏng vấn, Phụ lục B.)*

Khi duyệt cần kiểm bộ câu hỏi có bao gồm **bốn câu Q1–Q4 của nhóm quy trình quản lý** đã đề
xuất ở [phạm vi nhóm quản lý](ho-so-quy-trinh/quan-ly/pham-vi-nhom-quan-ly.md) mục 6 hay
không. Bốn câu này quyết định ba chỉ số khả thi nhất của hồ sơ M3.

## 4. Ghi nhận chỉnh sửa sau duyệt

> *(chưa có — chưa có lượt duyệt nào dẫn tới yêu cầu sửa. PR #2 kết luận đạt.)*

| PR | Nội dung yêu cầu sửa | Người sửa | Ngày sửa xong | Xác nhận |
|---|---|---|---|---|
| | | | | |

## 5. Ba PR của Hồng Phúc — chờ Danh duyệt

Phần này ghi để theo dõi, **người duyệt là Danh (24730090)**, không phải Hồng Phúc tự duyệt.

| PR | Nhánh | Nội dung | Trạng thái |
|---|---|---|---|
| #3 | `docs/quy-trinh-quan-ly` | Hồ sơ M1–M4 | ⏳ Mở, chờ Danh duyệt |
| #4 | `model/bpmn-quan-ly-ho-tro` | BPMN M3 (12 gateway), S1 (10 gateway) | ⚠️ Đã merge lúc 10:21 ngày 20/08 **mà chưa có review nào của Danh** — xem ghi chú |
| — | `analysis/dinh-tinh` | VA/BVA/NVA, Move/Hold/Overdo, fishbone | Chờ mở PR |

> **Ghi chú về PR #4.** PR này bị merge khi số review = 0 và số comment = 0, tức là Danh
> chưa duyệt. Điều này lặp lại đúng vấn đề đã nêu ở mục 2 với PR #2, và lần này còn nặng
> hơn vì **người merge cũng chính là người mở PR** — trái với P0-chung mục 4 ("một người
> khác duyệt rồi merge") và mục 8.
>
> Trên remote hiện có nhánh `revert-4-model/bpmn-quan-ly-ho-tro` chứa một commit revert
> toàn bộ PR #4. Nhánh này **chưa được merge**, nên nhánh chính vẫn còn đủ hai mô hình M3,
> S1 và biên bản review. Người mở nhánh revert cần nói rõ ý định trước khi nhóm xử lý tiếp —
> **không tự ý xóa hay merge nhánh đó**.
>
> Đề nghị xử lý: Danh vẫn review nội dung PR #4 và ghi nhận xét vào mục 3.2 của biên bản
> review chéo. Việc PR đã merge không làm mất giá trị của lượt review, vì mốc khóa mô hình
> là **30/08** — còn thời gian sửa nếu review phát hiện vấn đề.
