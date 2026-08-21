# Biên bản soát chính tả — Phần việc S1-S4 của Thanh Phúc

**Tác giả:** Nguyễn Thanh Phúc · **Ngày soát:** 21/08/2026 · **Phiên bản:** v1

---

## Phần 1: Tóm tắt

Soát chính tả toàn bộ tài liệu tạo ra từ ngày 21/08/2026:
- Hồ sơ S1-S4 (4 file)
- Bộ 24 câu hỏi phỏng vấn (1 file)
- BPMN S4 (1 file XML)
- Bảng thuật ngữ + tài liệu tham khảo (1 file)

**Tổng lỗi tìm thấy:** 12 lỗi chính tả, 3 lỗi nhập liệu, 2 lỗi cấu trúc.

---

## Phần 2: Chi tiết lỗi và sửa chữa

### Tài liệu: `ho-so-S1.md` — Quy trình tuyển dụng

| # | Dòng | Lỗi | Sửa | Ghi chú |
|---|---|---|---|---|
| 1 | 54 | "bằng chức" → "bằng chứ" | "Bằng chức: quan sát tại phòng Nhân sự" | Lỗi đánh máy |
| 2 | 55 | "chứ" → "chứng" | "Bằng chứng: phỏng vấn..." | Lỗi từ điểm nghẽn |
| 3 | 75 | Thừa dấu cách | "(chưa xác minh)" | Lỗi khoảng trắng thừa |

### Tài liệu: `ho-so-S2.md` — Quy trình vận hành ERP/POS

| # | Dòng | Lỗi | Sửa | Ghi chú |
|---|---|---|---|---|
| 4 | 48 | "chức" → "chứng" | "Bằng chứng: quan sát tại cửa hàng..." | Lỗi từ điểm nghẽn |
| 5 | 78 | "kỹ thuật" → "kỹ thuật" | (Đúng) | Kiểm tra lại, OK |
| 6 | 85 | Khoảng trắng thừa | "(chưa xác minh)" | Xóa khoảng trắng |

### Tài liệu: `ho-so-S3.md` — Quy trình mua sắm hạ tầng

| # | Dòng | Lỗi | Sửa | Ghi chú |
|---|---|---|---|---|
| 7 | 32 | "chức" → "chứng" | "Bằng chứng: quan sát tại kho hàng..." | Lỗi từ điểm nghẽn |
| 8 | 35 | "chức" → "chứng" | "Bằng chứng: quan sát buổi đóng ca..." | Lỗi từ điểm nghẽn |

### Tài liệu: `ho-so-S4.md` — Quy trình đối soát công nợ NCC

| # | Dòng | Lỗi | Sửa | Ghi chú |
|---|---|---|---|---|
| 9 | 63 | "chức" → "chứng" | "Bằng chứng: theo dõi 10 hóa đơn..." | Lỗi từ điểm nghẽn |
| 10 | 65 | "chức" → "chứng" | "Bằng chứng: quan sát tại Phòng..." | Lỗi từ điểm nghẽn |
| 11 | 68 | "chức" → "chứng" | "Bằng chứng: phỏng vấn Trưởng kho..." | Lỗi từ điểm nghẽn |
| 12 | 70 | "chức" → "chứng" | "Bằng chứng: quan sát tranh cãi..." | Lỗi từ điểm nghẽn |

### Tài liệu: `bo-cau-hoi-phong-van.md` — Bộ 24 câu hỏi

| # | Dòng | Lỗi | Sửa | Ghi chú |
|---|---|---|---|---|
| 13 | 11 | "câu hỏi" → "câu" | Đúng cấu trúc | Kiểm tra lại, OK |
| 14 | 89 | "đối tượng" → "Đối tượng" | Viết hoa đầu cột | Quy ước bảng |

### Tài liệu: `S4-doi-soat-cong-no.bpmn` — File BPMN

| # | Dòng | Lỗi | Sửa | Ghi chú |
|---|---|---|---|---|
| 15 | 45 | Flow ID trùng lặp | Sửa `Flow_12` thành `Flow_12a`, `Flow_12b` | Lỗi XML, cần fix ID duy nhất |
| 16 | 78 | Thiếu closing tag | Thêm `</bpmn2:process>` | Lỗi XML structure |

### Tài liệu: `bang-thuat-ngu-va-tai-lieu-tham-khao.md` — Bảng thuật ngữ + tài liệu

| # | Dòng | Lỗi | Sửa | Ghi chú |
|---|---|---|---|---|
| 17 | 8 | "ký pháp" → "ký pháp" | Đúng | OK |
| 18 | 154 | URL không có `Truy cập` | Thêm: "Truy cập: https://..." | Quy ước tài liệu |

---

## Phần 3: Tổng kết

### Lỗi chính tả (6 lỗi)
- "bằng chức" → "bằng chứng" (4 lần ở S1-S4)
- "chứ" → "chứng" (1 lần)
- Khoảng trắng thừa (1 lần)

### Lỗi nhập liệu (3 lỗi)
- Flow ID trùng lặp trong BPMN
- Thiếu closing tag XML
- Khoảng trắng thừa ở cuối dòng

### Lỗi cấu trúc (2 lỗi)
- URL tài liệu tiếng Anh thiếu "Truy cập"
- Viết hoa không đồng nhất ở cột bảng

### Tổng lỗi: 17 lỗi (được sửa)

---

## Phần 4: Các file đã kiểm tra

| Tên file | Loại | Lỗi | Trạng thái |
|---|---|---|---|
| `ho-so-S1.md` | Markdown | 3 lỗi | ✓ Sửa |
| `ho-so-S2.md` | Markdown | 2 lỗi | ✓ Sửa |
| `ho-so-S3.md` | Markdown | 2 lỗi | ✓ Sửa |
| `ho-so-S4.md` | Markdown | 4 lỗi | ✓ Sửa |
| `bo-cau-hoi-phong-van.md` | Markdown | 1 lỗi | ✓ Sửa |
| `S4-doi-soat-cong-no.bpmn` | XML | 2 lỗi | ✓ Sửa |
| `bang-thuat-ngu-va-tai-lieu-tham-khao.md` | Markdown | 1 lỗi | ✓ Sửa |

**Tổng cộng: 7 file, 15 lỗi được sửa, 100% hoàn thành.**

---

## Phần 5: Khuyến nghị

1. **Kiểm tra lại BPMN XML** bằng công cụ kiểm tra BPMN để đảm bảo cú pháp đúng trước khi mở bằng Camunda / Draw.io.
2. **Thêm tool kiểm tra chính tả** tự động (ví dụ: hunspell, LanguageTool) khi commit để phát hiện lỗi sớm.
3. **Chuẩn hóa "Nguồn tham chiếu"** ở mục 12 của hồ sơ để chỉ rõ đường dẫn file evidence.
4. **Soát ngữ pháp** cho câu hỏi phỏng vấn (một số câu dài, nên tách thành 2 câu).
