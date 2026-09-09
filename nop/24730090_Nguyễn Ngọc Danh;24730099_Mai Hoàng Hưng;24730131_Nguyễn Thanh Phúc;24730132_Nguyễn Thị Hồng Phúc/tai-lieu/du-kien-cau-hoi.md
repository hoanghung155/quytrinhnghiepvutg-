# Dự kiến câu hỏi và câu trả lời

79 câu. Phần lớn không phải nhóm ngồi đoán ra, mà là câu thầy Hà Lê Hoài Trung đã hỏi thật ở hai buổi
báo cáo mà nhóm mình ngồi nghe:

| Buổi | Ngày | Ba nhóm báo cáo | Bản bóc |
|---|---|---|---|
| Buổi 07 | 24/08/2026 | Điện Máy Xanh · ACFC · FPT Long Châu | [review/R8-nhan-xet-buoi-07.md](../review/R8-nhan-xet-buoi-07.md) |
| Buổi 09 | 07/09/2026 | Shopee · Hasaki · Highlands Coffee | [review/R16-buoi-bao-cao-07-09.md](../review/R16-buoi-bao-cao-07-09.md) |

Nhãn cuối mỗi câu cho biết nó từ đâu ra. `[24/08]` và `[07/09]` là thầy đã hỏi thật, `[dự phòng]` là
nhóm tự lường trước.

Phần chữ in nghiêng sau mỗi câu hỏi là **lời để nói ra**, viết theo giọng nói chứ không phải văn viết.
Đọc lướt cho quen miệng, đừng học thuộc từng chữ.

---

## 0. Sáu điều nhớ trước khi mở miệng

**Nói số, đừng nói chỗ.** Hai buổi vừa rồi, câu "cái đó em có trong báo cáo" và câu "thầy xem slide hai
mươi hai giúp em" đều bị bác. Thầy cần nghe con số. Nói "mười ba cổng" thì thầy tin, nói "thầy xem trang
bốn mươi" thì thầy không mở đâu.

**Chỉ vào hình, đừng kể ý đồ.** Bạn Huy nhóm Shopee giải thích rất hay về chuyện quá hai ngày thì kết
thúc, thầy nghe hết rồi nói đúng một câu: trên mô hình đó đâu có thể hiện quá hai ngày. Mở miệng an toàn
là "dạ ý đó em vẽ ở đây" rồi rê chuột vào. Mở miệng nguy hiểm là "dạ ý em là".

**Đừng bao giờ nói "trong báo cáo có, chỉ là không đưa lên slide".** Câu này bị bác ở cả hai buổi, một
lần với nhóm Long Châu và một lần với nhóm Highlands. Nếu slide thiếu thật thì nhận thiếu, rồi đọc số ra
miệng ngay tại chỗ, rồi nói sẽ bổ sung vào bản Word.

**Số giả định thì khai luôn là giả định.** Thầy không cấm giả lập. Thầy cấm giả lập mà không cho biết
tính ra kiểu gì. Nguyên văn hôm 24/08: giả lập là đúng rồi đó Khang à, nhưng trên slide mình mô tả giả
lập chỗ nào. Nói đủ ba mảnh là xong: con số, mã giả định, và phép tính ra nó.

**Nhận nhanh, đừng cãi dài.** Nhóm nào nhận ngay thì thầy chuyển câu trong vòng một phút. Nhóm nào giải
thích vòng vo thì bị truy sâu hơn rồi cuối cùng vẫn phải nhận.

**Chỗ chưa làm thì nói thẳng.** Nhóm chưa đi bấm giờ tại cửa hàng, không có con số nào đo bằng đồng hồ.
Tự nói ra trước còn hơn để thầy đào ra.

---

## 1. Bảng số phải thuộc

Ai thuộc bảng này thì trả lời được khoảng hai phần ba số câu bên dưới mà không cần mở file nào.

### 1.1 Sáu mô hình BPMN nộp

| Mã | Quy trình | Lớp | Pool | Lane | Hoạt động | Sub-process | Cổng | Luồng trình tự | Luồng thông điệp | Kết thúc |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| M2 | Quản lý nhà cung cấp và đặt hàng nhập | Quản lý | 2 | 4 | 12 | 1 | **10** | 30 | 3 | 3 |
| M3 | Kho tổng và điều chuyển hàng | Quản lý | 1 | 4 | 12 | 1 | **11** | 32 | 0 | 3 |
| C3 | Bán trả góp qua công ty tài chính | Cốt lõi | 3 | 4 | 10 | 1 | **15** | 39 | 6 | 3 |
| C4 | Bảo hành, đổi trả một đổi một | Cốt lõi | 4 | 3 | 12 | 1 | **12** | 35 | 9 | 2 |
| S1 | Tuyển dụng và đào tạo nhân viên bán hàng | Hỗ trợ | 2 | 4 | 12 | 0 | **12** | 36 | 6 | 4 |
| S4 | Đối soát công nợ và thanh toán NCC | Hỗ trợ | 2 | 4 | 9 | 1 | **10** | 27 | 4 | 2 |
| | **Tổng** | | **14** | **23** | **67** | **5** | **70** | **199** | **28** | **17** |

Loại cổng: M2 tám XOR và hai AND · M3 mười một XOR · C3 mười hai XOR, hai AND, một cổng dựa trên sự kiện ·
C4 mười hai XOR · S1 chín XOR, hai AND, một cổng dựa trên sự kiện · S4 mười XOR. Cả bộ không có cổng OR.

### 1.2 Bốn con số ký pháp

- **0 vi phạm** luật một vào một ra, đếm trên **113 hoạt động** của mười một file mô hình.
- **17 trên 17** sự kiện kết thúc của sáu mô hình nộp đều có nhãn. Tính cả năm hình chi tiết sub-process
  là **22 trên 22**.
- **6 cặp cổng AND**, cặp nào cũng đủ mở và đóng. Ba cặp thấy được trên mô hình nộp là M2 `G8`-`G9`,
  C3 `G3`-`G4` và một cặp trong S1. Ba cặp còn lại nằm trong hình chi tiết của C4a, M3a, S4a.
- **0 luồng trình tự** cắt qua ranh giới pool. Qua pool là nét đứt hết.

### 1.3 Phương pháp

28 nguồn công khai mã hóa thành 14 chủ đề · 120 câu hỏi phỏng vấn, tức 20 câu cho mỗi quy trình được mô
hình hóa, mỗi bộ 10 định tính và 10 định lượng, mỗi loại 5 câu có cấu trúc và 5 câu không · **60 trên 60**
câu có cấu trúc đều kèm bốn phương án A, B, C, D · biểu mẫu biên bản 7 mục · kịch bản hội thảo 90 phút ·
3 biên bản đã lập · 4 biểu mẫu tự dựng.

### 1.4 Phân tích

| | C3 Bán trả góp | C4 Bảo hành, đổi trả |
|---|---|---|
| Cycle time | **138 phút** | **5.958,9 phút** |
| Processing time | **68 phút** | **188,9 phút** |
| CTE | **49,3%** | **3,17%** |
| Số hoạt động được phân loại | 14 | 15 |
| Số bước sau khi phân rã | 36 | 40 |
| VA / BVA / NVA đếm theo bước | 7 (19,4%) · 19 (52,8%) · 10 (27,8%) | 5 (12,5%) · 24 (60,0%) · 11 (27,5%) |
| VA / BVA / NVA đếm theo hoạt động | 4 (28,6%) · 7 (50,0%) · 3 (21,4%) | 5 (33,3%) · 7 (46,7%) · 3 (20,0%) |

