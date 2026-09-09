# Chương 4 – Phân tích định tính quy trình C3 và C4

Phục vụ Tiêu chí 4.1 của rubric. Hai quy trình được chọn theo `04-phan-tich-quy-trinh.md` mục 1:

| Mã | Quy trình | Lý do chọn |
|---|---|---|
| **C3** | Bán trả góp qua công ty tài chính | Ba bên tham gia, nhiều bàn giao giữa các lane, có hai điểm chờ nằm ngay trên đường chính |
| **C4** | Bảo hành, đổi trả 1 đổi 1 và thu hồi máy lỗi | Có mốc cam kết công bố để neo số (1 tháng, 15 ngày, phí 20% / 10% / 5% / 2%), và máy phải rời cửa hàng rồi quay về |

---

## 0. Nguồn của các bước và quy ước đọc bảng

### 0.1 Danh sách bước lấy từ đâu

Phân tích bám trực tiếp hai file mô hình thật:

- `do-an/bpmn/C3-ban-tra-gop.bpmn`, hình xuất kèm: `do-an/bpmn/C3-ban-tra-gop.png`
- `do-an/bpmn/C4-bao-hanh-doi-tra.bpmn`, hình xuất kèm: `do-an/bpmn/C4-bao-hanh-doi-tra.png`

Mọi mã hoạt động trong các bảng dưới đây (`T1`, `IE1`, `G6`, `E2`…) là `id` thật trong file XML, tra ngược được từng dòng bằng cách mở file trên <https://demo.bpmn.io>. Nhãn hoạt động trong cột "Hoạt động" chép nguyên văn thuộc tính `name` của phần tử; phần trong ngoặc là chú giải của nhóm, không phải nhãn trên hình. Phân tích không bám bản phác thảo ở `02-mo-hinh-hoa-bpmn.md`.

Bước thao tác thì không đọc thẳng ra được từ file `.bpmn`. Một hộp trên sơ đồ BPMN là một *hoạt động*, còn `chap05.pdf` trang 8 yêu cầu phân tích giá trị gia tăng phải *"chia nhỏ quy trình thành các bước"* rồi *"phân loại từng bước"*. Vì vậy mỗi hoạt động của C3 và C4 được nhóm phân rã tiếp thành các bước thao tác, và phần phân rã này suy từ bốn thứ đã có trên mô hình chứ không đặt thêm giả định nghiệp vụ nào:

| Suy từ đâu | Cho ra phần nào của bước | Ví dụ |
|---|---|---|
| Nhãn `name` của task | Các thao tác ghép trong một hoạt động | `T1 Sàng lọc sơ bộ và trình bày phương án trả góp` tách thành phần sàng lọc và phần trình bày |
| Lane chứa task | Cột "Người thực hiện", và các điểm đổi lane trên chuỗi tuần tự | `T9` ở lane Thu ngân nằm ngay sau `T8` ở lane NV tư vấn, nên có một bước bàn giao ca |
| Message flow đi ra hoặc đi vào task | Bước gửi và bước nhận tài liệu | `MF5` đi ra từ `T8` của C3 thành bước gửi hợp đồng đã ký |
| Nhánh quay lui và annotation | Bước chỉ chạy trên một nhánh | Vòng `G12` → `G13` của C3 thành bước bổ sung chứng từ, trần 2 lượt theo annotation `A7` |

Số bước mỗi hoạt động nằm trong khoảng 2 tới 4. Hoạt động nào không tách được thì để một dòng và ghi rõ lý do ngay trong ô, như `IE2` của C3 – sự kiện thời gian, không có người thao tác.

### 0.2 Kết quả đối chiếu với file `.bpmn` thật

Đã chạy đối chiếu tự động giữa file XML và các bảng dưới đây. Kết quả:

| Nội dung kiểm | C3 | C4 |
|---|---|---|
| Số hoạt động và mốc (task + event) trên cả hai hình của quy trình | 18 | 18 |
| Số hoạt động và mốc có mặt trong bảng giá trị gia tăng | 18 | 18 |
| Mã hoạt động thiếu / thừa / trùng lặp | 0 / 0 / 0 | 0 / 0 / 0 |
| Nhãn `name` khớp nguyên văn | Đủ 18 | Đủ 18 |
| Lane của từng hoạt động khớp với cột "Người thực hiện" | Khớp | Khớp |
| Thứ tự dòng khớp với `sequenceFlow` | Khớp | Khớp |
| Số bước phân rã từ các hoạt động được phân loại | 36 bước từ 14 hoạt động | 40 bước từ 15 hoạt động |

Mỗi quy trình nay trải trên hai file `.bpmn`. Sau đợt làm lại hình (R6), mỗi mô hình gói một đoạn vào sub-process thu gọn `SP1` và vẽ đoạn đó thành một hình chi tiết riêng. Không mã nào và không nhãn nào bị đổi: các hoạt động được gói chỉ chuyển sang file kia:

| Quy trình | Hoạt động nằm ở hình khung | Hoạt động nằm ở hình chi tiết |
|---|---|---|
| C3 | 16 hoạt động và mốc trong `C3-ban-tra-gop.bpmn` | `T10`, `T11` trong `C3a-giao-may-cho-khach.bpmn` (cùng hai luồng `MF6`, `MF7`) |
| C4 | 16 hoạt động và mốc trong `C4-bao-hanh-doi-tra.bpmn` | `T12`, `T13` trong `C4a-khep-ho-so-xu-ly.bpmn` (cùng luồng `MF7`) |

Phép đối chiếu ở bảng trên chạy trên hợp của hai file, và vẫn ra đủ 18/18 cho cả hai quy trình.

Bảng đếm cấu trúc trong `bpmn/thong-ke.md` cũng khớp với `docs/ch2-dac-ta-bpmn.md`: trên hình khung, C3 có 11 task (10 task thật + hộp `SP1`), 6 event, 15 gateway; C4 có 13 task (12 task thật + hộp `SP1`), 4 event, 12 gateway. Cộng thêm phần trong sub-process thì C3 có 17 cổng và C4 có 14 cổng. Không phải sửa mã hay nhãn nào của phần phân tích: gateway không có mặt trong bảng giá trị gia tăng và không tiêu tốn thời gian trong bảng thời gian chu kỳ, còn danh sách 18 hoạt động và mốc không phải gateway của cả hai mô hình vẫn nguyên vẹn cả về mã, nhãn lẫn thứ tự.

Ba việc mô hình đã chốt sau đợt soát ký pháp (phiên R7, sửa trong `docs/ch2-dac-ta-bpmn.md` rồi sinh lại file `.bpmn`):

| # | Chỗ treo trước đây | Đã chốt thế nào | Ảnh hưởng tới các bảng dưới |
|---:|---|---|---|
| 1 | Không có `messageFlow` nào đưa **máy lỗi** từ pool Trung tâm Bảo hành về cửa hàng, trong khi `T14 Nhập máy lỗi thu hồi` chạy trên cả ba nhánh vì nằm sau cặp AND `G11`–`G12` | **Thêm `MF9 Máy lỗi trả về cửa hàng`** từ pool Trung tâm Bảo hành vào `T14`, thay vì đẩy `T14` xuống từng nhánh. Chọn cách thêm message flow vì nó không đụng mã, nhãn hay thứ tự hoạt động nào – đẩy `T14` xuống nhánh sẽ làm lệch cả bảng 4.10 và 4.11 của `dinh-luong.md`. Riêng nhánh sửa chữa không có máy lỗi để thu hồi: ghi rõ ở annotation `A11` của mô hình chứ không giấu | **Không đổi số nào.** Chiều về của nhánh đổi máy và hoàn tiền nay đã có trên hình, nên ô "Quy mô ước tính" của nhóm **Move** ở bảng 4.4 đọc thẳng được từ mô hình. Câu *"chiều về chưa được mô hình hóa"* trong bảng 4.4 **đã bỏ**. Số lượt vận chuyển bình quân 1,45 của `dinh-luong.md` Bảng 4.13 được đếm từ trước khi có `MF9`, nên đã đếm lại ở `I-11` và ra **1,75 lượt/ca** – rồi lên **2,00** sau khi dòng 6 dưới đây thêm nốt `MF10` |
| 2 | Nhãn `T10 Chuyển máy đi sửa` mâu thuẫn nhãn `MF5 Yêu cầu sửa chữa theo cam kết bảo hành` – hai cách đọc cho ra số lượt vận chuyển khác nhau | **Chốt theo cách đọc "máy nằm lại Trung tâm Bảo hành"**, đúng như bảng 4.4 đang tính. Sửa **nhãn `MF5`** thành `Yêu cầu sửa chữa, máy đang giữ tại trung tâm`; nhãn `T10` **giữ nguyên** vì Chương 4 chép nguyên văn nó, còn `MF5` thì không | **Không đổi số nào** – bảng 4.4 vốn đã đọc theo `MF5`. Hai chỗ ghi nguyên văn nhãn cũ của `MF5` (bảng 4.2 dòng `T10` và bảng 4.4 nhóm Move) **đã thay** chuỗi trích dẫn |
| 3 | **Vòng làm lại "bổ sung giấy tờ" của C3 không có trên mô hình**, dù `dinh-luong.md` tính nó chiếm 20% hồ sơ và 60,7% thời gian chờ | **Đã vẽ.** `G12 Hồ sơ đủ chứng từ theo yêu cầu bên cho vay?` đặt ngay sau `IE1`; nhánh "Thiếu chứng từ" quay ngược về `G13` – một XOR join mới đặt trước cặp AND `G3`–`G4` – để chạy lại `T4` và chờ thẩm định thêm một vòng | **Không đổi số nào.** Mỗi lượt quay lui tốn `max(T4 15, T5 3) = 15` phút, khớp đúng cách bảng 4.9 đang tính *"duyệt thẳng + T4 làm lại 15"*. Câu *"kịch bản này không có trên mô hình"* ở mục 2.2 của `dinh-luong.md` **đã bỏ**, thay bằng dòng trỏ tới `G12` và `G13`. Vòng quay lui này nay có một bước riêng trong bảng 4.1, mã `T4.4` |

Cùng đợt đó, C3 thêm `G14` và `G15`, C4 thêm `G13` và `G14`, bốn XOR join gỡ lỗi *"Mỗi hoạt động phải có 1 luồng vào và 1 luồng ra"* (`chap04` trang 39). Đây là bốn cổng thuần thêm mới; không mã, nhãn hay thứ tự hoạt động nào của C3 và C4 bị đổi, trừ đúng nhãn `MF5` nêu ở dòng 2.

Ba việc mô hình chốt tiếp ở đợt soát logic 08/09/2026. Ba lỗi này khác ba việc trên: chúng không phải chuyện ký pháp mà là chuyện đúng sai nghiệp vụ, đúng thứ thầy nói sẽ chấm trên bản Word. Cả ba do chính nhóm bắt ra và treo trong Issue Register từ trước buổi báo cáo 07/09.

| # | Chỗ treo | Đã chốt thế nào | Ảnh hưởng tới các bảng dưới |
|---:|---|---|---|
| 4 | `I-08` – máy bị khóa IMEI ở nhánh hồ sơ bị từ chối **không có bước nào giải phóng**: `T6` chỉ có đường vào từ `IE2` và `G9` | **Thêm cổng XOR `G16 Máy đang bị khóa IMEI và giữ trên ERP?`** ngay sau `T2`. Nhánh "Đang giữ máy" gộp ở `G15` rồi chạy `T6` → `E3`; nhánh "Chưa giữ máy" đi thẳng `E2` cho ca bị `G1` chặn từ bước sàng lọc, tức chưa hề khóa máy. Không mã, nhãn hay thứ tự hoạt động nào bị đổi | **Có đổi số.** `T6` nay chạy trên 15% hồ sơ nên `dinh-luong.md` Bảng 4.12 lên 64.558 đ nhân công và 65.904 đ một ca; Bảng 4.9 kịch bản từ chối lên PT 43 · CT 113. Bảng 4.1 và bảng căn cứ của file này **không đổi**: `G16` là cổng, mà cổng không có mặt trong bảng giá trị gia tăng |
| 5 | `I-09` – nhánh trả góp **qua thẻ tín dụng** vẫn đi qua `T8 Ký hợp đồng vay với công ty tài chính`, thứ không tồn tại ở hình thức thanh toán đó | **Thêm XOR join `G17`** giữa `T8` và `T9`: `G8` chỉ còn gom hai nhánh của đường vay, `T3` của nhánh thẻ nhập lại ở `G17`. Không chọn cách đổi nhãn `T8` vì Bảng 4.1 và bảng căn cứ của file này chép nguyên văn nhãn ấy | **Không đổi số nào.** Mọi bảng định lượng của C3 lấy `GT22` làm mẫu số, tức chỉ đếm nhánh đi qua công ty tài chính, nên nhánh thẻ vốn có trọng số 0 |
| 6 | Nhánh **"Từ chối"** của C4 – 25% số ca theo `GT26` – không có đường đưa máy về cửa hàng cho khách, dù ba nhánh kết cục còn lại đều có chiều về | **Thêm message flow `MF10 Máy trả về cửa hàng cho khách`** từ pool Trung tâm Bảo hành vào `T4`, kèm annotation `A12`. Cùng cách đã dùng cho `MF9` ở dòng 1: thuần thêm, không đụng mã, nhãn hay thứ tự | **Có đổi số.** Số lượt vận chuyển bình quân của `dinh-luong.md` Bảng 4.13 lên **2,00 lượt/ca**; kéo theo chi phí một ca C4, tỷ số C4/C3, bậc thang quy mô và cột `I-03` của biểu đồ Pareto tiền C4 ở mục 3.3 file này |

Ngoài sáu điểm trên, cả hai mô hình không có chỗ nào lệch so với phân tích. Ba ô "cần rà lại Chương 4" ở cột cuối đã được rà ở phiên R10, và số lượt vận chuyển của C4 nay đã chốt ở `I-11`.

### 0.3 Đơn vị liệt kê trong bảng giá trị gia tăng

Bảng giá trị gia tăng làm việc trên hai đơn vị chồng lên nhau. Đơn vị của mô hình là hoạt động, tức một hộp trên sơ đồ BPMN, và cột "Hoạt động" giữ đúng danh sách 18 phần tử của mỗi quy trình để tra ngược được về file `.bpmn`. Đơn vị của phân tích giá trị là bước, và cột "Phân loại" chấm điểm ở mức bước, đúng câu *"phân loại từng bước"* ở `chap05.pdf` trang 8. Mọi tỷ lệ VA / BVA / NVA trong chương này đếm theo bước, không đếm theo hoạt động.

| Loại phần tử | Có đưa vào bảng không | Có phân rã thành bước không | Có tính vào tỷ lệ VA / BVA / NVA không |
|---|---|---|---|
| Task (hoạt động) | Có | Có, 2 tới 4 bước tùy hoạt động | Có, tính theo số bước |
| Intermediate event (sự kiện trung gian mang thời gian chờ) | Có | Có, khi tách được quãng chờ ra khỏi việc nhận và đọc kết quả | Có – chờ là NVA theo định nghĩa slide chương 5 trang 13 |
| Start event, End event | Có, đánh dấu `– (mốc)` | Không | **Không** – là mốc bắt đầu và kết quả, không phải hoạt động |
| Gateway | Không | Không | Không – là điểm quyết định, không tiêu tốn công việc đáng kể |

Nhờ vậy C3 có 18 dòng hoạt động và mốc, trong đó 14 hoạt động được phân loại và phân rã thành 36 bước; C4 có 18 dòng, trong đó 15 hoạt động được phân loại và phân rã thành 40 bước. Phạm vi vẫn đúng bằng phạm vi mô hình, chỉ khác độ mịn.

### 0.4 Ba nguyên tắc thận trọng, giữ nguyên lối của bài tập ngày 04/08

