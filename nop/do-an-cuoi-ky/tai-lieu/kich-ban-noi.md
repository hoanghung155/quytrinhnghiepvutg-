# Kịch bản nói – buổi báo cáo 07/09/2026

**Thời lượng: 27,5 phút, trần cứng 30 phút.** Quá giờ bị trừ điểm ở tiêu chí 5.
**Một người nói cả năm phần: Ngọc Danh.**

File slide: [24730090_24730099_24730131_24730132.pptx](../24730090_24730099_24730131_24730132.pptx) – 40 slide, sinh lại bằng `python gen_slide.py`.

## Cách đọc file này

Mỗi phần có **hai thứ**, và bộ dựng dùng cả hai:

| Thứ | Việc của nó |
|---|---|
| Bảng đầu mỗi phần | Ngân sách: slide nào, bao nhiêu phút, ý chính là gì, câu chuyển tiếp là gì |
| Khối `### Slide N` | **Lời nói đầy đủ**, đúng chữ sẽ nói ra miệng. Khối này **đè lên** ô "Ý chính" của bảng |

Slide nào chưa có khối `### Slide N` thì ghi chú lấy tạm ô "Ý chính" của bảng, tức
vẫn chỉ là dòng chỉ dẫn chứ chưa phải lời nói. Ngược lại, khối khai một số slide
không có dòng nào trong bảng thì bộ dựng **báo đích danh**, không im lặng bỏ qua.

Ngân sách chữ tính theo **130 từ mỗi phút**. Đây là hằng số để lập kế hoạch, không
phải số đo: nhịp nói thật chỉ biết được khi bấm giờ chạy thử.

Cột `Người nói` ở bảng phân bổ nay lặp cùng một tên năm lần. Nhìn thừa, nhưng
`doc_kich_ban()` đọc chính cột đó để gắn tên vào ghi chú từng slide, bỏ đi là hỏng
bộ dựng. Cột `Phút` cũng vậy: `doi_chieu_thoi_luong()` cộng nó lại để đối chiếu.

Ba thứ **không viết tay vào đây**, bộ dựng tự thêm vào ghi chú: dòng đầu ghi số
slide và phút, dòng dự phòng thời gian, và dòng nguồn của con số trên slide.

---

## Phân bổ thời gian

| Phần | Slide | Người nói | Phút | Dồn |
|---|---|---|---:|---:|
| 1. Doanh nghiệp, phạm vi, kiến trúc | 1–9 | Ngọc Danh | 5,0 | 5,0 |
| 2. Phương pháp khám phá | 10–14 | Ngọc Danh | 4,3 | 9,3 |
| 3. Mô hình hóa BPMN | 15–25 | Ngọc Danh | 9,6 | 18,9 |
| 4. Phân tích quy trình | 26–38 | Ngọc Danh | 7,9 | 26,8 |
| 5. Kết luận | 39–40 | Ngọc Danh | 0,7 | 27,5 |

### Vì sao ngân sách xuống 27,5 phút (sửa 07/09/2026)

Trần vẫn là 30 phút, nhưng bản này nhắm 27,5 vì hai lý do gộp lại.

Lý do thứ nhất là chỉ còn một người nói. Trước đây bốn người chia nhau, mỗi người
nói liền tối đa mười phút rồi có người khác đỡ lời. Một người nói liền ba mươi phút
thì đuối giọng ở đoạn cuối, mà lúc vấp cũng không có ai chen vào gỡ. Chừa hai phút
rưỡi là chừa chỗ cho chính chỗ vấp đó.

Lý do thứ hai là slide phân công nhóm đã bỏ khỏi bộ slide, trả lại 0,3 phút. Phần
đóng góp của bốn thành viên vẫn giữ nguyên trong báo cáo Word, và nếu thầy hỏi thì
câu trả lời nằm ở mục Q79 của [du-kien-cau-hoi.md](du-kien-cau-hoi.md).

| Phần | Trước | Sau | Cắt gì |
|---|---:|---:|---|
| 1 | 5,5 | 5,0 | Slide 2 và 4 nói gọn hơn, ba slide danh mục mỗi slide bớt 0,1 |
| 2 | 5,0 | 4,3 | Bốn slide công cụ đều bớt, phần nói thẳng chỗ chưa khảo sát được giữ nguyên |
| 3 | 10,0 | 9,6 | Mỗi mô hình bớt 0,1 ở băng dưới, slide quy ước bớt 0,1 |
| 4 | 8,5 | 7,9 | Bốn slide bảng bớt 0,1 tới 0,2, sáu slide hình chú giữ nguyên |
| 5 | 1,0 | 0,7 | Bỏ slide phân công nhóm |

Phần 3 bị cắt ít nhất vì đó là chỗ ăn điểm mô hình hóa. Sáu slide hình chú của phần
4 cũng giữ nguyên, vì chúng là bằng chứng nhóm đã làm đủ hai bước phân tích.

---

## Phần 1 – Ngọc Danh (5,0 phút)

