# P0-D — Phần việc của Hưng (24730099, chủ repo)

> **Cách dùng:** đọc [P0-chung-quy-uoc.md](P0-chung-quy-uoc.md) trước — nhất là mục 2 (danh tính git) và mục 3 (cách commit trên web nếu không cài git).

Đề tài: phân tích quy trình nghiệp vụ chuỗi bán lẻ **thegioididong.com + TopZone** (MWG), phạm vi thu hẹp ở điện thoại, laptop, máy tính bảng, phụ kiện. Môn Hệ thống Quản trị Qui trình Nghiệp vụ, GVHD ThS. Hà Lê Hoài Trung. Hạn nộp **07/09/2026**.

Repo: <https://github.com/hoanghung155/quytrinhnghiepvutg-> — bạn là chủ repo.

---

## Bạn giữ gì

Khoảng 20%. Bạn **không vẽ mô hình BPMN nào** — đổi lại bạn là người duy nhất mang dữ liệu thật về cho nhóm. Toàn bộ số liệu thời gian của Chương 4 đi ra từ buổi khảo sát của bạn, và đó cũng là phần khác biệt lớn nhất so với các nhóm khác.

| Khối | Sản phẩm | Hạn |
|---|---|---|
| Quản trị repo | Cấp quyền collaborator, để repo public, theo dõi nhịp commit | 19/08 |
| **Khảo sát tại cửa hàng TGDĐ** | Báo cáo khảo sát: bảng bấm giờ, phỏng vấn nhân viên, ảnh biểu mẫu | **23/08**, chót 26/08 |
| Hồ sơ 1 quy trình | C2 bán online, giao hàng và nhận tại cửa hàng | 26/08 |
| Bằng chứng | Ảnh chính sách, biểu mẫu, sơ đồ mặt bằng cửa hàng dựng lại từ quan sát | 28/08 |
| Phân tích định lượng | Bảng giả định · cycle time (CT) · hiệu suất thời gian (CTE) · bảng chi phí | 02/09 |

---

## Bước 0 — Danh tính git

Bỏ qua bước này thì commit **không vào đồ thị đóng góp**, thầy nhìn vào không thấy bạn làm gì.

Tài khoản `hoanghung155` của bạn đăng ký bằng `maihoanghung155@gmail.com` — dùng đúng địa chỉ đó để commit.

Kiểm tra một lần: GitHub → **Settings → Emails**, địa chỉ đó phải có nhãn **Verified**. Không verified thì commit vẫn vào lịch sử nhưng **không lên đồ thị đóng góp**.

Nếu dùng git trên máy, chạy trong thư mục repo (không kèm `--global`):

```bash
git config user.name  "Mai Hoàng Hưng"
git config user.email "maihoanghung155@gmail.com"
```

Nếu commit trên web thì không cần làm gì — GitHub tự gán đúng tài khoản bạn đang đăng nhập.

---

## Việc quản trị repo — làm ngay 19/08

- [ ] Settings → Collaborators: mời `24730090`, `hongphuc0212`, `phucnguyen24730131` quyền **Write**
- [ ] Settings → General → Default branch là `main`
- [ ] Repo để **public** — thầy xem được mà không cần mời
- [ ] Chủ Nhật hằng tuần chạy hai lệnh kiểm tra nhịp ở cuối file này, ai 0 commit thì nhắn nhóm chat

---

## Nhánh của bạn

| Thứ tự | Nhánh | Nội dung | Người duyệt | Hạn merge |
|---|---|---|---|---|
| 1 | `survey/khao-sat-cua-hang` | Báo cáo khảo sát, ảnh bằng chứng, hồ sơ C2 | Danh | 26/08 |
| 2 | `analysis/dinh-luong` | Bảng giả định, cycle time, CTE, chi phí | Danh | 02/09 |

Bạn **duyệt chéo** cho `setup/khung-repo` và BPMN C4 của Danh.

---

## Buổi khảo sát — đặc tả chi tiết

Một buổi khoảng 3 tiếng, ở một cửa hàng TGDĐ bất kỳ. Nên đi **hai người** (bạn + một bạn nữa): một người hỏi, một người bấm giờ và chụp. Sản phẩm vẫn ghi tên bạn.

**Mang theo:** điện thoại (chụp + bấm giờ), sổ ghi, bản in 6–8 câu hỏi ngắn. Bộ 24 câu đầy đủ Thanh Phúc gửi trước 26/08, nhưng đừng mang cả 24 câu đi hỏi — chọn 6 câu dễ trả lời.

| Việc | Cách làm | Ra sản phẩm gì |
|---|---|---|
| Bấm giờ giao dịch bán | Quan sát, bấm giờ 6–10 lượt khách: từ lúc nhân viên tiếp cận đến lúc rời quầy. Ghi cả lượt bị ngắt quãng | Bảng `n = …` lượt, nhỏ nhất / lớn nhất / trung bình |
| Bấm giờ khâu bảo hành | Nếu có khách đến bảo hành thì bấm riêng: chờ tới lượt, tiếp nhận, lập phiếu | Bảng thời gian theo chặng |
| Chụp biểu mẫu | Phiếu tiếp nhận bảo hành, bảng giá trả góp, hóa đơn của chính mình. **Che thông tin cá nhân** | 4–6 ảnh |
| Hỏi nhân viên | Xin 10 phút lúc vắng khách. Giới thiệu là sinh viên làm bài tập môn học, **không ghi âm nếu họ không đồng ý** | Ghi chép 6–8 câu trả lời |
| Quan sát bố trí | Vị trí quầy tư vấn, quầy thu ngân, kho, khu bảo hành | Sơ đồ mặt bằng vẽ tay rồi số hóa |

