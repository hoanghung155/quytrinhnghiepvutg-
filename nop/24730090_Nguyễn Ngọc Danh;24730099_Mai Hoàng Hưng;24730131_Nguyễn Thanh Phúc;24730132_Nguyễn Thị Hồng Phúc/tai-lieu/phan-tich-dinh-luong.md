# Chương 4 – Phân tích định lượng quy trình C3 và C4

Phục vụ Tiêu chí 4.2 của rubric: ba khía cạnh Thời gian · Chất lượng · Chi phí (`chap05.pdf` trang 43), làm cho cùng cặp quy trình đã dùng ở phần định tính.

| Mã | Quy trình | File mô hình |
|---|---|---|
| **C3** | Bán trả góp qua công ty tài chính | `do-an/bpmn/C3-ban-tra-gop.bpmn` |
| **C4** | Bảo hành, đổi trả 1 đổi 1 và thu hồi máy lỗi | `do-an/bpmn/C4-bao-hanh-doi-tra.bpmn` |

---

## 0. Ba điều phải đọc trước khi dùng bất kỳ con số nào

### 0.1 Nhóm không có buổi quan sát tại cửa hàng – hệ quả trực tiếp

`04-phan-tich-quy-trinh.md` mục 2 chia số liệu làm ba loại: công bố / quan sát / ước lượng. Đối chiếu với thực tế đang có:

| Mức tin cậy | Có dùng được trong tài liệu này không | Vì sao |
|---|---|---|
| `công bố` | **Có** | Trang chính sách, tin tuyển dụng và báo cáo kết quả kinh doanh đã thu thập, có link và ngày truy cập |
| `quan sát` | **Không có dòng nào** | Biên bản buổi 3 (`evidence/bien-ban/buoi-03.md`) còn để trống toàn bộ – nhóm **chưa** tổ chức buổi bấm giờ tại cửa hàng. Không có một con số nào trong tài liệu này được đo bằng đồng hồ |
| `ước lượng` | **Có** – chiếm phần lớn | Mỗi giá trị đều có một mã `GT` ở mục 1, ghi rõ căn cứ suy ra và hệ quả nếu sai |

Không tô mức tin cậy cho đẹp: cột "Mức tin cậy" trong bảng giả định không có giá trị `quan sát` nào. Khi nào nhóm chạy được buổi quan sát thì thay giá trị của các mã `GT10`–`GT19` và tính lại, công thức và cấu trúc bảng giữ nguyên.

### 0.2 Quy tắc truy nguồn – ràng buộc cứng

Mọi con số trong mọi bảng dưới đây thuộc đúng một trong ba dạng:

| Dạng | Ký hiệu trong bảng | Ví dụ |
|---|---|---|
| Số công bố | `[#n]` – số hiệu nguồn trong `evidence/nghien-cuu-thu-cap/bao-cao-nguon-thu-cap.md` mục 1, hoặc `[N1]`/`[N3]` – mã nguồn của Chương 1 | 15 ngày cam kết sửa chữa `[#18]`; 1.012 cửa hàng `[N1]` |
| Số giả định | `GTnn` | Chờ tới lượt thẩm định tại Trung tâm Bảo hành = 4 ngày `GT18` |
| Số dẫn xuất | ghi công thức đầy đủ trong ô | `CT = PT + WT` · `62.500 = 13.000.000 ÷ 26 ÷ 8` |

Nếu một ô không có `GTnn`, không có `[#n]` và không có công thức thì đó là lỗi, báo lại để sửa, không dùng.

### 0.3 Đơn vị và cách quy đổi

| Quy ước | Giá trị | Căn cứ |
|---|---|---|
| Chặng trong cửa hàng | tính bằng **phút** | Theo yêu cầu của rubric và của `04-phan-tich-quy-trinh.md` |
| Chặng vận chuyển và chờ thẩm định | tính bằng **ngày**, quy về phút khi cộng | Cùng nguồn |
| **1 ngày = 8 giờ = 480 phút** | `GT01` | Đúng cách thầy quy đổi ở ví dụ credit application: `Efficiency = 8,9 giờ / 8,65 ngày = 12,9%`, tức 8,65 ngày được đọc thành 69,2 giờ (`chap05.pdf` trang 53) |

Quy ước 8 giờ/ngày là cách dè dặt khi tính C4: máy nằm tại Trung tâm Bảo hành thì nằm liên tục 24 giờ chứ không chỉ trong giờ hành chính. Mục 2.7 tính lại theo ngày lịch 1.440 phút để thấy con số thật còn xấu hơn.

---

## 1. Bảng giả định

### 1.1 Nhóm A – Quy ước đơn vị và ngày công

| Mã GT | Giả định | Giá trị dùng | Căn cứ | Mức tin cậy |
|---|---|---|---|---|
| `GT01` | Một ngày quy ra phút | 480 phút (8 giờ) | Cách quy đổi của `chap05.pdf` trang 53 | ước lượng (theo quy ước giáo trình) |
| `GT02` | Số ngày công một tháng | 26 ngày | Tin tuyển dụng công bố ca xoay 08:00–… `[#31]` nhưng không ghi số ngày công; nhóm lấy 26 ngày (nghỉ 1 ngày mỗi tuần) | ước lượng |

### 1.2 Nhóm B – Đơn giá nhân công

Công thức chung: `đơn giá giờ = trung điểm khoảng lương công bố ÷ GT02 ÷ 8 giờ`. Khoảng lương lấy nguyên từ `bao-cao-nguon-thu-cap.md` mục 3.2, là khoảng lương niêm yết trong tin tuyển dụng, không phải quỹ lương thực chi.

| Mã GT | Vị trí | Khoảng công bố | Trung điểm | Đơn giá giờ | Nguồn | Mức tin cậy |
|---|---|---|---:|---:|---|---|
| `GT03` | Nhân viên tư vấn bán hàng | 11 – 15 tr/tháng | 13.000.000 | **62.500 đ/giờ** | `[#28]` | công bố (khoảng lương) + `GT02` |
| `GT04` | Nhân viên thu ngân | 5 – 8 tr/tháng | 6.500.000 | **31.250 đ/giờ** | `[#33]` | công bố + `GT02` |
| `GT05` | Nhân viên kho | 5 – 8 tr/tháng | 6.500.000 | **31.250 đ/giờ** | `[#34]` | công bố + `GT02` |
| `GT06` | Nhân viên hỗ trợ kỹ thuật (đóng vai NV tiếp nhận bảo hành) | 10 – 15 tr/tháng | 12.500.000 | **60.100 đ/giờ** | `[#30]` | công bố + `GT02` |
| `GT07` | Nhân viên giao nhận kho trung tâm | 10 – 15 tr/tháng | 12.500.000 | **60.100 đ/giờ** | `[#35]` | công bố + `GT02` |
| `GT08` | Quản lý cửa hàng | **không có tin tuyển dụng trong bộ nguồn** | – | **62.500 đ/giờ** (lấy bằng `GT03`) | suy từ `GT03` | ước lượng – đây là **cận dưới**, lương quản lý chắc chắn cao hơn nhân viên |
| `GT09` | Kỹ thuật viên Trung tâm Bảo hành | **không có tin tuyển dụng trong bộ nguồn** | – | **60.100 đ/giờ** (lấy bằng `GT06`) | suy từ `GT06` | ước lượng |

Làm tròn: 12.500.000 ÷ 26 ÷ 8 = 60.096,15 → lấy 60.100 đ/giờ. Hai đơn giá còn lại chia hết nên không phải làm tròn.

### 1.3 Nhóm C – Thang thời gian thao tác

Không có buổi bấm giờ, nên nhóm không gán một con số riêng cho từng bước, làm vậy chỉ tạo cảm giác chính xác giả. Thay vào đó dùng một thang năm mức, mỗi bước được xếp vào một mức và ghi rõ mức đó ngay trong bảng thời gian.

| Mã GT | Mức | Giá trị | Áp dụng cho loại thao tác | Neo theo |
|---|---|---:|---|---|
| `GT10` | `M1` | 3 phút | Thao tác hệ thống đơn: quét mã, tra cứu, cập nhật ERP | Đối tác công bố quy trình đã số hóa "chỉ mất 3 phút" `[#26]` – dùng làm mốc cho thao tác hệ thống thuần |
| `GT10` | `M2` | 10 phút | Thao tác có chứng từ hoặc giao tiếp khách ngắn: lập phiếu, thu tiền, bàn giao | ước lượng |
| `GT10` | `M3` | 15 phút | Tư vấn, thương lượng, ký kết | ước lượng |
| `GT11` | – | 10 phút | Chờ tới lượt tại quầy, giờ thường | ước lượng – **không phải phần tử trên mô hình**, xem mục 2.1 |
| `GT12` | `M4` | 30 phút | Thẩm định kỹ thuật tại Trung tâm Bảo hành | ước lượng |
| `GT13` | `M5` | 90 phút | Thao tác sửa chữa tại Trung tâm Bảo hành | ước lượng |

Mức tin cậy của cả nhóm C: ước lượng. `GT10-M1` có neo công bố cho cận dưới, phần còn lại không có neo.

### 1.4 Nhóm D – Thời gian chờ

| Mã GT | Giả định | Giá trị dùng | Căn cứ | Mức tin cậy |
|---|---|---:|---|---|
| `GT14` | C3 – chờ kết quả thẩm định của công ty tài chính (quãng trước `IE1`) | **60 phút** | Dải quan sát được từ nguồn rất rộng: đối tác quảng cáo "3 phút" `[#26]`, trang đối tác ghi nhân viên gọi xác nhận "trong 60 phút" `[#27]`, còn nguồn 2016 mô tả thẩm định gọi 2 người thân, tới 3 cuộc cho một người `[#25]`. Nhóm lấy mốc 60 phút – đầu trên của con số công bố | ước lượng (neo `[#27]`) |
| `GT15` | C3 – khách về lấy giấy tờ bổ sung rồi quay lại | **1 ngày** = 480 phút | ước lượng, chưa kiểm chứng | ước lượng |
| `GT16` | C3 – hạn giữ máy chờ hồ sơ (timer `IE2`) | **1 ngày** | Mô hình có timer nhưng không ghi hạn; ước lượng | ước lượng |
| `GT17` | C4 – chờ chuyến và vận chuyển **một lượt** cửa hàng ↔ Trung tâm Bảo hành | **1 ngày** | ước lượng; nguồn thứ cấp không mô tả lịch chuyến (`bao-cao-nguon-thu-cap.md` mục 4.2) | ước lượng |
| `GT18` | C4 – chờ tới lượt thẩm định tại Trung tâm Bảo hành | **4 ngày** | Chọn sao cho tổng nhánh sửa chữa nằm **trong** cam kết 15 ngày `[#18]`. Người dùng tự thuật "gần 20 ngày chưa có kết quả" và "phải mất 1 tháng" `[#3]` `[#4]` – tức thực tế có thể xấu hơn | ước lượng (neo `[#18]`) |
| `GT19` | C4 – chờ linh kiện và xếp hàng sửa chữa tại Trung tâm Bảo hành | **6 ngày** | Cùng lý do `GT18` | ước lượng (neo `[#18]`) |

`GT17` + `GT18` + `GT19` + `GT17` = 1 + 4 + 6 + 1 = 12 ngày, tức nhánh sửa chữa vừa lọt cam kết 15 ngày với biên 3 ngày. Đây là lựa chọn có lợi cho doanh nghiệp: nhóm cố tình đặt giả định ở phía đẹp, để kết luận "quy trình vẫn kém hiệu quả" không bị quy là do chọn số xấu.

### 1.5 Nhóm E – Phân bố nhánh

Nhóm E là ước lượng thuần, không có nguồn nào, trừ đúng một dòng: `GT44` là số dẫn xuất từ ba mã khác, không phải một giá trị nhóm tự đặt thêm. `bao-cao-nguon-thu-cap.md` mục 4.3 ghi rõ nhóm không biết tỷ lệ thật của từng nhánh.

> Không được suy tỷ lệ nhánh từ biểu đồ Pareto đếm nguồn. Hai hình `pareto-C3` và `pareto-C4` đếm số nguồn công khai nhắc tới một chủ đề, không phải số ca. Giới hạn 2 nêu ở `dinh-tinh.md` mục 3.2.3 đã cấm phép suy này. Các số dưới đây do nhóm tự đặt, và mục 2.3 với 2.6 cho biết kết luận đổi thế nào nếu đặt sai.
>
> Chiều ngược lại cũng phải nói cho rõ: hai hình `pareto-tien-C3` và `pareto-tien-C4` ở mục 4.6 đứng trên chính các tỷ lệ của nhóm E này, chứ không phải là nguồn độc lập xác nhận chúng. Đặt hai loại Pareto cạnh nhau là để đối chiếu, không phải để cái này chứng minh cái kia.