1. Không gọi mọi bước kiểm tra là lãng phí. Việc thẩm định của Công ty tài chính (C3) và của Trung tâm Bảo hành (C4) là BVA: nó chặn rủi ro tín dụng và chặn gian lận bảo hành. Hơn nữa cả hai đều nằm trong pool hộp đen, tức không phải bước của quy trình cửa hàng nên không xuất hiện trong bảng. Cái được kết luận là lãng phí chỉ gồm: quãng chờ kết luận (IE1) và việc lặp lại một thao tác đã làm ở quầy.
2. Không đủ dữ kiện thì ghi thẳng. Ô nào không có căn cứ thì ghi "chưa đủ dữ kiện để kết luận" kèm cách thu thập số thật, không suy diễn.
3. Số ước lượng phải tự khai báo. Mọi giá trị do nhóm suy ra đều mang chữ (ước lượng) ngay trong ô. Số lấy từ nguồn công khai ghi kèm mã nguồn và cỡ mẫu. Nguyên tắc này áp cho cả phần phân rã bước: bản thân cách chia hoạt động thành bước là quy ước phân tích của nhóm chứ không phải số đo tại cửa hàng, khai ở `GT44` của `dinh-luong.md`; ba bước có nội dung nhóm tự suy thêm được đánh dấu ngay trong ô và tra về `GT45` (lượt đi lấy máy từ kho ra quầy) và `GT46` (máy chờ chuyến tại quầy tiếp nhận C4).

### 0.5 Ký hiệu nguồn dùng chung

| Ký hiệu | Nghĩa |
|---|---|
| `BH1`…`BH9`, `TG1`…`TG5` | Mã chủ đề trong bảng mã hóa `evidence/nghien-cuu-thu-cap/bao-cao-nguon-thu-cap.md` mục 2.1 và 2.2, thu thập 19/08/2026 |
| `T4.2`, `IE1.1` | Mã bước: mã hoạt động trên mô hình, dấu chấm, số thứ tự bước bên trong hoạt động đó |
| "n nguồn" | Số **URL phân biệt** công khai nhắc tới chủ đề. **Không phải** số ca, không phải tỷ lệ của doanh nghiệp |
| "(ước lượng)" | Nhóm tự suy, chưa kiểm chứng, phải có dòng giả định tương ứng ở phần định lượng |
| "(công bố)" | Số do doanh nghiệp tự công bố trên trang chính sách hoặc tin tuyển dụng |

---

## 1. Phân tích giá trị gia tăng

Slide chương 5 chia phần này làm hai bước, và bài làm đủ cả hai.

Bước một chú VA / BVA / NVA lên chính sơ đồ quy trình, để nhìn được các cụm cùng màu nằm ở đâu trên đường đi. Bốn hình `C3-va`, `C3a-va`, `C4-va` và `C4a-va` ở mục 1.1 và 1.2 làm việc này. Bước hai lập bảng, theo đúng khuôn ba cột `Step – Performer – Classification` ở `chap05.pdf` trang 15, mở rộng thêm bốn cột cho hợp với việc phải bắc cầu sang phần thiết kế màn hình.

Hai bước này khác nhau ở độ mịn, và khác một cách có chủ đích. Hình giữ ở mức hoạt động, bảng xuống mức bước. Lý do là hộp trên sơ đồ BPMN vốn là một hoạt động: muốn vẽ bước lên hình thì phải bung mỗi hộp thành hai tới bốn hộp con, C3 sẽ nhảy từ 18 lên 36 hộp và C4 từ 18 lên 40 hộp, cộng thêm 15 và 14 cổng điều kiện. Mô hình phình ra như vậy thì mất hẳn khả năng đọc trên khổ giấy in, mà cũng không còn là mô hình quy trình nữa – nó thành sơ đồ thao tác. Nhóm chọn giữ mô hình nộp ở mức hoạt động, đúng phạm vi Chương 2, và đẩy toàn bộ độ mịn xuống bảng. Cột "Hoạt động" của bảng mang đúng mã và nhãn của hộp trên hình, nên đặt hình cạnh bảng là đối chiếu được từng hộp một.

Tiêu chí phân loại theo slide chương 5 (`chap05.pdf` trang 8, 11, 13):

| Loại | Tiêu chí nhận biết |
|---|---|
| **VA** | Khách hàng sẵn sàng trả tiền cho bước này; bỏ đi thì khách thấy dịch vụ kém giá trị hơn |
| **BVA** | Khách không trả tiền cho nó, nhưng doanh nghiệp cần để vận hành, tạo doanh thu hoặc tuân thủ quy định |
| **NVA** | Mọi thứ còn lại: bàn giao, chuyển đổi, chờ đợi, chậm trễ, làm lại, sửa lỗi |

Bảy cột của bảng đọc như sau. STT đánh số liên tục theo bước, mốc bắt đầu và mốc kết thúc để trống vì không phải bước. Hoạt động ghi mã và nhãn nguyên văn ở dòng đầu của mỗi hoạt động, các dòng bước tiếp theo chỉ lặp lại mã. Bước mở đầu bằng mã bước rồi tới thao tác. Người thực hiện lấy từ lane chứa hoạt động, bước nào do hệ thống chạy thì ghi rõ là hệ thống. Phân loại chấm ở mức bước, nên trong cùng một hoạt động có thể vừa có bước VA vừa có bước NVA. Nhóm lãng phí chỉ điền cho dòng NVA, theo bảy dạng của Ohno ở `chap05.pdf` trang 19-25. Màn hình cần có ghi màn hình nào phục vụ bước đó, nội dung gì phải hiện và ràng buộc nào phải chặn.

### 1.1 Bảng 4.1 – C3 Bán trả góp qua công ty tài chính

Hai hình dưới đây là bước một: tô từng hoạt động của C3 theo ba loại, xanh là VA, vàng là BVA, đỏ là NVA; mốc bắt đầu, mốc kết thúc, cổng điều kiện và hộp sub-process thu gọn để trắng vì chúng không phải hoạt động. Bố cục hai hình giữ nguyên hình mô hình C3 ở Chương 2 – không đổi nhãn, không đổi kích thước hộp nào – nên đặt cạnh hình gốc là đối chiếu được từng hộp một. Hình thứ hai là phần bên trong hộp `SP1`, chứa hai hoạt động còn lại của quy trình.

Màu trên hình là màu của hoạt động, và nó lấy theo loại chiếm phần lớn thời gian của hoạt động đó. Bảng phía sau mới cho thấy phân loại thật ở mức bước, và ở bảy trong mười bốn hoạt động của C3 thì một hộp cùng màu trên hình lại chứa các bước khác loại nhau.

@@FIG:va-C3@@

@@FIG:va-C3a@@

@@BANGNGANG@@

| STT | Hoạt động | Bước | Người thực hiện | Phân loại | Nhóm lãng phí | Màn hình cần có: nội dung và ràng buộc |
|---:|---|---|---|---|---|---|
| – | E1 – Khách đã chọn hình thức thanh toán trả góp (start event dạng message, nhận qua MF1) | Mốc kích hoạt quy trình, không phải thao tác nên không phân rã | Khách hàng, pool ngoài | – (mốc) | – | Màn đặt trước trên app: cho khách khai giấy tờ và chọn công ty tài chính trước khi tới quầy; chỉ mở hồ sơ nháp sau khi khách xác thực số điện thoại |
| 1 | T1 – Sàng lọc sơ bộ và trình bày phương án trả góp | T1.1 Hỏi giấy tờ tùy thân, độ tuổi và đối chiếu với điều kiện tối thiểu của từng bên cho vay | NV tư vấn trả góp | BVA | – | Màn tư vấn trả góp: hiện điều kiện tối thiểu của từng công ty tài chính theo tuổi, giấy tờ và thu nhập; chặn chuyển sang bước chọn gói khi khách không đạt điều kiện của bên nào |
| 2 | T1 | T1.2 Trình bày các gói trả góp: lãi suất, số tháng, mức trả trước | NV tư vấn trả góp | VA | – | Cùng màn: bảng so sánh gói của các bên cho vay đặt cạnh nhau theo đúng model máy khách chọn (annotation A1) |
| 3 | T1 | T1.3 Tính thử lịch trả hằng tháng và chốt gói khách chọn | NV tư vấn trả góp | VA | – | Cùng màn: lịch trả từng tháng và tổng số tiền phải trả; chặn sang T4 khi chưa ghi gói khách chốt vào đơn |
| 4 | T2 – Tư vấn phương án thay thế cho khách | T2.1 Nêu lý do không đạt điều kiện sơ bộ và các phương án còn lại | NV tư vấn trả góp | BVA | – | Màn phương án thay thế: hiện lý do loại theo đúng tiêu chí đã kiểm ở T1.1, không để nhân viên tự diễn giải |
| 5 | T2 | T2.2 So sánh phương án thay thế (thẻ tín dụng, hạ cấu hình, giảm kỳ hạn) và ghi nhận lựa chọn của khách | NV tư vấn trả góp | BVA | – | Cùng màn: ba phương án chuẩn kèm điều kiện; bắt chọn một lý do dừng từ danh mục cố định trước khi đóng đơn, để đo được tỷ lệ ca rơi vào E2 |
| – | E2 – Giao dịch trả góp đã dừng, khách chuyển phương án khác (end event) | Kết quả kết thúc, không phải thao tác | – | – (mốc) | – | Màn báo cáo ca dừng: đếm ca theo từng luồng vào E2 (G1, G6, G7) để biết mất khách ở đâu |
| 6 | T3 – Lập giao dịch trả góp qua thẻ tín dụng | T3.1 Nhập thẻ và chọn kỳ hạn chuyển đổi trả góp trên máy POS | Thu ngân | VA | – | Màn giao dịch POS trả góp: danh sách ngân hàng có chương trình chuyển đổi, phí chuyển đổi, kỳ hạn cho phép; chặn chọn kỳ hạn ngân hàng không hỗ trợ cho hạng thẻ đó |
| 7 | T3 | T3.2 Ký biên lai và lập hóa đơn cho giao dịch | Thu ngân | BVA | – | Cùng màn: hóa đơn điện tử sinh thẳng từ giao dịch POS; không cho đóng ca khi hóa đơn chưa phát hành |
| 8 | T4 – Lập hồ sơ vay và tải chứng từ lên hệ thống bên cho vay | T4.1 Nhập thông tin khách và điều kiện khoản vay vào hệ thống bên cho vay | NV tư vấn trả góp | BVA | – | Màn hồ sơ vay: biểu mẫu theo đúng bên cho vay đã chọn; kiểm định dạng số căn cước và số điện thoại ngay khi nhập |
| 9 | T4 | T4.2 Chụp và tải chứng từ theo danh mục của bên cho vay | NV tư vấn trả góp | BVA | – | Cùng màn: checklist chứng từ sinh theo bên cho vay và theo giá trị khoản vay, kèm trạng thái từng chứng từ; chặn tải ảnh mờ không đọc được số |
| 10 | T4 | T4.3 Đối chiếu bộ chứng từ rồi gửi hồ sơ đi thẩm định qua MF2 | NV tư vấn trả góp | BVA | – | Cùng màn: nút gửi bị khóa khi còn chứng từ thiếu và chỉ rõ chứng từ nào thiếu (đối phó TG1) |
| 11 | T4 | T4.4 Bổ sung chứng từ thiếu và nộp lại, chỉ chạy trên vòng quay lui qua G12 | NV tư vấn trả góp | **NVA** | Defects | Cùng màn: khung ghi yêu cầu bổ sung của bên cho vay và bộ đếm số lượt bổ sung; trần 2 lượt theo annotation A7, quá thì đẩy lên quản lý cửa hàng |
| 12 | T5 – Khóa số IMEI và giữ máy trên ERP (service task) | T5.1 Chọn máy theo IMEI trong tồn kho và chuyển sang trạng thái giữ | Hệ thống ERP, lane Kho cửa hàng | BVA | – | Màn giữ máy theo IMEI: IMEI, model, mã hồ sơ vay gắn kèm; chặn khóa IMEI khi hồ sơ chưa gửi đi thẩm định ở T4.3 |
| 13 | T5 | T5.2 Ghi hạn giữ máy và gắn hồ sơ vay vào máy đã giữ | Hệ thống ERP, lane Kho cửa hàng | BVA | – | Cùng màn: đồng hồ đếm ngược hạn giữ; hạn giữ đặt theo nhóm rủi ro hồ sơ chứ không dùng một hạn chung (annotation A2) |
| 14 | IE1 – Kết quả thẩm định đã nhận (intermediate message event, nhận qua MF3 từ pool Công ty tài chính) | IE1.1 Hồ sơ nằm trong hàng chờ thẩm định phía bên cho vay | Công ty tài chính, pool hộp đen; phía cửa hàng không ai làm gì | **NVA** | Waiting | Màn theo dõi hồ sơ chờ: danh sách hồ sơ đang chờ, số giờ đã chờ, hạn giữ máy còn lại; cảnh báo khi đã dùng hết 70% hạn giữ |
| 15 | IE1 | IE1.2 Nhận thông báo kết quả, mở đọc và ghi kết luận vào hồ sơ vay | NV tư vấn trả góp | **NVA** | Unnecessary transportation | Cùng màn: kết quả do bên cho vay đẩy về tự ghi vào hồ sơ, không phải gõ lại; chặn sang T7 hoặc T8 khi chưa có mã kết luận |
| 16 | IE2 – Hết thời hạn giữ máy chờ hồ sơ (intermediate timer event) | IE2.1 Đồng hồ hạn giữ chạy hết mà chưa có kết luận. Không tách được thành thao tác vì đây là sự kiện thời gian, không có người làm | Quản lý cửa hàng nhận cảnh báo | **NVA** | Waiting | Không có màn hình thao tác. Cần cảnh báo tự động đẩy ca treo về màn quản lý, kèm IMEI và số ngày đã giữ |
| 17 | T6 – Giải phóng máy về tồn bán và hủy đơn | T6.1 Mở khóa IMEI và trả máy về trạng thái bán được | Quản lý cửa hàng | **NVA** | Over-production | Màn xử lý ca hết hạn giữ máy: IMEI, số ngày đã giữ, mã hồ sơ; thao tác giải phóng chạy tự động, người chỉ xác nhận |
| 18 | T6 | T6.2 Hủy đơn và đóng hồ sơ vay trên hệ thống bên cho vay | Quản lý cửa hàng | **NVA** | Over-production | Cùng màn: bắt chọn lý do đóng từ danh mục cố định, không cho để trống, để mục 4 đếm được tỷ lệ nhánh |
| – | E3 – Đơn đã hủy, máy được giải phóng về tồn bán (end event) | Kết quả kết thúc, không phải thao tác | – | – (mốc) | – | Màn báo cáo ca hủy: tỷ lệ ca rơi vào mốc này là chỉ số trực tiếp của lãng phí Hold và Over-production |
| 19 | T7 – Thương lượng mức trả trước và kỳ hạn mới với khách | T7.1 Đọc điều kiện duyệt có điều kiện và tính lại lịch trả theo mức trả trước mới | NV tư vấn trả góp | VA | – | Màn thương lượng điều kiện vay: điều kiện gốc và điều kiện bên cho vay đề nghị đặt cạnh nhau, kèm lịch trả theo từng mức trả trước |
| 20 | T7 | T7.2 Trình bày phương án mới cho khách qua MF4 và chốt lựa chọn | NV tư vấn trả góp | VA | – | Cùng màn: chỉ cho chốt trong khung điều kiện bên cho vay đã duyệt; ghi lại số vòng thương lượng của mỗi hồ sơ |
| 21 | T8 – Ký hợp đồng vay với công ty tài chính | T8.1 Xuất hợp đồng vay theo mẫu bên cho vay và giải thích các điều khoản chính | NV tư vấn trả góp | BVA | – | Màn hợp đồng vay: bản hợp đồng điền sẵn từ hồ sơ, đánh dấu các điều khoản bắt buộc đọc cho khách |
| 22 | T8 | T8.2 Khách và nhân viên ký đủ chữ ký trên bộ hợp đồng | NV tư vấn trả góp | BVA | – | Cùng màn: danh sách chữ ký còn thiếu; chặn sang T9 khi bộ hợp đồng chưa đủ chữ ký |
| 23 | T8 | T8.3 Gửi hợp đồng đã ký về bên cho vay qua MF5 | NV tư vấn trả góp | **NVA** | Unnecessary transportation | Cùng màn: trạng thái gửi và biên nhận của bên cho vay; nếu ký điện tử thì bước này chạy nền, bỏ được thao tác in, quét và gửi lại |
| 24 | T9 – Thu khoản trả trước và lập hóa đơn | T9.1 Bàn giao ca từ quầy tư vấn sang quầy thu ngân và nhắc lại nội dung đơn | NV tư vấn trả góp chuyển cho Thu ngân | **NVA** | Unnecessary transportation | Màn thu ngân giao dịch trả góp mở thẳng bằng mã đơn, không nhập lại; mọi trường của đơn ở trạng thái chỉ đọc |
| 25 | T9 | T9.2 Thu khoản trả trước bằng tiền mặt hoặc chuyển khoản | Thu ngân | BVA | – | Cùng màn: số tiền trả trước khóa theo hợp đồng đã ký, không cho sửa tay; mở kênh trả trước qua QR trên app trước khi khách tới quầy |
| 26 | T9 | T9.3 Lập và phát hành hóa đơn cho phần trả trước | Thu ngân | BVA | – | Cùng màn: hóa đơn điện tử sinh thẳng từ giao dịch; chặn sang SP1 khi hóa đơn chưa phát hành |
| 27 | T10 – Bàn giao máy và hướng dẫn khui hộp kiểm tra (nằm trong SP1, vẽ ở hình chi tiết C3a) | T10.1 Đi lấy máy đã giữ theo IMEI từ kho ra quầy **(ước lượng – GT45)** | Kho cửa hàng | **NVA** | Motion | Không cần màn hình thao tác. Cần màn xếp việc lấy máy hiện trước IMEI và vị trí kệ để gộp nhiều lượt đi lại thành một |
| 28 | T10 | T10.2 Đối chiếu IMEI trên hộp với IMEI trên hóa đơn trước mặt khách | Kho cửa hàng | BVA | – | Màn bàn giao máy: IMEI phải giao lấy thẳng từ T5; chặn đóng ca khi IMEI quét được khác IMEI đã giữ |
| 29 | T10 | T10.3 Khui hộp, hướng dẫn khách kiểm ngoại quan và bật máy thử | Kho cửa hàng | VA | – | Cùng màn: checklist khui hộp theo model, ô đính ảnh biên bản bàn giao |
| 30 | T10 | T10.4 Bàn giao máy và bộ chứng từ cho khách qua MF6 | Kho cửa hàng | VA | – | Cùng màn: chữ ký nhận máy của khách; chặn đóng ca khi chưa có chữ ký |
| 31 | T11 – Hẹn lịch giao và giữ máy theo số IMEI (nằm trong SP1, hình chi tiết C3a) | T11.1 Chốt ngày giờ khách hẹn nhận và ghi vào đơn | Kho cửa hàng | BVA | – | Màn hẹn giao máy: lịch trống theo ngày và theo khung giờ; chặn hẹn quá hạn giữ máy tối đa |
| 32 | T11 | T11.2 Gắn nhãn giữ máy theo IMEI và đặt hạn giữ | Kho cửa hàng | BVA | – | Cùng màn: IMEI đang giữ và hạn giữ còn lại; cảnh báo khi máy chạm ngưỡng tuổi giữ |
| 33 | T11 | T11.3 Gửi lịch hẹn giao máy cho khách qua MF7 | Kho cửa hàng | BVA | – | Cùng màn: nhắc khách tự động trước ngày hẹn; quá hạn hẹn thì chuyển sang giao tại nhà thay vì giữ máy tiếp |
| 34 | T12 – Đối chiếu khoản giải ngân của công ty tài chính với hóa đơn (service task) | T12.1 Nhận tệp giải ngân theo kỳ từ bên cho vay qua MF8 | Hệ thống ERP, lane Thu ngân | **NVA** | Unnecessary transportation | Không có màn hình thao tác. Cần màn nhật ký nhận tệp: kỳ đối soát, số dòng, thời điểm nhận |
| 35 | T12 | T12.2 Khớp từng dòng giải ngân với hóa đơn và hợp đồng tương ứng | Hệ thống ERP, lane Thu ngân | BVA | – | Màn đối soát giải ngân: bảng ghép tệp giải ngân với hóa đơn, cột lệch tiền và lệch ngày; khóa sửa tay số tiền trên tệp gốc (annotation A5) |
| 36 | T12 | T12.3 Lập danh sách ca lệch và xử lý từng ca | Thu ngân | BVA | – | Cùng màn: chỉ hiện ca lệch, mỗi ca một ô ghi cách xử lý; chặn đóng kỳ đối soát khi còn ca lệch chưa xử lý |
| – | E4 – Hợp đồng đã giải ngân và máy đã bàn giao cho khách (end event) | Kết quả thành công của quy trình | – | – (mốc) | – | Màn báo cáo ca thành công: đo thời gian từ E1 tới E4 làm cycle time gốc cho phần định lượng |
| | **Tổng kết 36 bước của 14 hoạt động được phân loại** | Bốn mốc E1, E2, E3, E4 không tính vào tỷ lệ | – | **VA 7 – 19,4%** · **BVA 19 – 52,8%** · **NVA 10 – 27,8%** | 10 bước NVA: T4.4 · IE1.1 · IE1.2 · IE2.1 · T6.1 · T6.2 · T8.3 · T9.1 · T10.1 · T12.1 | Ưu tiên xử lý theo thứ tự IE1.1 → T6.1 và T6.2 → IE2.1, vì cả bốn bước đều bắt nguồn từ một chỗ: quãng chờ kết quả thẩm định |

