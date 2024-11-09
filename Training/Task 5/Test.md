# File upload vulnerabilities
## File upload vulnerabilities là gì?
- **File upload vulnerabilities** là lỗ hổng bảo mật do web cho phép người dùng upload file lên mà không kiểm duyệt kỹ về nội dung, định dạng,...
- Những lỗ hổng đó có thể dẫn đến nhiều loại tấn công nguy hiểm như thực thi mã độc từ xa, tấn công từ chối dịch vụ, hoặc truy cập trái phép vào hệ thống.
## Nguyên nhân
- Lỗ hổng này thường tồn tại do:
    - Kiểm tra không đầy đủ định dạng hoặc nội dung file: Hệ thống không xác thực loại file hoặc nội dung bên trong file mà người dùng tải lên, dẫn đến việc các file độc hại có thể được tải vào máy chủ.
    - Thiếu biện pháp kiểm tra quyền truy cập: Sau khi file được tải lên, các file này có thể được lưu trữ ở những nơi mà người dùng hoặc hacker có thể truy cập trực tiếp, dẫn đến nguy cơ thực thi file độc hại.
    - Không hạn chế định dạng file: Nếu ứng dụng không giới hạn các loại file tải lên (ví dụ như chỉ cho phép hình ảnh), hacker có thể tải lên các file nguy hiểm như .php, .jsp, hoặc .exe để thực thi mã độc.
    - Cấu hình không đúng trong máy chủ: Một số hệ thống không cấu hình đúng các quyền truy cập đối với các thư mục chứa file tải lên, hoặc không kiểm soát việc thực thi mã trong các thư mục này, dẫn đến rủi ro thực thi file độc hại.
## Phương án khai thác
- **Upload file mã độc:** Tải lên các file mã độc, chẳng hạn như .php hoặc .jsp, vào máy chủ. Nếu máy chủ không cấu hình đúng, file mã độc sẽ có thể được thực thi và hacker có thể thực hiện các thao tác nguy hiểm như chiếm quyền kiểm soát máy chủ.
- **Tấn công web shell:** File độc hại có thể chứa mã để mở cổng điều khiển từ xa (web shell), cho phép hacker truy cập, chỉnh sửa, hoặc thực thi lệnh trên máy chủ.
- **Thực hiện SSRF hoặc XSS:** Hacker có thể tải lên các file chứa mã JavaScript độc hại để khai thác lỗ hổng Cross-Site Scripting (XSS), hoặc thực hiện các yêu cầu Server-Side Request Forgery (SSRF), giúp hacker truy cập đến các tài nguyên nội bộ của hệ thống.
- **Khai thác các lỗ hổng liên quan đến MIME Type:** Một số hệ thống dựa vào MIME Type để xác định loại file, nhưng hacker có thể thay đổi MIME Type để đánh lừa hệ thống cho phép tải lên các file nguy hiểm.

# Exploiting 
## Exploiting unrestricted file uploads
- Như cái tên thì ta thấy rằng với trường hợp này ta có thể upload file nên mà không có giới hạn gì về nội dung, định dạng,...
- Từ đó ta tải lên các file độc hại bằng nhiều phương pháp khác nhau, chẳng hạn như web shell hoặc các loại mã độc khác, giúp kẻ tấn công truy cập trái phép vào hệ thống.
### Demo
- Ở [đây](https://portswigger.net/web-security/file-upload/lab-file-upload-remote-code-execution-via-web-shell-upload) mình có 1 challenge demo.
- Theo chall thì ta cần tìm được secret của carlos. Chall cung cấp cho ta biết rằng web không xác thực bất kỳ điều gì với tệp được tải lên.
- Ta tạo một file php và upload thử.
```php
<?php system('ls / -la'); ?>
```
- Sau khi upload ta thấy web đã thực thi code. Ta tiến hành tìm thông tin bị ẩn giấu.

![image](https://github.com/user-attachments/assets/0aa164c4-3f86-43cf-9f9b-1a87a276ceb8)
- Do biết được đường dẫn nên ta cat ra thôi:)))
```php
<?php system('ls / -la'); ?>
<?php system('cat /home/carlos/secret'); ?>
```