| Mã GT | Điểm rẽ | Phân bố dùng | Ghi chú |
|---|---|---|---|
| `GT20` | C3 `G1` – đủ điều kiện sơ bộ | 85% đủ / 15% không | Chỉ dùng cho ngoại suy quy mô |
| `GT21` | C3 `G2` – hình thức trả góp | 80% qua công ty tài chính / 20% qua thẻ tín dụng | |
| `GT22` | C3 – kịch bản kết cục, **tính trên nhánh đi qua công ty tài chính** | Duyệt thẳng 45% · Duyệt có điều kiện & khách chấp nhận 20% · Bổ sung giấy tờ rồi mới duyệt 20% · Từ chối 15% | Bốn kịch bản mà rubric yêu cầu. Con số 20% "bổ sung giấy tờ" là **một lượt bổ sung**, và mọi bảng thời gian đều tính theo một lượt. Mô hình khai thêm trần **2 lượt** ở chú thích `A7` cạnh `G12` – đó là **giới hạn trên để vòng lặp có lối thoát**, không phải giá trị dùng để tính |
| `GT23` | C3 `G9` – thu khoản trả trước | 97% thành công / 3% không | |
| `GT24` | C3 `G10` – nhận máy | 85% nhận ngay / 15% hẹn nhận sau | |
| `GT25` | C4 `G1` – hộp và phụ kiện | 70% đủ / **30% thiếu** → phát sinh phí 5% hoặc 2% `[#19]` `[#21]` | |
| `GT26` | C4 `G3` – kết luận thẩm định | 75% lỗi do nhà sản xuất / **25% do người dùng** (bị từ chối) | |
| `GT27` | C4 `G6` – phương án khách chọn | Đổi máy 30% · Trả hàng 10% · Sửa chữa 60% | Tính trên phần đã qua `G3` |
| `GT28` | C4 `G7` – tồn kho hàng đổi | 70% còn hàng đúng model / 30% đã hết | |
| `GT29` | C4 `G9` – cam kết 15 ngày | 80% đúng hạn / **20% trễ hạn** | |
| `GT30` | C4 `G4` – mốc tháng đầu | 20% còn trong tháng đầu / 80% từ tháng thứ hai | Mốc 30 ngày là số công bố `[#17]`; **tỷ lệ** là ước lượng |
| `GT42` | C3 `G7` – khách chấp nhận điều kiện vay mới | 100% chấp nhận / 0% không chấp nhận | **Ước lượng.** Tách phần vốn nằm ngầm trong `GT22` – xem giải thích ngay dưới bảng |
| `GT43` | C4 `G8` – khách chấp nhận model tương đương khi hết hàng đúng model | 100% chấp nhận model tương đương / 0% chuyển sang hoàn tiền | **Ước lượng.** Tách phần vốn nằm ngầm trong `GT27` và `GT28` – xem giải thích ngay dưới bảng |
| `GT44` | C3 `G16` – ca dừng tại `T2` có đang giữ máy theo IMEI hay không | 40,5% đang giữ máy / 59,5% chưa giữ máy | **Dẫn xuất**, không phải ước lượng mới. Cổng `G16` thêm ngày 08/09/2026 khi chốt `I-08`; phép tính đầy đủ ngay dưới bảng |

**Hai giả định vừa tách, và vì sao cả hai bằng 100 / 0.**

`GT42` và `GT43` không phải số mới. Chúng là tỷ lệ mà Bảng 4.9 và Bảng 4.11 vẫn luôn dùng nhưng chưa viết ra, nay ghi tường minh để mọi nhánh cổng trên hình tra ngược được về đúng một mã.

- `GT42` – C3 `G7`. `GT22` gộp sẵn hai việc vào một con số ở dòng "Duyệt có điều kiện & khách chấp nhận 20%". Bảng 4.9 chỉ có bốn kịch bản, không có kịch bản thứ năm cho ca khách không chấp nhận điều kiện vay mới. Tức bảng cũ đã ngầm đặt tỷ lệ chấp nhận tại `G7` bằng 100%. Ghi ra thành `GT42` = 100 / 0.
- `GT43` – C4 `G8`. Bảng 4.11 tính nhánh đổi máy đủ 22,5% = 75% × 30%, tức toàn bộ phần khách chọn đổi máy, kể cả 30% mà `GT28` báo đã hết hàng đúng model. Nhánh hoàn tiền chỉ nhận đúng 7,5% = 75% × 10%, bằng phần chọn trả hàng của `GT27` và không nhận thêm ca nào từ `G8`. Tức bảng cũ đã ngầm đặt tỷ lệ chấp nhận model tương đương tại `G8` bằng 100%. Ghi ra thành `GT43` = 100 / 0.

Nhánh 0% vẫn giữ trên mô hình: đó là đường đi quy trình cho phép, chỉ là phần định lượng chưa gán ca nào cho nó. Đây là lựa chọn dè dặt về phía có lợi cho doanh nghiệp, cùng hướng với `GT17`–`GT19` ở mục 1.4: giả định khách luôn thuận, để kết luận "quy trình kém hiệu quả" không bị quy là do nhóm chọn số xấu. Có số thật thì chỉ phải sửa hai dòng này, không phải dựng lại bảng nào.

Vì cả hai bằng 100 / 0 nên việc tách không làm đổi một con số kết quả nào của chương: cycle time, CTE và chi phí kỳ vọng giữ nguyên.

**`GT44` được tính ra, không được đặt ra.**

Cổng `G16 Máy đang bị khóa IMEI và giữ trên ERP?` đặt sau `T2`, thêm khi chốt `I-08`. Hai loại ca cùng đi qua `T2`, và chỉ một loại có máy phải giải phóng:

| Ca đi tới `T2` | Cách tính trên 100 ca C3 vào `E1` | Số ca | Có máy đang bị khóa IMEI? |
|---|---|---:|:---:|
| `G1` nhánh "Không đủ điều kiện" | `15%` `GT20` | 15,0 | không – dừng trước cặp AND `G3`–`G4` nên `T5` chưa chạy |
| `G6` nhánh "Từ chối" | `85%` `GT20` × `80%` `GT21` × `15%` `GT22` | 10,2 | có |
| `G7` nhánh "Không chấp nhận" | `GT42` = 0% | 0,0 | có, nhưng chưa gán ca nào |
| **Cộng** | | **25,2** | |

Tỷ lệ tại cổng: `10,2 ÷ 25,2 = 40,5%` đang giữ máy, phần còn lại 59,5% chưa giữ máy.

`GT44` không đi vào bảng nào của mục 2 và mục 4, và đây không phải sơ suất. Mọi bảng định lượng của C3 lấy `GT22` làm mẫu số, tức chỉ đếm nhánh đi qua công ty tài chính; trong mẫu số ấy thì 100% ca dừng ở `T2` đều đang giữ máy, nên bước `T6` nhận trọng số đúng bằng tỷ lệ từ chối 15%. Con số 40,5% chỉ là xác suất tại cổng, dùng để chú lên hình `C3-time`, đúng như phần "Xác suất tại cổng khác xác suất trên toàn quy trình" ngay dưới đây đã nói.

**Xác suất tại cổng khác xác suất trên toàn quy trình.**

Số chú lên nhánh của hai hình `C3-time` và `C4-time` là xác suất của chính cổng đó, tính trên số ca đi tới cổng, nên tổng các nhánh ra của một cổng luôn bằng 100%. Đó không phải xác suất trên toàn quy trình. Bảng ghép bốn nhánh kết cục ngay dưới cho thấy khoảng cách: nhánh sửa chữa là 60% tại cổng `G6` nhưng 45,0% trên toàn quy trình.

Riêng `G12` của C3 có vòng làm lại chạy ngược về chính nó, nên số ghi ở cổng này là tỷ lệ của lượt đi qua đầu tiên, không phải tỷ lệ trên tổng số lượt đi qua cổng. Đó cũng đúng bằng tỷ lệ làm lại `r` = 20% mà mục 2.2 dùng trong công thức `15 ÷ (1 − 0,2)`, nên hình và bảng nói cùng một con số.

Hai chỗ phải cộng dồn mới ra được xác suất tại cổng, cả hai đều từ `GT22`:

- C3 `G12` nhánh Đủ chứng từ = 45 + 20 + 15 = 80%, tức ba kịch bản không phải kịch bản bổ sung giấy tờ.
- C3 `G6` nhánh Duyệt = 45 + 20 = 65%, vì kịch bản "bổ sung giấy tờ rồi mới duyệt" chạy lại vòng `G12` → `G13` → `T4` rồi mới tới `G6`, và tới nơi thì nó cũng đi nhánh Duyệt. Ghi 45% lên nhánh này là sai: 45% là tỷ lệ trên toàn nhánh trả góp, không phải tỷ lệ tại `G6`.

Bảng tra ngược cho toàn bộ nhánh có chú số trên hai hình:

| Hình | Cổng | Nhánh | % tại cổng | Lấy từ |
|---|---|---|---:|---|
| `C3-time` | `G1` | Đủ điều kiện | 85% | `GT20` |
| `C3-time` | `G1` | Không đủ điều kiện | 15% | `GT20` |
| `C3-time` | `G2` | Qua công ty tài chính | 80% | `GT21` |
| `C3-time` | `G2` | Qua thẻ tín dụng | 20% | `GT21` |
| `C3-time` | `G12` | Đủ chứng từ | 80% | `GT22`, cộng ba kịch bản |
| `C3-time` | `G12` | Thiếu chứng từ | 20% | `GT22` |
| `C3-time` | `G6` | Duyệt | 65% | `GT22`, cộng hai kịch bản |
| `C3-time` | `G6` | Duyệt có điều kiện | 20% | `GT22` |
| `C3-time` | `G6` | Từ chối | 15% | `GT22` |
| `C3-time` | `G7` | Chấp nhận | 100% | `GT42` |
| `C3-time` | `G7` | Không chấp nhận | 0% | `GT42` |
| `C3-time` | `G9` | Thành công | 97% | `GT23` |
| `C3-time` | `G9` | Không thành công | 3% | `GT23` |
| `C3-time` | `G16` | Đang giữ máy | 40,5% | `GT44` |
| `C3-time` | `G16` | Chưa giữ máy | 59,5% | `GT44` |
| `C4-time` | `G1` | Đủ | 70% | `GT25` |
| `C4-time` | `G1` | Thiếu | 30% | `GT25` |
| `C4-time` | `G3` | Do nhà sản xuất | 75% | `GT26` |
| `C4-time` | `G3` | Do người dùng | 25% | `GT26` |
| `C4-time` | `G4` | Còn trong tháng đầu | 20% | `GT30` |
| `C4-time` | `G4` | Từ tháng thứ hai | 80% | `GT30` |
| `C4-time` | `G6` | Đổi máy mới | 30% | `GT27` |
| `C4-time` | `G6` | Trả hàng | 10% | `GT27` |
| `C4-time` | `G6` | Sửa chữa | 60% | `GT27` |
| `C4-time` | `G7` | Còn hàng | 70% | `GT28` |
| `C4-time` | `G7` | Đã hết | 30% | `GT28` |
| `C4-time` | `G8` | Chấp nhận model tương đương | 100% | `GT43` |
| `C4-time` | `G8` | Chuyển sang hoàn tiền | 0% | `GT43` |
| `C4-time` | `G9` | Đúng hạn | 80% | `GT29` |
| `C4-time` | `G9` | Trễ hạn cam kết | 20% | `GT29` |

Ba chỗ cố ý để trống, không phải bỏ sót:

- C3 `G5` là cổng dựa trên sự kiện, hai nhánh đua nhau xem sự kiện nào nổ trước chứ không phải ai đó cân nhắc rồi chọn. Nhóm không có tỷ lệ quan sát được cho nó nên để trống, không bịa.
- C3 `G3` là cổng AND, không có điều kiện rẽ nên không có xác suất.
- `GT24` (C3 `G10` – nhận máy, 85 / 15) nằm ở hình chi tiết `C3a-time`, đợt này chưa chú lên hình.

Số chỉ chú lên hai hình `-time`. Hình mô hình gốc là bản nộp cho tiêu chí 2 nên giữ sạch; hình `-va` phân loại giá trị, không liên quan tới xác suất; hình `-cost` đã kín số tiền trên từng bước.

Xác suất bốn nhánh kết cục của C4 dùng ở mục 2.5 được ghép từ `GT26` và `GT27`:

| Nhánh | Cách ghép | Xác suất |
|---|---|---:|
| Từ chối (`T4` → `E2`) | `GT26` = 25% | **25,0%** |
| Đổi máy (`T7` → `T8`) | 75% × 30% | **22,5%** |
| Trả hàng, hoàn tiền (`T9`) | 75% × 10% | **7,5%** |
| Sửa chữa (`T10` → `T11`) | 75% × 60% | **45,0%** |
| **Tổng** | | **100%** |

### 1.6 Nhóm F – Chi phí

| Mã GT | Giả định | Giá trị dùng | Căn cứ | Mức tin cậy |
|---|---|---:|---|---|
| `GT31` | Số máy gom trong một chuyến cửa hàng ↔ Trung tâm Bảo hành | 20 máy | ước lượng | ước lượng |
| `GT32` | Thời gian nhân công một chuyến (hai chiều, gồm bốc dỡ) | 2 giờ | ước lượng | ước lượng |
| `GT33` | Nhiên liệu và cầu đường một chuyến | 100.000 đ | ước lượng | ước lượng |
| `GT34` | Giá trị hóa đơn bình quân một máy | 8.000.000 đ | ước lượng – có kiểm chéo ở `GT38` | ước lượng |
| `GT35` | Chi phí vốn tồn kho | 10%/năm | ước lượng | ước lượng |
| `GT36` | Vòng đời sử dụng máy, để quy giá trị sử dụng theo ngày | 24 tháng | ước lượng | ước lượng |

Ba đơn giá dẫn xuất từ nhóm F, không phải giả định mới:

| Đại lượng | Công thức | Giá trị |
|---|---|---:|
| Chi phí phân bổ một lượt vận chuyển cho một máy | `(GT32 × GT07 + GT33) ÷ GT31 = (2 × 60.100 + 100.000) ÷ 20` | **11.010 đ/lượt/máy** |
| Chi phí vốn của một máy nằm chờ, theo ngày | `GT34 × GT35 ÷ 365 = 8.000.000 × 10% ÷ 365` | **2.192 đ/ngày** |
| Giá trị sử dụng một máy, theo ngày (chi phí **khách** chịu) | `GT34 ÷ GT36 ÷ 30 = 8.000.000 ÷ 24 ÷ 30` | **11.111 đ/ngày** |

### 1.7 Nhóm G – Quy mô, dùng cho phần ngoại suy

Khác các nhóm trên, nhóm G có hai đầu vào công bố thật, chỉ hai tỷ lệ cuối là ước lượng.

| Mã GT | Đại lượng | Cách tính | Giá trị | Mức tin cậy |
|---|---|---|---:|---|
| – | Doanh thu chuỗi thegioididong.com + TopZone năm 2025 | – | 37.300 tỷ đồng | **công bố** `[N1]` |
| – | Số cửa hàng thegioididong.com cuối 2025 | – | 1.012 cửa hàng | **công bố** `[N1]` |
| `GT37` | Doanh thu bình quân một cửa hàng một tháng | `37.300 tỷ ÷ 1.012 ÷ 12` | **3,071 tỷ đồng** | dẫn xuất từ hai số công bố |
| `GT38` | Số hóa đơn một cửa hàng một tháng | `GT37 ÷ GT34 = 3.071.475.626 ÷ 8.000.000` | **≈ 384 hóa đơn** ≈ 13 hóa đơn/ngày | dẫn xuất |
| `GT39` | Tỷ lệ giao dịch chọn hình thức trả góp | ước lượng 25% → `384 × 25%` | **96 ca C3/tháng** | ước lượng |
| `GT40` | Tỷ lệ máy bán ra phát sinh yêu cầu bảo hành trong vòng đời | ước lượng 3% → `384 × 3%` | **≈ 12 ca C4/tháng** | ước lượng |