Bảng dưới giữ lại phần căn cứ và hướng khắc phục ở mức hoạt động. Tách ra thành bảng riêng vì hai cột này viết cho cả hoạt động chứ không cho từng bước, mà nhồi chúng vào bảng bảy cột ở trên thì không còn đọc được trên khổ giấy in.

| Mã | Nhãn trên mô hình | Phân loại ở mức hoạt động | Căn cứ phân loại các bước bên trong | Hướng khắc phục |
|---|---|---|---|---|
| E1 | Khách đã chọn hình thức thanh toán trả góp | – (mốc) | Mốc kích hoạt quy trình, không phải hoạt động | Cho khách khai báo trước giấy tờ và chọn công ty tài chính trên app, để lúc tới quầy đã có sẵn hồ sơ nháp |
| T1 | Sàng lọc sơ bộ và trình bày phương án trả góp | VA | Nhãn task ghép hai việc khác loại. Phần sàng lọc chặn rủi ro cho doanh nghiệp nên là BVA; phần trình bày và tính thử phương án chính là dịch vụ khách tới cửa hàng để mua kèm theo máy nên là VA. Ở mức hoạt động, cả cụm bị gộp thành một ô VA và phần BVA biến mất | Giữ. Bổ sung bảng so sánh điều kiện của từng công ty tài chính trên màn hình tư vấn để bước này ngắn lại và chọn đúng bên cho vay ngay lần đầu (annotation A1) |
| T2 | Tư vấn phương án thay thế cho khách | BVA | Khách không trả tiền cho lời tư vấn sau khi bị loại, nhưng doanh nghiệp cần bước này để không mất doanh thu. Đây **không** phải làm lại do lỗi nội bộ nên không xếp NVA | Chuẩn hóa sẵn 2-3 phương án thay thế (trả góp thẻ tín dụng, hạ cấu hình, giảm kỳ hạn) để không phải tư vấn lại từ đầu ở ba luồng vào khác nhau |
| E2 | Giao dịch trả góp đã dừng, khách chuyển phương án khác | – (mốc) | Kết quả kết thúc, không phải hoạt động | Đo tỷ lệ ca rơi vào mốc này theo từng nhánh vào (G1, G6, G7) để biết mất khách ở đâu |
| T3 | Lập giao dịch trả góp qua thẻ tín dụng | VA | Thao tác POS tạo ra đúng kết quả khách yêu cầu ngay tại quầy nên là VA; phần lập hóa đơn là nghĩa vụ thuế của doanh nghiệp nên là BVA | Đây là nhánh ngắn nhất của mô hình, nên đưa lên đầu bảng tư vấn ở T1 cho khách có sẵn thẻ tín dụng |
| T4 | Lập hồ sơ vay và tải chứng từ lên hệ thống bên cho vay | BVA | Ba bước lập và gửi hồ sơ đều bắt buộc để công ty tài chính thẩm định và để tuân thủ quy định cho vay tiêu dùng, nên là BVA. Bước bổ sung chứng từ trên vòng quay lui G12 là làm lại một việc đã làm, đúng định nghĩa Defects ở `chap05.pdf` trang 23 | Checklist giấy tờ động theo từng công ty tài chính và theo giá trị khoản vay, chặn không cho gửi khi còn thiếu (đối phó TG1 – chủ đề bị nhắc nhiều nhất của C3) |
| T5 | Khóa số IMEI và giữ máy trên ERP | BVA | Doanh nghiệp cần để không bán trùng máy đã cam kết với khách. Bản thân hai bước khóa và ghi hạn là hợp lý; cái sinh ra lãng phí là **khoảng thời gian máy bị giữ sau đó**, xử lý ở bảng 4.3 nhóm Hold (annotation A2) | Chỉ khóa IMEI sau khi hồ sơ qua sàng lọc cứng ở T4; đặt hạn giữ ngắn hơn cho nhóm hồ sơ rủi ro cao |
| IE1 | Kết quả thẩm định đã nhận | NVA | Hồ sơ nằm chờ, phía cửa hàng không làm gì, máy vẫn bị khóa. Bước nhận và đọc kết quả là bàn giao thuần túy, cùng loại với *"Mở yêu cầu và đọc (NVA)"* ở ví dụ BuildIT `chap05.pdf` trang 14. **Lưu ý:** việc thẩm định của công ty tài chính là BVA và nằm trong pool hộp đen nên không phải bước của quy trình này | Yêu cầu bên cho vay công bố SLA phản hồi; hiển thị trạng thái hồ sơ cho khách và cho nhân viên thay vì phải gọi hỏi; xếp hàng chờ theo hạn giữ máy chứ không theo thứ tự nộp |
| IE2 | Hết thời hạn giữ máy chờ hồ sơ | NVA | Độ trễ thuần túy. Sự kiện này chỉ nổ khi quãng chờ ở IE1 đã vượt ngưỡng chịu đựng, nó là hệ quả của chờ, không tạo giá trị cho ai | Rút ngắn bằng cách giải quyết IE1; đặt cảnh báo sớm ở 70% hạn giữ để nhân viên chủ động hỏi lại bên cho vay trước khi timer nổ |
| T6 | Giải phóng máy về tồn bán và hủy đơn | NVA | Cả hai bước đều là dọn dẹp sau một giao dịch không thành. Nếu hồ sơ được quyết trong hạn hoặc được sàng lọc chặt từ đầu thì hoạt động này không cần tồn tại. Đúng dạng Over-production của Ohno: đơn được tạo rồi bị hủy | Giảm số lần phải chạy hoạt động này bằng sàng lọc cứng trước khi khóa IMEI (T5) và bằng việc rút ngắn IE1. Tự động hóa hoàn toàn thao tác giải phóng trên ERP để không tốn công nhân viên |
| E3 | Đơn đã hủy, máy được giải phóng về tồn bán | – (mốc) | Kết quả kết thúc | Đo tỷ lệ ca rơi vào mốc này – đây là chỉ số trực tiếp của lãng phí Hold và Over-production |
| T7 | Thương lượng mức trả trước và kỳ hạn mới với khách | VA | Khách nhận được một phương án khả thi thay vì bị từ chối thẳng; đây là giá trị khách cảm nhận rõ nên cả hai bước đều VA. Chỉ khi phải thương lượng **nhiều vòng** cho cùng một hồ sơ thì phần lặp lại mới là lãng phí | Cho nhân viên thấy trước khung điều kiện mà bên cho vay thường chấp nhận, để chốt trong một vòng thay vì nhiều vòng qua lại |
| T8 | Ký hợp đồng vay với công ty tài chính | BVA | Khách không trả riêng cho hành vi ký, nhưng bắt buộc về pháp lý để khoản vay có hiệu lực, nên hai bước xuất và ký là BVA. Bước gửi bản đã ký về bên cho vay là gửi tài liệu, đúng định nghĩa Unnecessary transportation ở `chap05.pdf` trang 19 | Ký điện tử thay vì ký giấy, để bỏ được thời gian in, ký, quét và gửi lại |
| T9 | Thu khoản trả trước và lập hóa đơn | BVA | Khách không trả tiền cho hành vi thu tiền; doanh nghiệp cần để ghi nhận doanh thu và tuân thủ quy định hóa đơn. Bước đầu là điểm đổi lane từ NV tư vấn sang Thu ngân trên chuỗi tuần tự, tức một lần bàn giao ca, nên là NVA | Cho thanh toán khoản trả trước bằng chuyển khoản hoặc QR ngay trên app trước khi tới quầy, giảm chuyển giao giữa lane tư vấn và lane thu ngân |
| T10 | Bàn giao máy và hướng dẫn khui hộp kiểm tra | VA | Đây là lúc khách nhận đúng thứ đã mua; bỏ bước hướng dẫn khui hộp thì khách mất khả năng phát hiện lỗi ngay và giá trị dịch vụ giảm rõ, nên hai bước cuối là VA. Bước đi lấy máy từ kho ra quầy là chuyển động nội bộ, không đổi trạng thái của máy | Giữ nguyên phần khui hộp và bàn giao. Đây là các bước nên được bảo vệ thời lượng khi cải tiến chỗ khác |
| T11 | Hẹn lịch giao và giữ máy theo số IMEI | BVA | Phục vụ khách chưa lấy máy được ngay – là lựa chọn của khách, không phải trì hoãn do quy trình, nên **không** xếp NVA. Quãng giữ máy phát sinh sau đó mới là Hold, xử lý ở bảng 4.3 | Đặt hạn giữ rõ ràng và nhắc khách tự động; nếu quá hạn thì chuyển thành giao tại nhà thay vì tiếp tục giữ máy vô hạn |
| T12 | Đối chiếu khoản giải ngân của công ty tài chính với hóa đơn | BVA | Khách không trả tiền cho đối soát; doanh nghiệp cần để thu đủ tiền và phát hiện chuyển chậm hoặc chuyển thiếu (annotation A5). Bước nhận tệp giải ngân từ bên ngoài là nhận tài liệu làm đầu vào, nên là NVA | Đối soát tự động theo tệp giải ngân của bên cho vay, chỉ đẩy ca lệch cho người xử lý – bỏ thao tác so từng dòng bằng tay |
| E4 | Hợp đồng đã giải ngân và máy đã bàn giao cho khách | – (mốc) | Kết quả thành công của quy trình | Đo thời gian từ E1 tới E4 làm cycle time gốc cho phần định lượng |

> Xuống mức bước thì bức tranh đổi. Đếm theo hoạt động, C3 ra VA 4 (28,6%) · BVA 7 (50,0%) · NVA 3 (21,4%) trên 14 hoạt động. Đếm theo bước, cùng một quy trình ra VA 7 (19,4%) · BVA 19 (52,8%) · NVA 10 (27,8%) trên 36 bước. Tỷ lệ NVA tăng 6,4 điểm phần trăm và tỷ lệ VA giảm 9,2 điểm, vì mức hoạt động che mất bảy hoạt động chứa bước khác loại nhau: T1, T3, T4, T8, T9, T10 và T12. Rõ nhất là T10, trên hình là một hộp VA nhưng bên trong có một bước Motion và một bước BVA. Con số đúng để trích dẫn từ nay là con số theo bước.