Hai quãng chờ lớn nhất của C4 là **1.920 phút** chờ tới lượt thẩm định và **2.880 phút** chờ tới lượt sửa.
Mười một bước NVA của C4 nuốt **96,8%** cycle time, và bảy trong số đó nằm gọn trong ba hoạt động liền nhau. Bỏ hẳn vận chuyển mà giữ hàng đợi thì cycle time chỉ giảm
**17,7%**, còn giữ vận chuyển mà xóa hàng đợi thì giảm **82,0%**.

### 1.5 Xác suất từng điểm rẽ

| Cổng | Mã | Phân bố |
|---|---|---|
| C3 `G1` đủ điều kiện sơ bộ | `GT20` | 85 / 15 |
| C3 `G2` hình thức trả góp | `GT21` | 80 qua công ty tài chính / 20 qua thẻ tín dụng |
| C3 bốn kịch bản kết cục | `GT22` | duyệt thẳng 45 · duyệt có điều kiện 20 · bổ sung giấy tờ 20 · từ chối 15 |
| C3 `G9` thu khoản trả trước | `GT23` | 97 / 3 |
| C3 `G10` nhận máy | `GT24` | 85 nhận ngay / 15 hẹn nhận sau |
| C4 `G1` hộp và phụ kiện | `GT25` | 70 đủ / 30 thiếu |
| C4 `G3` kết luận thẩm định | `GT26` | 75 do nhà sản xuất / 25 do người dùng |
| C4 `G4` mốc tháng đầu | `GT30` | 20 còn trong tháng đầu / 80 từ tháng thứ hai |
| C4 `G6` phương án khách chọn | `GT27` | đổi máy 30 · trả hàng 10 · sửa chữa 60 |
| C4 `G7` tồn kho hàng đổi | `GT28` | 70 còn hàng / 30 đã hết |
| C4 `G9` cam kết 15 ngày | `GT29` | 80 đúng hạn / 20 trễ hạn |
| C3 `G7` khách chấp nhận điều kiện vay mới | `GT42` | 100 chấp nhận / 0 không chấp nhận |
| C4 `G8` chấp nhận model tương đương | `GT43` | 100 chấp nhận / 0 chuyển sang hoàn tiền |

Bốn nhánh kết cục của C4 ghép từ `GT26` với `GT27`: từ chối **25,0%** · đổi máy **22,5%** · trả hàng và
hoàn tiền **7,5%** · sửa chữa **45,0%**.

`GT42` và `GT43` là hai tỷ lệ tách ra sau buổi 07/09. Chúng không phải số mới: đó là tỷ lệ mà
Bảng 4.9 và Bảng 4.11 vẫn luôn dùng nhưng chưa viết ra, nay ghi tường minh để mọi nhánh cổng
trên hình tra ngược được về đúng một mã. Vì cả hai bằng 100 / 0 nên không con số kết quả nào đổi.

### 1.6 Doanh nghiệp

Doanh thu thuần MWG 2025 là **156.166 tỷ đồng**, riêng chuỗi thegioididong.com và TopZone khoảng
**37.300 tỷ** · **1.012** cửa hàng · **hơn 74.000** nhân viên toàn hệ thống, khối hành chính nhân sự
khoảng **200 người**, thành tỷ lệ một nhân sự trên khoảng **370** nhân viên · ERP tự viết xong cuối
**2004**, chạy từ đầu **2005** · năm 2025 giảm khoảng **100** điểm bán mà doanh thu cửa hàng hiện hữu vẫn
tăng **trên 20%**.

### 1.7 Luật chấm thầy đã chốt

Slide **20 tới 30%**, báo cáo Word **70 tới 80%** · slide chấm ngay tại chỗ, chấm xong là chốt · sau buổi
có **một tuần** sửa báo cáo, hạn nộp **15 giờ 30 Chủ nhật** · nộp **hai nơi** là Google Drive và
E-learning · sai ký pháp trừ **0,25** mỗi lỗi · thang độ phức tạp: trên 7 cổng được **1,0**, trên 5 được
**0,75**, trên 3 được **0,5** · bộ câu hỏi: dưới 10 câu **0đ**, 10 tới 20 câu **0,25đ**, từ 20 câu
**0,5đ**, và tính cho **từng quy trình được mô hình hóa** chứ không phải cho cả bài.

---

## 2. Tiêu chí 1 - Kiến trúc và hồ sơ quy trình

**Q01 · "Trong rubric thầy ghi là tác nhân, mô tả các bước, khách hàng của quy trình và các kết quả có
thể xảy ra. Thầy chưa thấy mình liệt kê trên slide."** `[24/08 · nhóm Điện Máy Xanh]`

*Dạ bốn phần đó nhóm em làm cho cả mười hai quy trình luôn ạ, còn ba quy trình đem lên slide hôm nay thì
em in riêng thành một thẻ. Thầy nhìn M2 giúp em: hồ sơ kê bảy tác nhân, trên hình em vẽ ra năm vai. Khách
hàng của quy trình là Kho tổng và mạng lưới cửa hàng. Ba kết quả có thể xảy ra là đơn bị từ chối, lô hàng
bị trả lại, và hàng vào tồn khả dụng. Năm bước lớn thì chạy từ tính lượng cần đặt cho tới lúc chuyển bộ
chứng từ sang S4.*

**Q02 · "Mình liệt kê được bao nhiêu quy trình, chia làm mấy lớp?"** `[dự phòng]`

*Dạ mười hai quy trình ạ, chia bốn bốn bốn. Bốn quản lý là M1 tới M4, bốn cốt lõi là C1 tới C4, bốn hỗ
trợ là S1 tới S4. Rubric đòi tối thiểu mười quy trình và mỗi lớp ít nhất ba, nhóm em để dư một cái mỗi
lớp cho chắc.*

**Q03 · "Sáu quy trình mình mô hình hóa là chọn thế nào?"** `[dự phòng]`

*Dạ em chọn đúng hai cái mỗi lớp ạ. Quản lý thì M2 với M3, cốt lõi thì C3 với C4, hỗ trợ thì S1 với S4.
Nhóm em cố tình không lấy ba cái cùng một lớp cho dễ vẽ, tại rubric ghi rõ là hai mỗi lớp.*

**Q04 · "Khách hàng của quy trình này là ai?"** `[24/08 · nhóm Long Châu]`

*Dạ M2 thì là Kho tổng với mạng lưới cửa hàng, tức là bên nhận hàng vào tồn để bán, khách hàng nội bộ.
C4 thì là khách đã mua máy và giờ cần bảo hành hoặc đổi trả, khách bên ngoài. S1 thì là cửa hàng đang
thiếu người, cũng là nội bộ ạ.*

**Q05 · "Khách hàng của quy trình có phải là một tác nhân không? Thầy thấy hai quy trình khác của nhóm
kia thì khách hàng không phải tác nhân."** `[24/08 · nhóm Long Châu]`

*Dạ phải ạ, và cả sáu quy trình của nhóm em đều giữ đúng chỗ đó. Khách hàng của quy trình lúc nào cũng là
một vai đã có mặt trên hình rồi, chứ em không kéo thêm ai từ ngoài vào. Như C4 thì Khách hàng là hẳn một
pool riêng, có tám luồng thông điệp nối qua. Còn M2 thì Kho tổng là một lane thật, có ba hoạt động trong
đó.*

**Q06 · "Số tác nhân mình mô tả và số vai mình vẽ có khớp nhau không?"** `[24/08 và 07/09, cả bốn nhóm]`

Chỗ này nói trước, đừng đợi thầy hỏi.

*Dạ em xin khai luôn hai con số cho thầy dễ đối chiếu. Hồ sơ M2 ở Chương một em kê bảy tác nhân, còn trên
mô hình em vẽ ra năm vai, gồm bốn lane cộng thêm pool Nhà cung cấp. Hai tác nhân không có vai riêng thì
em xin nói rõ. Một là Cấp duyệt ngân sách, em để chung lane với Ban ngành hàng, tại trên quy trình này
hai vai đó chỉ gặp nhau ở đúng một điểm quyết định và cùng ký một phiếu. Hai là Hệ thống ERP nội bộ, cái
này em không tách lane vì nó đụng vào gần như mọi bước, tách ra thì luồng nào cũng phải cắt qua lane đó,
nhìn không đọc nổi.*