| Slide | Phút | Ý chính | Chuyển tiếp |
|---:|---:|---|---|
| 1 | 0,4 | Chào thầy và các bạn. Giới thiệu tên đề tài, nhóm bốn người, GVHD. | "Nhóm em xin bắt đầu bằng nội dung trình bày." |
| 2 | 0,2 | Đọc nhanh năm phần của bài. | "Trước hết là về doanh nghiệp." |
| 3 | 0,4 | Bốn con số: doanh thu 156.166 tỷ, 1.012 cửa hàng, hơn 74.000 nhân viên, ERP tự xây từ 2005. | "Nhưng MWG có sáu chuỗi, nên nhóm phải chốt phạm vi." |
| 4 | 0,3 | Trong phạm vi: thegioididong.com và TopZone. Ngoài phạm vi: năm chuỗi còn lại. | "Trong phạm vi đó, nhóm dựng kiến trúc quy trình." |
| 5 | 1,7 | **Slide quan trọng nhất phần 1.** Kiến trúc quy trình ba lớp: quản lý, cốt lõi, hỗ trợ. Hình ngôi nhà chỉ là cách minh họa. | "Đi vào từng lớp." |
| 6 | 0,5 | Bốn quy trình quản lý, ánh xạ sang phân lớp Dumas. M2 và M3 được mô hình hóa. | – |
| 7 | 0,5 | Bốn quy trình cốt lõi. C3 và C4 được mô hình hóa. | – |
| 8 | 0,4 | Bốn quy trình hỗ trợ. S1 và S4 được mô hình hóa. Cộng lại đúng hai quy trình mỗi lớp. | – |
| 9 | 0,6 | Bốn thành phần bắt buộc của mỗi hồ sơ quy trình, cũng là bốn ý đầu của thẻ thông tin ở phần 3. | "Có khuôn hồ sơ rồi thì câu hỏi tiếp theo là lấy thông tin ở đâu ra." |

### Slide 1

Em chào thầy, chào các bạn. Em là Nguyễn Ngọc Danh, nhóm trưởng. Hôm nay em xin
thay mặt nhóm trình bày cả bài.

Đề tài của nhóm em là phân tích quy trình nghiệp vụ chuỗi Thế Giới Di Động. Thầy
nhìn giúp em dòng phạm vi ngay dưới tên đề tài: nhóm em chỉ làm chuỗi điện thoại
thôi, chứ không làm cả tập đoàn.

### Slide 2

Bài của nhóm em đi theo năm phần như trên bảng. Trong đó phần mô hình hóa BPMN là
phần dài nhất, vì đây cũng là phần nặng điểm nhất.

### Slide 3

Doanh thu thuần năm 2025 là 156.166 tỷ đồng. Riêng chuỗi điện thoại có 1.012 cửa
hàng, còn toàn hệ thống thì hơn 74.000 nhân viên.

Nhưng con số cuối mới là con số chi phối cả bài của nhóm em. Doanh nghiệp này tự
viết hệ ERP từ năm 2005, mà tự viết thì sửa được. Cho nên phần mềm ở đây vừa là công
cụ, vừa là cái khung mà mọi đề xuất của nhóm em phải nằm gọn bên trong.

### Slide 4

Cột bên trái là phần nhóm em làm, gồm thegioididong.com và TopZone. Cột bên phải là
năm chuỗi còn lại, nhóm em để ngoài phạm vi.

Sở dĩ nhóm em chọn hẹp như vậy là vì bán điện thoại khác hẳn bán hàng tươi sống. Gộp
cả sáu chuỗi vào một mô hình thì bước nào cũng phải kèm điều kiện, hình vẽ ra rối mà
lại không nói được gì chắc chắn. Bó lại một chuỗi thì mọi con số trong bài đều lấy
từ cùng một nguồn, thầy kiểm chéo được ngay.

### Slide 5

Đây là hình em muốn thầy nhìn kỹ nhất ở phần một. Nhóm em lấy mười hai quy trình đã
xác định, xếp thành kiến trúc quy trình ba lớp theo đúng cách phân lớp trong giáo
trình. Hình ngôi nhà ở đây chỉ là cách nhóm em vẽ cho dễ nhìn, còn tên gọi ba lớp
vẫn là tên chuẩn.

Lớp trên cùng là nhóm quy trình quản lý, tiếng Anh là management process. Đây là chỗ
đặt mục tiêu, giao hạn mức và ra ràng buộc cho các lớp dưới. Nhóm em vẽ nó thành mái
nhà, vì mái thì bao lên trên.

Lớp giữa là nhóm quy trình cốt lõi, core process. Đây mới là chỗ trực tiếp tạo ra
doanh thu, và cũng là chỗ duy nhất khách bên ngoài chạm vào doanh nghiệp. Trên hình
nhóm em vẽ nó thành thân nhà.

Lớp dưới cùng là nhóm quy trình hỗ trợ, support process. Lớp này cung cấp con người,
hệ thống, tài sản và dòng tiền cho lớp cốt lõi, nên nhóm em vẽ thành móng. Nói cho
dễ hình dung thì không tuyển được nhân viên, cửa hàng không mở nổi quầy.

[nghỉ một nhịp]

Thầy nhìn giúp em hai mũi tên dọc ở hai bên hình, nhóm em cố ý vẽ hai chiều. Lớp
quản lý đặt mục tiêu xuống cho lớp cốt lõi, rồi lớp cốt lõi báo số bán thật lên để
lớp quản lý chỉnh kế hoạch kỳ sau. Tương tự, lớp hỗ trợ cấp nguồn lực lên, còn lớp
cốt lõi báo nhu cầu xuống.

Có một điểm nhóm em bàn khá lâu, là vì sao bảo hành lại xếp vào lớp cốt lõi chứ
không phải lớp hỗ trợ. Lý do là khách hàng của quy trình bảo hành là khách bên
ngoài, và mỗi ca bảo hành đều động tới doanh thu. Còn khách hàng của tuyển dụng chỉ
là cửa hàng, tức khách nội bộ. Nhóm em lấy đúng tiêu chí đó để xếp lớp cho cả mười
hai quy trình.

### Slide 6

Bảng này là bốn quy trình thuộc lớp quản lý. Cột thứ ba nhóm em ánh xạ từng quy
trình sang phân lớp trong giáo trình, để thầy thấy danh mục này nhóm em không tự
nghĩ ra.

Còn cột cuối cho biết quy trình nào được nhóm em vẽ mô hình. Ở lớp này là quản lý
nhà cung cấp và kho tổng. Nhóm em chọn hai cái đó vì cả hai đều có tác nhân bên
ngoài, và đều có nhánh phê duyệt.

