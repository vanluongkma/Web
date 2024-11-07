# File upload vulnerabilities
- File upload vulnerabilities là khi máy chủ web cho phép người dùng tải tệp lên hệ thống tệp của nó mà không xác thực đầy đủ những thứ như tên, loại, nội dung hoặc kích thước của chúng. Việc không thực thi đúng cách các hạn chế đối với những hạn chế này có thể có nghĩa là ngay cả chức năng tải lên hình ảnh cơ bản cũng có thể được sử dụng để tải lên các tệp tùy ý và có khả năng gây nguy hiểm. Điều này thậm chí có thể bao gồm các tệp tập lệnh phía máy chủ cho phép thực thi mã từ xa.
- Trong một số trường hợp, bản thân hành động tải tệp lên đã đủ gây ra thiệt hại. Các cuộc tấn công khác có thể liên quan đến yêu cầu HTTP tiếp theo đối với tệp, thường là để kích hoạt quá trình thực thi tệp của máy chủ.
- File upload vulnerabilities thường phụ thuộc vào hai yếu tố chính:
    - Web không xác thực về kích thước, loại, nội dung, v.v.
    - Một số rule được đặt ra nhưng lại có thể bị by pass.
- Việc có lỗ hổng file upload có thể để lại 1 số hậu quả nghiêm trọng sau:
    - File gửi lên có thể thực thi từ đó bị lấy web shell.
    - Ghi đè file llamf mất dữ liệu.
    - Dos bằng cách load file dung lượng lớn.
## File Upload General Methodology
- Đây là phương pháp phổ biến là tìm cách bypass các cơ chế kiểm tra extension và mime-type nhằm tải lên file mã độc.
### 


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
- Đây mình up file nên thì sẽ được giải nén.
- Mình thử nén lại xong upload. Tuy nhiên vẫn không thể mở.

![image](https://github.com/user-attachments/assets/fb9e43d2-fbcb-4418-91ff-d8396b56742c)

- Mình làm theo cách trên:)) và có được flag.