Ba điều phải nói kèm `GT37`, không được bỏ:

1. Doanh thu 37.300 tỷ gồm cả TopZone, nhưng 1.012 là số cửa hàng riêng thegioididong.com. Phép chia vì thế thổi lên doanh thu bình quân mỗi cửa hàng. Đây là sai lệch theo hướng làm chi phí ngoại suy cao hơn thực tế.
2. Năm 2025 chuỗi này giảm khoảng 100 điểm bán so với bình quân năm `[N1]`, nên 1.012 là số cuối kỳ, không phải số bình quân năm.
3. `GT38` cho ra ≈ 13 hóa đơn mỗi cửa hàng mỗi ngày. Con số này là phép kiểm chéo cho `GT34`: nếu ai đó thấy 13 giao dịch mỗi ngày quá thấp hoặc quá cao so với thực tế, thì cái sai nằm ở `GT34`, sửa `GT34` rồi tính lại toàn bộ mục 4.4.

---

## 2. Thời gian

Công thức dùng suốt mục này (`chap05.pdf` trang 44-45):

```
CT  = PT + WT
CTE = PT / CT
```

Ba quy tắc ghép nhánh, lấy đúng cách thầy làm ở ví dụ credit application (`chap05.pdf` trang 49-53) và cách nhóm đã làm ở `bai-tap/2026-08-04/solution.md`:

| Cấu trúc | Quy tắc cho cycle time | Nguồn |
|---|---|---|
| Nhánh AND song song | lấy **max** của các nhánh | `chap05.pdf` trang 50 |
| Nhánh XOR | **trung bình có trọng số** theo xác suất | `chap05.pdf` trang 49 |
| Vòng làm lại tỷ lệ `r` | `T ÷ (1 − r)` | `chap05.pdf` trang 51 |

Điểm cần phân biệt, dùng lại ở mục 4: cycle time lấy `max` của nhánh song song, còn chi phí lấy `tổng`, vì hai việc song song vẫn tiêu tốn công của hai người, dù chỉ chiếm thời gian của việc dài hơn.

### 2.1 Bảng 4.8 – C3, thời gian từng bước

Danh sách bước lấy nguyên `id` và `name` từ `C3-ban-tra-gop.bpmn`, giữ đúng thứ tự và cách phân loại VA/BVA/NVA của Bảng 4.1 ở `dinh-tinh.md`. Dòng đầu tiên là quãng chờ tới lượt tại quầy: nó không phải phần tử trên mô hình (mô hình khởi động ở `E1` khi khách đã tới quầy), nhưng rubric và `04-phan-tich-quy-trinh.md` đều yêu cầu tính, nên để lại và đánh dấu rõ.

Trước khi vào bảng, hai hình dưới đây ghi thời gian xử lý `PT` và thời gian chờ `WT` lên thẳng từng bước của mô hình C3, kèm hộp tổng ở dải trên cùng. Đọc trên hình thấy ngay điều mà cột số trong bảng nói vòng hơn: gần như toàn bộ thời gian chờ của kịch bản duyệt thẳng đọng ở đúng một chỗ, sự kiện `IE1` chờ kết quả thẩm định.

@@FIG:time-C3@@

@@FIG:time-C3a@@

| STT | Mã | Bước | Loại | PT (phút) | WT (phút) | Mã GT / nguồn | Trên kịch bản duyệt thẳng |
|---:|---|---|---|---:|---:|---|:---:|
| 0 | – | *Chờ tới lượt tại quầy (ngoài phạm vi mô hình)* | NVA | 0 | 10 | `GT11` | ✔ |
| 1 | `E1` | Khách đã chọn hình thức thanh toán trả góp | – (mốc) | 0 | 0 | mốc, không tiêu tốn công | ✔ |
| 2 | `T1` | Sàng lọc sơ bộ và trình bày phương án trả góp | VA | 15 | 0 | `GT10-M3` | ✔ |
| 3 | `T2` | Tư vấn phương án thay thế cho khách | BVA | 10 | 0 | `GT10-M2` | – |
| 4 | `E2` | Giao dịch trả góp đã dừng, khách chuyển phương án khác | – (mốc) | 0 | 0 | mốc | – |
| 5 | `T3` | Lập giao dịch trả góp qua thẻ tín dụng | VA | 10 | 0 | `GT10-M2` | – (nhánh thẻ, `GT21`) |
| 6 | `T4` | Lập hồ sơ vay và tải chứng từ lên hệ thống bên cho vay | BVA | 15 | 0 | `GT10-M3` | ✔ (song song với `T5`) |
| 7 | `T5` | Khóa số IMEI và giữ máy trên ERP | BVA | 3 | 0 | `GT10-M1` | ✔ (song song với `T4`) |
| 8 | `IE1` | Kết quả thẩm định đã nhận | **NVA** | 0 | **60** | `GT14` | ✔ |
| 9 | `IE2` | Hết thời hạn giữ máy chờ hồ sơ | **NVA** | 0 | 480 | `GT16` | – |
| 10 | `T6` | Giải phóng máy về tồn bán và hủy đơn | **NVA** | 3 | 0 | `GT10-M1` | – |
| 11 | `E3` | Đơn đã hủy, máy được giải phóng về tồn bán | – (mốc) | 0 | 0 | mốc | – |
| 12 | `T7` | Thương lượng mức trả trước và kỳ hạn mới với khách | VA | 15 | 0 | `GT10-M3` | – |
| 13 | `T8` | Ký hợp đồng vay với công ty tài chính | BVA | 15 | 0 | `GT10-M3` | ✔ |
| 14 | `T9` | Thu khoản trả trước và lập hóa đơn | BVA | 10 | 0 | `GT10-M2` | ✔ |
| 15 | `T10` | Bàn giao máy và hướng dẫn khui hộp kiểm tra | VA | 10 | 0 | `GT10-M2` | ✔ |
| 16 | `T11` | Hẹn lịch giao và giữ máy theo số IMEI | BVA | 3 | 0 | `GT10-M1` | – (`GT24`) |
| 17 | `T12` | Đối chiếu khoản giải ngân của công ty tài chính với hóa đơn | BVA | 3 | 0 | `GT10-M1` | ✔ |
| 18 | `E4` | Hợp đồng đã giải ngân và máy đã bàn giao cho khách | – (mốc) | 0 | 0 | mốc | ✔ |
| | | **Cộng riêng kịch bản duyệt thẳng** | | **PT = 68** | **WT = 70** | `T4 ‖ T5` lấy max(15, 3) = 15 | |

```
Kịch bản duyệt thẳng:
CT  = PT + WT = 68 + 70 = 138 phút = 0,29 ngày
CTE = 68 / 138 = 49,3%
```

### 2.2 Bảng 4.9 – C3, cycle time theo kịch bản có xác suất

Xác suất lấy từ `GT22`, tính trên nhánh đi qua công ty tài chính. Kịch bản "bổ sung giấy tờ" đã có trên mô hình: cổng `G12 Hồ sơ đủ chứng từ theo yêu cầu bên cho vay?` đặt ngay sau `IE1`, nhánh "Thiếu chứng từ" quay ngược về `G13` (cổng XOR hội tụ đặt trước cặp AND `G3`–`G4`), nên hồ sơ chạy lại `T4` rồi chờ thẩm định thêm một vòng. Cách quy vòng lặp thành thời gian vẫn theo `chap05.pdf` trang 51: lặp lại `T4` một vòng, cộng một vòng chờ `IE1`, cộng quãng khách về lấy giấy tờ `GT15`.

| Kịch bản | Xác suất `GT22` | Cách tính PT | PT | Cách tính WT | WT | CT | CTE |
|---|---:|---|---:|---|---:|---:|---:|
| Duyệt thẳng (`G6` = Duyệt) | 45% | `T1 15 + max(T4 15, T5 3) + T8 15 + T9 10 + T10 10 + T12 3` | 68 | `GT11 10 + GT14 60` | 70 | **138** | 49,3% |
| Duyệt có điều kiện, khách chấp nhận (`G6` → `T7` → `G7` Chấp nhận) | 20% | duyệt thẳng `+ T7 15` | 83 | như trên | 70 | **153** | 54,2% |
| Bổ sung giấy tờ rồi mới duyệt (vòng làm lại `G12` → `G13` → `T4`) | 20% | duyệt thẳng `+ T4 làm lại 15` | 83 | `70 + GT15 480 + GT14 60` | 610 | **693** | 12,0% |
| Từ chối (`G6` = Từ chối → `T2` → `G16` → `T6` → `E3`) | 15% | `T1 15 + max(T4, T5) 15 + T2 10 + T6 3` | 43 | `GT11 10 + GT14 60` | 70 | **113** | 38,1% |
| **Trung bình có trọng số** | **100%** | `0,45×68 + 0,20×83 + 0,20×83 + 0,15×43` | **70,3** | `0,45×70 + 0,20×70 + 0,20×610 + 0,15×70` | **178,0** | **248,3 phút = 0,52 ngày** | **28,3%** |

Kiểm chéo bằng công thức vòng làm lại của thầy: với `r` = 20%, thời gian hiệu dụng của `T4` là `15 ÷ (1 − 0,2) = 18,75 phút`, mỗi hồ sơ gánh thêm 3,75 phút công lập hồ sơ chỉ vì vòng bổ sung giấy tờ. Công thức `1 ÷ (1 − r)` giả định vòng lặp không chặn số lượt, nên 18,75 phút là cận trên; với trần 2 lượt mà `A7` khai trên hình thì con số đúng là `15 × (1 + 0,2 + 0,04) = 18,6 phút`. Chênh 0,15 phút, và đây chỉ là phép kiểm chéo – Bảng 4.9 không dùng con số này, nên không dòng nào của bảng đổi.

Waiting time của C3 nằm ở đâu. Tách 178 phút chờ trung bình:

| Chặng chờ | Phút (đã nhân xác suất) | % của WT |
|---|---:|---:|
| Vòng bổ sung giấy tờ – khách về lấy giấy tờ và chờ thẩm định lại (`GT15` + `GT14`, ×20%) | 108,0 | **60,7%** |
| Chờ kết quả thẩm định lần đầu `IE1` (`GT14`, ×100%) | 60,0 | 33,7% |
| Chờ tới lượt tại quầy (`GT11`) | 10,0 | 5,6% |
| **Tổng** | **178,0** | **100%** |

Một kịch bản chiếm 20% số ca sinh ra 60,7% toàn bộ thời gian chờ. Điều này khớp độc lập với Pareto C3 ở `dinh-tinh.md`: chủ đề `TG1` (bộ giấy tờ thay đổi theo công ty tài chính, dễ chuẩn bị thiếu) chiếm 44,4% lượt nhắc và đứng đầu bảng. Hai công cụ khác nhau, hai bộ dữ liệu khác nhau, cùng chỉ vào bước `T4`.

### 2.3 Độ nhạy của C3 theo tỷ lệ bổ sung giấy tờ

`GT22` là ước lượng thuần, nên phải cho biết kết luận đổi thế nào nếu đặt sai. Giữ nguyên 20% duyệt có điều kiện và 15% từ chối, chỉ đổi tỷ lệ bổ sung giấy tờ `r`:

| `r` – thay cho tỷ lệ 20% của `GT22` | CT trung bình | CTE |
|---:|---:|---:|
| 0% | 137,3 phút | 49,0% |
| 10% | 192,8 phút | 35,7% |
| **20% (giá trị dùng)** | **248,3 phút** | **28,3%** |
| 35% | 331,5 phút | 21,9% |

Kết luận không đổi dấu trong toàn dải: vòng bổ sung giấy tờ là biến quyết định của C3. Từ 0% lên 35%, cycle time trung bình tăng 2,4 lần trong khi khối lượng công việc thật gần như không đổi.

### 2.4 Bảng 4.10 – C4, thời gian từng bước

Ba dòng đánh dấu *(pool đối tác)* là công việc thật của Trung tâm Bảo hành. Mô hình vẽ Trung tâm Bảo hành là participant hộp đen, không có task bên trong, nên ba dòng này không mang mã bước, nhưng bỏ chúng ra khỏi PT thì CTE bị kéo xuống thấp một cách giả tạo, nên phải tính.

Hai hình dưới đây chú `PT` và `WT` lên từng bước của mô hình C4. Ba dòng vừa nói được ghi thẳng lên hộp pool Trung tâm Bảo hành – không giấu đi, vì bỏ chúng khỏi hình thì cộng các số trên hình sẽ không ra được hộp tổng; còn quãng vận chuyển máy đã sửa quay về thì ghi trên nhãn của chính luồng thông điệp `MF6`. Đặt hình này cạnh hình của C3 là thấy ngay khoảng cách: cùng một cách đo, C3 hiệu suất chu kỳ gần một nửa, C4 chỉ hơn ba phần trăm.

@@FIG:time-C4@@

@@FIG:time-C4a@@

