## PicoCTF

### GET aHEAD
![image](https://github.com/user-attachments/assets/187c9f2a-a7ee-4bd5-80da-31cb7055e699)

- Open link with Burp Suite and check request.
- Ta mỗi lần choose một màu thì sẽ dùng 1 method khác. Cụ thể như sau:

![image](https://github.com/user-attachments/assets/feb70905-63ab-426e-9c4f-d2455a9263bd)
- Nếu choose red thì method là GET, blue thì là POST. Giờ ta cần tìm 1 method để đảm bảo method đó bao gồm cả 2 method trên. Ta dùng HEAD.
- Send request bằng repeater sau khi chỉnh method là HEAD ta có được flag.

![image](https://github.com/user-attachments/assets/e0b7e80d-ca31-4434-8631-81d463fe5a99)

### 