# Phân tích quy trình nghiệp vụ chuỗi bán lẻ thegioididong.com + TopZone

Đồ án môn **Hệ thống Quản trị Qui trình Nghiệp vụ** — GVHD: ThS. Hà Lê Hoài Trung.
Trường Đại học Công nghệ Thông tin, ĐHQG-HCM — Khoa Hệ thống Thông tin.

**Phạm vi:** chuỗi bán lẻ thegioididong.com và TopZone (Công ty CP Đầu tư Thế Giới
Di Động — MWG), thu hẹp ở bốn nhóm sản phẩm: điện thoại, laptop, máy tính bảng và
phụ kiện.

**Hạn nộp:** 07/09/2026.

---

## Thành viên

| MSSV | Họ và tên | GitHub | Phần phụ trách |
|---|---|---|---|
| 24730090 | Nguyễn Ngọc Danh (nhóm trưởng) | `24730090` | Kiến trúc quy trình, hồ sơ C1/C3/C4, BPMN M2/C3/C4, Issue Register, báo cáo Word, slide |
| 24730132 | Nguyễn Thị Hồng Phúc | `hongphuc0212` | Hồ sơ M1–M4, BPMN M3/S1, phân tích định tính, soát hình thức |
| 24730131 | Nguyễn Thanh Phúc | `phucnguyen24730131` | Hồ sơ S1–S4, bộ câu hỏi phỏng vấn, bảng thuật ngữ, BPMN S4, tài liệu tham khảo |
| 24730099 | Mai Hoàng Hưng | `hoanghung155` | Quản trị repo, khảo sát thực địa, hồ sơ C2, bằng chứng, phân tích định lượng |

---

## Mười hai quy trình theo ba lớp

| Lớp | Mã | Quy trình |
|---|---|---|
| **Cốt lõi** | C1 | Bán tại cửa hàng |
| | C2 | Bán online, giao hàng và nhận tại cửa hàng |
| | C3 | Bán trả góp |
| | C4 | Bảo hành, đổi trả |
| **Quản lý** | M1 | Hoạch định nhu cầu |
| | M2 | Quản lý nhà cung cấp |
| | M3 | Kho và điều chuyển |
| | M4 | Mạng lưới cửa hàng |
| **Hỗ trợ** | S1 | Tuyển dụng và đào tạo |
| | S2 | ERP / POS |
| | S3 | Mua sắm hạ tầng |
| | S4 | Đối soát công nợ nhà cung cấp |

Sáu quy trình được mô hình hóa BPMN: **M2, C3, C4, M3, S1, S4** — mỗi mô hình phải có
**hơn 7 gateway**.

---

## Cấu trúc thư mục

```
.
├── meta/                              # Quy ước làm việc nhóm, phân công (P0-*)
├── docs/                              # Nội dung báo cáo và hồ sơ quy trình
│   ├── de-cuong/                      # Đề cương Chương 1–4
│   ├── kien-truc-quy-trinh/           # Sơ đồ kiến trúc Hình 1.1, 12 quy trình 3 lớp
│   ├── ho-so-quy-trinh/
│   │   ├── cot-loi/                   # C1 · C2 · C3 · C4
│   │   ├── quan-ly/                   # M1 · M2 · M3 · M4
│   │   └── ho-tro/                    # S1 · S2 · S3 · S4
│   ├── cong-cu-khao-sat/              # 24 câu hỏi phỏng vấn, chia 4 nhóm
│   ├── bang-thuat-ngu/                # 25–30 mục
│   └── tai-lieu-tham-khao/            # Danh mục IEEE, tách tiếng Việt / tiếng Anh
├── model/                             # Mô hình hóa quy trình
│   ├── bpmn/                          # File nguồn .bpmn
│   └── hinh-xuat/                     # Ảnh xuất từ mô hình (PNG/SVG) để chèn báo cáo
├── evidence/                          # Bằng chứng thu thập được
│   ├── khao-sat/                      # Báo cáo khảo sát cửa hàng, bảng bấm giờ
│   ├── anh-bieu-mau/                  # Ảnh biểu mẫu, chính sách (đã che thông tin cá nhân)
│   └── bien-ban-review/               # Biên bản review chéo mô hình BPMN
├── analysis/                          # Bảng phân tích Chương 4
│   ├── dinh-tinh/                     # VA/BVA/NVA, Move/Hold/Overdo, Fishbone
│   ├── dinh-luong/                    # Bảng giả định, cycle time, CTE, bảng chi phí
│   └── issue-register/                # Bảng tổng hợp phát hiện
├── report/                            # Báo cáo Word và bản PDF nộp
└── slide/                             # Slide PowerPoint và kịch bản trình bày
```

Thư mục `2026-*/` ở gốc repo là bài tập theo tuần của môn học, không thuộc đồ án.

---

## Quy ước nhánh

Không ai commit thẳng lên nhánh mặc định `bai-tap-qua-trinh`. Mỗi khối việc một nhánh,
xong thì mở pull request, **một người khác** đọc và comment rồi mới merge.

```
tạo nhánh → commit dần trong lúc làm → push → mở PR → người duyệt comment → merge commit
```

Ba điều bắt buộc:

- **Merge bằng merge commit, không squash** — squash làm mất từng commit nhỏ.
- **Nhánh chỉ tạo khi thật sự bắt đầu làm việc trên đó**, không tạo nhánh rỗng rồi merge cho có.
- **Không duyệt PR im lặng.** Comment trong PR dùng luôn làm biên bản review chéo mô hình
  BPMN cho Chương 2.

### Bảng nhánh và người duyệt chéo

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

## Quy ước thông điệp commit

Tiền tố theo loại nội dung, phần mô tả viết tiếng Việt **không dấu** để không lỗi hiển
thị trên terminal máy khác.

| Tiền tố | Dùng cho |
|---|---|
| `docs:` | Nội dung báo cáo, hồ sơ quy trình, câu hỏi |
| `model:` | File `.bpmn` và ảnh xuất |
| `analysis:` | Bảng phân tích định tính, định lượng |
| `evidence:` | Ảnh chụp chính sách, biểu mẫu, biên bản họp |
| `report:` | File Word, PDF |
| `slide:` | File PowerPoint |
| `chore:` | Cấu trúc thư mục, README, cấu hình |

Ví dụ: `model: BPMN quy trinh bao hanh doi tra C4 - 12 gateway`

Commit theo **đơn vị việc**, không dồn cả ngày vào một commit.

---

## Ba mốc cứng

| Mốc | Ngày |
|---|---|
| Khảo sát thực địa tại cửa hàng | **23/08**, chót 26/08 |
| Khóa 6 mô hình BPMN | **30/08** |
| Word có bản đầy đủ | **03/09** |

Chi tiết phân công và nhịp làm việc xem [meta/P0-chung-quy-uoc-revised.md](meta/P0-chung-quy-uoc-revised.md).