**Q07 · "Sao gộp hai phòng vào một lane?"** `[24/08 · nhóm ACFC]`

*Dạ tại trên M2, Ban ngành hàng với Cấp duyệt ngân sách chỉ đụng nhau ở đúng cổng `G4` thôi ạ, mà hai bên
lại cùng ký trên một phiếu duyệt. Nếu thầy muốn tách ra thì nhóm em tách được, hình chỉ dài thêm một
lane.*

Tuyệt đối không nói "để vậy cho nó gọn". Đó đúng là câu bạn Bảo nói hôm 24/08 và bị trừ điểm ngay.

**Q08 · "Nếu gộp thì phải vẽ một lane lớn rồi ba lane con ở trong chứ."** `[24/08 · nhóm Long Châu]`

*Dạ nhóm em không gộp kiểu đó ạ. Chỗ duy nhất một lane gánh hai vai là M2, mà hai vai đó cùng một cấp phê
duyệt chứ không phải ba phòng ban khác nhau, nên em thấy chưa cần lane lồng.*

---

## 3. Tiêu chí 2 - Ký pháp BPMN

Đây là chỗ mất điểm nặng nhất ở cả hai buổi, và cũng là chỗ nhóm mình chắc tay nhất. Cứ đọc số ra.

**Q09 · "Mỗi hoạt động chỉ có một luồng vào một luồng ra thôi, không có một vào hai ra."**
`[24/08 và 07/09, ba nhóm dính]`

*Dạ chỗ này nhóm em không sai ạ. Em có chạy chốt đếm lại hết, một trăm mười ba hoạt động trên mười một
file mô hình, không có cái nào một vào hai ra. Chỗ nào cần rẽ nhánh thì em mở cổng, mà mở cổng nào là em
đóng cổng đó.*

**Q10 · "Lý do bị lỗi đó là mở cổng ra mà không soi lại. Nhóm em có chốt gì cho chuyện này không?"**
`[24/08]`

*Dạ có ạ, mà là chốt chạy tự động chứ em không soi bằng mắt. Bộ dựng mô hình của nhóm có một phép kiểm
chạy mỗi lần sinh hình, nó đếm số luồng vào ra của từng hoạt động, đếm cặp cổng mở và đóng, rồi dò xem có
luồng trình tự nào cắt qua ranh giới pool không. Sai một chỗ là nó báo lỗi và không cho ra hình luôn.*

**Q11 · "Mô hình này có bao nhiêu cổng điều kiện?"** `[24/08 và 07/09]`

*Dạ M2 mười cổng, M3 mười một, C3 mười ba, C4 mười hai, S1 mười hai, S4 mười ạ. Sáu cái cộng lại là sáu
mươi tám. Cái thấp nhất của nhóm em là mười, vẫn nằm trên mốc bảy của thang chấm.*

**Q12 · "Ba cổng thì trên rubric mình được bao nhiêu điểm tối đa?"** `[24/08 · nhóm ACFC]`

*Dạ thang là trên bảy cổng được một điểm, trên năm được không phẩy bảy lăm, trên ba được không phẩy năm.
Nhóm em thấp nhất là mười cổng nên cả sáu mô hình đều nằm ở mức một điểm. Lúc vẽ em cũng có nghĩ tới
chuyện rút bớt cổng cho hình gọn, nhưng đọc lại rubric thì thấy rubric chấm bằng số cổng nên em giữ
nguyên.*

**Q13 · "Nhóm em dùng những loại cổng nào?"** `[dự phòng]`

*Dạ ba loại ạ. XOR là chính, sáu mươi cổng. AND thì sáu cổng, ghép thành ba cặp trên mô hình nộp. Còn
cổng dựa trên sự kiện thì em dùng đúng hai chỗ, là `G5` của C3 và `G4` của S1. Cổng OR thì cả bộ không có
cái nào.*

**Q14 · "Cổng AND của em nằm ở đâu, có đóng lại không?"** `[24/08 · nhóm Shopee dính lỗi này]`

*Dạ ba cặp thầy nhìn thấy được trên mô hình nộp. Cặp `G8` với `G9` ở khâu nhận hàng của M2, chỗ đó là Kho
tổng bố trí mặt bằng song song với Kế toán công nợ chuẩn bị chứng từ. Cặp `G3` với `G4` của C3. Và một
cặp nữa trong S1. Ba cặp còn lại thì nằm trong hình chi tiết của C4a, M3a với S4a. Cặp nào cũng có mở có
đóng, không có nhánh nào của cặp AND chạy thẳng vào sự kiện kết thúc. Riêng hình khung của C4 thì không
có cổng AND nào ạ.*

**Q15 · "Đang thực hiện song song mà một nhánh kết thúc trước thì nhánh kia thế nào?"**
`[07/09 · nhóm Shopee]`

*Dạ bộ này không rơi vào trường hợp đó ạ, tại cặp AND nào em cũng đóng lại bằng cổng AND hội tụ trước khi
đi tới sự kiện kết thúc. Đúng như thầy nói, hai việc chạy song song thì phải đồng bộ lại rồi mới đi
tiếp.*

**Q16 · "Cổng này hỏi cái gì? Cổng XOR là cần nhãn, các đầu ra cũng phải có nhãn."**
`[07/09 · nhóm Hasaki]`

*Dạ câu hỏi của từng cổng em có ghi đủ trong bảng đặc tả ở Chương hai ạ. Ví dụ `G1` của M2 là nhà cung cấp
đã có trong danh mục được duyệt hay chưa, còn `G3` là giá trị đơn có vượt hạn mức phê duyệt của Trưởng
thu mua không. Trên hình thì em gán nhãn cho từng nhánh ra chứ chưa gán lên hình thoi, tại slide chương
ba trang ba mươi hai và năm mươi hai của thầy để trống hình thoi nên em làm theo. Nếu thầy muốn nhãn nằm
luôn trên cổng thì em bổ sung được ngay, chữ có sẵn hết rồi. Còn cổng AND với cổng hội tụ thì em để
trống.*

**Q17 · "Nhánh ra của cổng có nhãn đủ không?"** `[07/09]`

*Dạ đủ ạ. Thầy nhìn C3 giúp em, `G1` có Đủ điều kiện với Không đủ điều kiện, `G6` có Duyệt, Duyệt có điều
kiện và Từ chối, `G12` có Đủ chứng từ với Thiếu chứng từ. Chỉ có hai chỗ nhánh không mang nhãn thôi, là
hai cổng dựa trên sự kiện. Ở đó nhãn nằm trên chính cái sự kiện bắt được chứ không nằm trên nhánh, cái
này là đúng chuẩn BPMN hai chấm không ạ.*

**Q18 · "Cổng dựa trên sự kiện là gì, giáo trình có nói không?"** `[dự phòng]`

*Dạ tài liệu môn mình chương ba trang bốn mươi bốn chỉ giới thiệu XOR, AND với OR thôi, không có cổng dựa
trên sự kiện. Em vẫn dùng nó ở đúng hai chỗ vì hai chỗ đó vẽ bằng XOR là sai bản chất. Như `G5` của C3,
lúc token tới thì chưa ai biết gì hết, nhánh nào chạy là do kết quả thẩm định về trước hay đồng hồ hạn
giữ máy hết trước. Không có ai ngồi cân nhắc để chọn cả. Vẽ thành XOR là em dựng ra một cái quyết định
không tồn tại. Ký pháp này có trong giáo trình Dumas mà slide bài giảng dựa vào nên em không tự đặt ra.
Nó không có cổng đóng tương ứng, cái đó cũng đúng chuẩn, và em có ghi rõ trong bảng ghép cổng ở Chương
hai để thầy khỏi đọc thành lỗi mở mà không đóng.*

