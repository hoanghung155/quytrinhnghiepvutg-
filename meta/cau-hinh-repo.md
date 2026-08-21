# Cấu hình repo — nhật ký

**Người thực hiện:** Mai Hoàng Hưng (24730099, chủ repo) · **Ngày:** 21/08/2026

Ghi lại các thay đổi cấp quản trị đã thực hiện trên repo, để đối chiếu khi có ai hỏi vì
sao trạng thái repo khác với mô tả trong các file `meta/P0-*`.

## Thay đổi đã thực hiện ngày 21/08/2026

| Việc | Trước | Sau |
|---|---|---|
| Default branch | `bai-tap-qua-trinh` | `main` |
| Repo visibility | public | public (không đổi, đã public từ trước) |
| Collaborator quyền Write | `24730090`, `hongphuc0212`, `phucnguyen24730131` | không đổi, đã đủ 3 từ trước |

Lý do đổi default branch: checklist quản trị repo trong
[P0-D-hung-revised.md](P0-D-hung-revised.md) yêu cầu default branch là `main`, việc này
chỉ chủ repo mới đổi được nên bị trễ tới 21/08 mới làm.

## Ảnh hưởng cần các thành viên khác xử lý

Sau khi đổi default branch, ai đang có clone local trỏ theo `bai-tap-qua-trinh` cần chạy:

```bash
git branch -m bai-tap-qua-trinh main
git fetch origin
git branch -u origin/main main
git remote set-head origin -a
```

PR đang mở tại thời điểm đổi (21/08/2026): không có, nên không có PR nào bị retarget.

## Việc còn treo, chưa xử lý

- Nhánh `revert-4-model/bpmn-quan-ly-ho-tro` trên remote: tách ra sau PR #4, đang lùi lại
  19 commit so với `main` hiện tại. Có đúng 1 commit revert PR #4 (xóa mô hình BPMN M3 và
  S1). Chưa merge, chưa xóa — chờ xác nhận từ chủ repo trước khi xử lý.