> Đọc con số 27,8% cho đúng. Tỷ lệ NVA đếm theo số bước vẫn là con số dễ gây hiểu nhầm: mười bước NVA của C3 gần như chắc chắn chiếm phần áp đảo thời gian chu kỳ, vì các bước chờ tính bằng giờ hoặc ngày còn hai mươi sáu bước còn lại tính bằng phút. Đếm bước không thay được đếm thời gian, đây chính là chỗ phần định lượng (`cycle time efficiency`) phải làm rõ.

### 1.2 Bảng 4.2 – C4 Bảo hành, đổi trả 1 đổi 1 và thu hồi máy lỗi

Cùng lối đọc với C3: hai hình dưới đây chú phân loại lên mô hình C4 ở mức hoạt động, rồi bảng phía sau xuống mức bước. Điểm đáng chú ý ngay trên hình là ba hộp đỏ của C4 nằm liền nhau trên một đoạn duy nhất – từ lúc nhận máy tới lúc có kết luận và máy quay về – chứ không rải đều khắp quy trình như trực giác thường nghĩ.

@@FIG:va-C4@@

@@FIG:va-C4a@@

@@BANGNGANG@@

| STT | Hoạt động | Bước | Người thực hiện | Phân loại | Nhóm lãng phí | Màn hình cần có: nội dung và ràng buộc |
|---:|---|---|---|---|---|---|
| – | E1 – Khách đã mang máy lỗi và hóa đơn tới cửa hàng (start event dạng message, nhận qua MF1) | Mốc kích hoạt quy trình, không phải thao tác nên không phân rã | Khách hàng, pool ngoài | – (mốc) | – | Màn đặt lịch bảo hành trên app: cho khai báo lỗi và chọn khung giờ trước, để giảm thời gian mô tả lại tại quầy và giảm dồn tải cuối tuần |
| 1 | T1 – Quét IMEI, tra hóa đơn gốc và kiểm tra hộp cùng phụ kiện | T1.1 Quét IMEI, tra hóa đơn gốc và xác định máy còn hạn bảo hành | NV tiếp nhận | BVA | – | Màn tiếp nhận bảo hành: IMEI, ngày mua, số ngày còn lại của mốc tháng đầu và của hạn bảo hành; chặn lập phiếu khi IMEI không tra được hóa đơn gốc. Tra tự động theo số điện thoại thay vì nhập tay |
| 2 | T1 | T1.2 Nghe khách mô tả hiện tượng lỗi và ghi vào phiếu | NV tiếp nhận | BVA | – | Cùng màn: danh mục hiện tượng lỗi chuẩn hóa kèm ô mô tả tự do; hiện sẵn danh sách trường hợp loại trừ bảo hành để khách đọc trước khi gửi máy (BH2 – 5 nguồn) |
| 3 | T1 | T1.3 Kiểm hộp, phụ kiện và chụp ảnh hiện trạng máy | NV tiếp nhận | BVA | – | Cùng màn: ô đính ảnh bắt buộc theo sáu góc máy; chặn lưu phiếu khi thiếu ảnh hiện trạng hoặc thiếu chữ ký xác nhận của khách (BH8 – 3 nguồn) |
| 4 | T2 – Tính phí thiếu phụ kiện và thiếu hộp vào phiếu tiếp nhận | T2.1 Đối chiếu phụ kiện và hộp còn thiếu với biểu phí công bố | NV tiếp nhận | BVA | – | Màn biểu phí thiếu phụ kiện: checklist phụ kiện theo model, biểu phí 5% thiếu phụ kiện và 2% thiếu hộp (số công bố) |
| 5 | T2 | T2.2 Ghi mức phí vào phiếu và cho khách xác nhận | NV tiếp nhận | BVA | – | Cùng màn: số tiền phí tính tự động theo giá máy trên hóa đơn gốc; chặn lưu phiếu khi khách chưa xác nhận điện tử mức phí (BH5 – 3 nguồn) |
| 6 | T3 – Lập phiếu tiếp nhận và chuyển máy tới Trung tâm Bảo hành | T3.1 Lập phiếu tiếp nhận, in và đưa liên cho khách | NV tiếp nhận | BVA | – | Màn phiếu tiếp nhận: mã phiếu, IMEI, hiện tượng, ảnh hiện trạng, phí đã chốt, cam kết 15 ngày và ngày hẹn trả |
| 7 | T3 | T3.2 Đóng gói máy và niêm phong theo phiếu | NV tiếp nhận | **NVA** | Unnecessary transportation | Màn lập lô chuyển đi: mã niêm phong gắn với mã phiếu; chặn xuất lô khi còn phiếu chưa có mã niêm phong |
| 8 | T3 | T3.3 Xếp máy vào lô chờ chuyến lên Trung tâm Bảo hành **(ước lượng – GT46)** | NV tiếp nhận | **NVA** | Waiting | Cùng màn: giờ xuất chuyến kế tiếp và số máy đang chờ trong lô; cảnh báo ca sát mốc cam kết mà chưa lên được chuyến |
| 9 | T3 | T3.4 Bàn giao lô cho chuyến đi Trung tâm Bảo hành qua MF2 | NV tiếp nhận | **NVA** | Unnecessary transportation | Cùng màn: biên bản giao lô có chữ ký người vận chuyển; ca thuộc danh mục lỗi hiển nhiên đã chuẩn hóa thì không được xếp vào lô (annotation A3) |
| 10 | IE1 – Kết luận thẩm định đã nhận (intermediate message event, nhận qua MF3 từ pool Trung tâm Bảo hành) | IE1.1 Máy nằm trong hàng chờ thẩm định tại Trung tâm Bảo hành | Trung tâm Bảo hành, pool hộp đen; phía cửa hàng không ai làm gì | **NVA** | Waiting | Màn theo dõi ca bảo hành: trạng thái ca, số ngày đã trôi trên mốc 15 ngày, ngày hẹn trả; cảnh báo ca sắp chạm hạn (BH3 – 4 nguồn) |
| 11 | IE1 | IE1.2 Nhận kết luận nguyên nhân lỗi, mở đọc và ghi vào phiếu | NV tiếp nhận | **NVA** | Unnecessary transportation | Cùng màn: kết luận và ảnh giám định do trung tâm đẩy về tự ghi vào phiếu; chặn đóng ca khi chưa có mã kết luận |
| 12 | T4 – Thông báo từ chối và báo giá sửa chữa có phí | T4.1 Lập báo giá sửa chữa có phí theo kết luận | NV tiếp nhận | BVA | – | Màn báo giá sửa chữa: hạng mục và đơn giá lấy từ bảng giá của trung tâm; chặn gửi báo giá còn thiếu hạng mục |
| 13 | T4 | T4.2 Thông báo từ chối kèm báo giá cho khách qua MF4 | NV tiếp nhận | BVA | – | Cùng màn: bắt đính kết luận nguyên nhân và ảnh giám định vào thông báo; lưu vết thời điểm khách nhận |
| – | E2 – Yêu cầu đã bị từ chối, khách đã nhận báo giá sửa chữa có phí (end event) | Kết quả kết thúc, không phải thao tác | – | – (mốc) | – | Màn báo cáo ca từ chối: mỗi ca ở đây là toàn bộ công tiếp nhận, vận chuyển và chờ bị bỏ đi, nên tỷ lệ này phải đo riêng |
| 14 | T5 – Tư vấn phương án đổi mới miễn phí, trả hàng chịu phí hoặc sửa chữa | T5.1 Đối chiếu quyền lợi theo bản chính sách đang hiệu lực tại ngày mua | NV tiếp nhận | BVA | – | Màn tư vấn phương án trong tháng đầu: hiện số hiệu và ngày hiệu lực của bản chính sách áp cho ngày mua đó, để khách và nhân viên nói chuyện trên cùng một bản |
| 15 | T5 | T5.2 Trình bày ba phương án và mức phí kèm theo | NV tiếp nhận | VA | – | Cùng màn: ba phương án đặt cạnh nhau kèm điều kiện và phí; chỉ hiện phương án đổi máy khi tồn kho cho phép (BH6 – 4 nguồn) |
| 16 | T5 | T5.3 Ghi nhận phương án khách chọn vào phiếu | NV tiếp nhận | BVA | – | Cùng màn: chặn sang bước sau khi chưa ghi phương án khách chọn |
| 17 | T6 – Tư vấn phương án trả hàng chịu phí lũy tiến hoặc sửa chữa | T6.1 Tính phí lũy tiến theo số tháng đã dùng | NV tiếp nhận | BVA | – | Màn tư vấn phương án sau tháng đầu: số tháng đã dùng và biểu phí lũy tiến 20% và 10% (số công bố); phí tính tự động theo ngày mua, không cho sửa tay |
| 18 | T6 | T6.2 Trình bày hai phương án và mức phí cho khách | NV tiếp nhận | VA | – | Cùng màn: số tiền hoàn dự kiến sau khi trừ mọi khoản phí, cho khách xem được trên app trước khi ra cửa hàng |
| 19 | T6 | T6.3 Ghi nhận phương án khách chọn | NV tiếp nhận | BVA | – | Cùng màn: chặn sang bước sau khi chưa ghi phương án khách chọn |
| 20 | T7 – Kiểm tra tồn kho hàng đổi cùng model (service task) | T7.1 Tra tồn máy đổi đúng model tại kho cửa hàng | Hệ thống ERP, lane Kho hàng đổi | BVA | – | Màn tra tồn hàng đổi: tồn theo model tại cửa hàng và các cửa hàng lân cận; chỉ cho giữ máy đổi sau khi khách đã xác nhận phương án |
| 21 | T7 | T7.2 Tra tồn model tương đương, chỉ chạy trên nhánh "Đã hết" của G7 | Hệ thống ERP, lane Kho hàng đổi | BVA | – | Cùng màn: danh sách model tương đương kèm chênh lệch giá; bắt khách xác nhận điện tử model tương đương trước khi xuất |
| 22 | T8 – Xuất máy đổi và bàn giao cho khách | T8.1 Đi lấy máy đổi từ kho ra quầy **(ước lượng – GT45)** | Kho hàng đổi | **NVA** | Motion | Không cần màn hình thao tác. Cần màn xếp việc lấy máy hiện IMEI và vị trí kệ |
| 23 | T8 | T8.2 Xuất máy đổi trên ERP và ghi IMEI mới vào phiếu | Kho hàng đổi | BVA | – | Màn xuất máy đổi: IMEI cũ và IMEI mới đặt cạnh nhau; chặn xuất khi IMEI mới khác model khách đã xác nhận |
| 24 | T8 | T8.3 Khui hộp, kiểm tra cùng khách và bàn giao | Kho hàng đổi | VA | – | Cùng màn: checklist khui hộp và biên bản đổi máy có chữ ký khách; chặn đóng ca khi chưa có chữ ký |
| 25 | T9 – Tính số tiền hoàn sau khi trừ phí và chi trả về phương thức gốc | T9.1 Bàn giao ca từ quầy tiếp nhận sang kế toán hoàn tiền | NV tiếp nhận chuyển cho Kế toán hoàn tiền | **NVA** | Unnecessary transportation | Màn hoàn tiền mở thẳng bằng mã phiếu, không nhập lại; mọi trường của phiếu ở trạng thái chỉ đọc |
| 26 | T9 | T9.2 Tính số tiền hoàn sau khi trừ phí lũy tiến và phí thiếu phụ kiện | Kế toán hoàn tiền | BVA | – | Cùng màn: bảng bóc tách giá mua và từng khoản phí đã trừ; số tiền hoàn tính tự động, không gõ tay |
| 27 | T9 | T9.3 Chi trả về đúng phương thức khách đã thanh toán | Kế toán hoàn tiền | VA | – | Cùng màn: khóa phương thức chi trả theo phương thức thanh toán gốc; với máy mua trả góp ở C3 thì chặn chi thẳng cho khách và bắt mở hồ sơ phối hợp với công ty tài chính (annotation A10) |
| 28 | T10 – Chuyển máy đi sửa và theo dõi cam kết 15 ngày | T10.1 Ra lệnh sửa chữa gửi Trung tâm Bảo hành qua MF5, máy đang giữ tại trung tâm | NV tiếp nhận | **NVA** | Unnecessary transportation | Màn lệnh sửa chữa: mã phiếu, kết luận lỗi, phương án khách đã chọn; chặn ra lệnh khi khách chưa chọn phương án |
| 29 | T10 | T10.2 Máy nằm chờ tới lượt sửa tại Trung tâm Bảo hành | Trung tâm Bảo hành, pool hộp đen | **NVA** | Waiting | Cùng màn: đồng hồ đếm ngược mốc 15 ngày; cảnh báo khi còn ba ngày tới hạn |
| 30 | T10 | T10.3 Theo dõi mốc cam kết 15 ngày và cập nhật trạng thái ca | NV tiếp nhận | BVA | – | Cùng màn: lịch sử trạng thái ca; mỗi lần đổi trạng thái tự phát thông báo cho khách (BH3 – 4 nguồn) |
| 31 | T11 – Bàn giao máy đã sửa kèm phiếu bảo hành | T11.1 Nhận lô máy đã sửa từ chuyến về qua MF6 và nhập lại vào cửa hàng | NV tiếp nhận | **NVA** | Unnecessary transportation | Màn nhận lô máy về: đối chiếu danh sách IMEI trong lô với danh sách đã gửi đi; cảnh báo IMEI thiếu |
| 32 | T11 | T11.2 Đối chiếu IMEI và chạy thử máy trước khi gọi khách | NV tiếp nhận | BVA | – | Màn bàn giao máy sau sửa chữa: hạng mục đã sửa và kết quả chạy thử; chặn gọi khách khi chưa có kết quả chạy thử |
| 33 | T11 | T11.3 Bàn giao máy kèm phiếu bảo hành cho khách | NV tiếp nhận | VA | – | Cùng màn: thời hạn bảo hành cho phần đã sửa; chặn đóng ca khi chưa có chữ ký nhận máy. Cho chọn nhận máy tại nhà để bỏ lần quay lại cửa hàng thứ hai (BH7 – 3 nguồn) |
| 34 | T12 – Thông báo kết quả xử lý cho khách (send task, nằm trong SP1, hình chi tiết C4a) | T12.1 Soạn nội dung thông báo theo phương án đã thực hiện | NV tiếp nhận | BVA | – | Màn thông báo kết quả: mẫu thông báo theo từng phương án và lịch sử các lần đã báo |
| 35 | T12 | T12.2 Gửi thông báo cho khách qua MF7 | NV tiếp nhận | BVA | – | Cùng màn: phát thông báo tự động ở mọi lần đổi trạng thái chứ không chỉ ở bước cuối (BH3 – 4 nguồn) |
| 36 | T13 – Cập nhật nghiệp vụ nhập đổi hoặc nhập trả trên ERP (service task, hình chi tiết C4a) | T13.1 Ghi bút toán nhập đổi hoặc nhập trả | Hệ thống ERP, lane NV tiếp nhận | BVA | – | Không có màn hình thao tác, bước chạy nền. Cần màn nhật ký bút toán: mã phiếu, IMEI, loại bút toán, trạng thái ghi sổ |
| 37 | T13 | T13.2 Cập nhật tồn kho và trạng thái IMEI | Hệ thống ERP, lane NV tiếp nhận | BVA | – | Cùng màn nhật ký: chặn đóng ca khi còn bút toán lỗi chưa xử lý |
| 38 | T14 – Nhập máy lỗi thu hồi và gom chuyển trả hãng theo kỳ | T14.1 Nhận máy lỗi trả về từ Trung tâm Bảo hành qua MF9 và nhập kho máy lỗi | Kho hàng đổi | BVA | – | Màn kho máy lỗi thu hồi: IMEI, mã phiếu gốc, ngày nhập kho; nhánh sửa chữa không có máy lỗi để thu hồi nên phải cho phép bỏ trống, đúng annotation A11 |
| 39 | T14 | T14.2 Máy lỗi nằm chờ gom đủ kỳ tại kho | Kho hàng đổi | **NVA** | Inventory | Cùng màn: tuổi tồn của từng máy và ngưỡng gom; cảnh báo máy vượt ngưỡng tuổi tồn |
| 40 | T14 | T14.3 Đóng lô và chuyển trả hãng theo kỳ qua MF8 | Kho hàng đổi | BVA | – | Cùng màn: cho đóng lô sớm theo ngưỡng số lượng hoặc ngưỡng tuổi tồn, thay vì chỉ theo kỳ cố định |
| – | E3 – Yêu cầu đã xử lý xong và máy lỗi đã được thu hồi (end event) | Kết quả thành công của quy trình | – | – (mốc) | – | Màn báo cáo ca hoàn tất: đo thời gian từ E1 tới E3 và so với cam kết 15 ngày công bố |
| | **Tổng kết 40 bước của 15 hoạt động được phân loại** | Ba mốc E1, E2, E3 không tính vào tỷ lệ | – | **VA 5 – 12,5%** · **BVA 24 – 60,0%** · **NVA 11 – 27,5%** | 11 bước NVA: T3.2 · T3.3 · T3.4 · IE1.1 · IE1.2 · T8.1 · T9.1 · T10.1 · T10.2 · T11.1 · T14.2 | Tám trong mười một bước NVA nằm trên cùng một đoạn: từ lúc máy rời quầy ở T3 tới lúc máy quay về cửa hàng ở T11. Đó là đoạn đáng đầu tư cải tiến trước |