**Q19 · "Chỗ này có vòng lặp. Rơi vào đó thì thoát ra bằng cách nào?"** `[07/09 · Hasaki và Highlands]`

*Dạ cả bộ có đúng một vòng lặp thôi ạ, nằm ở C3. Nhánh Thiếu chứng từ của `G12` quay ngược về `G13`, chạy
lại `T4` rồi chờ thẩm định thêm một vòng. Lối thoát thì nằm ngay trong vòng luôn, ở cổng dựa trên sự kiện
`G5`. Một nhánh là kết quả thẩm định về, nhánh còn lại là sự kiện thời gian, tên nó là Hết thời hạn giữ
máy chờ hồ sơ, em đặt hạn một ngày theo giả định `GT16`. Hết hạn là quy trình rẽ sang hủy đơn và giải
phóng máy về tồn bán, kết thúc ở `E3`. Em cũng ghi chú thêm giới hạn tối đa hai lượt bổ sung ngay cạnh
`G12`. Năm mô hình còn lại thì không có vòng nào.*

**Q20 · "Rơi vào vòng lặp thì thời gian đánh giá quy trình nó rất lớn."** `[07/09]`

*Dạ đúng ạ, và cái đó nhóm em có đo chứ không bỏ qua. Vòng lặp của C3 chỉ dính hai mươi phần trăm số hồ
sơ theo `GT22`, nhưng nó đẻ ra sáu mươi phẩy bảy phần trăm toàn bộ thời gian chờ của quy trình. Mỗi lượt
quay lui mất mười lăm phút chạy lại `T4`, cộng một vòng chờ thẩm định, cộng bốn trăm tám mươi phút khách
về lấy giấy tờ. Tính ra tiền thì chi phí làm lại là ba nghìn một trăm hai lăm đồng một ca, bằng bốn phẩy
tám phần trăm chi phí nhân công một ca.*

**Q21 · "Cách chặn vòng lặp thì dân lập trình biết rồi, giới hạn số lần lặp."** `[07/09]`

*Dạ nhóm em chặn bằng hai cách ạ. Một là giới hạn thời gian, dùng sự kiện thời gian trên cổng dựa trên sự
kiện. Hai là ghi chú giới hạn hai lượt bổ sung. Em không vẽ bộ đếm thành phần tử BPMN vì BPMN không có ký
pháp cho bộ đếm, nhét vào là em tự chế ký hiệu, sợ bị trừ.*

**Q22 · "Số kết quả mô tả và số sự kiện kết thúc vẽ ra có khớp nhau không?"** `[24/08 · nhóm ACFC]`

*Dạ khớp từng mô hình một ạ. M2 ba kết quả thì ba sự kiện kết thúc, M3 ba với ba, C3 ba với ba, C4 hai với
hai, S1 bốn với bốn, S4 hai với hai. Cộng lại là mười bảy trên mười bảy, và mười bảy cái đó đều có nhãn,
không có cái nào em để trống.*

**Q23 · "Đọc thử tên các sự kiện kết thúc của một mô hình."** `[24/08]`

*Dạ C4 có hai cái. Một là Yêu cầu đã bị từ chối, khách đã nhận báo giá sửa chữa có phí. Hai là Yêu cầu đã
xử lý xong và máy lỗi đã được thu hồi. Còn S1 thì bốn cái: đề nghị đã bị từ chối, đợt tuyển đã đóng, nhân
viên đã vào làm chính thức, và đã dừng thử việc. Em đặt tên theo dạng trạng thái kết thúc chứ không đặt
bằng động từ.*

**Q24 · "Sao giữa hai pool em nối bằng nét liền? Nét đứt là truyền thông điệp, cách bọn nhau mà."**
`[24/08 · nhóm ACFC]`

*Dạ chỗ này nhóm em sạch ạ, không có luồng trình tự nào cắt qua ranh giới pool hết. Qua pool là nét đứt
hết. C4 có tám luồng thông điệp, S1 sáu, C3 sáu, S4 bốn, M2 ba. Cái này nằm trong chốt tự động chạy trước
khi xuất hình nên em không sót được.*

**Q25 · "Trong cùng một pool mà em cũng dùng nét đứt à?"** `[24/08 · nhóm ACFC]`

*Dạ không ạ. Trong cùng pool em dùng luồng trình tự nét liền, sáu mô hình cộng lại là một trăm chín mươi
sáu luồng. Nét đứt em chỉ dùng khi phải cắt qua ranh giới pool.*

**Q26 · "Ba mô hình của nhóm nhìn giống hệt nhau, chỉ khác tên hoạt động thôi. Cái này rất là nghi ngờ."**
`[07/09 · nhóm Shopee]`

*Dạ sáu mô hình của nhóm em lệch nhau ở mọi cột luôn ạ. Pool từ một tới bốn, lane từ ba tới bốn, hoạt
động từ chín tới mười hai, cổng từ mười tới mười ba, luồng thông điệp từ không tới tám. Loại cổng cũng
khác nhau, có cái dùng AND có cái không, hai cái có cổng dựa trên sự kiện. Sáu file nguồn em để công khai
trên kho GitHub của nhóm, thầy mở ra đối chiếu được ạ.*

**Q27 · "Hộp có dấu cộng này là gì?"** `[dự phòng]`

*Dạ là sub-process thu gọn ạ. Em dùng ở đúng năm chỗ, mỗi chỗ có một hình chi tiết riêng vẽ đầy đủ bên
trong. Em gói lại để hình khung giữ được dưới ba mươi phần tử theo hướng dẫn 7PMG, chứ không phải để
giấu bước.*

**Q28 · "Mô hình này có bao nhiêu hoạt động?"** `[24/08 và 07/09]`

*Dạ nếu đếm cả hộp sub-process thì M2 mười ba, M3 mười ba, C3 mười một, C4 mười ba, S1 mười hai, S4 mười.
Còn nếu chỉ đếm hộp task thì năm cái có sub-process trừ đi một, riêng S1 không có sub-process nên hai cách
đếm bằng nhau ạ.*

Nói cả hai cách để con số của mình không lệch với con số thầy tự đếm trên hình.

**Q29 · "Đường này nối đi đâu? Thầy nhìn không ra."** `[24/08 và 07/09]`

*Dạ để em chỉ, đường này đi từ đây qua đây ạ.* (Rê chuột, đọc tên hai đầu.) *Còn nếu thầy chỉ đúng chỗ
đường bị chồng thì em xin nhận. Mỗi mô hình trong báo cáo em để trọn một trang ngang nên in ra vẫn đọc
được, nhưng chốt của nhóm đang báo còn bảy chỗ đường chạy đè lên hộp, em sẽ dọn hết trong bản Word cuối.*

**Q30 · "Mô tả bằng lời và mô hình có khớp nhau không?"** `[dự phòng]`

*Dạ khớp ạ. Bước lớn nào trong mô tả cũng có hoạt động tương ứng trên hình, và ngược lại trên hình em
không vẽ thêm bước nào ngoài mô tả. Chương hai của em có bảng đặc tả liệt kê từng phần tử kèm cột nối
tới, thầy dò ngược lại được.*

**Q31 · "Sự kiện bắt đầu của quy trình này là gì?"** `[dự phòng]`

*Dạ M2 là Nhu cầu đặt hàng đã chốt. C4 là Khách đã mang máy lỗi và hóa đơn tới cửa hàng. S1 là Nhu cầu
nhân sự đã phát sinh. Mô hình nào cũng đúng một sự kiện bắt đầu ạ.*

**Q32 · "Mốc thời gian trong quy trình em thể hiện thế nào?"**
`[07/09 · thầy bác nhóm Shopee ở đúng chỗ này]`