| STT | Mã | Bước | Loại | PT (phút) | WT (phút) | Mã GT / nguồn | Nhánh sửa chữa |
|---:|---|---|---|---:|---:|---|:---:|
| 0 | – | *Chờ tới lượt tại quầy (ngoài phạm vi mô hình)* | NVA | 0 | 10 | `GT11` | ✔ |
| 1 | `E1` | Khách đã mang máy lỗi và hóa đơn tới cửa hàng | – (mốc) | 0 | 0 | mốc | ✔ |
| 2 | `T1` | Quét IMEI, tra hóa đơn gốc và kiểm tra hộp cùng phụ kiện | BVA | 10 | 0 | `GT10-M2` | ✔ |
| 3 | `T2` | Tính phí thiếu phụ kiện và thiếu hộp vào phiếu tiếp nhận | BVA | 3 | 0 | `GT10-M1`, chỉ 30% ca `GT25` | 30% ca |
| 4 | `T3` | Lập phiếu tiếp nhận và chuyển máy tới Trung tâm Bảo hành | **NVA** | 10 | **480** | PT `GT10-M2`; WT = 1 lượt `GT17` | ✔ |
| 5 | – | *Chờ tới lượt thẩm định tại Trung tâm Bảo hành (pool đối tác)* | **NVA** | 0 | **1.920** | `GT18` = 4 ngày × `GT01` | ✔ |
| 6 | – | *Thẩm định kỹ thuật (pool đối tác)* | BVA | **30** | 0 | `GT12-M4` | ✔ |
| 7 | `IE1` | Kết luận thẩm định đã nhận | **NVA** | 0 | 0 | mốc nhận tin; quãng chờ đã tính ở dòng 5 | ✔ |
| 8 | `T4` | Thông báo từ chối và báo giá sửa chữa có phí | BVA | 10 | 0 | `GT10-M2` | – (nhánh từ chối) |
| 9 | `E2` | Yêu cầu đã bị từ chối, khách đã nhận báo giá sửa chữa có phí | – (mốc) | 0 | 0 | mốc | – |
| 10 | `T5` | Tư vấn phương án đổi mới miễn phí, trả hàng chịu phí hoặc sửa chữa | VA | 15 | 0 | `GT10-M3`, nhánh tháng đầu `GT30` | 20% ca |
| 11 | `T6` | Tư vấn phương án trả hàng chịu phí lũy tiến hoặc sửa chữa | VA | 15 | 0 | `GT10-M3`, nhánh từ tháng hai `GT30` | 80% ca |
| 12 | `T7` | Kiểm tra tồn kho hàng đổi cùng model | BVA | 3 | 0 | `GT10-M1` | – (nhánh đổi máy) |
| 13 | `T8` | Xuất máy đổi và bàn giao cho khách | VA | 10 | 0 | `GT10-M2` | – (nhánh đổi máy) |
| 14 | `T9` | Tính số tiền hoàn sau khi trừ phí và chi trả về phương thức gốc | VA | 10 | 0 | `GT10-M2` | – (nhánh hoàn tiền) |
| 15 | `T10` | Chuyển máy đi sửa và theo dõi cam kết 15 ngày | **NVA** | 3 | **2.880** | PT `GT10-M1`; WT `GT19` = 6 ngày × `GT01` | ✔ |
| 16 | – | *Sửa chữa tại Trung tâm Bảo hành (pool đối tác)* | VA | **90** | 0 | `GT13-M5` | ✔ |
| 17 | – | *Vận chuyển máy đã sửa về cửa hàng (message flow `MF6`)* | **NVA** | 0 | **480** | 1 lượt `GT17` | ✔ |
| 18 | `T11` | Bàn giao máy đã sửa kèm phiếu bảo hành | VA | 10 | 0 | `GT10-M2` | ✔ |
| 19 | `T12` | Thông báo kết quả xử lý cho khách | BVA | 10 | 0 | `GT10-M2`, song song `T13` | ✔ |
| 20 | `T13` | Cập nhật nghiệp vụ nhập đổi hoặc nhập trả trên ERP | BVA | 3 | 0 | `GT10-M1`, song song `T12` | ✔ |
| 21 | `T14` | Nhập máy lỗi thu hồi và gom chuyển trả hãng theo kỳ | BVA | 10 | 0 | `GT10-M2` | ✔ |
| 22 | `E3` | Yêu cầu đã xử lý xong và máy lỗi đã được thu hồi | – (mốc) | 0 | 0 | mốc | ✔ |
| | | **Cộng riêng nhánh sửa chữa, đúng hạn** | | **PT = 188,9** | **WT = 5.770** | `T12 ‖ T13` lấy max(10, 3) = 10; `T2` tính theo 30% ca | |

```
Nhánh sửa chữa, đúng hạn:
CT  = 188,9 + 5.770 = 5.958,9 phút = 12,41 ngày
CTE = 188,9 / 5.958,9 = 3,17%
```

Giữ nguyên con số 3,17%. Trong hơn 12 ngày một ca bảo hành trôi qua, chỉ hơn ba giờ là có người thật sự làm việc trên máy. Và 12,41 ngày vẫn nằm trong cam kết 15 ngày `[#18]`, nghĩa là quy trình có thể đạt cam kết công bố mà vẫn lãng phí gần 97% thời gian.

### 2.5 Bảng 4.11 – C4, cycle time theo nhánh kết cục

Xác suất ghép từ `GT26` và `GT27` (mục 1.5). Mọi nhánh đều đã cộng sẵn `T2` theo tỷ lệ 30% của `GT25`, nên PT có phần thập phân.

| Nhánh kết cục | Xác suất | Cách tính PT | PT | Cách tính WT | WT | CT | CT (ngày) | CTE |
|---|---:|---|---:|---|---:|---:|---:|---:|
| Từ chối (`G3` = do người dùng) | 25,0% | `T1 10 + 0,3×T2 + T3 10 + thẩm định 30 + T4 10` | 60,9 | `GT11 10 + GT17 480 + GT18 1.920` | 2.410 | 2.470,9 | 5,15 | 2,46% |
| Đổi máy mới | 22,5% | `T1 + 0,3×T2 + T3 + thẩm định + tư vấn 15 + T7 3 + T8 10 + max(T12, T13) 10 + T14 10` | 98,9 | như trên | 2.410 | 2.508,9 | 5,23 | 3,94% |
| Trả hàng, hoàn tiền | 7,5% | `… + T9 10 + max(T12, T13) 10 + T14 10` | 95,9 | như trên | 2.410 | 2.505,9 | 5,22 | 3,83% |
| Sửa chữa, đúng hạn | 45,0% | `… + T10 3 + sửa chữa 90 + T11 10 + max(T12, T13) 10 + T14 10` | 188,9 | `2.410 + GT19 2.880 + GT17 480` | 5.770 | 5.958,9 | 12,41 | 3,17% |
| **Trung bình có trọng số** | **100%** | | **129,7** | | **3.922,0** | **4.051,7** | **8,44** | **3,20%** |

Waiting time của C4 nằm ở đâu. Tách 3.922 phút chờ trung bình:

| Chặng chờ | Phút (đã nhân xác suất) | % của WT |
|---|---:|---:|
| Chờ tới lượt thẩm định tại Trung tâm Bảo hành (`GT18`, 100% ca) | 1.920 | **49,0%** |
| Chờ linh kiện và xếp hàng sửa chữa (`GT19`, 45% ca) | 1.296 | **33,0%** |
| Vận chuyển hai chiều (`GT17`, bình quân 1,45 lượt/ca trong quãng khách phải chờ – xem ghi chú ngay dưới) | 696 | 17,7% |
| Chờ tới lượt tại quầy (`GT11`) | 10 | 0,3% |
| **Tổng** | **3.922** | **100%** |

Vì sao dòng vận chuyển ở đây đếm 1,45 lượt còn Bảng 4.13 đếm 2,00. Bảng chi phí đếm mọi lượt máy được chở, vì đơn giá `11.010 đ` phân bổ theo đầu máy mỗi lượt nên lượt nào cũng tốn tiền. Bảng thời gian chỉ đếm lượt mà ca của khách phải chờ, và hai chặng chênh nhau đều nằm ngoài quãng chờ ấy. Chặng thứ nhất là chiều về của máy lỗi qua `MF9`: `T14` gom máy lỗi theo kỳ chứ không theo ca (`dinh-tinh.md` Bảng 4.5, nhánh Method), và lúc đó khách đã nhận máy đổi ở `T8` hoặc nhận tiền hoàn ở `T9` rồi. Chặng thứ hai là chiều về của ca bị từ chối qua `MF10`: nó chạy sau mốc `E2`, tức sau khi khách đã nhận thông báo từ chối và báo giá sửa chữa – mốc kết thúc quy trình. Nếu vẫn muốn cộng riêng `MF9` thì `WT` trung bình lên 4.066 phút, cycle time 8,74 ngày và CTE 3,09%; `I-11` ở mục 5 ghi lại lựa chọn này để người chấm thấy nó là quyết định có chủ đích, không phải chỗ bỏ sót.

Hai chặng xếp hàng chờ tới lượt (không phải bản thân việc thẩm định, không phải bản thân việc sửa) chiếm 82,0% toàn bộ thời gian chờ. Vận chuyển, thứ trực quan nhất và hay bị đổ lỗi nhất, chỉ chiếm 17,7%.

Đây là chỗ kết quả định lượng sửa lại trực giác của phần định tính. Bảng 4.4 xếp `Move, Unnecessary transportation` lên dòng đầu tiên, và Pareto C4 xếp `BH1` (máy đi qua nhiều tầng) ở vị trí số một. Bảng trên cho thấy nếu bỏ hẳn được vận chuyển mà vẫn giữ nguyên hàng đợi thì cycle time chỉ giảm 17,7%; còn nếu giữ nguyên vận chuyển mà xóa được hàng đợi thì giảm 82,0%. Nút thắt là hàng đợi, không phải quãng đường.

### 2.6 Độ nhạy của C4

| Đổi `GT18` (chờ thẩm định) | CT trung bình | CTE | | Đổi `GT19` (chờ sửa chữa) | CT trung bình | CTE |
|---:|---:|---:|---|---:|---:|---:|
| 1 ngày | 5,44 ngày | 4,97% | | 2 ngày | 6,64 ngày | 4,07% |
| 2 ngày | 6,44 ngày | 4,19% | | 4 ngày | 7,54 ngày | 3,58% |
| **4 ngày (giá trị dùng)** | **8,44 ngày** | **3,20%** | | **6 ngày (giá trị dùng)** | **8,44 ngày** | **3,20%** |
| 6 ngày | 10,44 ngày | 2,59% | | 9 ngày | 9,79 ngày | 2,76% |
| 8 ngày | 12,44 ngày | 2,17% | | | | |

Ngay ở giả định lạc quan nhất của cả dải (chờ thẩm định rút còn 1 ngày) CTE cũng chỉ lên 4,97%. Kết luận "phần lớn thời gian là chờ" không phụ thuộc vào việc nhóm đặt `GT18` bằng bao nhiêu.

### 2.7 Nếu tính theo ngày lịch thay vì ngày làm việc

Máy nằm tại Trung tâm Bảo hành thì nằm cả ngoài giờ hành chính, còn cam kết "15 ngày" ở `[#18]` gần như chắc chắn là ngày lịch. Tính lại nhánh sửa chữa với 1 ngày = 1.440 phút:

| Cách quy đổi | CT nhánh sửa chữa | CTE |
|---|---:|---:|
| 1 ngày = 8 giờ (`GT01`, dùng chính thức) | 5.958,9 phút | **3,17%** |
| 1 ngày = 24 giờ (ngày lịch) | 17.479 phút | **1,08%** |

Nhóm giữ cách 8 giờ làm con số chính vì đó là cách thầy quy đổi ở `chap05.pdf` trang 53, và vì nó cho kết quả có lợi hơn cho doanh nghiệp. Cách 24 giờ ghi lại ở đây để không ai nghĩ 3,17% là con số bi quan nhất, nó là con số dè dặt nhất.

### 2.8 So sánh hai quy trình

Mọi con số trong bảng lấy từ dòng Trung bình có trọng số của Bảng 4.9 (C3) và Bảng 4.11 (C4); không có giả định mới.

| | C3 | C4 |
|---|---:|---:|
| PT trung bình | 70,3 phút | 129,7 phút |
| WT trung bình | 178,0 phút | 3.922,0 phút |
| CT trung bình | 248,3 phút = 0,52 ngày | 4.051,7 phút = 8,44 ngày |
| **CTE** | **28,3%** | **3,20%** |
| Chặng chờ lớn nhất | Vòng bổ sung giấy tờ – 60,7% WT | Chờ tới lượt thẩm định – 49,0% WT |
| Bản chất cái chờ | Chờ **thông tin**: giấy tờ và kết quả thẩm định | Chờ **hàng đợi vật lý**: máy nằm xếp lượt |

Hai quy trình có tỷ lệ bước NVA gần bằng nhau khi đếm theo bước (27,8% trên 36 bước và 27,5% trên 40 bước ở `dinh-tinh.md`), nhưng CTE chênh gần chín lần. Đây là bằng chứng số cho cảnh báo đã đặt ở `dinh-tinh.md` mục 1.1: đếm bước không thay được đo thời gian. Mười một bước NVA của C4 ngắn trên hình vẽ nhưng nuốt 96,8% cycle time.

---

## 3. Chất lượng

Tám chỉ số, vượt mức tối thiểu năm chỉ số mà rubric yêu cầu. Ô nào mang mã `GT` là ước lượng; ô nào không tính được thì ghi thẳng, không suy diễn.