### Slide 7

Lớp cốt lõi cũng có bốn quy trình, trình bày y như bảng vừa rồi. Hai mô hình nhóm
em vẽ ở lớp này là bán trả góp và bảo hành đổi trả.

Hai quy trình này cũng chính là hai quy trình được phân tích sâu ở phần bốn. Nhóm em
cố ý chọn trùng, để phần mô hình và phần phân tích dùng chung một bộ bước, thầy đối
chiếu qua lại được.

### Slide 8

Lớp cuối là bốn quy trình hỗ trợ. Hai mô hình ở đây là tuyển dụng đào tạo, và đối
soát công nợ thanh toán nhà cung cấp.

Cộng cả ba lớp lại thì vừa đúng sáu mô hình, mỗi lớp hai cái, đúng như đề bài yêu
cầu chứ nhóm em không dồn hết vào một lớp dễ vẽ.

### Slide 9

Mỗi quy trình đều có một hồ sơ khai đủ bốn thành phần như trên slide, và cả mười
hai quy trình nhóm em đều làm đủ.

Có hai chỗ hồ sơ rất dễ vênh nhau, nên em xin nói rõ. Thứ nhất, khách hàng của quy
trình phải là một trong những tác nhân đã kê ở mục a. Nếu xuống mục b mà lại hiện ra
một đối tượng chưa từng có tên ở mục a thì hồ sơ đó sai rồi. Thứ hai, mục c phải kê
đủ cả nhánh xấu chứ không riêng nhánh thuận lợi. Và mỗi kết quả kê ra đều phải có
đúng một sự kiện kết thúc tương ứng trên hình.

## Phần 2 – Ngọc Danh (4,3 phút)

| Slide | Phút | Ý chính | Chuyển tiếp |
|---:|---:|---|---|
| 10 | 1,0 | Ba nhóm phương pháp, ba trạng thái khác nhau. **Nêu rõ lựa chọn phương pháp**: không điền số phỏng đoán, mọi ước lượng đều có mã giả định. | "Bắt đầu từ nhóm đã chạy xong." |
| 11 | 0,9 | Sáu loại bằng chứng, tất cả đều có sản phẩm cụ thể. 28 nguồn mã hóa thành 14 chủ đề. | – |
| 12 | 0,8 | Biểu mẫu biên bản bảy mục và kịch bản 90 phút. Ba câu hỏi mồi. | – |
| 13 | 0,9 | **Điểm khác biệt**: bộ câu hỏi soạn riêng cho từng quy trình, 20 câu mỗi quy trình, tổng 120 câu. | – |
| 14 | 0,7 | Bốn loại câu hỏi kèm ví dụ thật. Câu có cấu trúc bắt buộc phải in ra phương án A, B, C, D. | "Từ bộ dữ liệu đó, nhóm em dựng sáu mô hình BPMN." |

### Slide 10

Để khám phá quy trình thì nhóm em dùng ba nhóm phương pháp, đúng ba nhóm trong giáo
trình. Thầy nhìn giúp em dòng nhãn dưới mỗi cột, vì ba cột đang ở ba trạng thái khác
nhau.

Cột đầu là phương pháp dựa trên bằng chứng, cái này nhóm em chạy xong rồi. Hai mươi
tám nguồn công khai, nhóm em đọc hết và mã hóa hết, ra sản phẩm cụ thể mà em sẽ đưa
ở slide sau.

Hai cột sau là hội thảo và phỏng vấn. Ở hai cột này nhóm em dựng sẵn đủ bộ công cụ
trước: biểu mẫu biên bản bảy mục, kịch bản chín mươi phút, và một trăm hai mươi câu
hỏi soạn riêng theo từng quy trình. Đây là phần chuẩn bị để đi triển khai, chứ chưa
phải dữ liệu thu về.

Đến đây có một lựa chọn về phương pháp mà nhóm em muốn nói rõ với thầy. Những con số
mà phải xuống tận nơi khảo sát mới biết được, nhóm em không điền bừa vào cho đầy
bảng. Mỗi con số kiểu đó nhóm em đều ghi rõ là ước lượng, kèm căn cứ vì sao suy ra
như vậy, rồi cho đứng thành một dòng riêng trong bảng giả định ngay đầu chương ba.
Nhóm em làm vậy để thầy tách được ngay đâu là số có bằng chứng, đâu là số nhóm em
suy luận.

### Slide 11

Bảng này là sáu loại bằng chứng nhóm em đã thu được. Chỗ em muốn nhấn là cột giữa:
mỗi loại bằng chứng đều ra một sản phẩm cầm được, chứ không phải nói suông. Bản chụp
trang chính sách, sơ đồ tổ chức, bảng thuật ngữ, rồi các biểu mẫu, tất cả nhóm em
đều nộp kèm.

Dòng em muốn nói kỹ là dòng nghiên cứu thứ cấp. Nhóm em đọc hai mươi tám nguồn công
khai, rồi mã hóa lại thành mười bốn chủ đề vấn đề. Chính mười bốn chủ đề này là đầu
vào cho biểu đồ Pareto ở phần bốn. Nghĩa là phần bằng chứng và phần phân tích của
nhóm em nối thẳng vào nhau, chứ không rời nhau.

### Slide 12

Đây là bộ công cụ nhóm em soạn cho buổi hội thảo. Bên trái là biểu mẫu biên bản bảy
mục. Em xin nhấn hai mục cuối: mục sáu ghi những điểm đã chốt được, còn mục bảy ghi
việc còn treo kèm tên người chịu trách nhiệm. Thiếu hai mục này thì họp xong ai về
nhà nấy, không ai biết phải làm gì tiếp.