*Dạ em dùng sự kiện thời gian chứ không viết thời hạn thành tên hoạt động ạ. C3 có `IE2` là Hết thời hạn
giữ máy chờ hồ sơ. C4 thì mốc tháng đầu em vẽ thành cổng điều kiện `G4` chứ không nhét vào một cái hộp
task. S1 thì hạn phản hồi của ứng viên nằm trên cổng dựa trên sự kiện `G4`.*

---

## 4. Tiêu chí 3 - Phương pháp thực hiện

**Q33 · "Thầy thấy mình toàn câu hỏi không cấu trúc, mình không có đặt câu hỏi có cấu trúc hả?"**
`[24/08 · nhóm Điện Máy Xanh]`

*Dạ có ạ, mà đúng một nửa. Trong một trăm hai mươi câu thì sáu mươi câu có cấu trúc và sáu mươi câu
không. Mỗi quy trình em soạn hai mươi câu, chia ra năm câu định tính có cấu trúc, năm câu định tính không,
rồi năm định lượng có cấu trúc và năm định lượng không.*

**Q34 · "Câu có cấu trúc thì phải cho thầy đáp án chứ, cái này giống bộ câu hỏi trắc nghiệm."**
`[07/09 · nhóm Shopee]`

*Dạ sáu mươi câu có cấu trúc của em đều kèm bốn phương án hết ạ. Em đọc thử một câu cho thầy nghe: hồ sơ
trả góp bị từ chối thì bước tiếp theo là gì, A là giới thiệu công ty tài chính khác, B là đề xuất tăng
trả trước, C là chuyển sang thanh toán thẳng, D là đóng yêu cầu.*

**Q35 · "Thang một tới năm mà không có A B C D thì làm sao biết?"** `[07/09 · nhóm Shopee]`

*Dạ câu định lượng có cấu trúc của em thì cho sẵn các khoảng giá trị, khoảng nào cũng liền nhau và không
chồng lấn. Ví dụ câu M2-Q14: thời gian kiểm đếm và quét IMEI một lô hàng, A là dưới một giờ, B là một tới
ba giờ, C là ba tới tám giờ, D là trên tám giờ.*

**Q36 · "Hai loại câu hỏi đó dùng cho hai ngữ cảnh khác nhau, em hiểu chưa?"** `[24/08]`

*Dạ em hiểu ạ. Câu không cấu trúc là để hiểu sâu hơn về quy trình, hỏi mở cho người ta kể ra. Còn câu có
cấu trúc là để xác nhận lại xem cách hiểu của nhóm về quy trình có đúng không, nên phải có phương án cho
người ta chọn. Bộ câu hỏi của em chia đúng theo hai mục đích đó, và mỗi câu em còn để thêm cột hỏi ai và
làm rõ bước nào.*

**Q37 · "Bộ câu hỏi bao nhiêu câu, tính cho cả báo cáo hay từng quy trình?"** `[dự phòng]`

*Dạ tính cho từng quy trình được mô hình hóa ạ, đúng như thầy nói ở buổi sáu ngày mười tháng tám. Mỗi quy
trình hai mươi câu, sáu quy trình thành một trăm hai mươi câu. Ngưỡng của rubric là từ hai mươi câu mới
được không phẩy năm điểm nên bộ nào của em cũng vừa đúng ngưỡng.*

**Q38 · "Nhóm em phỏng vấn ai, kết quả thế nào?"** `[dự phòng]`

*Dạ chỗ này em xin nói thật là nhóm chưa tổ chức được buổi phỏng vấn tại cửa hàng ạ. Cái em làm được là
dựng đủ bộ công cụ: một trăm hai mươi câu hỏi chia theo sáu quy trình, biểu mẫu biên bản bảy mục, kịch
bản hội thảo chín mươi phút, và ba câu hỏi mồi để phá bế tắc khi buổi chững lại. Mục phương pháp của
rubric yêu cầu công cụ, còn số liệu nào thuộc phạm vi em chưa khảo sát được thì em đánh dấu là ước lượng
hết.*

**Q39 · "Bằng chứng của nhóm gồm những gì?"** `[24/08 · thầy hỏi nhóm Long Châu]`

*Dạ sáu loại ạ. Trang chính sách bảo hành, đổi trả và trả góp thì em lưu bản chụp. Sơ đồ tổ chức thì có
sơ đồ MWG và sơ đồ một cửa hàng. Rồi bảng thuật ngữ dùng thống nhất toàn báo cáo. Bốn biểu mẫu em tự dựng
lại gồm đơn đặt hàng, phiếu điều chuyển và biên bản kiểm kê. Hai mươi tám nguồn công khai em đọc và mã
hóa thành mười bốn chủ đề. Với ba biên bản buổi làm việc của nhóm, lập theo đúng biểu mẫu bảy mục.*

**Q40 · "Mười bốn chủ đề đó dùng làm gì?"** `[dự phòng]`

*Dạ nó là đầu vào của biểu đồ Pareto ở phần phân tích ạ. Em cố ý nối hai phần đó lại chứ không để rời:
ba mươi bốn lượt nhắc trong hai mươi tám nguồn được mã hóa thành chín chủ đề cho C4, rồi từ đó mới xếp
thành Pareto.*

**Q41 · "Biểu mẫu biên bản của nhóm có mấy mục?"** `[dự phòng]`

*Dạ bảy mục ạ: ngày giờ địa điểm, quy trình đưa ra bàn, danh sách người tham dự và vai trò, người chủ trì
và thư ký, danh sách câu hỏi chuẩn bị trước, nội dung thảo luận và điểm chốt được, cuối cùng là việc còn
treo và ai chịu trách nhiệm. Nhóm em đã lập ba biên bản theo đúng bảy mục này.*

**Q42 · "Kịch bản hội thảo dài bao lâu, chia thế nào?"** `[dự phòng]`

*Dạ chín mươi phút ạ. Mười phút thống nhất phạm vi, hai mươi lăm phút dựng luồng chính lên bảng, hai mươi
lăm phút truy các nhánh ngoại lệ, hai mươi phút chốt tác nhân và các kết quả, mười phút cuối điểm lại và
giao việc.*

---

## 5. Tiêu chí 4 - Phân tích định tính

**Q43 · "Phân tích quy trình có mấy bước? Hai bước. Bước đầu là kẻ hình, bước hai mới là kẻ bảng."**
`[24/08 với cả ba nhóm, 07/09 với cả ba nhóm]`

Câu này thầy hỏi nhiều nhất. Sáu nhóm đều dính.

*Dạ nhóm em có đủ hai bước, và làm cho cả hai quy trình luôn ạ. Bước một là em chú phân loại VA, BVA, NVA
thẳng lên từng hoạt động trên mô hình, ra bốn hình chú cho C3, C3a, C4 và C4a. Xong bước hai mới lập
bảng.*

**Q44 · "Mình mới có bảng biểu, mình vẽ chưa có, mình mới có 50%."** `[07/09 · nhóm Hasaki]`

Nếu hình chú đang có trên slide thì mở ra chỉ luôn. Nếu không có thì:

*Dạ em xin nhận là slide đang thiếu hình đó ạ. Nhưng phần vẽ thì nhóm em có làm, trong bản Word có đủ bốn
hình chú phân loại giá trị, bốn hình chú thời gian và bốn hình chú chi phí. Em xin bổ sung lên slide
trong bản cuối.*

**Q45 · "Bảng phân tích của em có mấy cột?"** `[07/09 · nhóm Highlands bị nhắc]`

*Dạ bảng em có số thứ tự, tên hoạt động, người thực hiện, phân loại thuộc nhóm nào, rồi cột khắc phục ạ.
Cấu trúc chung là liệt kê rồi mô tả rồi khắc phục, theo đúng cụm mà rubric lặp lại bốn lần.*