| # | Chỉ số | Quy trình | Công thức | Giá trị | Mã GT / nguồn | Khắc phục |
|---:|---|---|---|---:|---|---|
| 1 | Tỷ lệ xử lý xong ngay lần tiếp xúc đầu | C4 | số ca kết thúc ngay tại quầy ÷ tổng ca tiếp nhận | **0%** | **Đọc thẳng từ mô hình** – mọi đường đi từ `E1` đều bắt buộc qua `T3` "chuyển máy tới Trung tâm Bảo hành"; không có nhánh nào kết thúc tại cửa hàng | Phân quyền kết luận tại cửa hàng cho một **danh mục lỗi hiển nhiên đã chuẩn hóa** (màn hình vỡ do sản xuất, không lên nguồn, lỗi phần mềm) – thêm một gateway ngay sau `T1` |
| 2 | Tỷ lệ xử lý xong ngay lần tiếp xúc đầu | C3 | số ca duyệt thẳng ÷ tổng hồ sơ qua công ty tài chính | **45%** | `GT22` | Checklist giấy tờ theo từng công ty tài chính, kiểm ngay tại `T1` trước khi lập hồ sơ |
| 2b | – cùng chỉ số, tính trên **toàn bộ** giao dịch trả góp | C3 | `20% (thẻ tín dụng) + 80% × 45%` | **56%** | `GT21` + `GT22` | như trên |
| 3 | Tỷ lệ hồ sơ phải làm lại | C3 | số hồ sơ phải bổ sung giấy tờ ÷ tổng hồ sơ nộp | **20%** | `GT22`. Chủ đề `TG1` đứng đầu Pareto C3 (44,4% lượt nhắc) xác nhận đây là trở ngại số một, nhưng **không** dùng để suy ra con số 20% | Cho khách tải trước chứng từ qua app; chạy kiểm tính đầy đủ tự động trước khi đẩy hồ sơ sang bên cho vay |
| 4 | Tỷ lệ yêu cầu bị từ chối | C4 | số ca `G3` = "do người dùng" ÷ tổng ca tiếp nhận | **25%** | `GT26`. Chủ đề `BH2` đồng hạng nhất Pareto C4 (5 nguồn) | Đưa danh sách trường hợp loại trừ lên bước `T1`; chụp ảnh hiện trạng máy làm căn cứ; nói rõ với khách khả năng bị từ chối **trước** khi gửi máy đi |
| 5 | Tỷ lệ yêu cầu bị từ chối | C3 | số hồ sơ `G6` = "Từ chối" ÷ tổng hồ sơ nộp | **15%** | `GT22` | Sàng lọc sơ bộ ở `T1` theo đúng tiêu chí của từng bên cho vay |
| 6 | Tỷ lệ trễ so với cam kết 15 ngày | C4 | số ca quá 15 ngày ÷ tổng ca đi nhánh sửa chữa | **20%** | `GT29`. Cam kết 15 ngày là số **công bố** `[#18]`; **tỷ lệ trễ là ước lượng**. Nguồn người dùng tự thuật "gần 20 ngày" và "phải mất 1 tháng" `[#3]` `[#4]` cho thấy hiện tượng có thật nhưng không cho tần suất | Xếp hàng đợi tại Trung tâm Bảo hành theo **hạn cam kết còn lại**, không theo vào trước ra trước; mở trang tra cứu trạng thái ca cho khách tự xem |
| 7 | Tỷ lệ ca bị tính phí thiếu phụ kiện hoặc thiếu hộp | C4 | số ca qua `T2` ÷ tổng ca tiếp nhận | **30%** | `GT25`. Mức phí là số **công bố**: thiếu phụ kiện tối đa 5%, mất hộp 2% giá trị hóa đơn `[#19]` `[#21]` | Nhắc mang đủ hộp và phụ kiện ngay khi khách đặt lịch; checklist ảnh tại `T1` để khách xác nhận trước khi ký phiếu |
| 8 | Tỷ lệ ca không còn hàng đổi đúng model | C4 | `22,5% × 30%` | **6,75%** | `GT27` + `GT28` | Cho tra tồn kho hàng đổi toàn khu vực ngay tại `T7`, thay vì chỉ tra kho của cửa hàng |

**Bốn chỉ số không tính được, giữ nguyên mục này, không lấp bằng số ước lượng:**

| Chỉ số | Vì sao không tính được | Cách lấy nếu có quyền truy cập |
|---|---|---|
| Tỷ lệ ca C4 **thật sự** đạt cam kết 15 ngày | Cần log ERP mốc nhận máy và mốc gọi khách. `bao-cao-nguon-thu-cap.md` mục 4.3 ghi rõ không có | Trích log ERP 3 tháng, đếm theo chênh lệch hai mốc |
| Tỷ lệ khiếu nại sau khi khép ca | Không nguồn nào cho số; kênh khiếu nại thì có công bố `[#22]` | Log tổng đài 1800.1062 và form khiếu nại trên website |
| Tỷ lệ ca phải xử lý lại sau khi đã trả máy (lỗi tái phát) | Mô hình không vẽ nhánh này; nguồn không nhắc tới | Đếm số ca có cùng IMEI mở phiếu tiếp nhận lần hai trong 30 ngày |
| Tỷ lệ hồ sơ C3 bị từ chối rồi nộp lại thành công | Nguồn duy nhất `[#23]` đăng năm 2015, đã lỗi thời | Log hệ thống của bên cho vay |

---

## 4. Chi phí

Phạm vi: chi phí mà cửa hàng và Trung tâm Bảo hành thật sự bỏ ra cho một ca. Không tính giá vốn máy, không tính chi phí mặt bằng và khấu hao, hai khoản đó không thay đổi theo số ca, nên không dùng để so sánh phương án cải tiến.

Quy tắc đã nêu ở đầu mục 2: cycle time lấy `max` của nhánh song song, chi phí lấy `tổng`. Ví dụ rõ nhất là cặp `T4 ‖ T5` của C3, cycle time chỉ ghi 15 phút, nhưng chi phí phải ghi cả 15 phút của nhân viên tư vấn lẫn 3 phút của nhân viên kho.

### 4.1 Bảng 4.12 – Chi phí một ca C3

Thời gian mỗi vai lấy từ lane thật trong `C3-ban-tra-gop.bpmn`, nhân với xác suất `GT22` của bốn kịch bản.

Hai hình dưới ghi tiền công của từng bước lên thẳng mô hình C3: mỗi ô là thời gian xử lý của bước nhân đơn giá của vai đang làm bước ấy. Đọc trên hình thấy ngay điều bảng nói bằng cột: tiền của C3 dồn vào lane nhân viên tư vấn, và dồn vào bốn bước tư vấn – lập hồ sơ – thương lượng – ký hợp đồng, mỗi bước 15 phút. Số trên hình là chi phí thô của một lượt chạy bước, chưa nhân xác suất nhánh, nên cộng hết lại sẽ lớn hơn dòng tổng của bảng; hộp chú giải ở mép trên mỗi hình ghi rõ chênh lệch đó.

@@FIG:cost-C3@@

@@FIG:cost-C3a@@

| Vai (lane trên mô hình) | Bước phụ trách | Phút bình quân/ca | Đơn giá | Mã GT | Thành tiền |
|---|---|---:|---:|---|---:|
| Nhân viên tư vấn trả góp | `T1`, `T2`, `T4`, `T7`, `T8` | 50,25 | 1.041,67 đ/phút | `GT03` | **52.344 đ** |
| Thu ngân | `T3`, `T9`, `T12` | 11,05 | 520,83 đ/phút | `GT04` | **5.755 đ** |
| Kho cửa hàng | `T5`, `T10`, `T11` | 11,50 | 520,83 đ/phút | `GT05` | **5.990 đ** |
| Quản lý cửa hàng | `T6` | 0,45 | 1.041,67 đ/phút | `GT08` | **469 đ** – xem ghi chú 1 |
| | **Cộng nhân công** | **73,25** | | | **64.558 đ** |
| Vận chuyển | không có chặng vận chuyển trong C3 | – | – | – | **0 đ** |
| Chi phí cơ hội máy bị khóa IMEI chờ hồ sơ | `0,614 ngày × 2.192 đ/ngày` | – | – | `GT34` `GT35` | **1.346 đ** |
| | **Tổng chi phí xử lý một ca C3** | | | | **65.904 đ** |

Bốn ghi chú bắt buộc đi kèm bảng:

| # | Nội dung |
|---:|---|
| 1 | **Ô "Quản lý cửa hàng" trước đây bằng 0 vì `T6` không đến lượt chạy – đó là lỗi mô hình, nay đã sửa.** `T6` chỉ có đường vào từ `IE2` và từ `G9`, nên hồ sơ bị `G6` rẽ nhánh "Từ chối" đi thẳng `T2` → `E2` và máy nằm lại trạng thái khóa IMEI mà không bước nào mở ra. Đợt soát logic 08/09/2026 thêm cổng `G16` sau `T2` để nhánh này chạy tiếp `G15` → `T6`, chi tiết ở `I-08` mục 5. Vì vậy `T6` nay gánh `3 phút × 15% GT22 = 0,45 phút/ca`, thành **469 đ/ca** |
| 2 | Chi phí làm lại được tách riêng để thấy quy mô: chênh lệch nhân công giữa kịch bản bổ sung giấy tờ và kịch bản duyệt thẳng là `76.042 − 60.417 = 15.625 đ`, nhân tỷ lệ 20% `GT22` → **3.125 đ/ca**, tức **4,7% tổng chi phí** một ca. Khoản này đã nằm trong 64.558 đ, không cộng thêm |
| 3 | Công bỏ đi ở nhánh từ chối: `46.354 đ × 15% = 6.953 đ/ca` – công đã làm mà không sinh ra giao dịch nào. Cũng đã nằm trong 64.558 đ. Con số 46.354 đ gồm cả `T6` 3 phút dọn dẹp sau khi hồ sơ bị từ chối, bước mà `G16` vừa mở đường cho chạy |
| 4 | Chi phí cơ hội 1.346 đ là **cận dưới**: chỉ tính chi phí vốn `GT35`, chưa tính khoản lãi gộp mất đi khi máy bị khóa không bán được cho khách khác. Không có số liệu biên lợi nhuận theo model máy nên không tính tiếp – ghi "chưa đủ dữ kiện" |

### 4.2 Bảng 4.13 – Chi phí một ca C4

Xác suất bốn nhánh lấy ở mục 1.5. Số lượt vận chuyển bình quân, đếm lại trên mô hình đã có hai message flow chiều về `MF9` và `MF10`:

| Nhánh kết cục | Xác suất | Lượt đi | Lượt về | Luồng mang máy về | Lượt/ca |
|---|---:|---:|---:|---|---:|
| Từ chối (`G3` = do người dùng) | 25,0% | 1 | 1 | `MF10` Máy trả về cửa hàng cho khách → `T4` | 2 |
| Đổi máy mới | 22,5% | 1 | 1 | `MF9` Máy lỗi trả về cửa hàng → `T14` | 2 |
| Trả hàng, hoàn tiền | 7,5% | 1 | 1 | `MF9` → `T14` | 2 |
| Sửa chữa | 45,0% | 1 | 1 | `MF6` máy đã sửa (đúng hạn) hoặc `MF9` máy lỗi (trễ hạn) | 2 |
| **Bình quân** | **100%** | | | | **2,00** |

`0,25×2 + 0,225×2 + 0,075×2 + 0,45×2 = 2,00 lượt/ca`, gọn hơn là `1 + 1`: ca nào cũng đi lên một lượt và ca nào cũng có một lượt về. Hai con số cũ đều là ảnh chụp của mô hình ở hai thời điểm trước đó: 1,45 lượt/ca đếm khi chưa có `MF9`, tức chỉ nhánh sửa chữa mới có chiều về; 1,75 lượt/ca đếm khi đã có `MF9` nhưng nhánh "Từ chối" vẫn chưa có đường trả máy. `I-11` ở mục 5 ghi lại đầy đủ ba lần đếm.

Hai hình dưới đọc theo đúng cách vừa nêu ở C3. Chỗ khác biệt nằm ở pool Trung tâm Bảo hành: nó là hộp đen nên bên trong không có bước nào để chú, tiền công kỹ thuật viên vì thế ghi thẳng trên pool. Đặt hai hình cạnh nhau là thấy ngay kết luận của cả mục: khối tiền lớn nhất của C4 nằm ngoài cửa hàng.

@@FIG:cost-C4@@

@@FIG:cost-C4a@@

| Vai | Bước phụ trách | Phút bình quân/ca | Đơn giá | Mã GT | Thành tiền |
|---|---|---:|---:|---|---:|
| Nhân viên tiếp nhận (lane cửa hàng) | `T1`–`T6`, `T10`–`T13` | 50,25 | 1.001,67 đ/phút | `GT06` | **50.334 đ** |
| Kho hàng đổi | `T7`, `T8`, `T14` | 10,43 | 520,83 đ/phút | `GT05` | **5.430 đ** |
| Kế toán hoàn tiền | `T9` | 0,75 | 520,83 đ/phút | `GT04` | **391 đ** |
| Kỹ thuật viên Trung tâm Bảo hành | thẩm định 30′ + sửa chữa 90′ | 70,50 | 1.001,67 đ/phút | `GT09` | **70.618 đ** |
| | **Cộng nhân công** | **131,93** | | | **126.772 đ** |
| Vận chuyển hai chiều cửa hàng ↔ Trung tâm Bảo hành | `2,00 lượt × 11.010 đ` | – | – | `GT31` `GT32` `GT33` `GT07` | **22.020 đ** |
| Chi phí cơ hội máy nằm chờ **của doanh nghiệp** | – | – | – | – | **0 đ** – máy đang sửa là **tài sản của khách**, không phải tồn kho của cửa hàng |
| | **Tổng chi phí doanh nghiệp bỏ ra cho một ca C4** | | | | **148.792 đ** |

**Bốn dòng ghi nhớ, đặt ngoài tổng vì không phải chi phí của doanh nghiệp hoặc chưa đủ dữ kiện:**

| Khoản | Cách tính | Giá trị | Vì sao để ngoài tổng |
|---|---|---:|---|
| Chi phí **khách hàng** chịu vì máy nằm chờ | `8,44 ngày × 11.111 đ/ngày` (`GT34` `GT36`) | **93.789 đ/ca**; riêng nhánh sửa chữa `12,41 × 11.111` = **137.938 đ** | Không phải chi phí của MWG, nhưng có thật, và doanh nghiệp đã ngầm thừa nhận: chính sách công bố có dịch vụ **cho mượn máy tạm** trong thời gian bảo hành `[#20]`. Con số này chính là giá trị mà dịch vụ cho mượn máy đang bù đắp |
| Công bỏ đi ở nhánh từ chối | `(61.002 đ nhân công + 22.020 đ vận chuyển hai chiều) × 25%` | **20.756 đ/ca** = **13,9%** tổng chi phí | Đã nằm trong 148.792 đ; tách ra để lấp cột "Quy mô ước tính" mà `dinh-tinh.md` Bảng 4.4 đang để trống cho lãng phí `Overdo – Defects`. Đây là cột cao nhất của biểu đồ Pareto tiền C4 ở mục 4.6, mã `I-03` |
| Chi phí chuyến gom máy lỗi trả về hãng (`T14` → `MF8`) | – | **chưa đủ dữ kiện** | Gom theo kỳ, không rõ chu kỳ và số máy mỗi lô; nguồn thứ cấp không mô tả (`bao-cao-nguon-thu-cap.md` mục 4.2) |
| Chi phí phát sinh khi trễ cam kết 15 ngày | – | **chưa đủ dữ kiện** | Không rõ doanh nghiệp bồi thường hay chỉ cho mượn máy; `[#20]` không nêu điều kiện áp dụng |

Điểm đáng chú ý nhất của bảng: kỹ thuật viên Trung tâm Bảo hành chiếm 70.618 đ trên 126.772 đ nhân công, tức 55,7% chi phí nhân công của một ca C4 nằm ngoài cửa hàng. Mọi phương án cải tiến chỉ động vào thao tác tại quầy đều chạm được chưa tới một nửa chi phí.

