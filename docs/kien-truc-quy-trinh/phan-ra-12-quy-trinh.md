# Phân rã 12 quy trình theo ba lớp

Ba lớp theo mô hình phân loại quy trình phổ biến trong BPM: quy trình **cốt lõi** tạo ra
giá trị trực tiếp cho khách hàng, quy trình **quản lý** điều phối nguồn lực và ra quyết
định, quy trình **hỗ trợ** duy trì năng lực vận hành.

---

## Lớp cốt lõi — trực tiếp sinh doanh thu

| Mã | Tên quy trình | Kích hoạt bởi | Kết quả | Người phụ trách | BPMN |
|---|---|---|---|---|---|
| **C1** | Bán tại cửa hàng | Khách bước vào cửa hàng | Đơn hàng hoàn tất, hàng giao tay khách | Danh | — |
| **C2** | Bán online, giao hàng và nhận tại cửa hàng | Khách đặt trên website/app | Hàng giao tận nơi hoặc khách nhận tại cửa hàng | Hưng | — |
| **C3** | Bán trả góp | Khách chọn hình thức trả góp | Hợp đồng trả góp được duyệt, hàng giao | Danh | ✅ |
| **C4** | Bảo hành, đổi trả | Khách mang máy lỗi tới | Máy được sửa, đổi, hoàn tiền hoặc từ chối có lý do | Danh | ✅ |

C1 là quy trình nền — C2 và C3 tách ra vì có nhánh riêng đủ lớn (vận chuyển ở C2, thẩm
định tín dụng ở C3), nhưng cả hai đều quay về C1 ở khâu xuất hàng và thu tiền.

## Lớp quản lý — điều phối và ra quyết định

| Mã | Tên quy trình | Kích hoạt bởi | Kết quả | Người phụ trách | BPMN |
|---|---|---|---|---|---|
| **M1** | Hoạch định nhu cầu | Chu kỳ lập kế hoạch, tín hiệu tồn kho | Kế hoạch nhập hàng theo nhóm sản phẩm | Hồng Phúc | — |
| **M2** | Quản lý nhà cung cấp | Nhu cầu nhập hàng, đánh giá định kỳ | Hợp đồng, đơn đặt hàng, kết quả đánh giá NCC | Danh | ✅ |
| **M3** | Kho và điều chuyển | Lệnh nhập, yêu cầu điều chuyển từ cửa hàng | Hàng về đúng cửa hàng, tồn kho cập nhật | Hồng Phúc | ✅ |
| **M4** | Mạng lưới cửa hàng | Kế hoạch mở rộng, rà soát hiệu quả điểm bán | Quyết định mở, giữ, chuyển hoặc đóng cửa hàng | Hồng Phúc | — |

## Lớp hỗ trợ — duy trì năng lực vận hành

| Mã | Tên quy trình | Kích hoạt bởi | Kết quả | Người phụ trách | BPMN |
|---|---|---|---|---|---|
| **S1** | Tuyển dụng và đào tạo | Thiếu nhân sự, mở cửa hàng mới | Nhân viên được tuyển và đào tạo đủ chuẩn quầy | Thanh Phúc | ✅ |
| **S2** | Vận hành ERP / POS | Sự cố hệ thống, yêu cầu thay đổi cấu hình | Hệ thống bán hàng hoạt động ổn định | Thanh Phúc | — |
| **S3** | Mua sắm hạ tầng | Nhu cầu thiết bị, sửa chữa mặt bằng | Hạ tầng cửa hàng sẵn sàng | Thanh Phúc | — |
| **S4** | Đối soát công nợ nhà cung cấp | Chu kỳ đối soát, hóa đơn về | Công nợ khớp, thanh toán được duyệt | Thanh Phúc | ✅ |

---

## Quan hệ giữa các quy trình

Sáu liên kết chính, dùng để vẽ mũi tên trong Hình 1.1:

| Từ | Đến | Nội dung trao đổi |
|---|---|---|
| M1 | M2 | Kế hoạch nhu cầu → yêu cầu đặt hàng nhà cung cấp |
| M2 | M3 | Đơn đặt hàng đã duyệt → lệnh nhập kho |
| M3 | C1, C2, C3 | Tồn kho khả dụng tại cửa hàng → điều kiện xuất hàng |
| C1, C2, C3 | C4 | Đơn hàng đã bán → căn cứ xác định điều kiện bảo hành |
| C4 | M2 | Tỷ lệ lỗi theo model → đầu vào đánh giá nhà cung cấp |
| M2 | S4 | Hợp đồng và đơn hàng → căn cứ đối soát công nợ |

Vòng phản hồi **C4 → M2** là điểm đáng chú ý: dữ liệu bảo hành quay ngược lên khâu chọn
nhà cung cấp. Đây là chỗ Chương 4 sẽ soi kỹ vì độ trễ ở vòng này ảnh hưởng trực tiếp đến
chi phí bảo hành.

## Lý do chọn 6 quy trình để mô hình hóa

| Mã | Lý do chọn |
|---|---|
| C3 | Nhiều nhánh rẽ: hồ sơ đủ/thiếu, duyệt/từ chối, trả trước bao nhiêu phần trăm |
| C4 | Nhiều điều kiện: còn hạn/hết hạn bảo hành, lỗi phần cứng/phần mềm, sửa tại chỗ/gửi trung tâm, đổi/hoàn tiền |
| M2 | Có vòng đánh giá và phê duyệt nhiều cấp theo giá trị hợp đồng |
| M3 | Điều chuyển giữa cửa hàng phát sinh nhiều điều kiện tồn kho và ưu tiên |
| S1 | Nhiều vòng sàng lọc và điểm quyết định đạt/không đạt |
| S4 | Khớp/lệch số liệu, quá hạn, thiếu chứng từ, duyệt vượt hạn mức |

Sáu quy trình này đều có sẵn **hơn 7 điểm ra quyết định** trong thực tế vận hành, đủ để
mô hình BPMN đạt yêu cầu độ phức tạp mà không phải thêm gateway giả tạo.
