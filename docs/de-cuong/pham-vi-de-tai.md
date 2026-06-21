# Phạm vi đề tài

## 1. Đối tượng phân tích

Chuỗi bán lẻ thiết bị công nghệ của Công ty Cổ phần Đầu tư Thế Giới Di Động (MWG),
gồm hai chuỗi cửa hàng:

| Chuỗi | Định vị | Vai trò trong đề tài |
|---|---|---|
| **thegioididong.com (TGDĐ)** | Chuỗi phổ thông, đa thương hiệu | Nguồn quan sát chính cho quy trình bán và bảo hành |
| **TopZone** | Chuỗi ủy quyền cao cấp của Apple (AAR/APR) | Đối chiếu điểm khác biệt về quy trình bảo hành và chính sách đổi trả |

Hai chuỗi dùng chung nền tảng vận hành của MWG (ERP, hệ thống kho, hệ thống bảo hành),
nên phân tích quy trình lõi có thể gộp và chỉ tách khi có khác biệt thật sự.

## 2. Phạm vi sản phẩm

Thu hẹp ở bốn nhóm hàng:

1. Điện thoại di động
2. Laptop
3. Máy tính bảng
4. Phụ kiện đi kèm bốn nhóm trên (sạc, ốp, tai nghe, thẻ nhớ)

**Loại khỏi phạm vi:** đồng hồ thông minh, thiết bị gia dụng của Điện Máy Xanh, hàng
tiêu dùng của Bách Hóa Xanh, dịch vụ SIM số và thanh toán hộ.

## 3. Phạm vi quy trình

Phân tích **12 quy trình** chia ba lớp — cốt lõi, quản lý, hỗ trợ. Chi tiết phân rã xem
[phan-ra-12-quy-trinh.md](../kien-truc-quy-trinh/phan-ra-12-quy-trinh.md).

Trong 12 quy trình đó, **6 quy trình được mô hình hóa BPMN**: M2, C3, C4, M3, S1, S4.
Sáu quy trình còn lại chỉ lập hồ sơ dạng văn bản.

## 4. Phạm vi không gian và thời gian

- **Không gian:** cửa hàng TGDĐ tại khu vực TP.HCM. Buổi khảo sát thực địa diễn ra tại
  một cửa hàng cụ thể, thông tin cửa hàng ghi trong báo cáo khảo sát.
- **Thời gian:** dữ liệu quan sát thu thập trong tháng 08/2026. Chính sách và biểu mẫu
  đối chiếu theo bản công bố công khai tại thời điểm truy cập, có ghi ngày.

## 5. Giới hạn của đề tài

Nhóm là người quan sát bên ngoài, không có quyền truy cập hệ thống nội bộ MWG. Do đó:

- **Không có số liệu vận hành nội bộ.** Doanh số, tồn kho, chi phí nhân sự, thời gian
  chuẩn theo quy định nội bộ đều không tiếp cận được.
- Mọi con số thời gian trong Chương 4 đến từ **bấm giờ trực tiếp tại cửa hàng** (mẫu
  nhỏ, `n` ghi rõ) hoặc từ **bảng giả định** có đánh dấu "(ước lượng)".
- Quy trình được dựng lại từ quan sát, phỏng vấn nhân viên và tài liệu công khai — là
  **mô hình suy luận**, không phải quy trình chuẩn do MWG ban hành.

Ba giới hạn trên được nêu lại ở đầu Chương 4 để mọi kết luận định lượng đều truy được
về nguồn.

## 6. Nguồn dữ liệu

| Loại | Nguồn | Ghi chú |
|---|---|---|
| Quan sát trực tiếp | Buổi khảo sát tại cửa hàng TGDĐ | Bảng bấm giờ, sơ đồ mặt bằng |
| Phỏng vấn | Nhân viên tư vấn, nhân viên tiếp nhận bảo hành | Không ghi âm nếu không được đồng ý |
| Tài liệu công khai | Website TGDĐ/TopZone, chính sách bảo hành, chính sách đổi trả | Kèm ngày truy cập |
| Báo cáo doanh nghiệp | Báo cáo thường niên MWG | Chỉ dùng số đã công bố |

Ảnh chụp biểu mẫu và chính sách lưu tại [evidence/anh-bieu-mau/](../../evidence/anh-bieu-mau/),
đã che thông tin cá nhân của khách và nhân viên.
