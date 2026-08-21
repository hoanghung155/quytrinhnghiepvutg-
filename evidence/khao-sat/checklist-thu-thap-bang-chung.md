# Checklist thu thập bằng chứng và bảo mật ảnh

**Dùng cho:** buổi khảo sát tại cửa hàng TGDĐ, phụ trách Mai Hoàng Hưng.

## 1. Trước khi đi

- [ ] Mang điện thoại đủ pin/bộ nhớ để chụp và bấm giờ.
- [ ] Mang sổ ghi tay dự phòng nếu điện thoại hết pin.
- [ ] In sẵn 6 câu hỏi ngắn (xem P0-D-hung-revised.md, giữ ngoài repo).
- [ ] Rủ thêm 1 bạn đi cùng — một người hỏi, một người bấm giờ/chụp.

## 2. Ảnh cần chụp (4–6 ảnh)

| # | Nội dung | Che thông tin gì | Lưu vào |
|---|---|---|---|
| 1 | Phiếu tiếp nhận bảo hành | Che tên, SĐT, địa chỉ khách; **giữ lại** loại máy, IMEI có thể che một phần | `evidence/anh-bieu-mau/` |
| 2 | Bảng giá trả góp / thông tin công ty tài chính liên kết | Không có thông tin cá nhân, chụp nguyên | `evidence/anh-bieu-mau/` |
| 3 | Hóa đơn của chính mình (nếu có mua) | Che số hóa đơn nếu cần, giữ lại phần trình bày | `evidence/anh-bieu-mau/` |
| 4 | Sơ đồ mặt bằng (vẽ tay tại chỗ) | Không cần che | `evidence/anh-bieu-mau/` |
| 5–6 | Ảnh bổ sung khác nếu nhân viên đồng ý | Tùy nội dung | `evidence/anh-bieu-mau/` |

## 3. Quy tắc bảo mật khi xử lý ảnh sau buổi khảo sát

- **Che mọi thông tin định danh khách hàng và nhân viên**: tên đầy đủ, số điện thoại, địa
  chỉ, số CMND/CCCD, chữ ký. Dùng công cụ che (blur/mosaic), không chỉ crop lề ảnh.
- Không đăng ảnh gốc chưa xử lý lên repo, kể cả tạm thời rồi xóa sau — repo public nên
  lịch sử git vẫn giữ ảnh gốc.
- Ảnh chụp màn hình hệ thống nội bộ (nếu nhân viên cho xem) không đăng lên repo, kể cả đã
  che — chỉ mô tả bằng lời trong báo cáo.
- Đặt tên file theo quy ước: `<loai>-<mo-ta>-<nn>.jpg`, ví dụ `bieu-mau-phieu-bao-hanh-01.jpg`
  (xem [quy-uoc-dat-ten-file.md](../../docs/quy-uoc-dat-ten-file.md)).

## 4. Ghi âm

- **Không ghi âm nếu nhân viên không đồng ý rõ ràng.** Xin phép trước khi bắt đầu, không
  bật máy ghi âm ngầm.
- Nếu được đồng ý ghi âm: chỉ dùng để đối chiếu khi viết báo cáo, không đăng file ghi âm
  lên repo.

## 5. Sau buổi khảo sát — trước khi commit

- [ ] Rà lại từng ảnh, xác nhận đã che hết thông tin cá nhân.
- [ ] Đối chiếu số lượt bấm giờ đã ghi khớp với ghi chép tay/sổ.
- [ ] Viết mục "những gì chưa xác minh được" trước khi coi báo cáo là hoàn thành.
