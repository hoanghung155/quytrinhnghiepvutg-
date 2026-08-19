# P0 chung — quy ước làm việc trên repo lớp

> **Ai đọc:** cả bốn thành viên. Đọc một lần, mất 5 phút. Bốn file `P0-A` đến `P0-D` là phần việc riêng của từng người, đọc sau file này.

Repo: <https://github.com/hoanghung155/quytrinhnghiepvutg->

---

## 1. Vì sao phải commit đàng hoàng

Thầy chấm 5 tiêu chí, mỗi tiêu chí 10 điểm. Một trong số đó nhìn vào **lịch sử hoạt động GitHub**: repo im lặng ba tuần liên tiếp là bị trừ, và commit phải mang **tên tài khoản của chính người làm** thì mới chứng minh được nhóm có bốn người cùng làm.

Hai hệ quả:

- **Không ai push hộ ai.** Danh soạn nội dung rồi gửi vào nhóm chat là bình thường, nhưng nút Commit phải do chính người phụ trách bấm.
- **Mỗi người ít nhất 1 commit mỗi tuần**, và repo không im quá 3 ngày. Trên mức đó thì ai làm nhiều commit nhiều, không cần cân bằng cho đều.
- Với đồ án này, mục tiêu nội bộ là khoảng **66 commit nội dung** cho cả nhóm, chưa tính merge commit: Danh 22 · Hồng Phúc 16 · Thanh Phúc 14 · Hưng 14.
- Không chia nhỏ vô nghĩa để tăng số lượng. Một commit phải tương ứng với một phần việc có thể gọi tên được.

> **Lưu ý về mốc trước 19/08:** bảng dưới dùng để mô tả tiến độ từ 06/07. Chỉ gắn một commit vào ngày cũ nếu đúng là phần việc/phiên bản đó đã được làm ở thời điểm tương ứng. Nếu không, commit ở ngày thực tế và giữ nguyên nội dung công việc.

### Nhịp chung 06/07 → 07/09

| Giai đoạn | Nhịp dự kiến | Việc chính |
|---|---:|---|
| 06–19/07 | 1–2 commit/người/tuần | Chốt phạm vi, khung đề tài, phân rã quy trình, thu thập tài liệu nền |
| 20/07–02/08 | 2–3 commit/người/tuần | Dựng skeleton hồ sơ, glossary, nguồn tham khảo, khung khảo sát |
| 03–16/08 | 2–4 commit/người/tuần | Hoàn thiện draft đầu, chuẩn hóa cấu trúc, chuẩn bị nhánh chính |
| 17–23/08 | 3–5 commit/người/tuần | Hồ sơ quy trình, khung repo, chuẩn bị/triển khai khảo sát |
| 24–30/08 | 4–6 commit/người/tuần | BPMN, khảo sát thực địa, evidence, khóa mô hình |
| 31/08–06/09 | 3–6 commit/người/tuần | Phân tích, Issue Register, Word, slide, soát hình thức |
| 07/09 | 0–1 commit/người | Kiểm tra lần cuối và nộp |

### Mục tiêu số commit nội dung

| Thành viên | Mục tiêu |
|---|---:|
| Nguyễn Ngọc Danh | **22** |
| Nguyễn Thị Hồng Phúc | **16** |
| Nguyễn Thanh Phúc | **14** |
| Mai Hoàng Hưng | **14** |
| **Tổng** | **66** |

Không cần số commit từng tuần bằng nhau. Lịch sử tự nhiên sẽ có ngày 2 commit khi hoàn thành hai đơn vị việc, và cũng có 2–3 ngày không commit khi đang đọc tài liệu, họp, khảo sát hoặc vẽ mô hình.

---

## 2. Bước bắt buộc trước commit đầu tiên — danh tính git

Chỗ này hỏng là hỏng hết: commit vẫn nằm trong lịch sử nhưng **không vào đồ thị đóng góp**, tức là thầy nhìn vào không thấy bạn làm gì.

Email dùng để commit **phải là email đã xác thực trên GitHub** của chính tài khoản bạn.

Mỗi người dùng đúng email đã đăng ký tài khoản GitHub của mình (bảng dưới). Danh dùng email trường nên `git log` đối chiếu được MSSV ngay; ba bạn còn lại dùng Gmail cá nhân, phần đối chiếu dựa vào tên tài khoản GitHub trong bảng.

Kiểm tra một lần trước khi commit đầu: GitHub → **Settings → Emails**, địa chỉ trường phải có nhãn **Verified**. Nếu chưa verified thì commit vẫn nằm trong lịch sử nhưng **không được tính vào đồ thị đóng góp** — đây là lỗi hay gặp nhất và nó làm hỏng đúng cái mình đang muốn chứng minh.

Nếu có dùng git trên máy, chạy trong thư mục repo lớp (**không** kèm `--global`, để repo cá nhân khác không bị đổi theo):

```bash
git config user.name  "<Họ tên đầy đủ>"
git config user.email "<email GitHub cua ban>"
```

Kiểm tra ngay sau commit đầu:

```bash
git log -1 --format='%an <%ae>'
```

Bốn tài khoản của nhóm:

| MSSV | Họ tên | GitHub | Email commit |
|---|---|---|---|
| 24730090 | Nguyễn Ngọc Danh | `24730090` | `24730090@ms.uit.edu.vn` |
| 24730132 | Nguyễn Thị Hồng Phúc | `hongphuc0212` | `hongphuc02121998@gmail.com` |
| 24730131 | Nguyễn Thanh Phúc | `phucnguyen24730131` | `phucnguyen.winn@gmail.com` |
| 24730099 | Mai Hoàng Hưng | `hoanghung155` | `maihoanghung155@gmail.com` |

