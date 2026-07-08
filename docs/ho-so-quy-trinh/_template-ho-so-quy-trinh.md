# Template hồ sơ quy trình

> Sao chép file này khi lập hồ sơ một quy trình mới. Giữ nguyên thứ tự mục và tên mục để
> Chương 3 dàn trang đồng nhất. Mục nào chưa có dữ liệu thì ghi `(chưa xác minh)`, đừng
> xóa mục.

---

# `<Mã>` — `<Tên quy trình>`

**Lớp:** cốt lõi / quản lý / hỗ trợ
**Người lập:** `<tên>` · **Ngày lập:** `<dd/mm/yyyy>` · **Phiên bản:** `<v1>`
**Có mô hình BPMN:** có / không

## 1. Mục đích

Một đoạn, trả lời: quy trình này tồn tại để làm gì, và nếu không có nó thì doanh nghiệp
mất gì.

## 2. Phạm vi

- **Bắt đầu từ:** sự kiện kích hoạt
- **Kết thúc khi:** trạng thái kết thúc (liệt kê đủ các kết thúc, kể cả kết thúc thất bại)
- **Không bao gồm:** những việc dễ nhầm là thuộc quy trình này nhưng thực ra thuộc quy trình khác

## 3. Actor và vai trò

| Actor | Loại | Trách nhiệm chính |
|---|---|---|
| | Nội bộ / Bên ngoài / Hệ thống | |

Ghi rõ actor nào là **hệ thống** (ERP, POS, cổng tín dụng) vì khi vẽ BPMN chúng thành
lane riêng hoặc service task.

## 4. Đầu vào và đầu ra

| Loại | Tên | Từ đâu / đi đâu | Bắt buộc |
|---|---|---|---|
| Đầu vào | | | Có / Không |
| Đầu ra | | | |

## 5. Các bước thực hiện

| # | Bước | Actor | Đầu vào | Đầu ra | Ghi chú |
|---|---|---|---|---|---|
| 1 | | | | | |

Đánh số liên tục. Bước nào có rẽ nhánh thì ghi ở cột Ghi chú và mô tả kỹ ở mục 6.

## 6. Điểm ra quyết định

| # | Câu hỏi quyết định | Điều kiện | Nhánh kết quả | Ai quyết |
|---|---|---|---|---|
| G1 | | | | |

Đây là mục dùng để đếm gateway khi vẽ BPMN. Quy trình có mô hình BPMN cần **hơn 7** dòng
ở bảng này.

## 7. Ngoại lệ và xử lý

| Mã | Tình huống ngoại lệ | Cách xử lý | Ai xử lý |
|---|---|---|---|
| E1 | | | |

## 8. Quy tắc nghiệp vụ

| Mã | Quy tắc | Nguồn |
|---|---|---|
| R1 | | Chính sách công bố / quan sát / phỏng vấn / (ước lượng) |

Cột **Nguồn** bắt buộc. Quy tắc suy ra từ quan sát mà không có văn bản thì ghi
`quan sát`; số liệu không có nguồn công khai thì ghi `(ước lượng)` và thêm dòng vào bảng
giả định ở Chương 4.

## 9. Chỉ số đo lường

| Chỉ số | Đơn vị | Cách đo | Giá trị ghi nhận | Nguồn |
|---|---|---|---|---|
| | phút / % / lần | | | bấm giờ n=… / (ước lượng) |

## 10. Hệ thống và biểu mẫu liên quan

| Tên | Loại | Ghi chú |
|---|---|---|
| | Hệ thống / Biểu mẫu | |

## 11. Điểm nghẽn quan sát được

Liệt kê ngắn, mỗi dòng một điểm, kèm bằng chứng. Mục này là đầu vào trực tiếp cho Issue
Register ở Chương 4.

## 12. Nguồn tham chiếu

Liệt kê tài liệu, ảnh evidence, đoạn phỏng vấn đã dùng. Ảnh ghi đường dẫn trong
`evidence/`. Tài liệu web ghi kèm ngày truy cập.
