# Thong ke phan tu 11 file BPMN

Sinh tu dong boi `gen_bpmn.py` tu dac ta `docs/ch2-dac-ta-bpmn.md`.
Dung sua tay file nay - sua dac ta roi chay lai script.

## 6 mo hinh nop

| Ma | Quy trinh | Pool | Lane | Task | Event | **Gateway** | Sequence flow | Message flow | File |
|---|---|---:|---:|---:|---:|---:|---:|---:|---|
| M2 | Quản lý nhà cung cấp và đặt hàng nhập | 2 | 4 | 13 | 4 | **10** | 30 | 3 | `M2-quan-ly-ncc-dat-hang.bpmn` |
| M3 | Quản lý kho tổng và điều chuyển hàng giữa cửa hàng | 1 | 4 | 13 | 4 | **11** | 32 | 0 | `M3-kho-tong-dieu-chuyen.bpmn` |
| C3 | Bán trả góp qua công ty tài chính | 3 | 4 | 11 | 6 | **15** | 39 | 6 | `C3-ban-tra-gop.bpmn` |
| C4 | Bảo hành, đổi trả một đổi một và thu hồi máy lỗi | 4 | 3 | 13 | 4 | **12** | 35 | 9 | `C4-bao-hanh-doi-tra.bpmn` |
| S1 | Tuyển dụng và đào tạo nhân viên bán hàng | 2 | 4 | 12 | 7 | **12** | 36 | 6 | `S1-tuyen-dung-dao-tao.bpmn` |
| S4 | Đối soát công nợ và thanh toán nhà cung cấp | 2 | 4 | 10 | 3 | **10** | 27 | 4 | `S4-doi-soat-thanh-toan-ncc.bpmn` |
| | **Tong** | **23** | **28** | **85** | **39** | **82** | **236** | **37** | |

Rubric tieu chi 2.4 cho 1.0 diem khi so gateway `> 7`. Mo hinh thap nhat trong bo nay co 10 gateway, deu vuot moc.

## 5 hinh chi tiet sub-process

Moi hinh duoi day la phan ben trong mot hop sub-process thu gon cua mo hinh cha, ve thanh mot hinh rieng. Phan tu cua chung KHONG cong vao bang tren, va chung khong chiu moc 7 cong cua rubric - moc do tinh tren mo hinh nop.

| Ma | Quy trinh | Pool | Lane | Task | Event | **Gateway** | Sequence flow | Message flow | File |
|---|---|---:|---:|---:|---:|---:|---:|---:|---|
| M2a | Phát hành và chốt đơn (chi tiết sub-process SP1 của M2) | 2 | 1 | 2 | 3 | **2** | 7 | 3 | `M2a-phat-hanh-va-chot-don.bpmn` |
| M3a | Soạn và chuyển hàng đi (chi tiết sub-process SP1 của M3) | 1 | 1 | 3 | 2 | **2** | 7 | 0 | `M3a-soan-va-chuyen-hang.bpmn` |
| C3a | Giao máy cho khách (chi tiết sub-process SP1 của C3) | 2 | 1 | 2 | 2 | **2** | 6 | 2 | `C3a-giao-may-cho-khach.bpmn` |
| C4a | Khép hồ sơ xử lý (chi tiết sub-process SP1 của C4) | 2 | 1 | 2 | 2 | **2** | 6 | 1 | `C4a-khep-ho-so-xu-ly.bpmn` |
| S4a | Chi tiền và ghi giảm nợ (chi tiết sub-process SP1 của S4) | 2 | 1 | 4 | 2 | **4** | 11 | 3 | `S4a-chi-tien-ghi-giam-cong-no.bpmn` |

## Bo cuc

`layout()` gap cac cot xuong nhieu bang trong cung mot lane khi hinh qua det. Muc gap khong phai hang so: script sinh thu tung muc, uoc luong khung anh SAU khi `report/tools/squeeze_bpmn.py` nen khoang trang, roi giu muc cho CO CHU IN RA lon nhat. Ty le hinh chi con la rang buoc tran, khong vuot 3.0 : 1.

| Ma | Cot moi bang | Tong cot | Bang | Duong vong | Canh quay lui | Ty le hinh |
|---|---:|---:|---:|---:|---:|---:|
| M2 | 13 | 23 | 2 | 2 | 0 | 1.81 : 1 |
| M2a | 4 | 7 | 2 | 2 | 0 | 1.10 : 1 |
| M3 | 16 | 21 | 2 | 2 | 0 | 1.88 : 1 |
| M3a | 4 | 6 | 2 | 1 | 0 | 1.32 : 1 |
| C3 | 17 | 22 | 2 | 5 | 1 | 1.78 : 1 |
| C3a | 5 | 5 | 1 | 0 | 0 | 2.15 : 1 |
| C4 | 12 | 21 | 2 | 3 | 0 | 1.61 : 1 |
| C4a | 5 | 5 | 1 | 0 | 0 | 2.15 : 1 |
| S1 | 17 | 24 | 2 | 2 | 0 | 1.88 : 1 |
| S4 | 15 | 18 | 2 | 2 | 0 | 2.08 : 1 |
| S4a | 5 | 9 | 2 | 1 | 0 | 1.10 : 1 |

Ty le do tren chinh khung ve cua file `.bpmn`. `bpmn-to-image` xen dung khung do roi phong 1,5 lan, nen file PNG truoc khi nen khoang trang ra dung ty le nay; sau buoc nen thi ty le doi, vi khoang trang bi bo di khong deu hai chieu.

## Kiem tra da chay tu dong

1. Parse lai bang `xml.etree` - khong loi cu phap
2. Moi mo hinh >= 8 gateway
3. Moi `sequenceFlow` co `sourceRef` va `targetRef` ton tai
4. Khong `sequenceFlow` nao noi hai `process` khac nhau (giua pool chi dung `messageFlow`)
5. Moi phan tu ngu nghia deu co `BPMNShape`, moi luong deu co `BPMNEdge`
6. Moi phan tu nam trong dung mot lane
7. So dem sinh ra khop voi bang dem trong `docs/ch2-dac-ta-bpmn.md`
8. Khong hinh nao de len hinh nao, khong nhan nao de len hinh
9. Ty le hinh khong vuot 3.0 : 1
10. Khong doan duong noi nao cat qua hinh (muc canh bao)