Bên phải là kịch bản 90 phút. Ba câu hỏi mồi ở dòng cuối dùng khi buổi họp chững lại.
Câu nhóm em ưu tiên là hỏi về một ca kéo dài gấp đôi bình thường. Hỏi kiểu đó thì
người ta kể ngoại lệ thật, còn hỏi quy trình chạy thế nào thì họ đọc lại quy định.

### Slide 13

Đây là chỗ nhóm em chủ động làm khác. Bộ câu hỏi nhóm em không soạn chung cho cả
doanh nghiệp, mà soạn riêng cho từng quy trình một. Mỗi quy trình hai mươi câu, chia
đôi mười câu định tính và mười câu định lượng. Sáu quy trình vị chi một trăm hai
mươi câu.

Cách đánh mã ở cột bên phải cho phép nhóm em tách riêng bộ của một quy trình ra
thành phiếu phỏng vấn độc lập mà không phải đánh số lại. Đi hỏi bộ phận bảo hành thì
chỉ cầm đúng bộ đó xuống thôi.

Nhóm câu em quý nhất là ba mươi câu định lượng không cấu trúc. Đây là những câu hỏi
thẳng vào các con số mà nhóm em đang phải giả định: hạn mức phê duyệt là bao nhiêu,
thời hạn cam kết mấy ngày, quy trình chạy bao lâu một lần.

### Slide 14

Bảng này nhóm em phân biệt bốn loại câu hỏi bằng dấu hiệu nhận biết, chứ không bằng
định nghĩa. Cột giữa là dấu hiệu, còn cột phải là ví dụ thật lấy ngay từ bộ câu hỏi
của nhóm em.

Em xin nhấn dòng cuối slide, vì đây là lỗi hay gặp nhất. Một câu muốn gọi là câu có
cấu trúc thì bắt buộc phải in kèm phương án cho người ta chọn. Hỏi về con số mà
không cho sẵn các khoảng giá trị thì câu đó thành câu mở mất rồi, không tính là câu
có cấu trúc nữa.

## Phần 3 – Ngọc Danh (9,6 phút)

**Nghỉ vài giây trước khi vào phần này.** Uống một ngụm nước, lấy lại nhịp. Đây là
phần dài nhất và nặng điểm nhất, vào phần mà đang hụt hơi là hỏng cả đoạn sau.

| Slide | Phút | Ý chính | Chuyển tiếp |
|---:|---:|---|---|
| 15 | 0,6 | Chín quy ước đã áp dụng khi vẽ. Đọc nhanh, không giải thích lý thuyết BPMN. | "Ba mô hình đại diện ba lớp." |
| 16 | 1,1 | M2 băng trên. **Nói rõ cách cắt băng ngay ở slide này, các mô hình sau không nhắc lại.** Hai cấp phê duyệt. | – |
| 17 | 0,9 | M2 băng dưới. Cặp cổng song song và pool nhà cung cấp. | – |
| 18 | 0,6 | Thẻ thông tin M2. **Câu đầu nói cả hai con số tác nhân**, rồi chỉ nói ý ② và ⑤. | – |
| 19 | 1,1 | C4 băng trên. Mốc tháng đầu và cổng phân loại nguyên nhân lỗi. | – |
| 20 | 0,9 | C4 băng dưới. Ba pool bên ngoài và ba hướng khép hồ sơ. | – |
| 21 | 0,6 | Thẻ thông tin C4. Câu đầu nói cả hai con số, rồi ý ② và ⑤. | – |
| 22 | 1,1 | S1 băng trên. Cổng chọn nguồn ứng viên và hai kết thúc xấu. | – |
| 23 | 0,9 | S1 băng dưới. Cổng dựa trên sự kiện đặt hạn phản hồi, pool ứng viên. | – |
| 24 | 0,6 | Thẻ thông tin S1. Câu đầu nói cả hai con số, rồi ý ② và ⑤. | – |
| 25 | 1,2 | Bảng thống kê sáu mô hình. **Đọc to con số cổng điều kiện thấp nhất** và nhắc mốc trọn điểm là trên 7 cổng. | "Sáu mô hình đó là đầu vào của phần phân tích." |

> Nếu tới slide 22 mà đã quá 22 phút thì **bỏ hai slide băng của S1, chiếu thẳng
> slide 24 thẻ thông tin**. Thầy nói rõ: không đủ thời gian thì báo cáo một hoặc hai
> quy trình còn hơn cháy giờ, phần còn lại đã có đủ trong báo cáo Word.

### Slide 15

Đây là chín quy ước nhóm em tự đặt ra cho mình trước khi bắt tay vào vẽ. Bốn quy
ước đầu đếm ra được thành số, nên cột giữa là số nhóm em đo trên chính mười lăm tệp
mô hình.

Dòng em muốn nhấn là dòng đầu tiên: một hoạt động chỉ được có một luồng vào và một
luồng ra. Trên tổng số một trăm mười ba hoạt động thì nhóm em không sai chỗ nào. Năm
quy ước còn lại phải kiểm bằng mắt, và sáu mô hình nhóm em nộp đều nằm trong ngưỡng
ba mươi phần tử.

### Slide 16

Mô hình đầu tiên là quản lý nhà cung cấp và đặt hàng nhập, đây là quy trình quản lý
thứ nhất.

Trước khi vào nội dung em xin nói một câu về cách trình bày, và hai mô hình sau em
sẽ không nhắc lại nữa. Mô hình này rộng lắm, chiếu nguyên lên một slide thì chữ bé
tới mức thầy không đếm nổi cổng. Cho nên nhóm em cắt nó làm hai băng ngang, và cắt
đúng tại đường kẻ ngăn giữa hai lane.

Dải màu bên trái là số đếm của **cả mô hình**, không phải của riêng băng đang chiếu:
hai pool, bốn lane, mười hai hoạt động, mười cổng điều kiện.