> Repo để public nên email này hiện công khai trong `git log`. Email trường thì chấp nhận được, và đổi lại thầy đối chiếu MSSV nhanh hơn.

---

## 3. Không dùng git cũng làm được — commit trên web

Không cần cài gì, điện thoại cũng xong, và commit vẫn mang đúng tên tài khoản người bấm.

| Bước | Thao tác |
|---|---|
| 1 | Nhận lời mời collaborator trong email, hoặc mở thẳng link repo |
| 2 | Vào file cần sửa, bấm **biểu tượng bút chì** góc trên bên phải |
| 3 | Dán nội dung vào |
| 4 | Kéo xuống cuối, chọn **Create a new branch for this commit** rồi bấm **Propose changes** |

Sửa nhiều file một lúc: mở repo rồi **bấm phím `.`** — GitHub bật VS Code ngay trên trình duyệt (github.dev), kéo thả và sửa thoải mái.

Tạo file mới: vào đúng thư mục, bấm **Add file → Create new file**.

---

## 4. Quy trình nhánh và pull request

Không ai commit thẳng lên `main`. Mỗi khối việc một nhánh, xong mở pull request, **một người khác** duyệt rồi merge.

```
tạo nhánh → commit dần trong lúc làm → push → mở PR → người duyệt đọc và comment → merge commit
```

Ba điều phải giữ:

- **Merge bằng merge commit**, không squash. Squash là gộp mất từng commit nhỏ, đúng cái thầy muốn nhìn.
- **Nhánh chỉ sinh ra khi thật sự bắt đầu làm việc trên đó.** Nhánh rỗng rồi merge cho có thì `git log --graph` nhìn ra ngay một cây toàn merge mà không có commit nội dung ở giữa.
- **Comment trong PR dùng luôn làm biên bản review chéo mô hình BPMN** mà Chương 2 cần. Một việc ra hai sản phẩm, nên đừng merge im lặng — viết vài dòng nhận xét thật.

Bảng nhánh và người duyệt chéo:

| Nhánh | Người làm | Người duyệt | Hạn merge |
|---|---|---|---|
| `setup/khung-repo` | Danh | Hưng | 19/08 |
| `docs/quy-trinh-cot-loi` | Danh | Hồng Phúc | 22/08 |
| `docs/quy-trinh-quan-ly` | Hồng Phúc | Danh | 22/08 |
| `docs/quy-trinh-ho-tro` | Thanh Phúc | Hồng Phúc | 22/08 |
| `survey/khao-sat-cua-hang` | Hưng | Danh | 26/08 |
| `model/bpmn-cot-loi` | Danh | Hồng Phúc | 30/08 |
| `model/bpmn-quan-ly-ho-tro` | Hồng Phúc | Danh | 30/08 |
| `docs/cong-cu-khao-sat` | Thanh Phúc | Hồng Phúc | 30/08 |
| `analysis/dinh-tinh` | Hồng Phúc | Danh | 02/09 |
| `analysis/dinh-luong` | Hưng | Danh | 02/09 |
| `report/word-slide` | Danh | Hồng Phúc | 05/09 |

---

## 5. Quy ước thông điệp commit

Tiền tố theo loại nội dung, viết tiếng Việt **không dấu** để không lỗi hiển thị trên terminal máy khác.

```
docs:     nội dung báo cáo, hồ sơ quy trình, câu hỏi
model:    file .bpmn và ảnh xuất
analysis: bảng phân tích định tính, định lượng
evidence: ảnh chụp chính sách, biểu mẫu, biên bản họp
report:   file Word, PDF
slide:    file PowerPoint
chore:    cấu trúc thư mục, README, cấu hình
```

Ví dụ: `model: BPMN quy trinh bao hanh doi tra C4 - 12 gateway`

Commit theo **đơn vị việc**, không dồn cả ngày vào một commit. Xong một hồ sơ quy trình thì commit, đừng đợi xong cả bốn.

Không dùng commit rỗng, đổi tên file qua lại, hoặc sửa một ký tự chỉ để tăng activity. Số lượng chỉ là nhịp tham khảo; nội dung thay đổi trong từng commit mới là phần quan trọng.

---

## 6. Ba mốc cứng — trượt là kéo cả nhóm

| Mốc | Ngày | Trễ thì sao |
|---|---|---|
| Khảo sát thực địa tại cửa hàng | **23/08**, chót 26/08 | Chương 4 không có số liệu thật, phải chuyển hết sang bảng giả định |
| Khóa 6 mô hình BPMN | **30/08** | Mô hình còn đổi thì toàn bộ phân tích Chương 4 phải làm lại |
| Word có bản đầy đủ | **03/09** | Mất 4 ngày đệm để sửa hình thức trước hạn 07/09 |

Hạn nộp: **07/09/2026**. Lưu ý 02/09 là nghỉ lễ Quốc khánh, đừng xếp việc nặng vào ngày đó.

---

## 7. Kiểm tra nhịp — Hưng chạy mỗi Chủ nhật

```bash
git log -1 --format='%ar | %an'          # commit gần nhất cách đây bao lâu
git shortlog -sn --since='7 days ago'    # số commit mỗi người trong 7 ngày
```

Ai 0 commit trong tuần thì nhắn ngay trong nhóm chat, đừng đợi tới buổi họp.

---

## 8. Không làm

- **Không push hộ người khác.** Commit mang tên sai là mất đúng cái đang cần chứng minh.
- **Không commit thẳng lên `main`.**
- **Không squash khi merge.**
- **Không tạo nhánh rỗng rồi merge cho có.**
- **Không bịa số liệu vận hành nội bộ của doanh nghiệp.** Số không có nguồn công khai thì ghi rõ "(ước lượng)" và thêm một dòng vào bảng giả định. Số công bố thì kèm nguồn và ngày truy cập.