Bảng dưới giữ căn cứ và hướng khắc phục ở mức hoạt động, cùng lối với bảng phụ của C3.

| Mã | Nhãn trên mô hình | Phân loại ở mức hoạt động | Căn cứ phân loại các bước bên trong | Hướng khắc phục |
|---|---|---|---|---|
| E1 | Khách đã mang máy lỗi và hóa đơn tới cửa hàng | – (mốc) | Mốc kích hoạt quy trình | Cho khai báo lỗi và đặt lịch trước qua app để giảm thời gian mô tả lại tại quầy và giảm dồn tải cuối tuần |
| T1 | Quét IMEI, tra hóa đơn gốc và kiểm tra hộp cùng phụ kiện | BVA | Cả ba bước đều cần để xác định quyền lợi bảo hành và chống gian lận; khách không trả tiền cho chúng nhưng bỏ đi thì doanh nghiệp không kiểm soát được rủi ro | Tra tự động theo số điện thoại thay vì nhập tay; chụp ảnh hiện trạng máy và phụ kiện đính vào phiếu ngay tại hoạt động này để không phải tranh luận về sau (BH8 – 3 nguồn) |
| T2 | Tính phí thiếu phụ kiện và thiếu hộp vào phiếu tiếp nhận | BVA | Doanh nghiệp cần để thu hồi phần giá trị đã mất theo chính sách công bố (5% thiếu phụ kiện, 2% thiếu hộp). Khách chắc chắn không muốn trả, nhưng đây là quy định đã công bố công khai chứ không phải việc thừa | Hiển thị biểu phí ngay trên phiếu tiếp nhận và cho khách xác nhận điện tử trước khi ký, để việc này không thành bất ngờ ở phút cuối (BH5 – 3 nguồn) |
| T3 | Lập phiếu tiếp nhận và chuyển máy tới Trung tâm Bảo hành | NVA | Đây là hoạt động mà mức hoạt động che giấu nhiều nhất: nhãn task ghép **lập phiếu** (BVA, bắt buộc để lưu vết và tính phí) với **chuyển máy đi** (ba bước đóng gói, chờ chuyến và bàn giao lô, đều NVA vì máy không đổi trạng thái). Ở mức hoạt động cả cụm bị chấm NVA theo phần chi phối, phần BVA biến mất. Chú thích A3 gọi đoạn này là nút thắt lớn nhất của quy trình | Phân quyền kết luận tại cửa hàng cho một danh mục lỗi hiển nhiên đã chuẩn hóa, để nhóm ca đó không phải rời cửa hàng. Việc **tách T3 thành hai bước riêng ở mô hình to-be** nay đã có căn cứ đo được: ba trong bốn bước của T3 là NVA |
| IE1 | Kết luận thẩm định đã nhận | NVA | Máy nằm chờ tới lượt thẩm định rồi chờ chuyến về; khách không nhận được gì trong suốt quãng này. Bước nhận và đọc kết luận là bàn giao thuần túy. **Lưu ý quan trọng:** bản thân việc thẩm định là **BVA** – nó chống gian lận bảo hành, và nó nằm trong pool hộp đen Trung tâm Bảo hành nên không phải bước của quy trình cửa hàng | Công bố trạng thái ca bảo hành cho khách tra cứu, thay vì để khách gọi hỏi (BH3 – 4 nguồn); xếp hàng chờ thẩm định theo hạn cam kết 15 ngày thay vì vào trước ra trước |
| T4 | Thông báo từ chối và báo giá sửa chữa có phí | BVA | Doanh nghiệp cần thông báo minh bạch kết quả và mở đường sang dịch vụ sửa có phí; khách không trả tiền cho lời từ chối. Cùng lối phân loại với "Prepare rejection letter – BVA" ở bài tập ngày 03/08 | Đưa danh sách các trường hợp loại trừ bảo hành lên bước T1.2 để khách biết rủi ro bị từ chối **trước khi** gửi máy đi, thay vì biết sau nhiều ngày chờ (BH2 – 5 nguồn) |
| E2 | Yêu cầu đã bị từ chối, khách đã nhận báo giá sửa chữa có phí | – (mốc) | Kết quả kết thúc | Đo tỷ lệ ca rơi vào mốc này – mỗi ca ở đây là toàn bộ công tiếp nhận, vận chuyển và chờ bị bỏ đi |
| T5 | Tư vấn phương án đổi mới miễn phí, trả hàng chịu phí hoặc sửa chữa (trong tháng đầu) | VA | Khách nhận được quyền chọn phương án, đó chính là giá trị mà chính sách bảo hành đem lại, nên bước trình bày phương án là VA. Hai bước tra quyền lợi và ghi nhận lựa chọn phục vụ lưu vết nội bộ nên là BVA | Chuẩn hóa kịch bản tư vấn và bảng phí kèm theo để mọi nhân viên nói cùng một nội dung với chính sách công bố (BH6 – 4 nguồn) |
| T6 | Tư vấn phương án trả hàng chịu phí lũy tiến hoặc sửa chữa (từ tháng thứ hai) | VA | Cùng lối với T5: bước trình bày phương án kèm mức phí là VA, bước tính phí và bước ghi nhận là BVA | Cho khách xem trước mức phí lũy tiến theo số tháng đã dùng ngay trên app trước khi ra cửa hàng |
| T7 | Kiểm tra tồn kho hàng đổi cùng model | BVA | Doanh nghiệp cần biết có thực hiện được phương án vừa hứa với khách hay không; khách không trả tiền cho bước tra tồn | Kiểm tồn **trước** bước tư vấn T5 và T6, để nhân viên không tư vấn một phương án mà kho không đáp ứng được rồi phải quay lại thương lượng |
| T8 | Xuất máy đổi và bàn giao cho khách | VA | Bước khui hộp và bàn giao là kết quả khách mong đợi khi chọn phương án đổi máy nên là VA; bước xuất trên ERP là ghi sổ nội bộ nên BVA; bước đi lấy máy từ kho ra quầy là chuyển động nội bộ | Giữ nguyên phần bàn giao. Rút bước lấy máy bằng cách xếp việc lấy máy theo lô thay vì theo từng ca |
| T9 | Tính số tiền hoàn sau khi trừ phí và chi trả về phương thức gốc | VA | Bước chi trả là kết quả của phương án khách đã chọn nên VA; bước tính phí là nghiệp vụ nội bộ nên BVA; bước đầu là điểm đổi lane từ NV tiếp nhận sang Kế toán hoàn tiền, tức một lần bàn giao ca | Với máy mua trả góp ở C3 thì phải phối hợp hoàn tiền với công ty tài chính nên lâu hơn (annotation A10) – cần một luồng hoàn tiền riêng cho nhóm này thay vì dùng chung |
| T10 | Chuyển máy đi sửa và theo dõi cam kết 15 ngày | NVA | Phần chiếm thời gian áp đảo là quãng máy tiếp tục nằm tại Trung tâm Bảo hành chờ tới lượt sửa; phần theo dõi cam kết 15 ngày là BVA và nay đã tách được thành bước riêng. **Đọc theo message flow của file thật:** MF5 đi ra từ T10 chỉ mang "Yêu cầu sửa chữa, máy đang giữ tại trung tâm", không mang máy – tức máy đã nằm sẵn ở trung tâm từ T3, không phát sinh chặng vận chuyển thứ hai. Nhãn task vẫn ghi "Chuyển máy đi sửa" theo nghĩa chuyển sang công đoạn sửa; cách đọc này đã chốt ở mục 0.2 điểm 2 | Cho phép Trung tâm Bảo hành sửa luôn ngay khi kết luận là lỗi nhà sản xuất và khách đã chọn sẵn phương án sửa ở T5 hoặc T6, để bỏ được vòng hỏi ý kiến quay về cửa hàng rồi mới ra lệnh sửa |
| T11 | Bàn giao máy đã sửa kèm phiếu bảo hành | VA | Khách nhận lại máy hoạt động được, đó là kết quả cuối cùng của phương án sửa chữa nên bước bàn giao là VA; bước chạy thử là kiểm soát nội bộ nên BVA; bước nhận lô máy từ chuyến về là chiều về của chặng vận chuyển | Cho khách chọn nhận máy tại nhà để bỏ được lần quay lại cửa hàng thứ hai (BH7 – 3 nguồn) |
| T12 | Thông báo kết quả xử lý cho khách | BVA | Là hoạt động giao tiếp chính thức, cần để khép ca và lưu vết; khách không trả tiền riêng cho thông báo. Cùng lối phân loại với "Prepare letter of offer – BVA" ở bài tập ngày 03/08 | Tự động phát thông báo theo trạng thái ca ở mọi mốc chứ không chỉ ở cuối, để khách không phải gọi hỏi giữa chừng (BH3 – 4 nguồn) |
| T13 | Cập nhật nghiệp vụ nhập đổi hoặc nhập trả trên ERP | BVA | Cần để tồn kho và sổ sách đúng; khách không thấy và không trả tiền cho hai bước ghi bút toán và cập nhật tồn | Giữ. Đã chạy song song với T12 qua cặp AND G11 và G12 – đây là điểm mô hình hiện tại đã làm tốt, không cần sửa |
| T14 | Nhập máy lỗi thu hồi và gom chuyển trả hãng theo kỳ | BVA | Bước nhận máy lỗi về và bước chuyển trả hãng đều cần để thu hồi giá trị từ hãng và tuân thủ thỏa thuận với hãng. Cái sinh ra lãng phí là bước ở giữa: máy lỗi nằm chờ gom đủ kỳ, đúng dạng Inventory | Giữ hoạt động, đổi cách chạy: chuyển trả hãng theo ngưỡng số lượng hoặc theo ngưỡng tuổi tồn, thay vì chỉ theo kỳ cố định |
| E3 | Yêu cầu đã xử lý xong và máy lỗi đã được thu hồi | – (mốc) | Kết quả thành công | Đo thời gian từ E1 tới E3 và so với cam kết 15 ngày công bố |

> Xuống mức bước, C4 đổi mạnh hơn C3. Đếm theo hoạt động, C4 ra VA 5 (33,3%) · BVA 7 (46,7%) · NVA 3 (20,0%) trên 15 hoạt động. Đếm theo bước, cùng quy trình ra VA 5 (12,5%) · BVA 24 (60,0%) · NVA 11 (27,5%) trên 40 bước. Số bước VA vẫn đúng bằng 5, nhưng tỷ lệ VA rơi từ 33,3% xuống 12,5%: mỗi hoạt động từng được chấm VA (T5, T6, T8, T9, T11) thật ra chỉ chứa một bước khách sẵn sàng trả tiền, hai bước còn lại là ghi sổ, lấy hàng hoặc chạy thử. Mức hoạt động đã tính công phụ trợ thành công tạo giá trị.

> Nhận xét chung hai bảng. Tỷ lệ NVA đếm theo bước của C3 và C4 gần bằng nhau (27,8% và 27,5%), nhưng bản chất khác hẳn: NVA của C3 là chờ thông tin (kết quả thẩm định đi bằng đường số, về nguyên tắc có thể rút xuống vài phút), còn NVA của C4 là chờ vật lý (máy phải đi và về, không rút xuống dưới thời gian vận chuyển được). Cải tiến C3 là bài toán thông tin; cải tiến C4 là bài toán phân quyền và tuyến vận chuyển. Đây cũng là kết luận mà mức hoạt động cho ra (21,4% và 20,0%), nên nó không đổi khi xuống mức bước – chỉ vững thêm.

---

## 2. Phân tích lãng phí Move / Hold / Overdo

Thầy chốt phạm vi của phần này ở buổi báo cáo 07/09: *"trong cái phần lãng phí thì mình sẽ tập trung vô những cái hoạt động là NVA, không tạo ra giá trị cho khách hàng"*. Vì vậy hai bảng dưới đây không phải danh sách lãng phí rời, mà là 21 dòng NVA của bảng 4.1 và bảng 4.2 được gom lại theo nhóm: C3 có 10 bước NVA, C4 có 11 bước. Cột "Mã bước NVA" cho tra ngược từng dòng về đúng ô trong bảng giá trị gia tăng.

Ánh xạ ba nhóm của rubric sang 7 dạng lãng phí Ohno (`chap05.pdf` trang 19-25), bản gốc bảy dạng ở [20]:

| Nhóm rubric | 7 lãng phí Ohno | Số bước NVA gánh nhóm này ở C3 | Ở C4 |
|---|---|---:|---:|
| **Move** | Unnecessary transportation · Motion | 5 | 7 |
| **Hold** | Inventory · Waiting | 2 | 4 |
| **Overdo** | Defects · Over-processing · Over-production | 3 | 0 |

Bốn ô trong hai bảng dưới đây không có bước NVA nào gánh: Over-processing của C3, rồi Defects, Over-processing và Over-production của C4. Lý do giống nhau ở cả bốn: chúng nằm ngoài phạm vi mô hình cửa hàng, hoặc là hiện tượng của cả một đường đi chứ không của riêng một bước. Hai mục 2.1 và 2.2 ghi rõ từng trường hợp thay vì bỏ trống ô.

### 2.1 Bảng 4.3 – Lãng phí trong C3