Băng trên có hai chỗ quan trọng. Thứ nhất là hai cấp phê duyệt: đơn trong hạn mức thì
thu mua chốt luôn, đơn vượt hạn mức phải chuyển xuống lane cấp duyệt. Thứ hai là một
sự kiện kết thúc nằm ngay trong băng này, đơn đặt hàng đã bị từ chối; hai kết thúc
còn lại ở băng dưới.

### Slide 17

Băng dưới của cùng mô hình đó gồm lane kho tổng và pool nhà cung cấp.

Thầy nhìn giúp em cặp cổng hình dấu cộng ở khâu nhận hàng. Đó là cổng song song: kho
tổng bố trí mặt bằng nhận hàng, cùng lúc kế toán công nợ chuẩn bị chứng từ ở băng
trên. Hai việc không chờ nhau, và mở bằng loại cổng nào thì đóng bằng đúng loại cổng đó.

Còn một chỗ nữa, pool nhà cung cấp ở dưới cùng. Nó là pool riêng nên mọi trao đổi
với nó đều là luồng thông điệp nét đứt.

Hai sự kiện kết thúc còn lại nằm ở băng này: lô hàng đã được trả lại, và hàng đã vào
tồn khả dụng.

### Slide 18

Đây là thẻ thông tin của mô hình vừa rồi. Ở ý một em xin đọc hai con số để thầy
tiện đối chiếu: trên mô hình có năm vai, tức bốn lane cộng pool nhà cung cấp; còn hồ
sơ ở chương một thì kê bảy tác nhân. Chênh hai tác nhân chính là hai tác nhân không
có lane riêng, lý do nhóm em ghi ngay dưới bảng tác nhân ở mục một chấm năm.

Năm ý trên thẻ đã in sẵn rồi nên em chỉ nói thêm hai ý. Ý hai, khách hàng của quy
trình này là kho tổng và mạng lưới cửa hàng. Ý năm, mô hình có mười cổng điều kiện,
tức là vượt mốc trên bảy cổng.

### Slide 19

Quy trình thứ hai là bảo hành, đổi trả một đổi một và thu hồi máy lỗi. Số đếm cả mô
hình: bốn pool, ba lane, mười hai hoạt động, mười hai cổng điều kiện.

Băng trên là lane nhân viên tiếp nhận, với hai cổng cần nói kỹ.

Cổng thứ nhất là mốc tháng đầu: trong tháng đầu khách được đổi máy mới miễn phí, từ
tháng thứ hai chuyển sang trả hàng chịu phí lũy tiến theo tháng. Mốc này nhóm em vẽ
thành một cổng điều kiện chứ không viết thành tên một hoạt động.

Cổng thứ hai phân loại nguyên nhân lỗi, đặt ngay sau khi trung tâm bảo hành trả kết
luận. Lỗi do nhà sản xuất thì đi nhánh bảo hành. Lỗi do người dùng thì đi nhánh từ
chối kèm báo giá sửa chữa có phí, đóng lại ở sự kiện kết thúc thứ nhất.

### Slide 20

Băng dưới gồm hai lane còn lại là kho hàng đổi và kế toán hoàn tiền, cộng ba pool bên
ngoài: khách hàng, trung tâm bảo hành, hãng sản xuất.

Ba pool đó nằm ngoài ranh giới doanh nghiệp nên mọi trao đổi đều là luồng thông điệp
nét đứt.

Còn một chỗ nữa là ba hướng khép hồ sơ, và ba hướng đó nằm ở ba chỗ khác nhau chứ
không gộp về một chỗ. Đổi máy thì xuất máy từ kho hàng đổi. Hoàn tiền thì kế toán tính số
tiền hoàn sau khi trừ phí rồi chi trả về phương thức gốc. Còn máy lỗi thu hồi thì gom
theo kỳ rồi chuyển trả hãng sản xuất.

### Slide 21

Đây là thẻ thông tin của quy trình bảo hành. Trên hình có sáu vai, trong hồ sơ kê
bảy tác nhân, chênh một chính là hệ thống ERP, lý do nhóm em ghi ở mục một chấm năm.
Khách hàng của quy trình này là khách đã mua máy, tức khách bên ngoài. Và mô hình có
mười hai cổng điều kiện.

### Slide 22

Mô hình thứ ba là tuyển dụng và đào tạo nhân viên bán hàng, quy trình hỗ trợ. Số đếm
cả mô hình: hai pool, bốn lane, mười hai hoạt động, mười hai cổng điều kiện.

Băng trên gồm hai lane, là quản lý cửa hàng và quản lý vùng. Ở băng này có hai chỗ
em muốn nói kỹ.

Chỗ thứ nhất là cổng chọn nguồn ứng viên. Trước khi đăng tin ra ngoài thì quy trình
hỏi một câu: trong vùng có ai điều động sang được không. Nếu có thì đi nhánh điều
động nội bộ, bỏ qua được cả vòng đăng tin lẫn vòng sàng lọc hồ sơ.

Chỗ thứ hai là hai sự kiện kết thúc xấu đóng ngay trong băng này. Một là đề nghị
tuyển bị từ chối vì ngoài định biên. Hai là đã dừng thử việc, tức người đã vào làm
nhưng không qua được kỳ kèm cặp.

### Slide 23

Băng dưới gồm lane bộ phận tuyển dụng, lane bộ phận đào tạo, và pool ứng viên ở dưới
cùng.

Chỗ em mời thầy nhìn là cổng hình ngũ giác ngay sau bước gửi thư mời phỏng vấn. Đó là
cổng dựa trên sự kiện. Nó chờ hai thứ cùng lúc: hoặc ứng viên xác nhận lịch, hoặc hết
hạn phản hồi. Ứng viên xác nhận thì luồng đi tiếp sang phỏng vấn vòng một. Hết hạn thì
luồng rẽ sang đóng đợt tuyển, chứ quy trình không đứng chờ vô hạn.