**Sáu câu mang đi hỏi** — ngắn, dễ trả lời, không đụng vào doanh số:

1. Một ca đổi trả trong tháng đầu thường xử lý xong tại cửa hàng luôn, hay phải gửi lên trung tâm bảo hành?
2. Nếu phải gửi lên thì thường bao lâu có kết quả?
3. Khách mua trả góp thì từ lúc nộp giấy tờ đến lúc có kết quả duyệt mất khoảng bao lâu?
4. Trường hợp nào hồ sơ trả góp hay bị vướng nhất?
5. Khi cửa hàng hết máy khách muốn mua, quy trình lấy hàng từ nơi khác về thế nào?
6. Việc gì trong ngày làm mất thời gian nhất mà anh/chị thấy đáng lẽ nhanh hơn được?

**Sản phẩm nộp:** `evidence/khao-sat/bao-cao-khao-sat.md` gồm thời gian và địa điểm, cách thu thập, bảng bấm giờ, tóm tắt câu trả lời, ảnh đính kèm, và mục **"những gì chưa xác minh được"**.

> Mục cuối cùng quan trọng hơn vẻ ngoài của nó: ghi thẳng cái gì hỏi không ra hoặc nhân viên không trả lời. Có mục đó thì cả Chương 4 đứng vững, vì mọi con số đều truy được về nó hoặc về bảng giả định. Không có nó thì mọi con số đều bị nghi là bịa.

**Nếu không đi khảo sát được:** tối 22/08 mà chưa hẹn được lịch thì báo nhóm ngay. Phương án thay thế là quan sát thuần (không phỏng vấn) cộng chụp biểu mẫu, Chương 4 chuyển hoàn toàn sang bảng giả định và ghi rõ lý do. **Nhân viên từ chối trả lời thì không nài** — ghi vào mục "chưa xác minh được", bảng bấm giờ và ảnh biểu mẫu vẫn còn nguyên giá trị.

---

## Việc theo ngày

Mục tiêu: **14 commit nội dung**.

> Các mốc trước 19/08 chỉ dùng nếu đúng với tiến độ thực tế đã làm. Nếu một đầu việc được làm muộn hơn, commit ở ngày thực tế.

| Ngày | Việc | Commit ra cái gì |
|---|---|---|
| 07/07 | Tạo ghi chú quản trị repo và checklist cộng tác | `chore: tao checklist quan tri repo` |
| 17/07 | Tổng hợp nguồn công khai phục vụ khảo sát | `docs: tong hop nguon khao sat` |
| 28/07 | Draft khung hồ sơ C2 bán online | `docs: draft ho so C2 ban online` |
| 06/08 | Tạo khung bảng quan sát và bấm giờ | `docs: khung bang quan sat bam gio` |
| 13/08 | Chuẩn bị checklist evidence và bảo mật ảnh | `evidence: checklist thu thap bang chung` |
| 19/08 | Cấu hình repo public và collaborator | `chore: cau hinh repo` |
| 22/08 | Chốt kế hoạch khảo sát và mẫu ghi nhận | `docs: chot ke hoach khao sat` |
| 24/08 | Viết báo cáo khảo sát cửa hàng | `evidence: bao cao khao sat cua hang` |
| 25/08 | Xử lý ảnh biểu mẫu và chính sách | `evidence: anh bieu mau va chinh sach` |
| 26/08 | Hoàn thiện hồ sơ C2 bán online | `docs: hoan thien ho so C2 ban online` |
| 28/08 | Bảng giả định cho các số chưa xác minh | `analysis: bang gia dinh` |
| 01/09 | Cycle time và CTE từ dữ liệu khảo sát | `analysis: cycle time va CTE` |
| 02/09 | Hoàn thiện bảng chi phí | `analysis: bang chi phi` |
| 06/09 | Soát dữ liệu định lượng trước bản nộp | `analysis: soat du lieu dinh luong` |

> Ngày 23/08 là buổi khảo sát thực địa nên không ép phải có commit. Tổng **14 commit nội dung**.

---

## Kiểm tra nhịp — chạy mỗi Chủ Nhật

```bash
git log -1 --format='%ar | %an'          # commit gần nhất cách đây bao lâu
git shortlog -sn --since='7 days ago'    # số commit mỗi người trong 7 ngày
```

Ai 0 commit trong tuần thì nhắn ngay trong nhóm chat, đừng đợi tới buổi họp.

---

## Không làm

- **Không nhờ người khác push hộ.** Phần của bạn phải do bạn bấm Commit — thầy chấm đúng chỗ đó.
- **Không commit thẳng lên `main`**, không squash khi merge.
- **Không đăng ảnh chưa che thông tin cá nhân** của khách hoặc nhân viên lên repo public.
- **Không ghi âm khi nhân viên không đồng ý.**
- **Không bịa số bấm giờ.** Bấm được bao nhiêu lượt ghi bấy nhiêu, `n = 6` là hợp lệ và trung thực hơn `n = 30` không có thật. Số nào không đo được thì đưa vào bảng giả định và ghi rõ "(ước lượng)".