| Nhóm | Lãng phí cụ thể | Mã bước NVA ở bảng 4.1 | Biểu hiện | Quy mô ước tính | Khắc phục |
|---|---|---|---|---|---|
| **Move** | Unnecessary transportation | `IE1.2` · `T8.3` · `T9.1` · `T12.1` | Bốn lần tài liệu hoặc ca đổi tay mà nội dung không đổi: đọc kết quả thẩm định về ghi vào hồ sơ, gửi hợp đồng đã ký cho bên cho vay, bàn giao ca từ quầy tư vấn sang thu ngân, nhận tệp giải ngân theo kỳ. Hồ sơ đi qua 4 lane trong cùng pool Cửa hàng TGDĐ: NV tư vấn trả góp (T1, T2, T4, T7, T8) · Thu ngân (T3, T9, T12) · Kho cửa hàng (T5, T10, T11) · Quản lý cửa hàng (T6) | **4 điểm bàn giao trên đường đi thuận lợi** (duyệt thẳng, nhận máy ngay) – **đếm trực tiếp từ lane trong file `.bpmn`, không phải ước lượng**: 3 lần đổi lane trên chuỗi tuần tự (T8 tư vấn → T9 thu ngân → T10 kho → T12 thu ngân), cộng nhánh song song T5 chạy ở lane Kho cửa hàng | Gộp thao tác của T5, T9, T12 vào một màn hình ERP để nhân viên tư vấn thao tác trực tiếp, chỉ giữ chuyển giao khi có yêu cầu kiểm soát chéo (thu tiền mặt, giải phóng máy). Ký điện tử ở T8 để bước gửi hợp đồng chạy nền |
| **Move** | Motion | `T10.1` | Chuyển động nội bộ của nhân viên trong cửa hàng: đi lấy máy từ kho ra quầy ở bước T10.1, đi tới quầy thu ngân, đi in hợp đồng | **Chưa đủ dữ kiện để kết luận về quy mô.** Bước T10.1 có mặt trên mọi ca nhận máy ngay, nhưng số lượt di chuyển thật thì nguồn thứ cấp không quan sát được (báo cáo nguồn mục 4.2), nên bước này đánh dấu **(ước lượng – GT45)** | Cách lấy số thật: một buổi quan sát tại cửa hàng, bấm giờ và đếm số lượt di chuyển cho n ≥ 8 ca. Chưa có số thì không đưa nhóm này vào phần cải tiến |
| **Hold** | Waiting | `IE1.1` · `IE2.1` | Hồ sơ nằm chờ kết quả thẩm định của công ty tài chính tại IE1.1; nếu chờ quá hạn thì timer IE2.1 nổ. Hai bước này là hai bước NVA duy nhất mà phía cửa hàng hoàn toàn không có ai thao tác | Nguồn đối tác công bố "toàn bộ quy trình số hóa, chỉ mất 3 phút" – **1 nguồn, lại là nội dung quảng cáo (TG3), không dùng làm số vận hành**. Nguồn 2016 kể thẩm định có gọi xác minh 2 người thân, tới 3 cuộc cho một người (TG2). **Thời gian chờ thật: chưa đo được** | Yêu cầu công ty tài chính công bố SLA phản hồi; hiển thị trạng thái hồ sơ theo thời gian thực cho cả nhân viên và khách; cảnh báo sớm ở 70% hạn giữ máy |
| **Hold** | Inventory | Không có bước riêng; hệ quả của `IE1.1` và `IE2.1` | Máy bị khóa IMEI ở T5.1 và giữ tại kho cửa hàng cho tới khi có kết quả – suốt hai bước chờ đó máy không bán được cho khách khác (annotation A2). Hai bước khóa và ghi hạn của T5 tự chúng là BVA, cái lãng phí là **độ dài của quãng giữ**, mà độ dài đó bằng đúng thời lượng của IE1.1 cộng IE2.1. Nhánh T11 "hẹn nhận sau" tiếp tục giữ máy thêm một quãng nữa | 1 máy bị giữ trên mỗi hồ sơ đang chờ, nhân với thời gian chờ ở IE1.1 **(ước lượng – cần số ở phần định lượng)** | Chỉ khóa IMEI sau khi hồ sơ qua sàng lọc cứng ở T4; đặt hạn giữ theo nhóm rủi ro thay vì một hạn chung; với nhánh T11 thì chuyển sang giao tại nhà khi quá hạn hẹn |
| **Overdo** | Defects | `T4.4` | Hồ sơ thiếu hoặc sai giấy tờ phải bổ sung rồi nộp lại, chạy trên vòng quay lui G12 → G13. Nguyên nhân gốc: bộ giấy tờ thay đổi theo từng công ty tài chính và theo giá trị khoản vay, nên nhân viên dễ chuẩn bị thiếu ở T4.2 | **TG1 – 4 nguồn, là chủ đề bị nhắc nhiều nhất trong nhóm C3.** Tỷ lệ hồ sơ phải bổ sung: **chưa biết** (báo cáo nguồn mục 4.3 ghi rõ không suy được tỷ lệ nhánh). Mô hình khai trần 2 lượt ở annotation A7 | Checklist giấy tờ động sinh theo công ty tài chính và giá trị khoản vay, chặn nút gửi khi còn thiếu; cho khách tải chứng từ trước qua app để kiểm đủ trước khi tới cửa hàng |
| **Overdo** | Over-processing | **Không có bước NVA nào** – cả hai biểu hiện nằm ngoài phạm vi mô hình | Đơn đặt online vẫn phải có nhân viên gọi xác nhận thủ công trong 60 phút (TG4): việc này xảy ra **trước E1**, tức trước khi quy trình C3 bắt đầu. Thẩm định gọi xác minh nhiều cuộc cho cùng một đầu mối (TG2 – 3 cuộc cho một người): việc này xảy ra **bên trong pool hộp đen** Công ty tài chính. **Lưu ý:** bản thân việc gọi xác minh là BVA, nó chặn rủi ro tín dụng. Cái lãng phí là **số cuộc gọi lặp lại cho cùng một đầu mối** | TG4 – 2 nguồn; TG2 – 2 nguồn. Số cuộc gọi trung bình mỗi hồ sơ: **chưa đo được**. Không gán được cho bước nào vì mô hình C3 không vẽ hai chỗ này | Xác thực thông tin khách ngay lúc đặt online (OTP, đối chiếu căn cước điện tử) để bỏ cuộc gọi xác nhận đơn; ghi nhận kết quả từng cuộc xác minh vào hồ sơ để bên cho vay không gọi lại đầu mối đã liên hệ được. Muốn đưa vào mô hình thì phải mở rộng phạm vi C3 lên trước E1 |
| **Overdo** | Over-production | `T6.1` · `T6.2` | Đơn được tạo, hồ sơ được lập ở T4, máy bị khóa ở T5 – rồi toàn bộ bị hủy ở hai bước T6.1 và T6.2 khi timer IE2 nổ hoặc khi thu khoản trả trước không thành ở G9. Đúng định nghĩa của Ohno: nhiệm vụ cần thiết được thực hiện nhưng tạo ra kết quả không tăng giá trị | Trên nhánh này, **8 bước từ T4.1 tới IE1.2** đã chạy xong rồi thành công bỏ đi, trong đó 3 bước vốn đã là NVA. Tỷ lệ ca đi vào nhánh T6: **chưa có dữ liệu, không suy diễn** | Sàng lọc cứng ở T1 và T4 trước khi khóa IMEI; hỏi trước khả năng thanh toán khoản trả trước ngay ở bước tư vấn để không tới G9 mới phát hiện |

### 2.2 Bảng 4.4 – Lãng phí trong C4

| Nhóm | Lãng phí cụ thể | Mã bước NVA ở bảng 4.2 | Biểu hiện | Quy mô ước tính | Khắc phục |
|---|---|---|---|---|---|
| **Move** | Unnecessary transportation | `T3.2` · `T3.4` · `IE1.2` · `T9.1` · `T10.1` · `T11.1` | Sáu bước, chia làm hai loại. Bốn bước là máy hoặc yêu cầu rời chỗ: đóng gói niêm phong, bàn giao lô cho chuyến đi (MF2 mang "Máy và phiếu tiếp nhận"), ra lệnh sửa gửi trung tâm (MF5), nhận lô máy đã sửa về (MF6). Hai bước còn lại là tài liệu và ca đổi tay: đọc kết luận thẩm định ghi vào phiếu, bàn giao ca sang kế toán hoàn tiền. Việc chuyển máy áp dụng cho **mọi ca**, kể cả lỗi hiển nhiên (annotation A3) | **2 lượt vận chuyển mỗi ca – đọc từ message flow của file thật.** Nhánh sửa chữa: đi ở MF2, về ở MF6. Nhánh đổi máy và hoàn tiền: đi ở MF2, về ở MF9 "Máy lỗi trả về cửa hàng" – chiều về này mới được vẽ, nên số lượt bình quân ở `dinh-luong.md` Bảng 4.13 còn phải đếm lại (`I-11`). Không có chặng thứ ba: MF5 chỉ mang yêu cầu sửa, không mang máy. Chủ đề "máy phải đi qua nhiều tầng" là **BH1 – 5 nguồn, cao nhất bảng mã hóa C4** | Phân quyền kết luận tại cửa hàng cho danh mục lỗi hiển nhiên đã chuẩn hóa, để nhóm ca đó không phải rời cửa hàng lần nào; cho Trung tâm Bảo hành sửa luôn khi khách đã chọn sẵn phương án sửa, thay vì hỏi ý kiến vòng về cửa hàng rồi mới ra lệnh sửa |
| **Move** | Motion | `T8.1` | Chuyển động của nhân viên giữa quầy tiếp nhận, kho hàng đổi và quầy kế toán hoàn tiền (T7, T8, T9, T14 nằm ở ba lane khác nhau). Bước đo được duy nhất là T8.1 đi lấy máy đổi từ kho ra quầy | **Chưa đủ dữ kiện để kết luận về quy mô** – không quan sát được từ nguồn công khai, nên T8.1 đánh dấu **(ước lượng – GT45)** | Cách lấy số thật: quan sát tại cửa hàng, đếm số lượt di chuyển giữa ba lane cho n ≥ 8 ca. Chưa có số thì không đưa vào phần cải tiến |
| **Hold** | Waiting | `T3.3` · `IE1.1` · `T10.2` | Ba quãng chờ nối nhau: máy chờ chuyến tại quầy tiếp nhận, máy chờ tới lượt thẩm định tại Trung tâm Bảo hành, máy chờ tới lượt sửa cũng tại trung tâm. **Không tính việc thẩm định và việc sửa là lãng phí** – chỉ tính quãng chờ tới lượt và chờ chuyến | Cam kết công bố: **15 ngày** kể từ khi nhận máy (3 nguồn, số công bố). Người dùng tự thuật: **gần 20 ngày vẫn chưa có kết quả, được báo chờ thêm 1 tuần; một ca khác được báo "mất 1 tháng"** (BH3 – 4 nguồn, số người dùng tự thuật, không phải số đo). Riêng bước T3.3 là **(ước lượng – GT46)**, lịch chuyến chưa kiểm chứng. Tỷ lệ ca trễ hạn: **chưa biết** | Công bố trạng thái ca cho khách tra cứu thay vì để khách gọi hỏi; xếp hàng chờ thẩm định theo hạn cam kết 15 ngày thay vì vào trước ra trước; đo và công bố tỷ lệ đạt cam kết; tăng tần suất chuyến trong khung giờ tiếp nhận cao điểm |
| **Hold** | Inventory | `T14.2`; hai chỗ còn lại là hệ quả của `IE1.1`, `T10.2` và của T7 | Ba chỗ hàng nằm chờ: (a) máy của khách nằm tại Trung tâm Bảo hành suốt IE1.1 và T10.2 – không có bước riêng, độ dài bằng đúng hai bước chờ đó; (b) máy đổi cùng model bị giữ ở kho sau khi kiểm tồn T7 cho tới khi bàn giao T8.3; (c) máy lỗi thu hồi nằm ở kho chờ gom đủ kỳ, đây là bước T14.2 và là chỗ duy nhất Inventory có mã bước riêng | (a) 1 máy mỗi ca nhân thời gian chờ **(ước lượng)**; (b) quãng ngắn, chưa đo; (c) tồn máy lỗi bằng số ca trong một kỳ gom **(ước lượng – phụ thuộc độ dài kỳ, chưa biết)** | (a) xử lý cùng với Waiting ở trên; (b) chỉ giữ máy đổi sau khi khách đã xác nhận phương án; (c) chuyển trả hãng theo ngưỡng số lượng hoặc ngưỡng tuổi tồn thay vì kỳ cố định |
| **Overdo** | Defects | **Không có bước NVA nào** – đây là hiện tượng của cả một đường đi | Khách bị từ chối ở G3 nhánh "do người dùng" sau khi đã qua toàn bộ tiếp nhận, vận chuyển và chờ. Không bước nào trong số đó tự nó là lỗi; cái hỏng là cả **13 bước từ T1.1 tới IE1.2** trở thành công bỏ đi, trong đó đã có sẵn 5 bước NVA. Thêm vào đó, thông tin quyền lợi không nhất quán giữa nhân viên, tổng đài và chính sách công bố khiến phải giải thích và xử lý lại – việc giải thích lại này không được vẽ trên mô hình | Từ chối bảo hành: **BH2 – 5 nguồn, đồng hạng cao nhất**. Thông tin không nhất quán: **BH6 – 4 nguồn**. Tỷ lệ ca bị từ chối: **chưa biết** | Đưa danh sách trường hợp loại trừ lên bước T1.2 và cho khách xác nhận đã đọc trước khi gửi máy; chụp ảnh hiện trạng tại T1.3 làm căn cứ; hợp nhất một nguồn chính sách duy nhất cho nhân viên, tổng đài và trang web, có ghi ngày hiệu lực |
| **Overdo** | Over-processing | **Không có bước NVA nào** – phần lặp lại nằm trong pool hộp đen | Kiểm tra hộp và phụ kiện ở T1.3 tại quầy, rồi Trung tâm Bảo hành kiểm tra lại tình trạng máy khi thẩm định. Bước T1.3 tự nó là BVA và cần thiết; phần thừa là lần kiểm thứ hai, mà lần đó nằm bên trong pool Trung tâm Bảo hành nên không có mã bước. **Lưu ý:** thẩm định nguyên nhân lỗi **không** phải over-processing – đó là việc chỉ họ có thẩm quyền làm | **1 lần lặp mỗi ca (ước lượng)** – suy từ việc cả hai bên đều phải ghi nhận hiện trạng máy | Chuẩn hóa lại vai trò: quầy **chỉ ghi nhận hiện trạng** bằng ảnh và checklist có chữ ký khách ở T1.3, Trung tâm Bảo hành nhận nguyên biên bản đó và chỉ thẩm định nguyên nhân lỗi, không kiểm lại ngoại quan |
| **Overdo** | Over-production | **Không có bước NVA nào** – ứng viên là hai bước BVA bị bỏ phí trên một nhánh | Ứng viên: hai bước tra tồn T7.1 và T7.2 được chạy, rồi khách chuyển sang hoàn tiền ở nhánh G8 nên công tra tồn bị bỏ. Cả hai bước đó là BVA khi ca đi tiếp sang đổi máy, chỉ thành vô ích trên đúng nhánh này, nên không thể chấm NVA cho chúng trong bảng 4.2 | **Chưa đủ dữ kiện để kết luận.** Cần tỷ lệ ca đi vào nhánh G8 "chuyển sang hoàn tiền", mà báo cáo nguồn mục 4.3 ghi rõ là không suy được từ nguồn công khai. Mô hình hiện đặt tỷ lệ nhánh này bằng 0% ở `GT43` | Cách lấy số thật: trích log ERP đếm số ca theo từng nhánh của G6, G7, G8 trong 3 tháng gần nhất. Trước khi có số đó thì **không** kết luận đây là lãng phí |

Đọc chéo hai bảng thì thấy hai quy trình lệch nhau đúng ở chỗ đáng lệch. C3 gánh cả ba dạng Overdo trên đường đi của giấy tờ: làm lại hồ sơ, gọi lặp, tạo đơn rồi hủy. C4 hầu như không có Overdo có mã bước, nhưng gánh 7 trên 11 bước NVA ở nhóm Move và 4 ở nhóm Hold, tức toàn bộ lãng phí của nó nằm trên đường đi của cái máy. Đó là lý do hai quy trình phải cải tiến theo hai hướng khác nhau, và cũng là điều mà một danh sách lãng phí rời, không gắn mã bước, sẽ không cho thấy.

---

## 3. Phân tích các bên liên quan

Rubric cho chọn một trong ba công cụ (Pareto, why-why, Fishbone). Nhóm làm hai trong ba: sơ đồ xương cá sáu nhánh 6M cho C4 ở mục 3.1, và biểu đồ Pareto cho cả hai quy trình C3 và C4 thay vì một, để so được hai quy trình trên cùng một thước đo.

Phần truy nguyên nhân 6M trình bày song song ở hai dạng: bảng để tra từng nguyên nhân kèm cột khắc phục, và sơ đồ để nhìn được toàn cảnh sáu nhánh cùng lúc. Giữ cả hai vì mục 5 dẫn ngược về từng nhánh của bảng này, mà bảng thì không cho thấy nhánh nào đang gánh nhiều nguyên nhân nhất, sơ đồ cho thấy ngay.

### 3.1 Truy nguyên nhân theo sáu nhánh 6M cho C4