Chỗ thứ hai là pool ứng viên. Tin tuyển dụng, thư mời phỏng vấn và thư mời nhận việc
đều đi qua ranh giới pool bằng luồng thông điệp nét đứt.

### Slide 24

Đây là thẻ thông tin cuối cùng, của quy trình tuyển dụng. Trên hình có năm vai,
trong hồ sơ kê sáu tác nhân, chênh một là hệ thống quản lý nhân sự. Khách hàng của
quy trình này là cửa hàng đang thiếu người. Mô hình có mười hai cổng điều kiện và
bốn sự kiện kết thúc, trong đó ba cái là nhánh xấu.

### Slide 25

Bảng này gộp cấu trúc của cả sáu mô hình lại một chỗ. Em mời thầy nhìn cột cuối
cùng bên phải.

Thang chấm cho điểm tối đa khi mô hình có trên bảy cổng điều kiện. Mô hình thấp nhất
của nhóm em đã có mười cổng, nghĩa là cả sáu mô hình đều vượt mốc.

Dòng tổng cộng ở cuối bảng: mười bốn pool, hai mươi ba lane, sáu mươi bảy hoạt động
cộng năm hộp sub-process, sáu mươi tám cổng điều kiện. Hai cột hoạt động cộng lại là
bảy mươi hai hộp, đúng bằng số hộp đếm được trên sáu hình.

Còn một điểm nữa ở cột lớp: hai mô hình quản lý, hai mô hình cốt lõi và hai mô hình
hỗ trợ. Đề bài bắt buộc mỗi lớp hai quy trình, và nhóm em chia đúng như vậy chứ
không dồn vào lớp nào dễ vẽ hơn.

## Phần 4 – Ngọc Danh (7,9 phút)

| Slide | Phút | Ý chính | Chuyển tiếp |
|---:|---:|---|---|
| 26 | 0,9 | Hai quy trình chọn phân tích và lý do. C3 chờ thông tin, C4 chờ hàng đợi vật lý. | – |
| 27 | 1,1 | Bảng VA/BVA/NVA hai quy trình, tức **bước hai**. **Nhấn cảnh báo**: đếm bước không thay được đo thời gian. | – |
| 28 | 0,4 | **Bước một**: C4 tô màu phân loại ngay trên mô hình. Chỉ tay vào cụm ba ô đỏ liền nhau. | – |
| 29 | 0,3 | Bước một của C3: ô đỏ chờ thẩm định và ba ô xanh. Nói nhanh, đã nói cách đọc màu ở slide trước. | – |
| 30 | 0,9 | Ba nhóm lãng phí Move, Hold, Overdo, mỗi nhóm có ví dụ thật. | – |
| 31 | 0,9 | Pareto và xương cá. Con số đếm theo số URL phân biệt, không phải theo số ca. | – |
| 32 | 1,3 | **Slide quan trọng nhất phần 4.** CTE 49,3% và 3,17%. Nút thắt là hàng đợi chứ không phải quãng đường. | – |
| 33 | 0,3 | Bước một cho thời gian: PT và WT trên từng bước của C4. Nói rõ 1.920 nằm ở pool bên ngoài. | – |
| 34 | 0,3 | Bước một cho thời gian của C3: vòng bổ sung giấy tờ và WT 60 ph. | – |
| 35 | 0,4 | Ba khía cạnh thời gian, chất lượng, chi phí. **Nói thẳng**: tất cả đều có mã giả định. | – |
| 36 | 0,3 | Bước một cho chi phí của C4. Khoản 70.618 đ nằm ngoài cửa hàng. | – |
| 37 | 0,3 | Bước một cho chi phí của C3. Tiền dồn vào lane nhân viên tư vấn. | – |
| 38 | 0,5 | Năm dòng Issue Register, mỗi vấn đề một đề xuất cụ thể. | "Còn lại là phần kết luận." |

### Slide 26

Sang phần bốn, nhóm em phân tích sâu hai quy trình thuộc lớp cốt lõi. Nhóm em chọn
hai quy trình này vì cả hai đều có tác nhân bên ngoài, và đều có nhánh chờ đủ dài để
đo được. Nhưng cái chờ của hai bên khác hẳn nhau về bản chất.

Ở bán trả góp thì đây là chờ thông tin: chờ khách nộp giấy tờ, rồi chờ kết quả thẩm
định. Mà thông tin thì đi bằng đường số, nên rút xuống còn vài phút là làm được, và
làm được bằng phần mềm.

Còn ở bảo hành thì đây là hàng đợi vật lý: cái máy nằm xếp lượt ở trung tâm bảo
hành. Cái này không phần mềm nào rút ngắn được, vì máy vẫn cứ phải chờ tới lượt.

### Slide 27

Bảng trên phân loại từng bước của hai quy trình theo ba mức giá trị. Em xin nói rõ
đơn vị trước, vì có hai đơn vị chồng nhau. Một hộp trên sơ đồ là một hoạt động, bên
trong nó còn hai tới bốn bước thao tác. Giáo trình yêu cầu phân loại tới mức bước,
nên bảng này đếm bước: quy trình trả góp ra ba mươi sáu bước, quy trình bảo hành ra
bốn mươi bước.

Thầy nhìn giúp em cột không gia tăng giá trị. Hai quy trình gần như bằng nhau, hai
mươi bảy phẩy tám phần trăm và hai mươi bảy phẩy năm phần trăm. Nhìn cột này thì
tưởng hai quy trình lãng phí ngang nhau.

