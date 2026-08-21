# Soát bốn danh mục và caption báo cáo

**Người lập:** Nguyễn Thị Hồng Phúc · **Hạn:** 04/09 · **Phiên bản:** v1
**Công cụ:** [`soat_caption.py`](soat_caption.py) — chạy trực tiếp trên file Word

> **TRẠNG THÁI: MỚI LÀM ĐƯỢC MỘT PHẦN.** Trong bốn danh mục được giao, chỉ **Danh mục từ
> viết tắt** hoàn tất được ngay. Ba danh mục còn lại phụ thuộc nội dung các chương mà
> nhiều phần chưa có — xem mục 3. Phần caption đã soát xong và **đạt**.

---

## 1. Kết quả soát caption

Chạy `python report/soat_caption.py`. Script duyệt thân tài liệu theo **đúng thứ tự xuất
hiện** của đoạn văn và bảng, nên phát hiện được caption đặt sai phía — cách đọc riêng danh
sách đoạn rồi riêng danh sách bảng thì không phát hiện được.

| Kiểm tra | Kết quả |
|---|---|
| Mỗi hình có label `Hình x.y` ngay **dưới** hình | ✅ 4/4 |
| Mỗi bảng có label `Bảng x.y` ngay **trên** bảng | ✅ 5/5 |
| Đánh số liên tục theo chương, không nhảy số, không trùng | ✅ |
| Hình không có caption | ✅ không có |
| Bảng không có caption | ✅ không có |

**Kết luận:** quy ước caption của P0-B — label hình nằm dưới hình, label bảng nằm trên
bảng, đánh số theo chương — đang được tuân thủ đúng trong phần báo cáo đã viết. Không cần
sửa gì ở thời điểm này.

Script thoát với mã 1 nếu phát hiện lỗi, nên có thể chạy lại như một bước kiểm trước khi
nộp mà không cần đọc kết quả bằng mắt.

## 2. Hiện trạng bốn danh mục

| Danh mục | Trạng thái | Chặn bởi |
|---|---|---|
| Mục lục | ⏳ Khung sẵn, chưa sinh được | 23 mục `[CHUA CO]` — xem mục 3 |
| Danh mục hình vẽ | ⏳ Có 4 hình, thiếu ít nhất 5 | Hình BPMN M3, S1, S4 và hai hình xương cá chưa được chèn vào Word |
| Danh mục bảng biểu | ⏳ Có 5 bảng, thiếu nhiều | Bảng VA/BVA/NVA, bảng phân nhóm lãng phí, bảng giả định, bảng bấm giờ |
| Danh mục từ viết tắt | ✅ **Xong** | — |

### 2.1 Danh mục hình vẽ — hiện có 4

| Số | Tên hình | Nguồn |
|---|---|---|
| Hình 1.1 | Kiến trúc quy trình nghiệp vụ chuỗi TGDĐ và TopZone | Danh |
| Hình 3.1 | Mô hình BPMN quy trình M2 — Quản lý nhà cung cấp (9 gateway) | Danh |
| Hình 3.2 | Mô hình BPMN quy trình C3 — Bán trả góp (10 gateway) | Danh |
| Hình 3.3 | Mô hình BPMN quy trình C4 — Bảo hành, đổi trả (11 gateway) | Danh |

**Hình đã có file trong repo nhưng chưa chèn vào Word:**

| Dự kiến | Tên hình | File | Ai chèn |
|---|---|---|---|
| Hình 3.4 | Mô hình BPMN M3 — Kho và điều chuyển (12 gateway) | `model/hinh-xuat/M3-kho-va-dieu-chuyen.png` | Hồng Phúc — đã có, chờ Chương 3.2 vào Word |
| Hình 3.5 | Mô hình BPMN S1 — Tuyển dụng và đào tạo (10 gateway) | `model/hinh-xuat/S1-tuyen-dung-dao-tao.png` | Hồng Phúc — đã có |
| Hình 4.x | Biểu đồ xương cá — C4 bảo hành, đổi trả | `analysis/dinh-tinh/fishbone-C4.png` | Hồng Phúc — đã có |
| Hình 4.y | Biểu đồ xương cá — điều chuyển gấp giữa các cửa hàng | `analysis/dinh-tinh/fishbone-dieu-chuyen-gap.png` | Hồng Phúc — đã có |
| Hình 3.z | Mô hình BPMN S4 — Đối soát công nợ NCC | *(chưa có file)* | **Thanh Phúc** |

Chưa đánh số cứng cho các hình mục 4 vì số thứ tự phụ thuộc việc mục 4.2 của Hưng có hình
hay không. Đánh số cuối cùng làm sau khi Chương 4 đủ nội dung.

**Lưu ý về hình BPMN M3.** Ảnh rộng 6316 × 1360, tỷ lệ khoảng 4,6:1 — rộng nhất trong năm
mô hình. Đề xuất khi dàn trang: tách thành ba hình con theo ba nhánh của gateway G1 (nhập
hàng, điều chuyển, kiểm kê), hoặc để trang ngang cả trang. Nếu thu vừa khổ dọc thì chữ
trong hình không đọc được.

### 2.2 Danh mục bảng biểu — hiện có 5

| Số | Tên bảng | Nguồn |
|---|---|---|
| Bảng 0.1 | Danh sách thành viên nhóm | Danh |
| Bảng 1.1 | Danh mục 12 quy trình theo ba lớp | Danh |
| Bảng 2.1 | Kết quả tự kiểm ba mô hình do nhóm trưởng vẽ | Danh |
| Bảng 3.1 | Tổng hợp ba quy trình cốt lõi do nhóm trưởng phụ trách | Danh |
| Bảng 4.1 | Issue Register — 13 phát hiện từ C1, C3 và C4 | Danh |