Vấn đề truy nguyên: *Thời gian xử lý một yêu cầu bảo hành hoặc đổi trả kéo dài nhiều ngày, dù chính sách cho phép đổi ngay trong tháng đầu.*

**Bảng 4.5 – Nguyên nhân theo 6 nhánh**

| Nhánh 6M | Nguyên nhân | Bám vào đâu trên mô hình hoặc bằng chứng | Khắc phục |
|---|---|---|---|
| **Man** – Con người | Thẩm quyền kết luận nguyên nhân lỗi không nằm ở cửa hàng, chỉ Trung tâm Bảo hành được kết luận | Annotation A3 của mô hình C4; pool Trung tâm Bảo hành là "bên duy nhất có quyền kết luận nguyên nhân lỗi" | Phân quyền có kiểm soát: ban hành danh mục lỗi hiển nhiên cho phép cửa hàng kết luận, kèm hậu kiểm theo mẫu |
| **Man** | Nhân viên tư vấn quyền lợi lệch với chính sách công bố | BH6 – 4 nguồn | Một nguồn chính sách duy nhất có ghi ngày hiệu lực, dùng chung cho nhân viên, tổng đài và trang web; kiểm tra định kỳ bằng ca giả lập |
| **Man** | Nhân viên tiếp nhận chưa có chuẩn ghi nhận hiện trạng máy ở T1 | Bước T1 của mô hình; BH8 – 3 nguồn về tranh chấp phụ kiện và hộp | Checklist ảnh bắt buộc tại T1, khách ký xác nhận điện tử ngay trên phiếu |
| **Method** – Phương pháp | T3 bắt buộc chuyển **mọi ca** lên Trung tâm Bảo hành, kể cả lỗi hiển nhiên | Bước T3 và annotation A3; BH1 – 5 nguồn | Định tuyến theo loại lỗi: nhóm lỗi hiển nhiên xử lý tại chỗ, nhóm còn lại mới gửi đi |
| **Method** | Sau IE1 phải vòng về cửa hàng tư vấn và chờ khách chọn phương án rồi mới ra lệnh sửa ở T10 – máy nằm chờ suốt vòng này | Chuỗi IE1 → G3 → G4 → T5 hoặc T6 → G6 → T10, rồi MF5 mới đi ra. Message flow MF5 chỉ mang yêu cầu sửa, không mang máy | Cho khách chọn trước phương án ngay lúc tiếp nhận ở T1 theo từng kịch bản kết luận, để khi kết luận về là ra lệnh sửa được ngay; hoặc cho Trung tâm Bảo hành sửa luôn với nhóm lỗi đã có phương án mặc định |
| **Method** | T14 gom máy lỗi thu hồi theo kỳ, không theo ca | Bước T14 | Chuyển trả hãng theo ngưỡng số lượng hoặc ngưỡng tuổi tồn |
| **Machine** – Máy móc, hệ thống | Trạng thái ca bảo hành không hiển thị cho khách, khách phải gọi hỏi | BH3 – 4 nguồn | Trang tra cứu trạng thái theo mã phiếu, tự động phát thông báo ở mỗi lần đổi trạng thái |
| **Machine** | ERP cửa hàng không nối trạng thái với hệ thống Trung tâm Bảo hành, nên IE1 phải chờ thông báo thủ công | Sự kiện IE1 và message flow MF3 | Tích hợp trạng thái hai chiều; trước mắt nếu chưa tích hợp được thì áp lịch cập nhật bắt buộc theo ngày |
| **Material** – Vật tư | Hết máy đổi đúng model tại kho, phải đổi model tương đương hoặc chuyển sang hoàn tiền | Nhánh G7 → G8 của mô hình | Dự trữ máy đổi theo top model bán chạy dựa trên lịch sử ca bảo hành; cho tra tồn liên cửa hàng trước khi tư vấn |
| **Material** | Thiếu hộp hoặc phụ kiện làm phát sinh phí ở T2 và kéo dài tranh luận tại quầy | Bước T2; BH8 – 3 nguồn; phí 5% và 2% (số công bố) | Nhắc khách mang đủ hộp và phụ kiện ngay khi đặt lịch; hiển thị biểu phí trước để khách quyết định trước khi tới |
| **Measurement** – Đo lường | Không đo thời gian từng chặng, nguồn chỉ cho tổng thời gian khách cảm nhận | Báo cáo nguồn thứ cấp mục 4.1 | Ghi mốc thời gian tại 5 điểm: nhận máy, rời cửa hàng, tới trung tâm, có kết luận, về cửa hàng |
| **Measurement** | Không có tỷ lệ thật của từng nhánh nên không biết nút thắt nằm ở nhánh nào | Báo cáo nguồn thứ cấp mục 4.3 | Trích log ERP đếm số ca theo từng nhánh của G3, G4, G6, G7, G9 trong 3 tháng |
| **Measurement** | Cam kết 15 ngày không được đo và công bố tỷ lệ đạt | Annotation A8; cam kết 15 ngày (số công bố, 3 nguồn) | Đưa "tỷ lệ ca đạt cam kết 15 ngày" thành chỉ số vận hành, công bố nội bộ theo tháng |
| **Milieu** – Môi trường | Lịch chuyến vận chuyển cố định trong ngày, ca đến sau phải chờ sang chuyến kế **(ước lượng)** | Suy từ bước T3; chưa kiểm chứng | Xác minh lịch chuyến trong phỏng vấn; nếu đúng thì tăng tần suất chuyến trong khung giờ tiếp nhận cao điểm |
| **Milieu** | Cuối tuần dồn tải tại quầy tiếp nhận **(ước lượng)** | Suy luận của nhóm, chưa quan sát | Đặt lịch hẹn bảo hành trước qua app để dàn tải; quan sát tại cửa hàng để xác nhận trước khi đề xuất chính thức |
| **Milieu** | Chính sách công bố đổi nhiều lần (bản đang hiệu lực ghi ngày cập nhật 11.10.2024), làm kỳ vọng của khách lệch với quy định đang áp dụng | Báo cáo nguồn thứ cấp mục 0 giới hạn 3 | Hiển thị phiên bản chính sách áp dụng theo ngày mua trên phiếu tiếp nhận, để khách và nhân viên nói chuyện trên cùng một bản |

![Hình 4.1, Xương cá 6M cho C4](../diagrams/fishbone-C4.png)

*Hình 4.1, Sơ đồ xương cá sáu nhánh 6M, nguyên nhân kéo dài thời gian xử lý một yêu cầu bảo hành hoặc đổi trả (C4). Dựng từ chính bảng trên.*

Đọc sơ đồ theo hai lớp, đúng cách phân tầng ở `chap05.pdf` trang 41: nhánh Primary nét liền là nguyên nhân rút gọn từ bảng trên, bản đầy đủ của từng nguyên nhân đọc ở chính bảng ấy; nhánh Secondary nét đứt là nguyên nhân gốc sâu hơn một cấp, suy từ cột *Khắc phục* của cùng dòng. Nhìn toàn cảnh thì hai nhánh Method và Machine mang nhiều nguyên nhân nhất, và cả hai đều nói về cùng một đoạn, quãng từ khi máy rời cửa hàng tới khi có kết luận thẩm định. Đó cũng là đoạn mà phần định lượng đo được là chiếm 82,0% toàn bộ thời gian chờ của C4.

### 3.2 Pareto cho C3

#### 3.2.1 Hai thước đo tác động, và vì sao giữ cả hai

Tài liệu môn học định nghĩa biểu đồ Pareto là *"biểu đồ cột trong đó chiều cao của cột biểu thị tác động của từng vấn đề; các cột được sắp xếp theo sự tác động"*, và ví dụ đi kèm đo tác động ấy bằng tiền: ba cột 60.000, 15.000 và 2.400 USD lấy nguyên từ cột *Tác động định lượng* của bảng đăng ký vấn đề đặt ngay trước đó. Pareto vì thế không phải một biểu đồ đếm, nó là một biểu đồ xếp hạng thiệt hại.

Nhóm dựng hai biểu đồ cho mỗi quy trình, vì hai thước đo trả lời hai câu khác nhau và câu nào cũng cần cho phần đề xuất cải tiến.

Thước thứ nhất, tiền, là thước chính. Trục tung là số tiền lãng phí trên một ca, mỗi cột là một vấn đề trong bảng đăng ký vấn đề, và cột đó chỉ được vẽ khi khai được trọn phép nhân ra con số. Bảng nguồn của cả hai biểu đồ tiền là {B:pareto-tien-bang}, bậc thang nhân lên quy mô là {B:bac-thang-quy-mo}, cả hai đặt ở phần phân tích định lượng.

Đây là số ước lượng, không phải số kế toán. Nhóm không có quyền truy cập dữ liệu vận hành nên không đo được đồng nào. Cách làm là: mỗi thừa số của phép nhân hoặc là số công bố có dẫn nguồn, hoặc là một giả định mang mã `GT` khai sẵn ở bảng giả định, và ô kết quả luôn viết ra phép nhân để tra ngược được. Đổi một mã `GT` là biết ngay phải tính lại dòng nào.

Thước thứ hai, số nguồn công khai nhắc tới chủ đề, là bằng chứng phụ. Rubric và quy ước phân tích của nhóm đề xuất trục tung là số ca, nhưng nhóm không có dữ liệu số ca: Phụ lục B mục 4.3 ghi rõ không suy được tỷ lệ nhánh của mô hình từ nguồn công khai, và bịa ra một cột "số ca" là đúng thứ mà quy ước ấy cấm. Thứ đếm được thật là bảng mã hóa chủ đề trong 28 nguồn đã đọc ngày 19/08/2026, đơn vị đếm là số đường dẫn phân biệt nhắc tới chủ đề. Trục tung được đặt tên đúng như vậy, không ghi "số ca". Chủ đề TG3 ("Số hóa rút ngắn thời gian duyệt", 3 nguồn) bị loại khỏi biểu đồ vì đó là nội dung quảng cáo của đối tác cho vay, mô tả điểm mạnh chứ không phải trở ngại; giữ lại sẽ làm sai nghĩa trục hoành.

Một điều phải nói trước khi đọc tiếp: hai biểu đồ không xác nhận lẫn nhau. Biểu đồ tiền đứng trên các tỷ lệ nhánh mà nhóm tự đặt ở bảng giả định nhóm E; biểu đồ đếm nguồn đứng trên 28 nguồn công khai. Đặt cạnh nhau là để thấy chỗ chúng lệch nhau, chứ không phải để cái này chứng minh cái kia.

#### 3.2.2 Pareto theo chi phí cho C3

@@FIG:pareto-tien-C3@@

Ba khoản lãng phí của C3 quy được ra tiền, xếp giảm dần:

- `I-15` Công bỏ đi ở hồ sơ trả góp bị từ chối, 6.953 đ/ca (ước lượng), 67,2%. Hồ sơ đi hết tư vấn, lập hồ sơ, một vòng chờ thẩm định, tới cổng `G6` mới bị rẽ nhánh "Từ chối". Toàn bộ công đã bỏ ra không sinh ra giao dịch nào, kể cả 3 phút dọn dẹp ở `T6` để mở khóa IMEI và trả máy về tồn bán.
- `I-04` Công làm lại vì hồ sơ thiếu giấy tờ, 3.125 đ/ca (ước lượng), lũy kế 97,4%. Vòng bổ sung giấy tờ bắt bước lập hồ sơ chạy lại một lượt.
- `I-13` Vốn nằm chờ cuộc gọi xác nhận thủ công, 274 đ/ca (ước lượng), lũy kế 100,0%. Máy bị khóa số IMEI suốt quãng chờ 60 phút, khoản này là chi phí vốn của quãng ấy.

Cộng lại 10.352 đ mỗi ca. Nhân theo bậc thang của {B:bac-thang-quy-mo}: một cửa hàng chạy 96 ca C3 mỗi tháng (ước lượng), tức 993.792 đ một cửa hàng một tháng, 11,9 triệu đồng một cửa hàng một năm, và ≈ 12,1 tỷ đồng một năm cho cả 1.012 cửa hàng của chuỗi. Đây là cách đọc mà một biểu đồ đếm lượt nhắc không cho được: nó nói thẳng cắt được bao nhiêu tiền.

Hai khoản đầu đã chiếm 97,4%. Cả hai đều nằm ở nửa đầu quy trình, đoạn chuẩn bị và nộp hồ sơ, và cả hai đều chữa được bằng cùng một việc: kiểm đủ điều kiện và đủ chứng từ ngay tại bước tiếp nhận, trước khi tốn 15 phút lập hồ sơ và một vòng chờ thẩm định.

#### 3.2.3 Bảng 4.6 – Bảng nguồn của biểu đồ Pareto đếm nguồn C3

| Thứ tự | Mã | Trở ngại trên đường hồ sơ đi tới giải ngân | Bước nào trên mô hình | Số nguồn | % | % lũy kế | Khắc phục |
|---:|---|---|---|---:|---:|---:|---|
| 1 | TG1 | Bộ giấy tờ thay đổi theo công ty tài chính và theo giá trị khoản vay, dễ chuẩn bị thiếu rồi phải bổ sung | T4 – lập hồ sơ vay và tải chứng từ | 4 | 44,4% | 44,4% | Checklist giấy tờ động sinh theo bên cho vay và giá trị vay, chặn nút gửi khi còn thiếu; cho khách tải chứng từ trước qua app |
| 2 | TG2 | Thẩm định gọi xác minh nơi làm việc và người thân, gọi lặp nhiều cuộc cho cùng một đầu mối | IE1 – chờ kết quả thẩm định | 2 | 22,2% | 66,7% | Ghi nhận kết quả từng cuộc xác minh vào hồ sơ để không gọi lại đầu mối đã liên hệ được; xin trước sự đồng ý của người tham chiếu ngay ở T4 |
| 3 | TG4 | Đơn đặt online vẫn phải có nhân viên gọi xác nhận thủ công trong 60 phút | Trước E1 – kênh đặt hàng trực tuyến | 2 | 22,2% | 88,9% | Xác thực khách ngay lúc đặt online bằng OTP và đối chiếu căn cước điện tử, bỏ cuộc gọi xác nhận cho đơn đã xác thực |
| 4 | TG5 | Hồ sơ bị từ chối thì phải chờ mới nộp lại được (có bên yêu cầu 6 tháng) | G6 nhánh "Từ chối" → T2 | 1 | 11,1% | 100,0% | Sàng lọc sơ bộ ở T1 theo tiêu chí của từng bên cho vay để chọn đúng bên ngay lần đầu, tránh đốt cơ hội nộp (annotation A1) |
| | | **Tổng** | | **9** | **100%** | | **Ba trở ngại đầu chiếm 88,9%** – xử lý TG1, TG2, TG4 là xử lý gần như toàn bộ phần quan sát được |

@@FIG:pareto-C3@@

#### 3.2.4 Kết luận Pareto C3

Đọc riêng biểu đồ đếm nguồn: ba chủ đề TG1, TG2, TG4 chiếm 88,9% tổng lượt nhắc, riêng TG1 đã 44,4%. Cả ba nằm ở nửa đầu quy trình, đoạn chuẩn bị và nộp hồ sơ, xác minh và xác nhận đơn, chứ không nằm ở khâu thanh toán hay bàn giao.

Đọc chồng hai biểu đồ thì thấy chỗ chúng lệch nhau, và chỗ lệch mới là phát hiện. `TG5` (hồ sơ bị từ chối) đứng cuối biểu đồ đếm nguồn với đúng 1 lượt nhắc, nhưng chính nó là `I-15`, cột cao nhất của biểu đồ tiền với 67,2%. Lý do khá dễ hiểu: khách bị từ chối vay thường im lặng, còn khách phải chạy đi bổ sung giấy tờ thì lên diễn đàn hỏi. Số lượt nhắc đo mức ồn ào, tiền đo mức thiệt hại, và hai thứ đó không đi cùng nhau. Nếu chỉ có biểu đồ đếm nguồn thì nhóm đã xếp sai thứ tự ưu tiên cải tiến.