Xuống mức bước còn cho thấy một chỗ mà mức hoạt động giấu mất. Tỷ lệ tạo giá trị của
quy trình bảo hành rơi từ ba mươi ba phẩy ba phần trăm xuống mười hai phẩy năm, vì
mỗi hoạt động trước đây được chấm là tạo giá trị thật ra chỉ chứa đúng một bước khách
sẵn sàng trả tiền.

Nhưng khung bên phải là cảnh báo nhóm em cố ý đặt vào, vì kết luận đó sai. Đếm bước
không thay được cho đo thời gian. Xét theo thời gian thì hiệu suất chu trình của hai
quy trình chênh nhau gần chín lần.

Lý do nằm ở ba ô đỏ của quy trình bảo hành. Trên hình chúng chỉ là ba ô nhỏ, nhưng
chúng nuốt tới chín mươi sáu phẩy tám phần trăm thời gian chu trình. Một ô vuông bé
trên sơ đồ ngoài đời có thể là mấy ngày.

Xin thầy lưu ý bảng này chính là bước hai của phân tích định tính. Hai slide tiếp
theo mới là bước một, tức là phần chú thẳng lên hình vẽ.

### Slide 28

Đây là bước một của phân tích định tính, nhóm em chú phân loại thẳng lên mô hình.
Màu xanh là bước có gia tăng giá trị, vàng là bước cần cho nghiệp vụ, còn đỏ là
không gia tăng giá trị. Thầy nhìn giúp em ba ô đỏ nối liền nhau thành một đoạn ngay
trên băng: chuyển máy đi thẩm định, chờ kết luận, rồi lại chuyển đi sửa.

### Slide 29

Vẫn cách đọc màu như vậy, lần này áp cho bán trả góp. Ô đỏ ở giữa băng là chỗ quy
trình đứng lại: cửa hàng phải chờ kết quả thẩm định từ công ty tài chính. Còn ba ô
xanh là ba bước mà khách thật sự nhận được giá trị.

### Slide 30

Nhóm em gom các lãng phí tìm được về ba nhóm, mỗi nhóm em xin nêu một ví dụ có thật
trong hai quy trình.

Nhóm thứ nhất là Move, tức vận chuyển thừa và thao tác thừa. Ví dụ rõ nhất là chiếc
máy bảo hành phải đi qua nhiều tầng, từ cửa hàng lên trung tâm bảo hành, rồi từ trung
tâm lên hãng sản xuất.

Nhóm thứ hai là Hold, tức tồn kho và chờ đợi. Ví dụ là chiếc máy bị khóa mã IMEI nằm
chờ kết quả thẩm định trả góp. Suốt thời gian đó máy vừa không bán được cho ai, mà
cũng chưa thuộc về khách.

Nhóm thứ ba là Overdo, tức lỗi và xử lý thừa. Ví dụ là thông tin chính sách bảo hành
không nhất quán giữa nhân viên cửa hàng, tổng đài và trang chính sách trên web.

Ba nhóm này quy về bảy lãng phí của Ohno, và mỗi dòng trong bảng đều có cột khắc
phục đi kèm.

### Slide 31

Hai hình này trả lời câu hỏi nguyên nhân gốc nằm ở đâu. Hình bên trái là biểu đồ
Pareto của quy trình bảo hành. Trục ngang là các chủ đề xếp theo số lượt nhắc giảm
dần, còn đường cong là phần trăm cộng dồn.

Ở đây phân bố khá phẳng, không có nguyên nhân đơn lẻ nào trội hẳn lên. Phải gộp tới
bảy chủ đề mới chạm tám mươi hai phẩy bốn phần trăm, tuy nhiên năm chủ đề đầu cũng
đã chiếm sáu mươi bốn phẩy bảy phần trăm rồi.

Em xin nói rõ một quy ước đếm: ba mươi bốn lượt nhắc ở đây là số địa chỉ web phân
biệt, chứ không phải số ca bảo hành. Còn hình bên phải là biểu đồ xương cá, nhóm em
gom các chủ đề đó về từng nhóm nguyên nhân.

### Slide 32

Đây là slide quan trọng nhất trong phần bốn. Quy trình bảo hành có hai con số chờ
lớn nhất: một nghìn chín trăm hai mươi phút chờ tới lượt thẩm định, và hai nghìn tám
trăm tám mươi phút chờ tới lượt sửa. Thầy để ý giúp em, cả hai đều là hàng đợi.

Hai ô trên là số tổng. Bán trả góp: chu trình một trăm ba mươi tám phút, xử lý thật
sáu mươi tám phút, hiệu suất chu trình bốn mươi chín phẩy ba phần trăm. Bảo hành: chu
trình năm nghìn chín trăm năm mươi tám phẩy chín phút, xử lý thật chỉ một trăm tám
mươi tám phẩy chín phút, hiệu suất chu trình ba phẩy mười bảy phần trăm.

Bỏ hẳn vận chuyển mà giữ hàng đợi thì chu trình chỉ giảm mười bảy phẩy bảy phần trăm;
xóa được hàng đợi thì giảm tám mươi hai phần trăm. Hai slide sau ghi chính hai con số
ấy lên mô hình.

### Slide 33

Đây là mô hình bảo hành, lần này nhóm em ghi thời gian xử lý và thời gian chờ lên
từng bước. Thầy nhìn giúp em ô dưới bên trái: bước chuyển máy đi sửa chỉ xử lý mất
ba phút, nhưng chờ tới hai nghìn tám trăm tám mươi phút. Con số lớn thứ hai là một
nghìn chín trăm hai mươi phút, nằm ở nửa dưới mô hình. Hai con số đó chính là hai
hàng đợi em vừa nói ở slide trước.

### Slide 34

Còn đây là bán trả góp, ghi theo đúng cách đó. Trên băng này thầy nhìn giúp em
nhánh thiếu chứng từ quay ngược về bước lập hồ sơ vay: cứ mỗi vòng bổ sung giấy tờ
là thêm mười lăm phút xử lý. Cái chờ ở đây là chờ thông tin, chứ không phải chờ hàng
như bên bảo hành.

