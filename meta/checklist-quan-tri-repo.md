# Checklist quản trị repo

**Phụ trách:** Mai Hoàng Hưng (24730099, chủ repo) — theo phân công ở
[P0-D-hung-revised.md](P0-D-hung-revised.md).

---

## 1. Việc làm một lần khi khởi tạo

| # | Việc | Trạng thái |
|---|---|---|
| 1 | Mời 3 collaborator quyền **Write**: `24730090`, `hongphuc0212`, `phucnguyen24730131` | ✅ Đã làm |
| 2 | Để repo **public** | ✅ Đã làm |
| 3 | Default branch là `main` | ✅ Đã đổi 21/08 (trước đó là `bai-tap-qua-trinh`) |
| 4 | Kiểm tra danh tính git commit đúng bốn tài khoản (mục 2, [P0-chung-quy-uoc-revised.md](P0-chung-quy-uoc-revised.md)) | ⏳ Từng người tự kiểm trước commit đầu |

## 2. Việc lặp lại hằng tuần — Chủ Nhật

```bash
git log -1 --format='%ar | %an'          # commit gần nhất cách đây bao lâu
git shortlog -sn --since='7 days ago'    # số commit mỗi người trong 7 ngày
```

- Ai 0 commit trong tuần → nhắn ngay trong nhóm chat, không đợi họp.
- Repo im lặng quá 3 ngày → nhắc cả nhóm.

## 3. Theo dõi PR và nhánh

- PR mở quá hạn merge ghi trong bảng nhánh ([P0-chung mục 4](P0-chung-quy-uoc-revised.md)) → nhắc người phụ trách và người duyệt.
- Nhánh tạo ra nhưng không có commit nội dung nào sau 1 tuần → hỏi lại người phụ trách trước khi coi là nhánh rác.
- Nhánh đã merge → không xóa ngay, giữ lại tới khi nộp bài để `git log --graph` còn nhìn được lịch sử merge commit.
- Nhánh không rõ nguồn gốc hoặc đã lỗi thời so với `main` (như `revert-4-model/bpmn-quan-ly-ho-tro` phát hiện ngày 21/08) → không tự xóa, báo cho người liên quan trước.

## 4. Không làm

- Không mời lại collaborator đã có quyền Write.
- Không đổi quyền của ai xuống thấp hơn Write mà không hỏi trước.
- Không tự ý xóa nhánh của người khác, kể cả nhánh trông như rác.