Chỗ hai biểu đồ đồng ý với nhau cũng đáng ghi: `TG1` và `I-04` là cùng một vấn đề, đứng đầu ở biểu đồ này và đứng thứ hai ở biểu đồ kia, và phần định lượng đo được nó sinh ra 60,7% toàn bộ thời gian chờ của C3. Ba cách đo độc lập cùng chỉ vào bước lập hồ sơ vay.

**Bốn giới hạn phải giữ nguyên khi đưa vào báo cáo:**

1. Cỡ mẫu của biểu đồ đếm nguồn nhỏ (n = 9 lượt nhắc trên 4 chủ đề). Kết luận 88,9% mô tả phần quan sát được từ nguồn công khai, không phải phân bố thật của doanh nghiệp.
2. Thiên lệch chọn mẫu: người có trải nghiệm suôn sẻ hầu như không viết bài. Không được suy ra tỷ lệ hồ sơ rớt từ biểu đồ đếm nguồn.
3. Lệch thời gian: TG2 lấy từ nguồn năm 2016, trong khi trang đối tác năm 2026 ghi "không yêu cầu thẩm định người thân". Hai nguồn không mâu thuẫn mà là dấu vết quy trình đã thay đổi, phải ghi năm bên cạnh mọi trích dẫn.
4. Biểu đồ tiền là ước lượng có điều kiện: nó đứng trên các tỷ lệ nhánh do nhóm tự đặt. Con số 6.953 đ và 3.125 đ đi liền với tỷ lệ từ chối 15% và tỷ lệ bổ sung giấy tờ 20%; hai tỷ lệ ấy đổi thì hai con số đổi theo đúng tỷ lệ, cấu trúc biểu đồ giữ nguyên.

Cách lấy số thật nếu có quyền truy cập: trích log ERP và log hệ thống của bên cho vay trong 3 tháng, đếm số hồ sơ theo trạng thái kết thúc (bổ sung giấy tờ, không đạt điều kiện thu nhập, khách từ chối lãi suất, hết hạn giữ máy, không đủ khoản trả trước), rồi thay tỷ lệ thật vào đúng những ô mang mã `GT` của bảng nguồn. Khung 5 lý do đó đã có sẵn trong quy ước phân tích của nhóm, giữ nguyên để thay số vào khi có dữ liệu.

### 3.3 Pareto bổ sung cho C4

C4 làm đúng cặp biểu đồ như C3: một biểu đồ tiền làm chính, một biểu đồ đếm nguồn làm bằng chứng phụ. Bộ đếm của C4 dày hơn hẳn bộ của C3, 34 lượt nhắc trên 9 chủ đề, nên chỗ hai biểu đồ lệch nhau càng rõ.

@@FIG:pareto-tien-C4@@

Ba khoản lãng phí của C4 quy được ra tiền:

- `I-03` Công và vận chuyển bỏ đi ở ca bị từ chối, 20.756 đ/ca (ước lượng), 73,4%. Ca bị kết luận "lỗi do người dùng" chỉ sau khi máy đã được lập phiếu, chở lên Trung tâm Bảo hành, xếp hàng chờ và thẩm định xong. Toàn bộ công và hai lượt vận chuyển đổ vào 25% số ca này không đem lại gì – máy đi lên rồi lại phải chở về cho khách theo `MF10`, vì nó là tài sản của khách chứ không phải hàng của cửa hàng.
- `I-02` Vận chuyển thừa của ca lẽ ra xong tại cửa hàng, 6.606 đ/ca (ước lượng), lũy kế 96,8%. Trên mô hình không có đường đi nào kết thúc tại cửa hàng, mọi ca đều phải qua bước chuyển máy đi. Khoản này tính trên phần ca không bị từ chối mà lẽ ra kết luận được ngay tại quầy nếu có danh mục lỗi hiển nhiên.
- `I-10` Công tính phí thiếu hộp và thiếu phụ kiện, 902 đ/ca (ước lượng), lũy kế 100,0%. Bước tính phí chạy trên 30% số ca chỉ vì khách không được nhắc mang đủ hộp trước khi tới.

Cộng lại 28.264 đ mỗi ca, tức 339.168 đ một cửa hàng một tháng với 12 ca C4 (ước lượng), và ≈ 4,1 tỷ đồng một năm cho cả chuỗi. Cộng cả hai quy trình, phần lãng phí quy được ra tiền là ≈ 16,2 tỷ đồng mỗi năm (ước lượng).

Ba khoản này không chồng lấn nhau: `I-03` tính trên 25% ca bị từ chối, `I-02` tính trên 75% ca không bị từ chối, hai tập rời nhau theo đúng cách chia của cổng `G3`; `I-10` là công của một bước khác hẳn. Bảng nguồn {B:pareto-tien-bang} ghi phép kiểm cho chỗ này.

**Bảng 4.7 – Bảng nguồn của biểu đồ Pareto đếm nguồn C4**

| Thứ tự | Mã | Chủ đề vấn đề | Số nguồn | % | % lũy kế | Nhóm lãng phí | Khắc phục |
|---:|---|---|---:|---:|---:|---|---|
| 1 | BH1 | Máy phải đi qua nhiều tầng: cửa hàng → Trung tâm Bảo hành → hãng | 5 | 14,7% | 14,7% | Move | Phân quyền kết luận tại cửa hàng cho danh mục lỗi hiển nhiên; giữ máy tại trung tâm giữa hai chặng |
| 2 | BH2 | Thẩm định kết luận không thuộc diện bảo hành, khách bị từ chối | 5 | 14,7% | 29,4% | Overdo | Đưa danh sách trường hợp loại trừ lên bước T1, chụp ảnh hiện trạng làm căn cứ, cho khách xác nhận trước khi gửi máy |
| 3 | BH3 | Thời gian chờ thực tế dài hơn thời gian nhân viên hẹn | 4 | 11,8% | 41,2% | Hold | Trang tra cứu trạng thái ca; xếp hàng chờ theo hạn cam kết 15 ngày; đo và công bố tỷ lệ đạt cam kết |
| 4 | BH4 | Mốc 30 ngày quyết định đổi tại chỗ hay phải gửi thẩm định | 4 | 11,8% | 52,9% | – (điểm rẽ chính sách) | Hiển thị số ngày còn lại của mốc tháng đầu ngay trên app và trên phiếu tiếp nhận |
| 5 | BH6 | Thông tin không nhất quán giữa nhân viên, tổng đài và chính sách công bố | 4 | 11,8% | 64,7% | Overdo | Một nguồn chính sách duy nhất có ghi ngày hiệu lực dùng chung cho ba kênh |
| 6 | BH5 | Phí đổi trả theo tháng sử dụng gây bất ngờ cho khách | 3 | 8,8% | 73,5% | Overdo | Hiển thị biểu phí lũy tiến theo số tháng đã dùng ngay khi khách tra cứu, trước khi tới cửa hàng |
| 7 | BH7 | Khách phải quay lại cửa hàng thêm lần nữa để nhận máy | 3 | 8,8% | 82,4% | Move | Cho chọn nhận máy tại nhà sau khi sửa xong |
| 8 | BH8 | Thiếu phụ kiện hoặc thiếu hộp làm phát sinh phí | 3 | 8,8% | 91,2% | Overdo | Nhắc mang đủ hộp và phụ kiện khi đặt lịch; checklist ảnh tại T1 |
| 9 | BH9 | Hàng cũ, hàng trưng bày có quyền lợi bảo hành khác hàng mới | 3 | 8,8% | 100,0% | – (phạm vi chính sách) | Ghi rõ nhóm sản phẩm và quyền lợi tương ứng trên hóa đơn ngay lúc bán |
| | | **Tổng** | **34** | **100%** | | | **Bảy chủ đề đầu chiếm 82,4%**; năm chủ đề đầu đã chiếm **64,7%** |

@@FIG:pareto-C4@@

Kết luận Pareto C4. Phân bố của biểu đồ đếm nguồn phẳng hơn hẳn C3, không chủ đề nào áp đảo, phải gộp tới bảy chủ đề mới chạm 82,4%. Nhưng năm chủ đề đầu (BH1, BH2, BH3, BH4, BH6) đã chiếm 64,7%, và bốn trong năm nằm trên cùng một đoạn: từ lúc tiếp nhận máy ở T1 đến lúc có kết luận thẩm định ở IE1. Kết luận này trùng khớp với hai công cụ khác:

- Bảng giá trị gia tăng của C4 chỉ ra bảy trong mười một bước NVA (T3.2, T3.3, T3.4, IE1.1, IE1.2, T10.1, T10.2) nằm trên đúng đoạn này, và đó là bảy bước gánh gần như toàn bộ thời gian chờ.
- Bảng 6M chỉ ra hai nhánh Method và Machine, đều nói về đoạn này, mang nhiều nguyên nhân nhất.

Biểu đồ tiền vừa đồng ý vừa sửa lại kết luận đó, và cả hai chiều đều phải nói ra:

- Đồng ý ở chỗ ưu tiên số một. `BH2` (thẩm định kết luận không thuộc diện bảo hành) đứng đồng hạng nhất ở biểu đồ đếm nguồn, và chính nó là `I-03`, đứng nhất ở biểu đồ tiền với 70,6%. Hai thước đo hoàn toàn khác nhau cùng chỉ vào một việc: phải nói cho khách biết khả năng bị từ chối trước khi gửi máy đi, chứ không phải sau khi đã tốn cả tuần.
- Sửa lại ở chỗ vấn đề tốn thời gian nhất. `BH3` và `BH1`, tức hàng đợi và quãng đường, đứng đầu bảng đếm nguồn và cũng là thứ phần định lượng đo được là chiếm 82,0% toàn bộ thời gian chờ, nhưng chúng không có mặt trên biểu đồ tiền. Lý do không phải bỏ sót mà là một phát hiện: máy nằm chờ là tài sản của khách chứ không phải tồn kho của cửa hàng, còn hàng đợi thì nằm trong pool của đối tác, nên quãng chờ ấy gần như không tốn đồng nào của doanh nghiệp. Toàn bộ tiền của nó rơi sang khách hàng, ước lượng 93.789 đ một ca, nhiều hơn cả ba khoản trên biểu đồ cộng lại.

Đó là câu trả lời cho một câu hỏi mà báo cáo phải trả lời được: vì sao một quy trình lãng phí 96,8% thời gian mà vẫn tồn tại nhiều năm. Vì cái giá của nó không nằm trong sổ sách của người có quyền sửa nó. Muốn khoản đó xuất hiện trên biểu đồ tiền của doanh nghiệp thì phải đưa nó vào hợp đồng với Trung tâm Bảo hành dưới dạng mức phí hoặc mức phạt theo thời gian lưu, hoặc phải đo nó bằng một thước khác, chẳng hạn tỷ lệ khách quay lại mua tiếp.

**Ba giới hạn của cặp biểu đồ C4:**

1. Thiên lệch chọn mẫu của biểu đồ đếm nguồn: khách hài lòng hầu như không viết bài, nên nó cho biết chủ đề nào bị nói tới nhiều nhất, không cho biết tần suất ca thực tế.
2. Biểu đồ tiền chỉ đếm tiền doanh nghiệp bỏ ra. Khoản 93.789 đ khách hàng chịu cố ý để ngoài, vì cộng hai túi tiền khác nhau vào một cột lũy kế là làm hỏng nghĩa của biểu đồ. Nó được ghi riêng trong bảng đăng ký vấn đề.
3. Những vấn đề còn lại của C4 chưa quy được ra tiền, trong đó có trễ cam kết 15 ngày và chuyển động nội bộ của nhân viên. {B:pareto-tien-loai-tru} ghi rõ từng trường hợp thiếu dữ kiện gì và lấy ở đâu, thay vì điền một con số ước lượng cho đủ cột.

---
## 4. Bàn giao sang phần định lượng

Những chỗ phần định tính buộc phải để trống, và phần định lượng (P6) phải lấp:

| # | Số cần | Dùng cho | Cách lấy |
|---:|---|---|---|
| 1 | Thời gian chờ ở IE1 của C3 và của C4 | Cycle time, CTE, chi phí cơ hội máy nằm chờ | Phỏng vấn nhân viên; hoặc trích log ERP mốc nhận máy và mốc có kết luận |
| 2 | Tỷ lệ ca theo từng nhánh của G6 (C3) và G3, G6, G7, G9 (C4) | Cycle time trung bình có trọng số; quy mô Defects và Over-production | Trích log ERP 3 tháng, đếm theo trạng thái kết thúc |
| 3 | Tỷ lệ hồ sơ trả góp phải bổ sung giấy tờ | Quy mô lãng phí Defects của C3 (mục 2.1) | Log hệ thống bên cho vay, hoặc đếm tay trong một tuần tại cửa hàng |
| 4 | Chi phí một lượt vận chuyển và thời gian mỗi lượt của C4 | Quy mô lãng phí Move của C4 (mục 2.2) và bảng chi phí | Số lượt đã đọc được từ mô hình (2 lượt mỗi ca, mục 2.2). Còn thiếu **đơn giá và thời gian mỗi lượt** – hỏi trong phỏng vấn, hoặc dùng đơn giá nhân viên giao nhận kho trung tâm ở báo cáo nguồn mục 3.2 |
| 4b | Chiều về của máy lỗi trên nhánh đổi máy và hoàn tiền của C4 | Hoàn thiện mô hình trước khi chụp vào Word; ảnh hưởng số lượt vận chuyển | **Chốt với người vẽ C4 (Danh) theo mục 0.2 điểm 1**, trước khi P6 tính chi phí vận chuyển |
| 5 | Số lượt di chuyển nội bộ của nhân viên | Nhóm Motion của cả hai bảng, hiện đang ghi "chưa đủ dữ kiện" | Một buổi quan sát tại cửa hàng, n ≥ 8 ca |
| 6 | Đơn giá nhân công theo giờ | Bảng chi phí | Đã có khoảng lương công bố ở báo cáo nguồn mục 3.2; chia theo số ngày công và số giờ mỗi ca, ghi rõ hai giả định đó |
| 7 | Tỷ lệ ca C4 đạt cam kết 15 ngày | Bảng chất lượng | Log ERP; nếu không có quyền thì ghi rõ là không đo được, không ước lượng |

---

## 5. Việc phải soát lại

| # | Việc | Trạng thái | Khi nào |
|---:|---|---|---|
| 1 | Đối chiếu toàn bộ mã bước, nhãn và lane trong file này với bốn file `.bpmn` của C3 và C4 (hai hình khung, hai hình chi tiết) | **Xong** – kết quả ở mục 0.2, khớp 18/18 cho cả C3 và C4 | Đã chạy sau khi P3B sinh `do-an/bpmn/` |
| 2 | Đếm lại số lượt vận chuyển của C4 sau khi `MF9` đưa chiều về lên mô hình (mục 0.2 điểm 1) | **Đã vẽ xong, còn chờ tính lại** | Trước khi chụp hình C4 đưa vào Word và trước khi P6 tính chi phí vận chuyển |
| 3 | Thống nhất nhãn task T10 với nhãn message flow MF5 của C4 (mục 0.2 điểm 2) | **Xong** – chốt cách đọc "máy nằm lại trung tâm", sửa nhãn MF5 | Đã chốt ở phiên R7 |
| 4 | Chạy lại đối chiếu mã bước nếu bộ file `.bpmn` được sinh lại | Chưa cần | Mỗi lần `gen_bpmn.py` chạy lại |
| 5 | Chụp màn hình trang chính sách bảo hành thegioididong.com lưu vào `evidence/` | Chưa làm | Trước khi trích các mốc phí 20% / 10% / 5% / 2% và mốc 15 ngày vào Word – chính sách có thể được cập nhật |
| 6 | Xác nhận số nguồn của từng mã `BH*` và `TG*` khớp với bảng mã hóa gốc | Chưa làm | Trước khi nộp |
| 7 | Kiểm mọi bảng đều có cột "Khắc phục" và mọi số ước lượng đều mang chữ "(ước lượng)" | Chưa làm | Bước soát cuối, theo P9 |