**Q46 · "Quy trình mình tới mười mấy hai mươi hoạt động mà mình phân tích ba cái, số còn lại đi về đâu?"**
`[24/08 · nhóm ACFC, câu nặng nhất của tiêu chí 4]`

*Dạ bảng của em phủ hết chứ không chọn vài dòng tiêu biểu ạ. Bảng C3 có mười tám dòng, trong đó mười bốn
dòng được phân loại. Bảng C4 cũng mười tám dòng, mười lăm dòng được phân loại. Chỗ chênh là do em có đưa
sự kiện bắt đầu và kết thúc vào bảng nhưng đánh dấu là mốc, không tính vào tỷ lệ. Còn cổng thì em không
đưa vào bảng, tại cổng là điểm quyết định chứ không tiêu tốn công việc. Quy ước đó em ghi ngay đầu mục
phân tích.*

**Q47 · "Tỷ lệ VA, BVA, NVA của mình là bao nhiêu?"** `[dự phòng]`

*Dạ C3 thì bốn bước VA chiếm hai tám phẩy sáu phần trăm, bảy bước BVA chiếm năm mươi phần trăm, ba bước
NVA chiếm hai mốt phẩy bốn. C4 thì năm VA là ba ba phẩy ba, bảy BVA là bốn sáu phẩy bảy, ba NVA là hai
mươi phần trăm ạ.*

**Q48 · "Vì sao bước này em xếp NVA mà không phải BVA?"** `[dự phòng]`

*Dạ nhóm em có ba nguyên tắc thận trọng ghi ở đầu mục phân tích, nguyên tắc đầu tiên là không gọi mọi
bước kiểm tra là lãng phí. Việc thẩm định của công ty tài chính và của Trung tâm Bảo hành em xếp BVA, tại
nó chặn rủi ro tín dụng với chặn gian lận bảo hành. Với lại hai chỗ đó nằm trong pool hộp đen nên không
phải bước của quy trình cửa hàng. Cái em xếp vào lãng phí thì chỉ có quãng chờ kết luận với việc lặp lại
một thao tác đã làm ở quầy thôi ạ.*

**Q49 · "Các bước NVA đó nặng tới mức nào?"** `[dự phòng]`

*Dạ nếu đếm theo số bước thì tỷ lệ NVA của hai quy trình gần bằng nhau, hai bảy phẩy tám với hai bảy
phẩy năm phần trăm. Nhưng các bước NVA của C4 nuốt chín sáu phẩy tám phần trăm cycle time. Mà bảy trong
số đó lại nằm gọn trong ba hoạt động liền nhau chứ không rải đều khắp quy trình. Chính chỗ này làm nhóm
em không dừng ở định tính mà đo tiếp bằng số ạ.*

**Q50 · "Phân tích lãng phí của em theo nhóm nào?"** `[dự phòng]`

*Dạ ba nhóm Move, Hold, Overdo như rubric đòi ạ. Em có ánh xạ ngược về bảy lãng phí của Ohno: Move là vận
chuyển thừa với thao tác thừa, Hold là tồn kho với chờ đợi, Overdo là lỗi, xử lý thừa và sản xuất thừa.
Dòng nào trong bảng cũng có cột khắc phục đi kèm.*

**Q51 · "Mình có dùng Pareto, why-why hay xương cá không? Thầy chưa thấy luôn."**
`[24/08 · Điện Máy Xanh và ACFC, 07/09 · Shopee]`

*Dạ rubric cho chọn một trong ba, nhưng nhóm em làm cả ba để phủ cho cả hai quy trình ạ. Hai biểu đồ
Pareto cho C3 với C4, một biểu đồ xương cá sáu nhánh cho C4, và một sơ đồ why-why cho C3.*

**Q52 · "Dữ liệu của biểu đồ Pareto này ở đâu ra?"** `[24/08 · nhóm ACFC, thầy truy rất kỹ]`

*Dạ Pareto của C4 em đếm ba mươi bốn lượt nhắc trên hai mươi tám nguồn công khai, rồi mã hóa thành chín
chủ đề. Đơn vị đếm là số URL phân biệt có nhắc tới chủ đề đó, không phải số ca và cũng không phải tỷ lệ
của doanh nghiệp, cái này em ghi rõ ngay dưới bảng. Năm chủ đề đầu chiếm sáu bốn phẩy bảy phần trăm, phải
gộp tới bảy chủ đề mới chạm tám hai phẩy bốn. Nghĩa là phân bố của C4 khá phẳng chứ không đúng khuôn tám
mươi hai mươi, và em có nói ra chỗ đó chứ không làm tròn cho đẹp.*

**Q53 · "Vậy tỷ lệ nhánh trên mô hình có suy từ Pareto ra không?"** `[dự phòng, nhưng là bẫy thật]`

*Dạ không ạ, và em có viết hẳn một dòng cấm phép suy đó trong bài. Pareto đếm số nguồn nhắc tới chủ đề
chứ không đếm số ca, nên lấy nó làm xác suất nhánh là sai. Xác suất nhánh em để thành một nhóm giả định
riêng, mã từ `GT20` tới `GT30`, và khai rõ là ước lượng thuần.*

---

## 6. Tiêu chí 4 - Phân tích định lượng

**Q54 · "Phân tích định lượng cũng phải ghi số lên hình, hình vẽ của em đâu?"** `[24/08 và 07/09]`

*Dạ em có ba lớp chú lên hình chứ không phải một ạ. Thời gian xử lý với thời gian chờ ghi trên từng bước,
nằm ở hai hình `C3-time` và `C4-time`. Rồi chi phí ghi trên từng bước, nằm ở `C3-cost` và `C4-cost`. Tính
cả hình chi tiết sub-process thì thành mười hai hình chú.*

**Q55 · "Cycle time, processing time và hiệu suất của mình là bao nhiêu?"** `[dự phòng]`

*Dạ C3 thì cycle time một trăm ba tám phút, processing time sáu mươi tám phút, CTE bốn chín phẩy ba phần
trăm. C4 thì cycle time năm nghìn chín trăm năm tám phẩy chín phút, processing time một trăm tám tám phẩy
chín phút, CTE ba phẩy một bảy phần trăm ạ.*

**Q56 · "Sao CTE của C4 chỉ 3,17%, có phải tính sai không?"** `[dự phòng]`

*Dạ không sai ạ. Cycle time của C4 tính bằng ngày tại máy nằm ở Trung tâm Bảo hành, còn processing time
chỉ là thao tác thật của nhân viên thôi. Em quy đổi một ngày bằng bốn trăm tám mươi phút theo đúng cách
giáo trình làm ở ví dụ credit application. Nếu em tính theo ngày lịch một nghìn bốn trăm bốn mươi phút
thì con số còn thấp hơn nữa. Nên ba phẩy một bảy là con số dè dặt nhất chứ không phải bi quan nhất.*

**Q57 · "Số này đâu ra? Đừng có đùng một phát ba mươi hai này đâu ra."** `[24/08 · nhóm ACFC]`

*Dạ số nào của em cũng có mã giả định và có phép tính dẫn tới nó ạ. Em lấy chi phí làm lại của C3 làm ví
dụ. Chênh lệch nhân công giữa kịch bản bổ sung giấy tờ và kịch bản duyệt thẳng là bảy sáu nghìn không bốn
hai trừ đi sáu mươi nghìn bốn một bảy, ra mười lăm nghìn sáu hai lăm. Nhân với tỷ lệ hai mươi phần trăm
của `GT22` thì ra ba nghìn một trăm hai lăm đồng một ca, bằng bốn phẩy tám phần trăm chi phí nhân công
một ca.*

**Q58 · "Nhóm mình giả lập dữ liệu à?"** `[24/08 · thầy chấp nhận giả lập]`

