## Root-me
### File upload - Double extensions
- Với chall này ta chỉ cần thay đổi đuôi mở rộng thành `.php.png` là có thể by pass được.
- Đầu tiên mình thử `ls` xem có những file gì.

![image](https://github.com/user-attachments/assets/09ab1444-f736-47dc-baf8-0439b7f0c1f5)
- Ta biết flag nằm ở file `.passwd`. Lúc này thì cần tìm được file và cat ra thôi.
- Thử `../` từng thư mục rồi cat thử thôi.

![image](https://github.com/user-attachments/assets/b36da3d6-62fa-4703-ad53-252d4647c812)

### File upload - MIME type
- Tương tự chall trên tuy nhiên đuôi mở rộng sẽ là `.png.php`
- Sau khi by pass được thì ta tiếp tục check file `.passwd` nằm ở đâu và cat ra.

![image](https://github.com/user-attachments/assets/09193d11-e34c-47bc-bde1-740c1dbd6fc4)


### File upload - Null byte
- Như tên bài thì ta sửa đuôi mở rộng theo null byte.
- Ở đây mình dùng `.php%00.png` send request và thu flag.

![image](https://github.com/user-attachments/assets/3c01c9b1-2ed4-4eaa-bb1c-3f50caedb05c)

### File upload - ZIP