### 4.3 So sánh hai quy trình

Mọi con số trong bảng lấy từ dòng tổng của Bảng 4.12 (C3) và Bảng 4.13 (C4); không có giả định mới.

| | C3 | C4 |
|---|---:|---:|
| Nhân công | 64.558 đ | 126.772 đ |
| Vận chuyển | 0 đ | 22.020 đ |
| Cơ hội (doanh nghiệp chịu) | 1.346 đ | 0 đ |
| **Tổng một ca** | **65.904 đ** | **148.792 đ** |
| Cơ hội (khách chịu, để ngoài tổng) | không đáng kể | 93.789 đ |

Một ca C4 tốn gấp 2,26 lần một ca C3, dù C3 có nhiều bước hơn trên hình vẽ. Nguyên nhân: C4 tiêu tốn 120 phút công của kỹ thuật viên đơn giá cao và 2,00 lượt vận chuyển, hai khoản C3 hoàn toàn không có.

### 4.4 Ngoại suy theo quy mô

> Đây là ngoại suy có giả định, không phải số thật của doanh nghiệp. Toàn bộ mục này đứng trên `GT39` và `GT40`, hai tỷ lệ nhóm tự đặt, không có nguồn. Chỉ hai đầu vào là số công bố: doanh thu 37.300 tỷ và 1.012 cửa hàng `[N1]`. Không được trích một dòng nào của mục này ra khỏi ngữ cảnh này.

**Bước 1, số ca mỗi tháng của một cửa hàng.**

| Bước tính | Công thức | Kết quả |
|---|---|---:|
| Doanh thu bình quân một cửa hàng một tháng | `37.300 tỷ ÷ 1.012 ÷ 12` `GT37` | 3,071 tỷ đồng |
| Số hóa đơn một tháng | `3.071.475.626 ÷ 8.000.000` `GT38` | ≈ 384 hóa đơn (≈ 13/ngày) |
| Số ca C3 | `384 × 25%` `GT39` | **96 ca/tháng** |
| Số ca C4 | `384 × 3%` `GT40` | **≈ 12 ca/tháng** |

Bước 2, chi phí theo quy mô. Cột "Một ca" lấy từ Bảng 4.12 và Bảng 4.13; các dòng dưới là phép nhân với số ca của Bước 1 và với 1.012 cửa hàng `[N1]`.

| Cấp độ | C3 | C4 | Cộng |
|---|---:|---:|---:|
| Một ca | 65.904 đ | 148.792 đ | – |
| Một cửa hàng mỗi tháng | `65.904 × 96` = 6.326.784 đ | `148.792 × 12` = 1.785.504 đ | **8.112.288 đ** |
| Một cửa hàng mỗi năm | `× 12` = 75.921.408 đ | `× 12` = 21.426.048 đ | **97.347.456 đ** |
| **Toàn chuỗi 1.012 cửa hàng mỗi năm** | `× 1.012` = **≈ 76,8 tỷ đồng** | `× 1.012` = **≈ 21,7 tỷ đồng** | **≈ 98,5 tỷ đồng** |

Bước 3, riêng phần lãng phí. Đây mới là con số dùng để thuyết phục, vì nó là phần cắt được chứ không phải toàn bộ chi phí vận hành. Hai khoản lớn nhất:

| Khoản lãng phí | Một ca | Toàn chuỗi một năm | Nguồn của con số |
|---|---:|---:|---|
| Công làm lại vì hồ sơ C3 thiếu giấy tờ (`I-04`) | 3.125 đ | **≈ 3,6 tỷ đồng** | mục 4.1 ghi chú 2 |
| Công bỏ đi vì ca C4 bị từ chối sau khi đã vận chuyển và chờ (`I-03`) | 20.756 đ | **≈ 3,0 tỷ đồng** | mục 4.2 dòng ghi nhớ 2 |
| **Cộng hai khoản** | | **≈ 6,7 tỷ đồng mỗi năm** | |

Cách nhân của cột cuối: `chi phí một ca × số ca mỗi tháng (Bước 1) × 12 tháng × 1.012 cửa hàng [N1]`.

Hai dòng trên chưa phải toàn bộ. Phần dưới đây xếp đủ sáu khoản lãng phí quy được ra tiền của cả hai quy trình lên hai biểu đồ Pareto và chạy cùng bậc thang quy mô này, ra ≈ 16,2 tỷ đồng mỗi năm toàn chuỗi. Bảng trên giữ nguyên hai dòng vì đó là hai khoản đứng đầu mỗi quy trình; bảng đầy đủ đọc ở mục 4.6.

Đặt cạnh doanh thu 37.300 tỷ `[N1]`: toàn bộ chi phí xử lý hai quy trình này chỉ chiếm 0,26% doanh thu chuỗi. Con số nhỏ, và phải nói thẳng điều đó thay vì giấu đi, lý do cải tiến hai quy trình này không phải để tiết kiệm 16,2 tỷ. Lý do là 8,44 ngày cycle time và 93.789 đ chi phí mỗi ca đổ lên đầu khách hàng, thứ không xuất hiện trong báo cáo tài chính nhưng xuất hiện dày đặc trên diễn đàn: chủ đề `BH3` (thời gian chờ thực tế dài hơn thời gian nhân viên hẹn) có 4 nguồn công khai nhắc tới.

### 4.5 Ước lượng lợi ích của phương án cải tiến chính

Phương án số một rút ra từ mục 2.5 và mục 3 chỉ số 1: phân quyền kết luận tại cửa hàng cho danh mục lỗi hiển nhiên đã chuẩn hóa. Giả định thêm, cũng là ước lượng, ghi thành `GT41`:

| Mã GT | Giả định | Giá trị | Mức tin cậy |
|---|---|---:|---|
| `GT41` | Tỷ lệ ca C4 kết luận được ngay tại cửa hàng nếu có danh mục lỗi hiển nhiên | 40% | ước lượng |

| Chỉ tiêu | Trước | Sau | Thay đổi |
|---|---:|---:|---:|
| Cycle time trung bình C4 | 8,44 ngày | **5,17 ngày** | **−38,7%** |
| CTE | 3,20% | **5,06%** | +1,86 điểm phần trăm |
| Chi phí vận chuyển mỗi ca | 22.020 đ | 13.212 đ | −8.808 đ |
| Tỷ lệ xử lý xong ngay lần tiếp xúc đầu | 0% | 40% | +40 điểm phần trăm |

Cột "Trước" lấy từ Bảng 4.11, Bảng 4.13 và mục 3 chỉ số 1. Cột "Sau" tính lại cùng công thức của mục 2.5, chỉ thay `GT41` = 40% số ca bỏ được `T3`, quãng vận chuyển `GT17` và quãng chờ thẩm định `GT18`.

Ngay cả khi cắt được 40% số ca khỏi vòng vận chuyển và thẩm định, CTE vẫn chỉ 5,06%. Nói cách khác: cải tiến này giải quyết được thời gian chờ cho gần một nửa số ca, nhưng không biến C4 thành một quy trình hiệu quả. Muốn vậy phải động vào hàng đợi tại Trung tâm Bảo hành, tức phải làm việc với chính sách xếp hàng của đối tác chứ không chỉ với quy trình của cửa hàng.

### 4.6 Bảng nguồn của hai biểu đồ Pareto theo chi phí

Mục này là bảng số nằm dưới hai hình `pareto-tien-C3` và `pareto-tien-C4` mà `dinh-tinh.md` mục 3.2 và 3.3 dùng. Nó tồn tại để trả lời đúng một câu: những con số trên cột của biểu đồ ở đâu ra.

Dạng chuẩn của biểu đồ Pareto trong `chap05.pdf` trang 36 là *"biểu đồ cột trong đó chiều cao của cột biểu thị tác động của từng vấn đề; các cột được sắp xếp theo sự tác động"*, và ví dụ BuildIT ở trang 37 đo tác động ấy bằng tiền: ba cột 60.000 – 15.000 – 2.400 USD lấy nguyên từ cột *Quantitative Impact* của Issue Register ở trang 35. Hai bảng dưới đây làm đúng chuỗi ấy: mỗi cột của biểu đồ là một vấn đề `I-nn` trong Issue Register ở mục 5, chiều cao là số tiền lãng phí một ca, và cột "Cách tính" viết ra trọn phép nhân dẫn tới con số đó.

Đây là ước lượng, không phải số liệu kế toán. Nhóm không có quyền truy cập cơ sở dữ liệu vận hành, nên không có một dòng nào là số đo. Cách làm là cách mục 0.2 đã ràng buộc: mỗi thừa số hoặc là số công bố có mã `[#n]` / `[Nn]`, hoặc là giả định có mã `GTnn` khai ở mục 1, và ô kết quả luôn viết ra phép nhân. Đọc ngược một mã `GT` là biết ngay con số cuối phụ thuộc vào cái gì.

#### 4.6.1 Bảng 4.14 – Nguồn của hai biểu đồ Pareto theo chi phí

| Mã | Tên ngắn | Quy trình | Cách tính ra tiền | Đồng/ca | % | % lũy kế |
|---|---|:---:|---|---:|---:|---:|
| `I-15` | Công bỏ đi ở hồ sơ trả góp bị từ chối | C3 | `(T1 15′ + T4 15′ + T2 10′ + T6 3′) × 1.041,67 đ/phút GT03 GT08 + T5 3′ × 520,83 đ/phút GT05 = 46.354 đ`, nhân tỷ lệ từ chối `15% GT22` | **6.953** | 67,2% | 67,2% |
| `I-04` | Công làm lại vì hồ sơ thiếu giấy tờ | C3 | Chênh nhân công giữa kịch bản bổ sung giấy tờ và kịch bản duyệt thẳng `76.042 − 60.417 = 15.625 đ` (chính là `T4 15′ × 1.041,67 GT03` chạy lại một vòng), nhân tỷ lệ bổ sung `20% GT22` | **3.125** | 30,2% | 97,4% |
| `I-13` | Vốn nằm chờ cuộc gọi xác nhận thủ công | C3 | Quãng chờ `GT14 60′ ÷ 480′ GT01 = 0,125 ngày`, nhân chi phí vốn một máy `GT34 8.000.000 × GT35 10% ÷ 365 = 2.192 đ/ngày` | **274** | 2,6% | 100,0% |
| | **Cộng C3** | | | **10.352** | **100%** | |
| `I-03` | Công và vận chuyển bỏ đi ở ca bị từ chối | C4 | `(T1 10′ + 0,3×T2 3′ + T3 10′ + thẩm định 30′ + T4 10′) = 60,9′ × 1.001,67 đ/phút GT06 GT09 = 61.002 đ`, cộng 2 lượt vận chuyển `2 × 11.010 = 22.020 đ GT31 GT32 GT33 GT07`, nhân tỷ lệ từ chối `25% GT26` | **20.756** | 73,4% | 73,4% |
| `I-02` | Vận chuyển thừa của ca lẽ ra xong tại cửa hàng | C4 | Ca **không** bị từ chối `75% GT26` × tỷ lệ kết luận được ngay tại cửa hàng `40% GT41` × 2 lượt × `11.010 đ` | **6.606** | 23,4% | 96,8% |
| `I-10` | Công tính phí thiếu hộp và thiếu phụ kiện | C4 | `T2 3′ GT10-M1 × 1.001,67 đ/phút GT06`, nhân tỷ lệ ca thiếu hộp hoặc thiếu phụ kiện `30% GT25` | **902** | 3,2% | 100,0% |
| | **Cộng C4** | | | **28.264** | **100%** | |

Hai hình `pareto-tien-C3` và `pareto-tien-C4` dựng từ đúng bảng này không đặt ở đây mà đặt tại phần phân tích các bên liên quan của `dinh-tinh.md`, cạnh hai biểu đồ Pareto đếm nguồn, để người đọc so hai cách đo tác động ngay trong một mạch. Bảng này là bảng số nằm dưới chúng.

Bốn điều phải đọc kèm bảng, không được bỏ:

1. Cột % lũy kế tính riêng trong từng quy trình. Hai biểu đồ là hai bộ vấn đề khác nhau, không cộng chung được: một ca C3 và một ca C4 không phải cùng một đơn vị, và số ca mỗi tháng của hai quy trình cũng khác nhau (96 với 12, mục 4.4 Bước 1).
2. Sáu khoản không chồng lấn nhau. `I-15` là công đổ vào hồ sơ bị từ chối, `I-04` là công làm thêm của vòng bổ sung, `I-13` là chi phí vốn của quãng chờ – ba khoản khác bản chất. Bên C4, `I-03` tính trên 25% ca bị từ chối còn `I-02` tính trên 75% ca không bị từ chối, hai tập rời nhau theo đúng cách chia của cổng `G3`. Phép kiểm: khoản vận chuyển tiết kiệm được của phương án cải tiến chính là `40% × 2,00 lượt × 11.010 = 8.808 đ/ca`, tách ra đúng bằng `6.606 đ` của `I-02` cộng `2.202 đ` phần vận chuyển của ca bị từ chối đã nằm sẵn trong `I-03`.
3. Cả sáu khoản đều đã nằm trong tổng chi phí một ca của Bảng 4.12 và Bảng 4.13, không cộng thêm. Bảng này bóc tách, không phát sinh chi phí mới. Cụ thể: `I-15` và `I-04` nằm trong 64.558 đ nhân công của C3, `I-13` nằm trong 1.346 đ chi phí cơ hội của C3, `I-03` và `I-10` nằm trong 126.772 đ nhân công cùng 22.020 đ vận chuyển của C4, `I-02` nằm trong 22.020 đ vận chuyển ấy.
4. `I-10` không phải đề nghị bỏ bước `T2`. `dinh-tinh.md` Bảng 4.2 xếp `T2` là BVA vì bước này bảo vệ doanh nghiệp trước tranh chấp phụ kiện. Khoản 902 đ là phần cắt được bằng cách báo trước cho khách mang đủ hộp để bước ấy không phải chạy, chứ không phải bằng cách bỏ bước.

#### 4.6.2 Bảng 4.15 – Bậc thang từ một ca lên toàn chuỗi

Đây là bậc thang mà mục 4.4 đã dựng, chạy lại cho riêng phần lãng phí. Số ca mỗi tháng dùng nguyên `GT39` = 96 ca C3 và `GT40` = 12 ca C4, không đặt số mới; số cửa hàng là 1.012 `[N1]`, số công bố.