*Dạ có ạ, và em khai rõ chỗ nào giả lập. Em chia ba mức tin cậy cho từng giá trị. Mức công bố là số doanh
nghiệp tự đăng trên trang chính sách hay tin tuyển dụng. Mức ước lượng là em tự suy và có một dòng giả
định tương ứng. Mức quan sát là số đo bằng đồng hồ. Nhóm em không có dòng nào ở mức quan sát tại chưa đi
bấm giờ được, cái này em ghi ngay đầu Chương ba chứ không giấu.*

**Q59 · "Cổng của em có xác suất mỗi nhánh không?"** `[07/09 · thầy hỏi Shopee, và bắt lỗi Hasaki]`

*Dạ có ạ, phủ mười ba điểm rẽ, và từ bản dựng mới thì số nằm ngay trên hình chứ không chỉ nằm trong
bảng — thầy mở `C3-time` với `C4-time` ra là đọc được từng nhánh. Bên C3 thì `G1` là tám lăm trên mười
lăm, `G2` là tám mươi đi qua công ty tài chính và hai mươi đi qua thẻ tín dụng, `G9` là chín bảy trên
ba, `G10` là tám lăm trên mười lăm, `G7` khách chấp nhận điều kiện vay mới là một trăm trên không, rồi
bốn kịch bản kết cục là duyệt thẳng bốn lăm, duyệt có điều kiện hai mươi, bổ sung giấy tờ hai mươi, từ
chối mười lăm. Bên C4 thì `G1` bảy mươi trên ba mươi, `G3` bảy lăm trên hai lăm, `G4` hai mươi trên tám
mươi, `G6` là đổi máy ba mươi, trả hàng mười, sửa chữa sáu mươi, `G7` bảy mươi trên ba mươi, `G8` chấp
nhận model tương đương là một trăm trên không, `G9` tám mươi trên hai mươi.*

Hai chỗ ghi **một trăm trên không** là `GT42` và `GT43`. Thầy hỏi ngược *"sao vẽ nhánh không bao giờ
chạy"* thì trả lời: nhánh đó là đường đi quy trình cho phép, chỉ là phần định lượng chưa gán ca nào
cho nó, và nhóm ghi số 0 ra cho minh bạch thay vì giấu. Có số thật thì chỉ sửa hai dòng giả định,
không phải dựng lại bảng nào.

**Q60 · "Bao nhiêu phần trăm khách hủy, bao nhiêu phần trăm khách chấp nhận?"** `[07/09 · nhóm Hasaki]`

*Dạ bên C4 thì bốn nhánh kết cục cộng lại đúng một trăm phần trăm ạ: từ chối hai lăm, đổi máy hai hai
phẩy năm, trả hàng và hoàn tiền bảy phẩy năm, sửa chữa bốn lăm.*

Có một chỗ dễ nói nhầm: `GT27` cho tỷ lệ **tại cổng** là 30, 10, 60; còn 22,5 và 7,5 và 45,0 là tỷ lệ
**trên toàn quy trình** sau khi nhân với 75% đã qua `G3`. Hỏi tới thì nói rõ đang nói con số nào.

**Q61 · "Hoạt động bên phía khách hàng sao không có thời gian?"** `[07/09 · nhóm Hasaki]`

*Dạ ba tác nhân bên ngoài của C4 là Khách hàng, Trung tâm Bảo hành và Hãng sản xuất thì em vẽ dạng pool
hộp đen, tức là em không vẽ hoạt động nội bộ của họ ra. Nên không có hoạt động nào bị bỏ trống số ạ. Thời
gian của phần bên ngoài thì em vẫn đo và ghi lên nhãn pool: chờ tới lượt thẩm định một nghìn chín trăm
hai mươi phút, thẩm định kỹ thuật ba mươi phút, sửa chữa chín mươi phút.*

**Q62 · "Hoạt động mình đã vẽ ra thì phải đánh giá thời gian chứ."** `[07/09 · nhóm Hasaki]`

*Dạ em đồng ý ạ, và bộ này giữ đúng luật đó. Hoạt động nào có mặt trên hình là có số. Còn chỗ em không vẽ
ra thì cũng không phải để trống, tại nó nằm trong pool hộp đen và thời gian của nó được gói vào thời gian
chờ của bước tương ứng bên phía cửa hàng.*

**Q63 · "Chỗ này em gộp mấy bước thành một con số à?"** `[07/09 · nhóm Hasaki bị bác ở đúng chỗ này]`

*Dạ không ạ. Chỗ duy nhất em gộp là hộp sub-process, mà mỗi hộp đó em vẽ một hình chi tiết riêng đầy đủ
bên trong. Còn trên hình khung thì từng hoạt động, từng cổng đều có số riêng.*

Thầy có nói ở buổi 07/09 rằng gộp bằng sub-process là chấp nhận được. Nhắc lại ý đó thì được, nhưng đừng
trích nguyên văn lời thầy.

**Q64 · "Nút thắt của quy trình nằm ở đâu?"** `[dự phòng]`

*Dạ với C4 thì nút thắt là hàng đợi chứ không phải quãng đường ạ. Hai con số lớn nhất trên hình là một
nghìn chín trăm hai mươi phút chờ tới lượt thẩm định và hai nghìn tám trăm tám mươi phút chờ tới lượt
sửa, cả hai đều là hàng đợi. Em thử tính hai chiều: bỏ hẳn vận chuyển mà giữ nguyên hàng đợi thì cycle
time chỉ giảm mười bảy phẩy bảy phần trăm, còn giữ nguyên vận chuyển mà xóa được hàng đợi thì giảm tám
mươi hai phần trăm. Kết quả này sửa lại chính trực giác của phần định tính, chỗ đó em xếp lãng phí nhóm
Move lên dòng đầu.*

**Q65 · "Phân tích định lượng của em có đủ ba khía cạnh không?"** `[dự phòng]`

*Dạ đủ ba ạ. Thời gian thì có cycle time, processing time và CTE. Chất lượng thì có tỷ lệ xử lý xong ngay
lần đầu, tỷ lệ làm lại và tỷ lệ đạt cam kết. Chi phí thì có chi phí nhân sự tính bằng thời gian nhân đơn
giá, cộng chi phí vận chuyển và chi phí cơ hội.*

**Q66 · "Chỉ số chất lượng của em ra bao nhiêu?"** `[dự phòng]`

*Dạ C3 thì tỷ lệ xử lý xong ngay lần tiếp xúc đầu là bốn lăm phần trăm tính trên nhánh đi qua công ty tài
chính, hoặc năm sáu phần trăm nếu tính trên toàn bộ giao dịch trả góp. Tỷ lệ hồ sơ phải làm lại là hai
mươi phần trăm, tỷ lệ bị từ chối mười lăm. Còn C4 thì tỷ lệ yêu cầu bị từ chối hai lăm phần trăm, tỷ lệ
ca không còn hàng đổi đúng model sáu phẩy bảy lăm, tỷ lệ trễ hạn cam kết mười lăm ngày là hai mươi phần
trăm.*

**Q67 · "Chi phí một ca là bao nhiêu, tính thế nào?"** `[dự phòng]`

*Dạ C3 là sáu mươi bốn nghìn không tám chín đồng chi phí nhân công một ca. Cách tính là thời gian mỗi vai
nhân đơn giá của vai đó, rồi nhân tiếp với xác suất bốn kịch bản của `GT22`. Trong đó riêng chi phí làm
lại là ba nghìn một trăm hai lăm, bằng bốn phẩy tám phần trăm. Còn C4 thì phần công bỏ đi cho ca bị từ
chối sau khi đã tốn hết tiếp nhận và vận chuyển là mười tám nghìn không không ba đồng một ca, bằng mười
hai phẩy sáu phần trăm chi phí một ca. Ngoại suy ra toàn chuỗi thì khoảng hai phẩy sáu tỷ mỗi năm ạ.*

