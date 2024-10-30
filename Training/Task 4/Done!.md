## PicoCTF

### GET aHEAD
![image](https://github.com/user-attachments/assets/187c9f2a-a7ee-4bd5-80da-31cb7055e699)

- Open link with Burp Suite and check request.
- Ta mỗi lần choose một màu thì sẽ dùng 1 method khác. Cụ thể như sau:

![image](https://github.com/user-attachments/assets/feb70905-63ab-426e-9c4f-d2455a9263bd)
- Nếu choose red thì method là GET, blue thì là POST. Giờ ta cần tìm 1 method để đảm bảo method đó bao gồm cả 2 method trên. Ta dùng HEAD.
- Send request bằng repeater sau khi chỉnh method là HEAD ta có được flag.

![image](https://github.com/user-attachments/assets/e0b7e80d-ca31-4434-8631-81d463fe5a99)

### Cookies
- Do chall tên cookies nên mình vào check cookies:)))
- Sau khi nhập tùm lum thì mình thấy không có gì thay đổi trong cookie. Chỉ khi mình nhập `snickerdoodle` thì thấy giá trị của Value trong cookie thay đổi. Nên mình thử thay đổi vài giá trị của của cookie coi có gì hiện ra không:))
- Với mỗi giá trị thì mình lại nhận được 1 chuỗi khác nhau. Và sau cùng khi value đặt giá trị 18 thì mình có được flag:))

![image](https://github.com/user-attachments/assets/0f82281f-8866-4a6f-91a6-335ec82a54b4)


## Rootme
### HTTP - IP restriction bypass
- Với chall này ta cần đặt ip sao cho request ta gửi đi là từ ip của client trong server để có thể truy cập vào link mà không cần đăng nhập.
- Mình có search gg và tìm được cách giả mạo ip bằng `X-Forwarded-For`, ở đây mình thử giả mạo ip thành `192.168.1.100` và gửi request đi.

![image](https://github.com/user-attachments/assets/64a2c518-138f-460a-a958-c3b020f52dd3)
- Ta lấy được pass. Submit thử thì đó là flag:)))

### HTTP - User-agent
- Truy cập link ta thấy: `Wrong user-agent: you are not the "admin" browser!`.
- Giờ chỉ cần chỉnh request bằng cách thêm `user-agent: admin`.

![image](https://github.com/user-attachments/assets/8ad0babb-d9f6-414e-b756-f234e490ef91)

### HTTP - Headers
- Chall này yêu cầu ta truy cập vào với quyền admin.
- Mình có thử nhiều cách để bypass như:
    - X-Admin: true
    - X-Forwarded-Role: admin
    - X-User-Role: admin
    - Thêm sau role=admin, admin=true vào cookie.
- Tuy nhiên lại không bypass được như mong đợi. Mình có thử thêm các cách sau:
    - Header-RootMe-Admin: true
    - Header-RootMe-Admin: 1
    - Header-RootMe-Admin: admin
- Và nhận được pass như mong muốn.

![image](https://github.com/user-attachments/assets/7a59c1f6-eea0-4fe5-a0f7-18112dd4bcb0)

### HTTP - POST
- Check request mình thấy được thay đổi score:))
- Thay đổi score ta có được flag.

![image](https://github.com/user-attachments/assets/ed040964-1c1d-4e2a-8c29-ad860c7628cc)