| Mã | Quy trình | Một ca | Một cửa hàng một tháng | Một cửa hàng một năm | Toàn chuỗi 1.012 cửa hàng một năm |
|---|:---:|---:|---:|---:|---:|
| `I-15` | C3 | 6.953 đ | 667.488 đ | 8.009.856 đ | **≈ 8,11 tỷ đồng** |
| `I-04` | C3 | 3.125 đ | 300.000 đ | 3.600.000 đ | **≈ 3,64 tỷ đồng** |
| `I-13` | C3 | 274 đ | 26.304 đ | 315.648 đ | **≈ 0,32 tỷ đồng** |
| | **Cộng C3** | **10.352 đ** | **993.792 đ** | **11.925.504 đ** | **≈ 12,07 tỷ đồng** |
| `I-03` | C4 | 20.756 đ | 249.072 đ | 2.988.864 đ | **≈ 3,02 tỷ đồng** |
| `I-02` | C4 | 6.606 đ | 79.272 đ | 951.264 đ | **≈ 0,96 tỷ đồng** |
| `I-10` | C4 | 902 đ | 10.824 đ | 129.888 đ | **≈ 0,13 tỷ đồng** |
| | **Cộng C4** | **28.264 đ** | **339.168 đ** | **4.070.016 đ** | **≈ 4,12 tỷ đồng** |
| | **Cộng cả hai quy trình** | | | | **≈ 16,19 tỷ đồng** |

Phép nhân của từng bậc, viết ra để tra ngược: `một cửa hàng một tháng = đồng/ca × 96 GT39` cho C3 và `× 12 GT40` cho C4; `một cửa hàng một năm = × 12 tháng`; `toàn chuỗi = × 1.012 [N1]`.

Hai dòng của mục 4.4 Bước 3 nằm gọn trong bảng này và khớp số: `I-04` ra ≈ 3,6 tỷ, `I-03` ra ≈ 3,0 tỷ. Bốn dòng còn lại là phần mục 4.4 chưa liệt kê.

Số nào là số công bố, số nào là giả định. Trong toàn bộ hai bảng trên chỉ có hai đầu vào công bố: số cửa hàng 1.012 và doanh thu chuỗi 37.300 tỷ `[N1]` (doanh thu vào gián tiếp qua `GT37` và `GT38`), thêm các khoảng lương niêm yết `[#28]`–`[#35]` đứng sau đơn giá nhân công. Mọi thừa số còn lại là ước lượng có mã `GT`: thang thời gian `GT10`–`GT13`, phân bố nhánh `GT22` `GT25` `GT26` `GT41`, chi phí vận chuyển `GT31`–`GT33`, giá trị máy `GT34`–`GT35`, quy mô `GT39`–`GT40`. Đổi một mã trong số đó là phải tính lại đúng những dòng dẫn mã ấy, cấu trúc bảng giữ nguyên.

#### 4.6.3 Bảng 4.16 – Những vấn đề không đưa lên biểu đồ, và vì sao

Luật cứng của tài liệu này: không có dữ kiện thì để trống, không ước lượng cho đủ cột. Chín vấn đề còn lại của Issue Register không lên biểu đồ Pareto tiền, mỗi vấn đề ghi rõ lý do và cách lấy số thật.

| Mã | Tên ngắn | Vì sao không quy được ra tiền | Cách lấy số thật |
|---|---|---|---|
| `I-01` | Hàng đợi tại Trung tâm Bảo hành | Chi phí **doanh nghiệp** bỏ ra cho quãng này gần bằng 0: máy nằm chờ là tài sản của khách nên không phát sinh chi phí vốn của cửa hàng, còn hàng đợi thì nằm trong pool đối tác. Toàn bộ tiền của nó rơi sang khách hàng và đã ghi ở `I-05`. Đây chính là lý do vấn đề tốn nhiều thời gian nhất lại không hiện lên biểu đồ tiền của doanh nghiệp | Thỏa thuận mức phí hoặc mức phạt theo thời gian lưu với Trung tâm Bảo hành, khi đó quãng chờ mới có giá |
| `I-05` | Chi phí xử lý dồn về phía khách hàng | **93.789 đ/ca** đã tính được, nhưng người chịu tiền là **khách hàng**, không phải doanh nghiệp. Đặt chung một biểu đồ với sáu khoản trên là cộng hai túi tiền khác nhau, và cột lũy kế mất nghĩa | Đã có số; nếu muốn lên biểu đồ thì phải dựng một Pareto riêng cho phía khách hàng |
| `I-06` | Đạt cam kết 15 ngày mà quy trình vẫn kém hiệu quả | Không phải một khoản chi. Đây là cảnh báo về **cách đo**, tác động của nó là chỉ số CTE 3,17% chứ không phải số tiền | Không áp dụng |
| `I-07` | Trễ cam kết 15 ngày | Không rõ doanh nghiệp bồi thường bằng gì. `[#20]` công bố có dịch vụ cho mượn máy tạm nhưng không nêu điều kiện áp dụng, cũng không nêu mức bồi thường | Trích chính sách nội bộ về xử lý ca trễ hạn; đếm số ca trễ và chi phí thực chi trong 3 tháng trên log ERP |
| `I-08` | Máy bị khóa IMEI không có đường giải phóng ở nhánh từ chối – **đã sửa** | Mô hình nay có cổng `G16` đưa nhánh từ chối về `T6`, nên quãng khóa IMEI có mốc kết thúc và nằm gọn trong cycle time của ca thay vì kéo dài vô hạn. Phần chi phí sinh ra từ nó là 3 phút công dọn dẹp của `T6`, và khoản đó **đã nằm trong `I-15`** chứ không đứng riêng thành một cột – tách ra là đếm hai lần | Không áp dụng. Muốn biết quãng khóa thật thì đo mốc khóa và mốc mở trên log ERP |
| `I-09` | Nhánh thẻ tín dụng vẫn đi qua bước ký hợp đồng vay – **đã sửa** | Đây là **lỗi ngữ nghĩa của mô hình**, không phải lãng phí của doanh nghiệp: 15 phút và 15.625 đ là phần bảng thời gian tính **dư** cho nhánh thẻ, và sửa mô hình thì con số biến mất chứ không thành một khoản cắt được. Cổng `G17` đã kéo `T8` ra khỏi đường chung; không bảng nào đổi số vì mọi bảng định lượng của C3 lấy `GT22` làm mẫu số, tức chỉ đếm nhánh đi qua công ty tài chính | Không áp dụng. Muốn đưa nhánh thẻ vào phần định lượng thì phải đặt thêm một bộ giả định thời gian riêng cho nó |
| `I-11` | Số lượt vận chuyển của C4 | Đã xử lý ở bảng chi phí một ca C4: đếm lại ra 2,00 lượt/ca sau khi thêm `MF10`. Bản thân nó là một sai sót của phép đếm, không phải một khoản lãng phí đứng riêng; phần tiền của lượt về nhánh từ chối đã vào cột `I-03` | Không áp dụng |
| `I-12` | Ca còn trong tháng đầu vẫn phải gửi đi thẩm định | 20% ca `GT30` này **nằm lẫn** trong tập ca mà `I-02` đã tính: một ca vừa còn trong tháng đầu vừa thuộc danh mục lỗi hiển nhiên thì hai dòng cùng nhận. Không có số liệu để tách phần giao, và nhóm không đặt thêm giả định chỉ để tách | Trích log ERP đếm ca theo cặp điều kiện *còn trong tháng đầu* và *lỗi thuộc danh mục hiển nhiên* |
| `I-14` | Chuyển động nội bộ của nhân viên | Chưa có số lượt di chuyển, cũng chưa có quãng đường. Ô này để trống từ `dinh-tinh.md` Bảng 4.3 và Bảng 4.4 tới giờ | Một buổi quan sát tại cửa hàng, n ≥ 8 ca, bấm giờ và đếm lượt di chuyển giữa các lane |

---

## 5. Issue Register tổng hợp

Theo cấu trúc slide chương 5 trang 33-34. Gom mọi phát hiện của cả P5 (định tính) và P6 (định lượng), xếp theo mức tác động giảm dần. Cột "Giả định" ghi mã `GT` mà con số ở cột "Tác động định lượng" phụ thuộc vào, mã đó sai thì con số đó sai.

Thứ tự trong bảng là thứ tự tác động tổng hợp, gồm cả thời gian, chất lượng lẫn chi phí. Muốn xếp riêng theo tiền thì đọc hai biểu đồ Pareto ở mục 4.6: chúng lấy đúng cột "Tác động định lượng" của bảng này và xếp lại theo số tiền, đúng cách slide trang 36-37 làm.

