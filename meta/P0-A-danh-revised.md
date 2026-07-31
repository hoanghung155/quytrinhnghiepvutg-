# P0-A — Phần việc của Danh (24730090, nhóm trưởng)

> **Cách dùng:** đọc [P0-chung-quy-uoc.md](P0-chung-quy-uoc.md) trước. File này chạy trên máy của Danh, trong thư mục repo lớp đã clone: `Documents\me\quytrinhnghiepvutg-`.

Đề tài: phân tích quy trình nghiệp vụ chuỗi bán lẻ **thegioididong.com + TopZone** (MWG), phạm vi thu hẹp ở điện thoại, laptop, máy tính bảng, phụ kiện. Môn Hệ thống Quản trị Qui trình Nghiệp vụ, GVHD ThS. Hà Lê Hoài Trung. Hạn nộp **07/09/2026**.

---

## Bạn giữ gì

Phần xương sống và phần ghép cuối — nặng nhất nhóm, khoảng 32%.

| Khối | Sản phẩm | Hạn |
|---|---|---|
| Khung repo | Cây thư mục, README, .gitignore, `meta/*` | 19/08 |
| Kiến trúc quy trình | Sơ đồ Hình 1.1, đủ 12 quy trình, 3 lớp | 22/08 |
| Hồ sơ 3 quy trình cốt lõi | C1 bán tại cửa hàng · C3 bán trả góp · C4 bảo hành đổi trả | 22/08 |
| Mô hình hóa 3 quy trình | BPMN **M2, C3, C4** — mỗi mô hình **> 7 gateway** | 30/08 |
| Issue Register | Bảng tổng hợp phát hiện cuối Chương 4 | 02/09 |
| Báo cáo Word | Ghép toàn bộ, dàn trang chuẩn UIT | 03/09 |
| Slide | 24 trang + kịch bản nói | 05/09 |

---

## Bước 0 — Danh tính git

Máy này có hai tài khoản GitHub của cùng một người. Repo lớp dùng **`24730090`** vì đó là tài khoản đã là collaborator và trùng MSSV thầy đối chiếu.

```bash
git config user.name  "Nguyễn Ngọc Danh"
git config user.email "24730090@ms.uit.edu.vn"
```

Đặt ở cấp repo, **không** `--global` — repo `doan` cá nhân giữ nguyên `ngocdanhx`.

Xác nhận trước khi đi tiếp:

```bash
git config user.email    # phải ra đúng chuỗi trên
```

---

## Nhánh của bạn

| Thứ tự | Nhánh | Nội dung | Người duyệt | Hạn merge |
|---|---|---|---|---|
| 1 | `setup/khung-repo` | Cấu trúc thư mục, README, .gitignore, meta | Hưng | 19/08 |
| 2 | `docs/quy-trinh-cot-loi` | Hồ sơ C1, C3, C4 + sơ đồ kiến trúc | Hồng Phúc | 22/08 |
| 3 | `model/bpmn-cot-loi` | BPMN M2, C3, C4 | Hồng Phúc | 30/08 |
| 4 | `report/word-slide` | Báo cáo Word, slide, Issue Register | Hồng Phúc | 05/09 |

Bạn **duyệt chéo** cho: nhánh của Hồng Phúc (`docs/quy-trinh-quan-ly`, `model/bpmn-quan-ly-ho-tro`, `analysis/dinh-tinh`) và của Hưng (`survey/khao-sat-cua-hang`, `analysis/dinh-luong`). Duyệt là đọc thật và comment thật — comment đó dùng làm biên bản review chéo cho Chương 2.

---

## Việc theo ngày

Mục tiêu: **22 commit nội dung**. Phần của Danh nặng nhất nên nhịp commit cao hơn ba thành viên còn lại.

> Các mốc trước 19/08 chỉ dùng nếu đúng với tiến độ thực tế đã làm. Nếu một đầu việc được làm muộn hơn, commit ở ngày thực tế.