### Slide 35

Nhóm em đo trên ba khía cạnh: thời gian, chất lượng và chi phí. Thầy nhìn giúp em
cột cuối ghi mức tin cậy, cả ba đều đang là ước lượng. Nhóm em chưa xuống bấm giờ
tại cửa hàng nên không con số nào đo bằng đồng hồ cả. Bù lại, mỗi giá trị đều mang
một mã giả định, ghi rõ căn cứ suy ra và hệ quả nếu con số đó sai.

### Slide 36

Chi phí ở mỗi ô nhóm em tính bằng thời gian thao tác nhân với đơn giá của vai làm
bước đó. Nhưng khoản đắt nhất lại không nằm trên băng này: kỹ thuật viên ở trung tâm
bảo hành một mình chiếm năm mươi lăm phẩy bảy phần trăm chi phí nhân công của cả quy
trình.

### Slide 37

Còn với bán trả góp thì tiền dồn hết vào lane nhân viên tư vấn. Bốn bước tư vấn,
lập hồ sơ, thương lượng và ký hợp đồng đều cùng một mức chi phí. Lane thu ngân thì
rẻ hơn hẳn, và chênh lệch đó hiện thẳng lên hình, thầy nhìn là thấy ngay.

### Slide 38

Năm dòng này là sổ ghi vấn đề, tiếng Anh là Issue Register. Mỗi dòng gắn với một
vấn đề cụ thể nhóm em đã nêu ở các slide trước, và mỗi vấn đề kèm đúng một đề xuất.

Nhóm em cố ý tránh những đề xuất chung chung kiểu tăng cường hay đẩy mạnh, vì viết
như vậy thì không ai làm được. Và xin thầy lưu ý, ba trong năm đề xuất chỉ cần chỉnh
trên hệ thống ERP hiện có, không phải đầu tư thêm.

## Phần 5 – Ngọc Danh (0,7 phút)

**Nghỉ vài giây trước khi vào phần này.** Hai slide cuối đều là bảng in sẵn, nói chậm
lại được. Lấy hơi rồi mới vào, vì ngay sau đó là phần hỏi đáp.

| Slide | Phút | Ý chính | Chuyển tiếp |
|---:|---:|---|---|
| 39 | 0,5 | Bốn mục tiêu và mức đạt. Nói thật mục tiêu thứ ba mới đủ công cụ, chưa triển khai. | – |
| 40 | 0,2 | Cảm ơn, mời thầy và các bạn đặt câu hỏi. | – |

### Slide 39

Bảng này đối chiếu bốn mục tiêu nhóm em đặt ra từ đầu với mức thực tế đạt được. Ba
mục tiêu đã hoàn thành trọn vẹn.

Riêng mục tiêu thứ ba dừng ở mức chuẩn bị: nhóm em đã dựng đủ bộ công cụ khám phá,
nhưng chưa triển khai tại cửa hàng. Đây cũng chính là hướng phát triển gần nhất của
đề tài, đưa bộ câu hỏi đã soạn ra chạy thật kèm một buổi quan sát tại cửa hàng.

### Slide 40

Phần trình bày của nhóm em xin hết. Em cảm ơn thầy và các bạn đã lắng nghe. Cả bốn
thành viên nhóm em đều đang có mặt và sẵn sàng nhận câu hỏi của thầy ạ.

---

## Việc phải làm trước buổi báo cáo

- [ ] **Chạy thử một mình có bấm giờ.** Lần chạy đầu thường vượt 40%.
- [ ] Chạy thử lần hai, cắt bớt câu ở phần nào vượt. Trần cứng vẫn là 30 phút.
- [ ] Đánh dấu sẵn hai chỗ nghỉ: trước phần 3 và trước phần 5. Có chai nước trong tầm tay.
- [ ] **Cả bốn thành viên bật camera**, không riêng người nói. Cả hai buổi thầy đều điểm danh từng người trước khi cho bắt đầu, và rubric ghi rõ không bật thì điểm trình bày thấp hơn nhóm khác.
- [ ] Mở sẵn file `bao-cao.pptx` **và** `bao-cao.pdf` phòng khi máy chiếu lỗi font.
- [ ] Kiểm tra hình BPMN khi phóng to trên máy chiếu có bị nhòe không – thầy đã bắt lỗi này ở hai nhóm.
- [ ] Đọc lại [du-kien-cau-hoi.md](du-kien-cau-hoi.md). Một người nói thì người đó phải thuộc cả năm phần, nhưng ba bạn còn lại vẫn đỡ được câu hỏi thuộc mảng mình làm.
- [ ] Kiểm tra MSSV trên slide bìa khớp mã đã đăng ký – thầy nói sai tên thì không sao, sai MSSV mới có sao.

## Nhắc về cơ chế chấm

Thầy chấm **trên slide**, không chấm lời nói: *"nói miệng lỡ lúc đó thầy quay qua quay
lại hoặc đi uống nước một phát là quên, mất điểm rồi"*. Hệ quả đúng của câu đó là:
thứ gì ăn điểm thì phải **nằm trên slide**. Ba thẻ thông tin in sẵn đủ năm ý cho thầy
đối chiếu, nên lời nói chỉ thêm hai con số tác nhân rồi lấy ý ② và ⑤. Ngược lại, thứ
**không** in trên slide mà chỉ định nói miệng thì coi như không có, nên đừng để ý nào
của rubric rơi vào diện đó.

Điểm buổi báo cáo chiếm khoảng 20–30%; báo cáo Word chấm sau đó một tuần và chiếm
70–80%. Nghĩa là mọi nhận xét thầy nói trong buổi **còn kịp sửa vào Word** trước khi nộp.