| Issue ID | Tên ngắn | Mô tả | Giả định | Tác động định tính | Tác động định lượng | Hành động cải tiến |
|---|---|---|---|---|---|---|
| **I-01** | Hàng đợi tại Trung tâm Bảo hành | Máy nằm xếp lượt chờ thẩm định rồi chờ sửa chữa. **Không phải** bản thân việc thẩm định – việc đó là BVA, chặn gian lận bảo hành | `GT18` `GT19` | `Hold – Waiting` và `Inventory`; nhánh Method và Machine của bảng 6M cho C4; `BH3` (4 nguồn) | **82,0% toàn bộ waiting time của C4**; CTE 3,20%; cycle time 8,44 ngày | Xếp hàng đợi theo **hạn cam kết còn lại** thay vì vào trước ra trước; mở trang tra cứu trạng thái ca; đặt mức dịch vụ nội bộ cho từng chặng thay vì chỉ đo mốc 15 ngày cuối |
| **I-02** | Không ca nào kết thúc tại cửa hàng | Mọi đường đi trên mô hình C4 đều bắt buộc qua `T3` "chuyển máy tới Trung tâm Bảo hành", kể cả lỗi hiển nhiên | **không cần giả định** – đọc thẳng từ `C4-bao-hanh-doi-tra.bpmn` | `Move – Unnecessary transportation`; `Overdo – Over-processing`; `BH1` (5 nguồn, đứng đầu Pareto C4) | **Tỷ lệ xử lý xong ngay lần đầu = 0%**. Nếu phân quyền cho 40% ca `GT41`: cycle time **−38,7%**, vận chuyển **−8.808 đ/ca**, trong đó **6.606 đ/ca** rơi vào ca không bị từ chối và lên biểu đồ Pareto tiền C4 (mục 4.6) | Chuẩn hóa **danh mục lỗi hiển nhiên** và phân quyền kết luận tại cửa hàng; thêm một gateway ngay sau `T1` |
| **I-03** | Ca bị từ chối sau khi đã tốn toàn bộ công tiếp nhận và vận chuyển | Khách bị từ chối ở `G3` nhánh "do người dùng" chỉ sau khi máy đã đi lên Trung tâm Bảo hành và đã chờ tới lượt | `GT26` | `Overdo – Defects`; `BH2` (5 nguồn, đồng hạng nhất Pareto C4) | **25% số ca**; công và hai lượt vận chuyển bỏ đi **20.756 đ/ca** = 13,9% chi phí một ca; toàn chuỗi **≈ 3,0 tỷ đồng mỗi năm**. Cột cao nhất của biểu đồ Pareto tiền C4, chiếm **73,4%** tiền lãng phí một ca C4 | Đưa danh sách trường hợp loại trừ lên `T1`; chụp ảnh hiện trạng máy làm căn cứ; báo trước khả năng bị từ chối **trước** khi gửi máy đi |
| **I-04** | Vòng bổ sung giấy tờ của hồ sơ trả góp | Bộ giấy tờ thay đổi theo từng công ty tài chính và theo giá trị khoản vay, khách dễ chuẩn bị thiếu rồi phải bổ sung và chờ thẩm định lại. Vòng này nằm trên mô hình: `G12` sau `IE1`, nhánh "Thiếu chứng từ" quay về `G13` để chạy lại `T4` | `GT22` `GT15` | `Overdo – Defects`; `TG1` đứng đầu Pareto C3 (44,4% lượt nhắc) | **20% số hồ sơ**, nhưng sinh ra **60,7% toàn bộ waiting time của C3**; `T4` hiệu dụng 18,75 phút thay vì 15; chi phí làm lại 3.125 đ/ca; toàn chuỗi **≈ 3,6 tỷ đồng mỗi năm**. Cột thứ hai của biểu đồ Pareto tiền C3, chiếm **30,2%** tiền lãng phí một ca C3 | Checklist giấy tờ theo từng bên cho vay ngay tại `T1`; cho khách tải trước chứng từ qua app; chạy kiểm tính đầy đủ tự động trước khi đẩy hồ sơ đi |
| **I-15** | Hồ sơ trả góp bị từ chối sau khi đã tốn toàn bộ công tư vấn và lập hồ sơ | Hồ sơ đi hết `T1` → `T4 ‖ T5` → chờ thẩm định `IE1`, tới `G6` mới bị rẽ nhánh "Từ chối" → `T2` → `G16` → `T6` → `E3`. Toàn bộ công đã bỏ ra không sinh ra giao dịch nào, kể cả 3 phút dọn dẹp ở `T6`. Đây là bản C3 của `I-03` | `GT22` | `Overdo – Defects`; `TG5` đứng cuối Pareto đếm nguồn C3 nhưng **đứng đầu** Pareto tiền C3 | **15% số hồ sơ**; công bỏ đi **6.953 đ/ca** = 10,6% chi phí một ca C3; toàn chuỗi **≈ 8,1 tỷ đồng mỗi năm**. Cột cao nhất của biểu đồ Pareto tiền C3, chiếm **67,2%** tiền lãng phí một ca C3 | Sàng lọc sơ bộ ngay tại `T1` theo đúng tiêu chí của từng bên cho vay, để hồ sơ không đạt bị chặn **trước** khi tốn 15 phút lập hồ sơ và một vòng chờ thẩm định; chọn đúng bên cho vay ngay lần đầu để không đốt cơ hội nộp (annotation `A1`) |
| **I-05** | Chi phí xử lý dồn về phía khách hàng | Thời gian máy nằm chờ là chi phí thật, nhưng rơi vào khách chứ không vào sổ sách doanh nghiệp | `GT34` `GT36` | `BH3`, `BH7`; nhánh Milieu của bảng 6M cho C4 | **93.789 đ/ca** bình quân, **137.938 đ** ở nhánh sửa chữa – bằng 63% (nhánh sửa chữa: 93%) của 148.792 đ mà doanh nghiệp bỏ ra. **Không đưa lên biểu đồ Pareto tiền** vì người chịu tiền là khách hàng, không phải doanh nghiệp – lý do đầy đủ ở mục 4.6 | Đưa dịch vụ cho mượn máy tạm `[#20]` thành mặc định cho nhánh sửa chữa, thay vì để khách phải hỏi mới biết là có |
| **I-06** | Đạt cam kết 15 ngày mà quy trình vẫn kém hiệu quả | Nhánh sửa chữa mất 12,41 ngày, **vẫn lọt** cam kết 15 ngày công bố `[#18]` | `GT17` `GT18` `GT19` | Cảnh báo về cách đo: đạt cam kết không đồng nghĩa quy trình tốt | **CTE 3,17%** ở nhánh đúng hạn; tính theo ngày lịch còn **1,08%** | Bổ sung chỉ tiêu nội bộ cho **từng chặng** (nhận → thẩm định, thẩm định → sửa xong, sửa xong → trả khách), không chỉ đo tổng 15 ngày |
| **I-07** | Trễ cam kết 15 ngày | Một phần ca vượt hạn công bố | `GT29` | `BH3`; `BH6` – thông tin không nhất quán giữa nhân viên, tổng đài và chính sách | **20% số ca sửa chữa** (ước lượng). Chi phí hệ quả: **chưa đủ dữ kiện** | Cùng hành động với `I-01`; thêm cảnh báo tự động khi ca chạm mốc 10 ngày |
| **I-08** | Máy bị khóa IMEI không có đường giải phóng ở nhánh từ chối – **đã sửa 08/09/2026** | Trên `C3-ban-tra-gop.bpmn`, `G5` là event-based gateway đua `IE1` với `IE2`. Khi `IE1` thắng và `G6` rẽ "Từ chối" → `T2` → `E2`, bước `T6` "Giải phóng máy về tồn bán" **không có đường nào để chạy** – máy ở lại trạng thái khóa | **không cần giả định** – đọc thẳng từ sequence flow của file `.bpmn` | `Hold – Inventory`; `Overdo – Over-production` | 15% số hồ sơ `GT22` rơi vào trạng thái này. Chi phí vốn 2.192 đ/ngày/máy là nhỏ, nhưng **rủi ro vận hành là máy không bán được cho khách khác mà không ai biết** | **Đã thêm cổng XOR `G16 Máy đang bị khóa IMEI và giữ trên ERP?` ngay sau `T2`**: nhánh "Đang giữ máy" gộp ở `G15` rồi chạy `T6` → `E3`, nhánh "Chưa giữ máy" đi thẳng `E2` cho ca bị `G1` chặn từ bước sàng lọc. Ba cách khác đã cân nhắc và loại, lý do ở [../review/R19-ba-loi-logic-mo-hinh.md](../review/R19-ba-loi-logic-mo-hinh.md). Số đổi theo: `T6` nay gánh 0,45 phút/ca nên Bảng 4.12 lên **64.558 đ nhân công** và **65.904 đ** một ca, Bảng 4.9 kịch bản từ chối lên **PT 43 · CT 113**, và `I-15` lên **6.953 đ/ca** |
| **I-09** | Nhánh thẻ tín dụng vẫn đi qua bước ký hợp đồng vay – **đã sửa 08/09/2026** | `G2` nhánh "Qua thẻ tín dụng" → `T3` → `G8` → `T8` "**Ký hợp đồng vay với công ty tài chính**". Giao dịch trả góp qua thẻ không có hợp đồng vay với công ty tài chính | **không cần giả định** – đọc thẳng từ file `.bpmn` | Lỗi ngữ nghĩa mô hình; ảnh hưởng trực tiếp tới cycle time và chi phí của 20% giao dịch `GT21` | Nhánh thẻ bị tính dư 15 phút `GT10-M3` và dư 15.625 đ nhân công. Khoản dư này **không có mặt trong bảng nào**: mọi bảng định lượng của C3 lấy `GT22` làm mẫu số, tức chỉ đếm nhánh đi qua công ty tài chính, nên nhánh thẻ có trọng số 0 | **Đã thêm XOR join `G17` giữa `T8` và `T9`**: `G8` chỉ còn gom hai nhánh của đường vay, `T3` nhập lại ở `G17`. Chọn cách tách thay vì đổi nhãn `T8` vì đổi nhãn phải sửa theo năm chỗ chép nguyên văn và chỉ hợp thức hóa khoản dư chứ không xóa được nó. **Không bảng nào đổi số.** Còn treo và ghi ra để không giấu: nhánh thẻ vẫn đi qua `T12` "Đối chiếu khoản giải ngân của **công ty tài chính** với hóa đơn" – khác `T8`, bước này có thật trên cả hai hình thức nên chỉ là nhãn thiếu chính xác; tách đúng cách cần thêm một cặp split – join nữa, đẩy C3 lên 34 phần tử |
| **I-10** | Phí thiếu phụ kiện và thiếu hộp gây bất ngờ cho khách | Khách mang máy đi bảo hành mới biết bị tính phí | `GT25` | `BH8` (3 nguồn); nhánh Material của bảng 6M cho C4 | **30% số ca**. Mức phí là số công bố: tối đa 5% và 2% giá trị hóa đơn `[#19]` `[#21]`. Công tính phí tại quầy **902 đ/ca**, cột thứ ba của biểu đồ Pareto tiền C4 | Nhắc mang đủ hộp và phụ kiện ngay khi khách đặt lịch; checklist ảnh tại `T1` để khách xác nhận trước khi ký phiếu |
| **I-11** | Số lượt vận chuyển của C4 chưa khớp chiều về vừa được mô hình hóa – **đã chốt 08/09/2026** | Mô hình **đã có** `MF9 Máy lỗi trả về cửa hàng` đưa máy lỗi từ Trung tâm Bảo hành vào `T14` "Nhập máy lỗi thu hồi" (`dinh-tinh.md` mục 0.2 điểm 1), nhưng Bảng 4.13 vẫn đếm `0,25×1 + 0,225×1 + 0,075×1 + 0,45×2 = 1,45 lượt/ca` – cách đếm chỉ cho nhánh sửa chữa có chiều về, tức **có trước khi `MF9` được vẽ** | **không cần giả định** – đọc thẳng từ `C4-bao-hanh-doi-tra.bpmn` | Ảnh hưởng số lượt vận chuyển mỗi ca, tức ảnh hưởng trực tiếp cột chi phí | **Đã đếm ba lần, chốt ở 2,00 lượt/ca** (bảng đếm lượt đặt ngay trên bảng chi phí một ca C4): 1,45 khi chưa có `MF9`, 1,75 khi đã có `MF9` nhưng nhánh từ chối chưa có đường về, và **2,00** sau khi thêm `MF10`. Số dẫn xuất đã tính lại theo bước cuối: vận chuyển **19.268 → 22.020 đ/ca**, tổng một ca C4 **146.040 → 148.792 đ**, tỷ số C4/C3 **2,23 → 2,26 lần**, khoản vận chuyển tiết kiệm được của phương án cải tiến chính **−7.707 → −8.808 đ/ca**, và cột `I-03` của biểu đồ Pareto tiền C4 **18.003 → 20.756 đ/ca** | Xong cả hai chỗ từng treo. (1) Nhánh "Từ chối" nay **có** đường đưa máy về cửa hàng: message flow `MF10` từ pool Trung tâm Bảo hành vào `T4`, kèm annotation `A12`. Máy đang bảo hành là tài sản của khách nên bỏ chiều về là bỏ một chặng vận chuyển có thật; cách đếm cũ 1 lượt là chọn phía có lợi cho doanh nghiệp, nay bỏ. (2) **Chốt không cộng** quãng `MF9` và `MF10` vào `WT` của Bảng 4.10 và 4.11: `MF9` chạy theo **kỳ gom** của `T14` chứ không theo ca, còn `MF10` chạy **sau** mốc `E2` khi khách đã nhận thông báo và báo giá – cả hai đều không kéo dài ca của khách. Nếu vẫn muốn cộng riêng `MF9` thì `WT` lên 4.066 phút, cycle time **8,74 ngày** và CTE **3,09%** |
| **I-12** | Không ca nào của C4 được xử lý mà không rời cửa hàng, kể cả khi còn trong tháng đầu | `G4` phân nhánh tháng đầu / từ tháng hai xảy ra **sau** `IE1`, tức sau khi máy đã đi và đã chờ. Chính sách 1 đổi 1 trong tháng đầu `[#17]` `[#21]` bị vô hiệu về mặt thời gian | `GT30` | `BH4` (4 nguồn); mâu thuẫn giữa chính sách công bố và luồng thực thi | 20% số ca `GT30` đáng lẽ đổi ngay nhưng vẫn mất trọn 5,15 ngày chờ | Đưa kiểm tra mốc 30 ngày lên trước `T3`; nếu còn trong tháng đầu và lỗi thuộc danh mục hiển nhiên thì đổi ngay tại cửa hàng |
| **I-13** | Đơn đặt online vẫn cần nhân viên gọi xác nhận thủ công | Đối tác công bố nhân viên gọi xác nhận "trong 60 phút" `[#27]` | – (số công bố) | `Overdo – Over-processing`; `TG4` (2 nguồn, hạng ba Pareto C3) | Là neo trực tiếp cho `GT14` = 60 phút, tức **33,7% waiting time của C3**. Quy ra tiền, quãng chờ này khóa vốn một máy hết **274 đ/ca**, cột thứ ba của biểu đồ Pareto tiền C3 | Xác thực khách ngay lúc đặt online bằng OTP và đối chiếu định danh; chỉ gọi lại với đơn có dấu hiệu bất thường |
| **I-14** | Chuyển động nội bộ của nhân viên | Nhân viên đi lại giữa các lane trong cửa hàng | – | `Move – Motion` | **Chưa đủ dữ kiện để kết luận** – cần một buổi quan sát n ≥ 8 ca. Giữ nguyên ô trống, không ước lượng | Tổ chức buổi quan sát tại cửa hàng; cũng chính là buổi lấy số thật cho `GT10`–`GT19` |

---

## 6. Việc phải soát lại trước khi đưa vào Word

| # | Việc | Ràng buộc | Trạng thái |
|---:|---|---|---|
| 1 | Chốt `I-08` và `I-09` với người vẽ C3 | Cả hai làm đổi số ở Bảng 4.12 | **Đã chốt 08/09/2026.** `I-08` sửa bằng cổng `G16` sau `T2`; Bảng 4.12 lên 64.558 đ nhân công và 65.904 đ một ca. `I-09` sửa bằng XOR join `G17` giữa `T8` và `T9`; **không bảng nào đổi số** vì nhánh thẻ có trọng số 0 trong mẫu số `GT22`. Phương án bị loại và lý do ở [../review/R19-ba-loi-logic-mo-hinh.md](../review/R19-ba-loi-logic-mo-hinh.md) |
| 1b | Chốt chiều về của máy trên nhánh "Từ chối" của C4 với người vẽ C4 | `I-11` đã đếm lại ra 1,75 lượt/ca theo đúng hình đang có; vẽ thêm chiều về cho nhánh từ chối thì thành 2,0 lượt và Bảng 4.13 đổi lần nữa | **Đã chốt 08/09/2026: vẽ chiều về.** Thêm message flow `MF10` từ pool Trung tâm Bảo hành vào `T4`, không thêm phần tử nào. Bảng 4.13 lên **2,00 lượt/ca** và **148.792 đ**; chuỗi dẫn xuất gồm mục 4.3, 4.4, 4.5, Bảng 4.14 cột `I-03`, Bảng 4.15 và hai hình `pareto-tien-C*` đều đã tính lại |
| 1c | Quyết có cộng quãng `MF9` và `MF10` vào `WT` của Bảng 4.10 và 4.11 hay không | Đang **không** cộng, lý do và con số nếu cộng ghi ở `I-11`. Cộng thì phải sinh lại hai hình `C4-time` và `C4a-time` cho khớp | **Đã chốt 08/09/2026: không cộng.** `MF9` chạy theo kỳ gom của `T14` chứ không theo ca; `MF10` chạy sau mốc `E2` của nhánh từ chối. Cả hai đều là chặng vận chuyển có thật nên **có** trong bảng chi phí, nhưng không nằm trong quãng khách phải chờ nên **không** vào bảng thời gian. Bảng 4.10 và 4.11 giữ nguyên, hai hình `C4-time` không phải sinh lại vì số trên chúng không đổi |
| 2 | Tổ chức buổi quan sát tại cửa hàng, n ≥ 8 ca, bấm giờ từng chặng | Thay giá trị `GT10`–`GT19` và đổi cột "Mức tin cậy" từ `ước lượng` sang `quan sát`. Công thức và cấu trúc bảng giữ nguyên | Chưa làm – biên bản buổi 3 còn trống |
| 3 | Chụp màn hình trang chính sách bảo hành và các tin tuyển dụng `[#28]`–`[#35]`, lưu vào `evidence/` | Mọi đơn giá nhân công ở mục 1.2 dựa vào chúng; tin tuyển dụng bị gỡ là mất toàn bộ cột "Căn cứ" | Chưa làm |
| 4 | Chụp màn hình báo cáo kết quả kinh doanh `[N1]`, phần doanh thu chuỗi và số cửa hàng | Toàn bộ mục 4.4 dựa vào hai con số này | Chưa làm |
| 5 | Soát chéo: mọi ô số trong tài liệu đều có `GTnn`, có `[#n]`/`[Nn]`, hoặc có công thức | Ràng buộc cứng của P6 | Chưa làm – để bước soát cuối theo P9 |
| 6 | Kiểm lại: không dòng nào ghi mức tin cậy `quan sát` khi buổi quan sát chưa diễn ra | Nếu việc 2 chạy xong thì bỏ ràng buộc này | Chưa làm |
| 7 | Đối chiếu: mọi mã `BH*`, `TG*` dẫn ở mục 5 đều tồn tại trong `dinh-tinh.md` và `bao-cao-nguon-thu-cap.md` | Chống dẫn nhầm mã | Chưa làm |