| Ngày | Việc | Commit ra cái gì |
|---|---|---|
| 06/07 | Khởi tạo skeleton đề tài và phạm vi phân tích | `chore: init project structure` |
| 10/07 | Chốt phạm vi TGDĐ + TopZone và nhóm sản phẩm | `docs: chot pham vi de tai` |
| 15/07 | Dựng đề cương Chương 1–4 | `docs: tao de cuong bao cao` |
| 21/07 | Phân rã sơ bộ 12 quy trình theo 3 lớp | `docs: phan ra 12 quy trinh` |
| 27/07 | Tạo khung hồ sơ quy trình cốt lõi C1 C3 C4 | `docs: tao khung ho so quy trinh cot loi` |
| 05/08 | Bổ sung actor, input/output cho C1 và C3 | `docs: bo sung ho so C1 C3` |
| 10/08 | Bổ sung actor, input/output cho C4 | `docs: bo sung ho so C4` |
| 14/08 | Chuẩn hóa template và quy ước đặt tên file | `chore: chuan hoa template va ten file` |
| 19/08 | Dựng khung repo, README, .gitignore, meta | `chore: hoan thien khung repo` |
| 20/08 | Hoàn thiện hồ sơ C1 bán tại cửa hàng | `docs: hoan thien ho so C1` |
| 20/08 | Hoàn thiện hồ sơ C3 bán trả góp | `docs: hoan thien ho so C3` |
| 21/08 | Hoàn thiện hồ sơ C4 bảo hành đổi trả | `docs: hoan thien ho so C4` |
| 22/08 | Sơ đồ kiến trúc Hình 1.1, đủ 12 quy trình | `docs: so do kien truc 12 quy trinh` |
| 25/08 | BPMN M2 quản lý nhà cung cấp | `model: BPMN M2 quan ly nha cung cap` |
| 27/08 | BPMN C3 bán trả góp | `model: BPMN C3 ban tra gop` |
| 29/08 | BPMN C4 bảo hành đổi trả | `model: BPMN C4 bao hanh doi tra` |
| 30/08 | Biên bản review chéo và khóa mô hình | `evidence: bien ban review BPMN` |
| 01/09 | Rà soát và ghép Chương 1–2 | `docs: ra soat chuong 1-2` |
| 02/09 | Hoàn thiện Issue Register | `analysis: hoan thien issue register` |
| 03/09 | Dựng báo cáo Word bản đầy đủ | `report: bao cao word ban day du` |
| 05/09 | Dựng slide và kịch bản trình bày | `slide: slide 24 trang va kich ban` |
| 06/09 | Soát checklist và chốt bản nộp | `report: chot ban cuoi` |
| 07/09 | Nộp | — |

> Bảng có 23 dòng công việc vì ngày 07/09 không tạo commit; tổng commit nội dung là **22**.

---

## Ràng buộc kỹ thuật không được quên

**Mỗi mô hình BPMN phải hơn 7 gateway** mới ăn trọn 1.0đ độ phức tạp. Đếm lại trước khi khóa mô hình 30/08.

**Chuẩn hình thức bắt buộc** (Phụ lục 2 khoa HTTT UIT): Times New Roman 13pt, giãn dòng 1.5, lề trên 3cm / dưới 3.5cm / trái 3.5cm / phải 2cm, số trang giữa bên dưới, tiêu đề chương bold 14pt, tiêu đề mục bold 13pt, đánh số bảng và hình theo chương, **label hình nằm dưới, label bảng nằm trên**, đủ 4 danh mục, tài liệu tham khảo chuẩn IEEE tách riêng tiếng Việt và tiếng Anh.

Rubric làm tròn từng hạng mục về 1 / 0.5 / 0 theo mốc 0.75 và 0.25 — nên đưa **mọi** hạng mục qua 0.75, đừng dồn công vào vài mục.

---

## Việc điều phối chỉ bạn làm

- [ ] Nhắc ba bạn nhận lời mời collaborator trong email
- [ ] Kiểm tra Settings → General → Default branch đang là `main`
- [ ] Repo để public, thầy xem được mà không cần mời
- [ ] Gửi ba file `P0-B`, `P0-C`, `P0-D` cho đúng người
- [ ] Chốt với thầy: hạn nộp 07/09 có đúng không, thời lượng trình bày tối đa bao nhiêu phút
- [ ] Cuối kỳ: sửa lại Bảng 0.2 cho khớp thực tế nếu có người trễ khối việc — bảng phân công phải đúng, không giữ nguyên cho đẹp

---

## Không làm

- **Không push hộ ba bạn còn lại.** Bạn soạn nội dung rồi gửi vào nhóm chat thì được, nhưng nút Commit phải do chính người phụ trách bấm — thầy chấm đúng chỗ đó.
- **Không commit thẳng lên `main`**, không squash khi merge.
- **Không bịa số liệu nội bộ doanh nghiệp.** Không có nguồn công khai thì ghi "(ước lượng)" và thêm dòng vào bảng giả định.