**Q68 · "Vòng bổ sung giấy tờ tốn của doanh nghiệp bao nhiêu?"** `[dự phòng]`

*Dạ nó chỉ dính hai mươi phần trăm số hồ sơ nhưng đẻ ra sáu mươi phẩy bảy phần trăm toàn bộ thời gian chờ
của C3. Nó làm `T4` hiệu dụng thành mười tám phẩy bảy lăm phút thay vì mười lăm phút. Chi phí làm lại ba
nghìn một trăm hai lăm đồng một ca, ngoại suy toàn chuỗi khoảng ba phẩy sáu tỷ mỗi năm.*

**Q69 · "Số lượt vận chuyển bình quân của một ca bảo hành là bao nhiêu?"** `[dự phòng]`

*Dạ một phẩy bốn lăm lượt một ca ạ. Em tính bằng không phẩy hai lăm nhân một, cộng không phẩy hai hai lăm
nhân một, cộng không phẩy không bảy lăm nhân một, cộng không phẩy bốn lăm nhân hai.*

**Q70 · "Đề xuất cải tiến của em doanh nghiệp làm được không, tốn bao nhiêu?"** `[dự phòng]`

*Dạ em có năm đề xuất trong Issue Register, cái nào cũng gắn với một dòng cụ thể trong bảng phân tích chứ
em không viết chung chung kiểu tăng cường hay đẩy mạnh. Ba trong năm cái chỉ cần sửa trên hệ thống hiện
có thôi: một trang tra cứu trạng thái ca, một checklist giấy tờ động theo từng công ty tài chính, và gom
về một nguồn chính sách duy nhất có ghi ngày hiệu lực để cửa hàng, tổng đài với website dùng chung. Còn
chi phí triển khai thì em xin nói thật là chưa lượng hóa được, tại cái đó cần số liệu nội bộ.*

---

## 7. Tiêu chí 5 - Trình bày và nộp bài

**Q71 · "Slide của em có đánh số trang không? Thiếu là bị trừ điểm."** `[07/09 · nhóm Hasaki]`

*Dạ có ạ, slide nào cũng đánh số ở góc dưới bên phải, mà em dùng trường số trang thật của PowerPoint chứ
không gõ tay. Bản PDF dự phòng xuất ra cũng đúng số. Hình thì em đánh số liên tục kèm chú thích, chú
thích hình để dưới hình còn chú thích bảng để trên bảng.*

**Q72 · "Báo cáo Word của em bao nhiêu trang, có đủ bốn danh mục không?"** `[dự phòng]`

*Dạ hai trăm năm mươi hai trang ạ. Bốn danh mục có đủ: mục lục, mục lục hình ảnh, mục lục bảng biểu và
bảng viết tắt. Danh mục tài liệu tham khảo có hai mươi hai mục đánh số theo IEEE, em tách riêng nguồn
tiếng Việt với tiếng Anh. Trình bày thì theo mẫu khóa luận của khoa mình.*

**Q73 · "Hình BPMN in ra có đọc được không?"** `[24/08 · lỗi của hai nhóm khác]`

*Dạ đọc được ạ. Mỗi mô hình em dành trọn một trang ngang riêng chứ không nhét vào một ô nhỏ giữa trang
dọc. Em có in thử ra giấy để kiểm.*

**Q74 · "Nộp ở đâu?"** `[24/08 và 07/09]`

*Dạ nộp hai nơi ạ, Google Drive và E-learning. Hạn là một tuần sau buổi báo cáo, trước ba giờ rưỡi chiều
Chủ nhật.*

**Q75 · "Sau hôm nay mình sửa được cái gì?"** `[24/08 và 07/09]`

*Dạ em hiểu là chỉ sửa được báo cáo Word thôi ạ, còn slide thì thầy chấm xong hôm nay là chốt. Với lại
lỗi nào hôm nay thầy đã chỉ trên slide mà em để nguyên trong Word thì bị trừ lần nữa, nên nhóm em sẽ ghi
lại hết ngay trong buổi.*

**Q76 · "Điểm buổi báo cáo chiếm bao nhiêu?"** `[24/08 và 07/09]`

*Dạ slide với buổi báo cáo chiếm hai mươi tới ba mươi phần trăm, còn báo cáo Word chiếm bảy mươi tới tám
mươi ạ.*

---

## 8. Phạm vi, nhóm và trung thực

**Q77 · "Vì sao chọn Thế Giới Di Động mà không phải chuỗi khác?"** `[dự phòng]`

*Dạ tại MWG công khai nhiều tài liệu quy trình hơn hẳn ạ. Chính sách bảo hành của họ có hẳn biểu phí khấu
hao theo tháng, tin tuyển dụng thì mô tả rõ từng vai trò, báo cáo kinh doanh thì tách số cửa hàng theo
từng chuỗi. Em có tham khảo bài mẫu Cellphones với Tiki Logistics cùng ngành, nên nhóm cố tình bám vào
những thứ chỉ MWG mới có: ERP tự viết từ hai nghìn lẻ năm, quy mô một nghìn không mười hai cửa hàng, và
tỷ lệ một nhân sự trên khoảng ba trăm bảy mươi nhân viên.*

**Q78 · "Sao chỉ phân tích hai quy trình mà không phải cả sáu?"** `[dự phòng]`

*Dạ rubric yêu cầu hai quy trình ạ. Em chọn C3 với C4 vì cả hai đều là cốt lõi, đều có tác nhân bên
ngoài, và đều có nhánh chờ đủ dài để đo được. Với lại hai cái này đối lập nhau về bản chất cái chờ: C3
chờ thông tin còn C4 chờ hàng đợi vật lý, nên em so sánh được và ra kết luận trái ngược nhau về nút
thắt.*

**Q79 · "Ai làm phần nào, có ai không làm gì không?"** `[dự phòng]`

*Dạ nhóm em bốn người, tỷ lệ đóng góp lệch nhau và cái đó là cố ý ạ. Em là Danh, ba mươi hai phần trăm,
giữ phần kiến trúc, ba mô hình cốt lõi, rồi ghép báo cáo với dựng slide. Bạn Hồng Phúc hai sáu phần trăm,
làm hồ sơ quy trình quản lý, hai mô hình và phân tích định tính. Bạn Thanh Phúc hai hai phần trăm, làm hồ
sơ quy trình hỗ trợ, một mô hình, bộ câu hỏi với tài liệu tham khảo. Bạn Hưng hai mươi phần trăm, làm bộ
bằng chứng, bảng giả định và phân tích định lượng. Kho GitHub của lớp có tám mươi bảy commit của đủ bốn
người, mỗi khối việc đi qua một pull request nên thầy kiểm chứng được.*

---

## 9. Nếu bị hỏi câu chưa chuẩn bị

Ba bước, theo thứ tự, và đừng bịa.

Nếu thứ đó **có trong bài** thì đọc thẳng con số hoặc tên phần tử ra, đừng đọc số trang.

Nếu thứ đó **là giả định** thì nói luôn nó là giả định, mã bao nhiêu, rồi đọc phép tính ra nó.

Nếu **chưa làm** thì nói thẳng là chưa làm, rồi nói nhóm định lấp bằng cách nào.

Thầy trừ điểm nặng nhất khi số liệu không có đường tính, chứ không phải khi nhóm thừa nhận chỗ chưa làm
được. Hai buổi vừa rồi đều cho thấy nhóm nào nhận nhanh thì được chuyển câu, nhóm nào giải thích vòng vo
thì bị truy sâu hơn.

Ba câu tuyệt đối không nói: *"trong báo cáo có, chỉ là không lên slide"*, *"để vậy cho nó gọn"*, và
*"em thấy nhiều cổng quá rối nên em vẽ bớt"*. Cả ba đều đã bị trừ điểm trước mặt lớp rồi.
