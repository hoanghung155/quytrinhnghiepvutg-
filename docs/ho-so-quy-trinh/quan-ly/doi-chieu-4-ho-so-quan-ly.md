# Đối chiếu chuẩn hóa 4 hồ sơ quy trình quản lý

**Người lập:** Nguyễn Thị Hồng Phúc · **Phiên bản:** v1
**Công cụ kiểm tra:** [kiem-tra-cau-truc-ho-so.py](../kiem-tra-cau-truc-ho-so.py)

Tài liệu này ghi lại kết quả rà soát bốn hồ sơ M1–M4 sau khi hoàn tất bản draft, trước
khi chuyển sang bước hoàn thiện. Mục đích là bảo đảm Chương 3 dàn trang được đồng nhất
giữa ba nhóm hồ sơ do ba người khác nhau lập.

---

## 1. Kết quả kiểm tra cấu trúc

Chạy `python docs/ho-so-quy-trinh/kiem-tra-cau-truc-ho-so.py`. Script đối chiếu tên và
thứ tự 12 mục với template, đếm số dòng ở các mục 5–8, và cảnh báo nếu hồ sơ có BPMN mà
không đủ hơn 7 điểm ra quyết định.

| Mã | 12 mục | Số bước (mục 5) | Điểm quyết định (mục 6) | Ngoại lệ (mục 7) | Quy tắc (mục 8) |
|---|---|---:|---:|---:|---:|
| M1 | khớp | 12 | 7 | 5 | 4 |
| M2 | khớp | 18 | 9 | 6 | 5 |
| M3 | khớp | 19 | 12 | 6 | 5 |
| M4 | khớp | 14 | 9 | 5 | 4 |

Đối chiếu với ba hồ sơ cốt lõi đã có để thấy mức chi tiết tương đương:

| Mã | Số bước | Điểm quyết định | Người lập |
|---|---:|---:|---|
| C1 | 14 | 9 | Danh |
| C3 | 15 | 10 | Danh |
| C4 | 16 | 11 | Danh |

Bốn hồ sơ quản lý nằm cùng dải với ba hồ sơ cốt lõi, không có hồ sơ nào mỏng bất thường.

## 2. Kiểm tra yêu cầu gateway cho hai hồ sơ có BPMN

| Mã | Có BPMN | Điểm quyết định ở mục 6 | Yêu cầu | Kết luận |
|---|---|---:|---|---|
| M2 | có — Danh đã dựng | 9 | hơn 7 | đạt |
| M3 | có — sẽ dựng ở nhánh `model/bpmn-quan-ly-ho-tro` | 12 | hơn 7 | đạt, còn dư biên |

M1 và M4 không được chọn mô hình hóa nên không chịu ràng buộc này.

> Số ở bảng trên là số **điểm ra quyết định trong hồ sơ**, không phải số gateway đã đếm
> trên file `.bpmn`. Số gateway thực tế phải đếm bằng script trên file mô hình và ghi vào
> biên bản review — hai con số này có thể lệch nhau khi một điểm quyết định được vẽ thành
> nhiều gateway hoặc ngược lại.

## 3. Bốn điểm đã chuẩn hóa trong đợt rà soát

| # | Điểm chuẩn hóa | Áp dụng cho |
|---|---|---|
| 1 | Dòng header thống nhất: Lớp, Người lập, Phiên bản, Có mô hình BPMN | M1–M4 |
| 2 | Actor bên ngoài in đậm trong bảng mục 3 và trong cột "Ai quyết" ở mục 6 | M2 (nhà cung cấp), M3 (đơn vị vận chuyển), M4 (chủ mặt bằng) |
| 3 | Mục 5 và mục 6 tham chiếu chéo bằng ký hiệu `→ Gn` ở cột Ghi chú | M1–M4 |
| 4 | Câu kết cuối mỗi hồ sơ nêu rõ giới hạn nguồn dữ liệu | M1–M4 |

Điểm 2 quan trọng cho Chương 4: mọi khoảng chờ do actor bên ngoài gây ra đều được xếp vào
nhóm **Hold** và cần cách xử lý khác với chờ do nguồn lực nội bộ.

## 4. Ba chỗ liên thông đã kiểm tra chéo với hồ sơ của người khác

| Liên kết | Nội dung | Trạng thái đối chiếu |
|---|---|---|
| C3 gateway G8 → M3 | Hết hàng sau khi hồ sơ trả góp đã duyệt, cần điều chuyển | Đã phản ánh ở M3 mục 5 bước 12 và mục 6 gateway G7 |
| C4 ngoại lệ E2 → M3 | Hết máy để đổi bảo hành, cần điều chuyển | Đã phản ánh ở M3 gateway G7 (nhánh hàng gấp) |
| C4 bước 16 → M2 | Tỷ lệ lỗi theo model là đầu vào đánh giá nhà cung cấp | Đã phản ánh ở M2 mục 4, bước 17 và gateway G9; quy tắc R4 |

Vòng phản hồi C4 → M2 tương ứng phát hiện **IR-13** trong Issue Register. Hồ sơ M2 đã ghi
rõ đây là quy tắc `(ước lượng)` chưa xác minh — nếu khảo sát bác bỏ thì IR-13 phải viết
lại, không chỉ sửa mỗi hồ sơ M2.

## 5. Mức độ chắc chắn của nguồn dữ liệu — bốn hồ sơ không bằng nhau

| Mã | Khảo sát cửa hàng xác minh được phần nào | Tỷ lệ nội dung `(ước lượng)` |
|---|---|---|
| M1 | Chỉ giao diện với cửa hàng: bước 7 và G4 | cao |
| M2 | Gần như không — quy trình khối văn phòng | cao |
| M3 | Phần cửa hàng: bước 10, 12, 16 | trung bình — phần khá nhất trong bốn hồ sơ |
| M4 | Không — quy trình cấp tập đoàn | cao nhất |

Đây là giới hạn thật của đề tài và phải nêu thẳng trong Chương 3, không trình bày bốn hồ
sơ như thể có cùng mức độ tin cậy. M3 là hồ sơ đáng đầu tư nhất cho buổi khảo sát 23/08.

## 6. Việc còn lại trước hạn 22/08

- [x] Dựng khung theo template 12 mục
- [x] Draft đủ bốn hồ sơ
- [x] Rà soát cấu trúc bằng script
- [ ] Hoàn thiện mục 9 (chỉ số đo lường) và mục 11 (điểm nghẽn) cho M1, M2
- [ ] Hoàn thiện mục 9 và mục 11 cho M3, M4
- [ ] Bổ sung phát hiện từ M1–M4 vào Issue Register, đánh số tiếp từ IR-14 (thuộc nhánh
      `analysis/dinh-tinh`)
