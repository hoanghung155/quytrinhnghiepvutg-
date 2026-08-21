# Quy ước đặt tên file và thư mục

Áp dụng cho toàn bộ repo. Mục đích: mọi người đoán được đường dẫn mà không phải hỏi, và
`git log` đọc được trên máy bất kỳ.

## 1. Nguyên tắc chung

| Quy tắc | Đúng | Sai |
|---|---|---|
| Tiếng Việt **không dấu** | `ho-so-C1.md` | `hồ-sơ-C1.md` |
| Chữ thường, nối bằng dấu `-` | `phan-ra-12-quy-trinh.md` | `Phan_Ra_12_QuyTrinh.md` |
| Không dùng khoảng trắng | `bao-cao-khao-sat.md` | `bao cao khao sat.md` |
| Không ký tự đặc biệt `# % & { } < > * ? $ ! : @` | `bang-gia-dinh.md` | `bang gia dinh (final)!.md` |
| Mã quy trình viết **hoa**, giữ nguyên | `C4-bao-hanh-doi-tra/` | `c4-bao-hanh-doi-tra/` |

Lý do bỏ dấu: file có dấu gây lỗi khi zip nộp bài, khi mở trên máy khác bảng mã khác, và
khi `git log` hiển thị trên terminal Windows mặc định.

## 2. Thư mục cấp 1

Trùng đúng với tiền tố commit đã quy ước, để nhìn commit là biết file nằm đâu:

| Thư mục | Tiền tố commit tương ứng |
|---|---|
| `docs/` | `docs:` |
| `model/` | `model:` |
| `analysis/` | `analysis:` |
| `evidence/` | `evidence:` |
| `report/` | `report:` |
| `slide/` | `slide:` |
| `bai-tap-tuan/` | `bai-tap:` |

## 3. Đặt tên theo loại file

| Loại | Mẫu | Ví dụ |
|---|---|---|
| Hồ sơ quy trình | `ho-so-<Mã>.md` | `ho-so-C3.md` |
| Thư mục quy trình | `<Mã>-<ten-khong-dau>/` | `M2-quan-ly-nha-cung-cap/` |
| File BPMN | `<Mã>-<ten-khong-dau>.bpmn` | `C4-bao-hanh-doi-tra.bpmn` |
| Ảnh xuất từ BPMN | `<Mã>-<ten-khong-dau>.png` | `C4-bao-hanh-doi-tra.png` |
| Bảng phân tích | `<loai>-<Mã>.md` | `va-bva-nva-C3.md` |
| Ảnh evidence | `<loai>-<mo-ta>-<nn>.jpg` | `bieu-mau-phieu-bao-hanh-01.jpg` |
| Báo cáo nộp | `<MSSV1>_<MSSV2>_<MSSV3>_<MSSV4>.docx` | theo mẫu đã dùng ở bài tập tuần |

File BPMN và ảnh xuất của cùng một quy trình **phải trùng tên**, chỉ khác đuôi — để biết
ảnh nào xuất từ mô hình nào.

## 4. Đánh số phiên bản

Không đặt `-final`, `-final2`, `-moi`, `-sua`. Git đã giữ lịch sử. Phiên bản ghi trong
**nội dung file** ở dòng header (`Phiên bản: v1 / v2`), không ghi vào tên file.

Ngoại lệ duy nhất: mô hình BPMN sau khi khóa ngày 30/08 thì thêm hậu tố `-v1-khoa` để
phân biệt với bản đang sửa.

## 5. File tạm và file không đưa lên repo

Đã cấu hình trong [.gitignore](../.gitignore): file tạm Office `~$*`, slide bài giảng PDF,
thư mục build, môi trường ảo Python. Trước khi commit chạy `git status` xem có file lạ
lọt vào không.

## 6. Chuẩn hóa header trong file hồ sơ quy trình

Mọi hồ sơ quy trình dùng chung template
[docs/ho-so-quy-trinh/_template-ho-so-quy-trinh.md](ho-so-quy-trinh/_template-ho-so-quy-trinh.md),
giữ nguyên 12 mục và đúng thứ tự. Mục chưa có dữ liệu ghi `(chưa hoàn thiện)` hoặc
`(chưa xác minh)`, không xóa mục — vì Chương 3 dàn trang theo đúng thứ tự này.