![image](https://github.com/user-attachments/assets/48398b45-dec5-4bab-afaa-bc0fff0ef635)
## Exploiting flawed validation of file uploads
- Với trường hợp này thì web check không đầy đủ các yếu tố hoặc check không chính xác loại file được upload. Từ đó ta có thể by pass để tải lên các file độc hại bằng nhiều phương pháp khác nhau, chẳng hạn như web shell hoặc các loại mã độc khác, giúp kẻ tấn công truy cập trái phép vào hệ thống.
### Flawed file type validation
- Có kha khá lỗ hổng về trường hợp này chả hạn như: web chỉ kiểm tra phần mở rộng file, kiểm tra MIME type thiếu chính xác,...
- Ở đây mình sẽ đề cập đến một số cách by pass với trường hợp này:

| **Phương Pháp Khai Thác Lỗi Xác Thực Upload**         | **Mô Tả Chi Tiết**                                                                  | **Ví Dụ**                                                                       |
|-------------------------------------------------------|-------------------------------------------------------------------------------------|----------------------------------------------------------------------------------|
| **Thiếu kiểm tra phần mở rộng file**                  | Hệ thống không giới hạn hoặc không kiểm tra đúng đuôi file (extension)              | Upload `shell.php` thay vì file ảnh nếu hệ thống không giới hạn extension       |
| **Kiểm tra MIME-type không chính xác**                | Hệ thống dựa vào MIME type để xác định loại file nhưng không kiểm tra nội dung thực | Dùng Burp Suite đổi `Content-Type` của file PHP thành `image/jpeg`              |
| **Chỉ kiểm tra tên file mà không kiểm tra nội dung**  | Hệ thống chỉ kiểm tra tên file mà bỏ qua việc kiểm tra nội dung thực của file       | Upload file PHP với tên `image.jpg` nhưng nội dung là mã PHP                     |
| **Sử dụng payload nhúng trong file ảnh**              | Chèn mã độc vào file ảnh như mã PHP vào cuối file `.jpg` để đánh lừa hệ thống       | Nhúng mã PHP như `<?php system($_GET['cmd']); ?>` vào cuối file `.jpg`          |
| **Sử dụng Null Byte Injection**                       | Chèn ký tự Null Byte (`%00`) vào giữa tên file để bỏ qua kiểm tra extension         | Upload `shell.php%00.jpg` để hệ thống nhận diện là `.jpg` nhưng thực thi `.php` |
| **Chỉ kiểm tra magic number không đầy đủ**            | Hệ thống chỉ kiểm tra magic number mà không xác thực toàn bộ file                   | Thay đổi magic number của file PHP thành JPEG để vượt qua kiểm tra              |
| **Quá trình kiểm tra không đầy đủ cho file nén**      | Hệ thống cho phép tải lên file nén mà không kiểm tra file được giải nén            | Upload `shell.zip` chứa file `.php`, sau đó giải nén trên server                |
| **Sử dụng phần mở rộng kép hoặc đặc biệt**            | Sử dụng tên file với hai đuôi hoặc đuôi đặc biệt mà máy chủ có thể nhận diện thực thi | Đổi tên `shell.php` thành `shell.php.jpg` hoặc sử dụng `.php5`, `.phtml`        |
| **Không có giới hạn kích thước file hợp lệ**          | Hệ thống không giới hạn kích thước file, có thể tải lên file lớn để tạo DoS         | Upload file lớn để tạo DoS hoặc nhúng mã độc vào file lớn                        |
| **Thiếu kiểm tra cho file kịch bản khác**             | Hệ thống chỉ kiểm tra loại file PHP mà bỏ qua các loại file script khác             | Upload shell với phần mở rộng `.jsp` hoặc `.asp` nếu hệ thống hỗ trợ script này  |
| **Chỉ lọc ký tự một phần tên file**                   | Hệ thống chỉ kiểm tra phần đuôi mở rộng `php` nhưng không loại bỏ ký tự đặc biệt    | Upload `shell;.php` để qua mặt bộ lọc nếu server chỉ kiểm tra `.php`            |

- Bạn có thể tham khảo chi tiết hơn ở [đây](https://book.hacktricks.xyz/pentesting-web/file-upload)
#### Demo
- Ở [đây](https://portswigger.net/web-security/file-upload/lab-file-upload-web-shell-upload-via-content-type-restriction-bypass) mình có 1 challenge demo.