**Bảng 4.1 cần cập nhật.** Issue Register nay đã lên **v2 với 31 phát hiện** (bổ sung
IR-14 đến IR-31 từ hồ sơ M1–M4). Caption hiện ghi "13 phát hiện từ C1, C3 và C4" nên phải
sửa lại cả nội dung bảng lẫn caption. Việc này thuộc khâu ghép nội dung vào Word, không
làm được ở bước soát hình thức.

**Bảng đã có nội dung trong repo nhưng chưa chèn vào Word:**

| Dự kiến | Tên bảng | Nguồn | Ai chèn |
|---|---|---|---|
| Bảng 3.x | Tổng hợp bốn quy trình quản lý M1–M4 | `docs/ho-so-quy-trinh/quan-ly/doi-chieu-4-ho-so-quan-ly.md` | Hồng Phúc |
| Bảng 4.x | VA/BVA/NVA cho C3 — 17 dòng | `analysis/dinh-tinh/va-bva-nva-C3.md` | Hồng Phúc |
| Bảng 4.x | VA/BVA/NVA cho C4 — 21 dòng | `analysis/dinh-tinh/va-bva-nva-C4.md` | Hồng Phúc |
| Bảng 4.x | Phân nhóm lãng phí Move / Hold / Overdo | `analysis/dinh-tinh/nhom-lang-phi-move-hold-overdo.md` | Hồng Phúc |
| Bảng 3.y | Tổng hợp bốn quy trình hỗ trợ S1–S4 | *(chưa có)* | **Thanh Phúc** |
| Bảng 4.y | Bảng giả định | *(chưa có)* | **Hưng** |
| Bảng 4.z | Bảng bấm giờ và cycle time | *(chưa có)* | **Hưng** |

### 2.3 Danh mục từ viết tắt — xong

Xem [danh-muc-tu-viet-tat.md](danh-muc-tu-viet-tat.md). Gồm 22 từ viết tắt chia bốn nhóm,
cộng hai mục bổ trợ: hệ thống mã ký hiệu trong hồ sơ quy trình (`Gn`, `En`, `Rn`, `Bn`,
`IR-xx`, `Qn`) và ba nhãn trạng thái dữ liệu.

Danh mục lập bằng cách **quét toàn bộ** file `.md` trong repo và nội dung file Word, không
liệt kê theo trí nhớ.

## 3. Vì sao ba danh mục còn lại chưa sinh được

Script đếm được **23 mục `[CHUA CO]`** trong file Word. Mục lục, danh mục hình và danh mục
bảng chỉ sinh đúng khi nội dung đã chốt — sinh sớm thì phải sinh lại, và nguy hiểm hơn là
dễ sót khi sinh lại lần cuối.

| Người phụ trách | Số mục chưa có | Nội dung |
|---|---:|---|
| **Hồng Phúc** | 9 | 4 danh mục (mục này), lý thuyết 2.1, bảng ký hiệu 2.2, khung lãng phí 2.3, nhận xét review 2.5, hồ sơ M1–M4 mục 3.2, VA/BVA/NVA 4.3, phân nhóm 4.4, fishbone 4.5 |
| **Danh** | 4 | Số liệu quy mô 1.1, đề xuất cải tiến 4.7, kết luận, Phụ lục A |
| **Hưng** | 4 | Phương pháp 2.4, bảng giả định 4.1, định lượng 4.2, Phụ lục C |
| **Thanh Phúc** | 3 | Hồ sơ S1–S4 mục 3.3, tài liệu tham khảo, Phụ lục B |

**Phần của Hồng Phúc:** nội dung cho các mục 3.2, 4.3, 4.4, 4.5 và 2.5 **đã có đầy đủ
trong repo** (nhánh `docs/quy-trinh-quan-ly`, `analysis/dinh-tinh`,
`model/bpmn-quan-ly-ho-tro`) nhưng **chưa được ghép vào file Word**. Việc ghép nội dung vào
Word thuộc khâu dựng báo cáo, không thuộc khâu soát hình thức — cần thống nhất với Danh ai
làm bước ghép này. Ba mục lý thuyết 2.1, 2.2, 2.3 thì chưa viết.

## 4. Việc phải làm lại sau khi các chương hoàn tất

Bốn bước dưới đây **bắt buộc chạy lại lần cuối** trước khi nộp, không được dùng kết quả
của lần soát này:

- [ ] Chạy lại `python report/soat_caption.py`, phải thoát mã 0
- [ ] Sinh lại mục lục trong Word sau khi mọi heading đã chốt
- [ ] Sinh lại danh mục hình và danh mục bảng, đối chiếu với hai bảng ở mục 2.1 và 2.2
- [ ] Quét lại từ viết tắt trên bản Word đầy đủ, bổ sung vào danh mục nếu chương 2 và 4
      phát sinh từ mới

Một việc nữa không thuộc hình thức nhưng phát hiện trong lúc soát:

- [ ] **Cập nhật Bảng 4.1** từ 13 lên 31 phát hiện, sửa cả caption — xem mục 2.2

## 5. Ghi chú về heading trong file Word

File Word hiện dùng **toàn bộ style `Normal`** cho 106 đoạn, kể cả các dòng tiêu đề chương
và tiêu đề mục. Word chỉ sinh được mục lục tự động khi tiêu đề dùng style `Heading 1`,
`Heading 2`…

Đây là việc phải xử lý **trước** khi sinh mục lục, và nó nằm ở khâu dựng file Word
(`report/gen_bao_cao.py` — của Danh), không phải khâu soát. Đã ghi vào đây để không quên;
cần trao đổi với Danh trong PR.
