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
## Một vài các khai thác
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

- Bạn có thể tham khảo chi tiết hơn ở [đây](https://book.hacktricks.xyz/pentesting-web/file-upload).
#### Demo
- Ở [đây](https://portswigger.net/web-security/file-upload/lab-file-upload-web-shell-upload-via-content-type-restriction-bypass) mình có 1 challenge demo.
- Với chall này thì ban đầu mình có thử upload file php. Tuy nhiên web lại chặn không cho phép mình upload.
- Mình lại thử upload file png thì ok web nhận. Sau đó mình sửa request. Gửi 1 file .php nhưng MIME type lại là `image/png`.

![image](https://github.com/user-attachments/assets/17b8d3dd-eae2-4862-944c-e1d03cfffa17)
### Preventing file execution in user-accessible directories
- Tại đây ta sẽ tìm hiểu về kỹ thuật **path traversal**.
- **Path traversal** là một lỗ hổng bảo mật phổ biến trong các ứng dụng web. Kỹ thuật này cho phép kẻ tấn công truy cập các file hoặc thư mục trên máy chủ nằm ngoài phạm vi mà ứng dụng dự kiến, thường là bằng cách khai thác các điểm yếu trong việc kiểm tra và xử lý đường dẫn.
- Cách hoạt động của Path Traversal
    -Path traversal xảy ra khi ứng dụng không lọc hoặc không xử lý đúng dữ liệu đầu vào là đường dẫn file. Bằng cách truyền các ký tự đặc biệt như ../ (chỉ đường dẫn thư mục cha), kẻ tấn công có thể thoát khỏi thư mục hiện tại và truy cập vào các thư mục cấp cao hơn trong hệ thống file.
- Ví dụ, nếu URL chứa đường dẫn file như sau:
```bash
http://example.com/view?file=images/photo.jpg
```
- Nếu ứng dụng không kiểm tra chặt chẽ tham số file, kẻ tấn công có thể thử sử dụng ../ để truy cập các file hệ thống nhạy cảm, chẳng hạn như:
```bash
http://example.com/view?file=../../../../etc/passwd
```

#### Demo
- Ở [đây](https://portswigger.net/web-security/file-upload/lab-file-upload-web-shell-upload-via-path-traversal) mình có 1 challenge demo.
- Với chall này ta có thể upload được file php tùy thích.
- Tuy nhiên server lại trả lại cho ta code dưới dạng text:)))
- Ta sẽ thử gửi file vào 1 thư mục khác sau bằng kỹ thuật path traversal.
- Xem chi tiết hơn tại [đây](https://owasp.org/www-community/attacks/Path_Traversal) nha.
![image](https://github.com/user-attachments/assets/8addad33-aeb1-414e-aff5-99cb7b1a00ee)

### Insufficient blacklisting of dangerous file types
- **Insufficient blacklisting of dangerous file types** là một lỗ hổng bảo mật khi hệ thống chỉ dựa vào **blacklist** để ngăn chặn việc upload các file nguy hiểm, nhưng không đủ hiệu quả hoặc bị bỏ sót một số loại file. Thay vì chỉ cho phép một số loại file an toàn, hệ thống cố gắng chặn các định dạng hoặc phần mở rộng file nguy hiểm như .exe, .php, hoặc .js. Tuy nhiên, nếu blacklist không đầy đủ hoặc dễ dàng bị bypass, kẻ tấn công có thể upload file nguy hiểm để thực hiện các hành vi như thực thi mã độc, chiếm quyền điều khiển server, hoặc đánh cắp dữ liệu.
- Đơn giản có thể hiểu là việc tồn tại lỗ hổng này là do blacklist ko đủ.
#### Overriding the server configuration
- **Overriding the server configuration** hay ghi đè cấu hình máy chủ là một phương pháp hacker dùng để thay đổi cách máy chủ xử lý các file hoặc yêu cầu từ người dùng, nhằm thực thi mã độc hoặc thực hiện các hành vi trái phép. Trong bối cảnh bảo mật, phương pháp này thường liên quan đến việc tải lên các file cấu hình có khả năng điều chỉnh cách máy chủ xử lý một số loại file hoặc yêu cầu cụ thể. Khi hacker có thể ghi đè cấu hình máy chủ, họ có thể kiểm soát cách thức thực thi file và mở ra nhiều cách khai thác khác nhau.
- Lấy ví dụ như một số máy chủ `Apache` hoặc `Nginx` cho phép sử dụng file cấu hình riêng ở cấp thư mục. Nếu máy chủ cho phép tải lên file cấu hình (ví dụ: '.htaccess' trên `Apache`), hacker có thể tận dụng điều này để ghi đè cấu hình và mở các lỗ hổng bảo mật.
- Cụ thể hơn với:
    - **Apache .htaccess File:**
        - Trong Apache, file .htaccess có thể ghi đè nhiều cài đặt máy chủ, bao gồm các quy tắc xử lý file. Hacker có thể tải lên file .htaccess với các cấu hình như sau để thay đổi cách xử lý file:
        > SetHandler application/x-httpd-php
        - Dòng lệnh trên yêu cầu Apache xử lý các file trong thư mục đó như file PHP, dù chúng có đuôi mở rộng là gì. Điều này cho phép hacker chạy mã PHP trong các file có đuôi khác (như .jpg hoặc .txt).
    - **Nginx Configuration:**
        - Nginx không hỗ trợ ghi đè cấu hình ở cấp thư mục tương tự .htaccess, nhưng nếu hacker có quyền truy cập vào file cấu hình của Nginx, họ có thể thay đổi cách thức xử lý file PHP, thiết lập quyền truy cập thư mục, hoặc điều chỉnh proxy để chuyển tiếp yêu cầu đến máy chủ khác.
    - **Override MIME Type hoặc file upload:**
        - Thay đổi MIME type để chỉ định kiểu file được xử lý theo cách khác, cho phép chạy mã tùy chỉnh. Ví dụ, hacker có thể cấu hình để xử lý file .jpg như một file PHP nếu máy chủ không giới hạn

- Nói một cách dễ hiểu hơn thì kỹ thuật này cho phép kẻ tấn công thay đổi cấu hình server bằng các file cấu hình, thường là .htaccess trên Apache. Khi server cho phép upload .htaccess hoặc các file cấu hình khác, kẻ tấn công có thể lợi dụng nó để thực thi mã PHP, thay đổi quyền truy cập file, hoặc can thiệp vào chính sách bảo mật.
- Ví dụ khi ta có quyền upload file `.htaccess` ta có thể cho phép server xử lý các file .phtml như file PHP và thực thi mã bên trong.
```apache
<FilesMatch ".*\.(php|php5|phtml)$">
    SetHandler application/x-httpd-php
</FilesMatch>
```
##### Demo
- Ở [đây](https://portswigger.net/web-security/file-upload/lab-file-upload-web-shell-upload-via-extension-blacklist-bypass) mình có 1 challenge demo.
- Quay lại chall. Ở đây ta sẽ ánh xạ `.l33t` thành `application/x-httpd-php` hay `.php` bằng cách dùng `.htaccess`. Tuy đây không phải **path traversal** mà là **overriding server configuration**.
- Ta thực hiện như sau:
    - Đâu tiên ta gửi 1 request với file `.htaccess` có `Content-Type` là `text/plain` kèm theo đó là
lệnh Apache sau:
    ```bash
    AddType application/x-httpd-php .l33t
    ```
    - Sau đó ta là tương tự như các demo trên tuy nhiên hãy gửi file `.l33t` thay vì `.php`
  
![image](https://github.com/user-attachments/assets/4911cc95-be1a-48c4-aed8-715288bf6ec7)
#### Obfuscating file extensions
- **Obfuscating file extensions** là kỹ thuật mà kẻ tấn công sử dụng để che giấu định dạng thực sự của file nhằm qua mặt các biện pháp kiểm tra bảo mật. Kỹ thuật này giúp file chứa mã độc hoặc mã thực thi có thể được tải lên mà không bị phát hiện, đặc biệt khi hệ thống chỉ kiểm tra phần mở rộng file mà không kiểm tra nội dung.
- Đơn giản thì đó là cách thay đổi các đuôi mở rộng để by pass qua việc check của server.
- Dưới đây là một vài cách để bạn thực hiện kỹ thuật này:

| Kỹ thuật                             | Mô tả                                                                                          | Ví dụ                   |
|--------------------------------------|-----------------------------------------------------------------------------------------------|-------------------------|
| Thêm ký tự đặc biệt hoặc không hợp lệ | Sử dụng dấu chấm hoặc ký tự đặc biệt để gây nhầm lẫn trong phần mở rộng file                  | `shell.php.jpg`         |
| Phần mở rộng kép                     | Đặt tên file với nhiều phần mở rộng, hệ thống kiểm tra chỉ xem xét phần cuối                  | `file.php.jpg`          |
| Mã hóa tên file                      | Sử dụng mã hóa URL hoặc mã Unicode để thay đổi cách hiển thị phần mở rộng                     | `file.ph%70`            |
| Phần mở rộng không phổ biến           | Đổi đuôi file sang phần mở rộng ít thấy nhưng vẫn có thể thực thi trên một số server          | `shell.phtml`           |
| Chèn dấu cách hoặc ký tự vô hình     | Thêm khoảng trắng, dấu chấm hoặc ký tự không hiển thị ở cuối tên file để che giấu phần mở rộng | `file.php .jpg`         |
- Vẫn còn rất nhiều cách khác để thực hiện kỹ thuật này ví dụ như ở [đây](https://book.hacktricks.xyz/pentesting-web/file-upload).

### Flawed validation of the file's contents
- Thay vì kiểm tra dựa trên các giá trị như `Content- Type` thì server có một số cách kiểm tra khác như là:
    - Kiểm tra kích thước và cấu trúc nội dung:
        - Ví dụ, khi server yêu cầu upload ảnh, nó có thể kiểm tra các thuộc tính của ảnh như kích thước hoặc độ phân giải. Nếu file không chứa thông tin về kích thước (ví dụ: file PHP), server có thể xác định rằng đây không phải là file ảnh và từ chối upload.
    - Kiểm tra Magic Bytes:
        - Một số loại file có các dãy byte đặc trưng (Magic Bytes) ở phần đầu hoặc cuối file giúp nhận diện loại file thật sự. Ví dụ:
            - JPEG luôn bắt đầu với byte `FF D8 FF`.
            - PNG bắt đầu với byte `89 50 4E 47`.
            - PDF bắt đầu với `%PDF`.
    - Xác thực chữ ký hoặc dấu hiệu đặc trưng:
        - Server có thể kiểm tra nội dung và dấu hiệu cụ thể của file để chắc chắn rằng file tuân thủ đúng định dạng mong đợi.
- Lợi dụng điều này ta hoàn toàn có thể điều chỉnh các request để by pass.
### Exploiting file upload race conditions
- **Exploiting File Upload Race Conditions** là một kỹ thuật tấn công khi kẻ tấn công lợi dụng race conditions (điều kiện tranh chấp) trong quá trình upload file để đánh lừa hệ thống thực hiện những hành vi không mong muốn.
- **Race condition** là một lỗi xảy ra khi hai hoặc nhiều tiến trình hoặc thao tác truy cập và thao tác trên cùng một tài nguyên (như file hoặc dữ liệu) đồng thời mà không có sự đồng bộ hóa. Kết quả của race condition là hệ thống có thể không xử lý tài nguyên theo cách dự kiến, tạo ra các lỗ hổng bảo mật.
- Trong trường hợp upload file, race condition có thể xuất hiện khi:
    - Hệ thống upload file lên server và thực hiện kiểm tra loại file, kích thước, hoặc nội dung file để đảm bảo rằng file an toàn.
    - Tuy nhiên, do việc kiểm tra và lưu file không diễn ra đồng bộ, kẻ tấn công có thể thay thế file hợp lệ bằng một file độc hại trong khoảng thời gian ngắn giữa kiểm tra và lưu trữ.
- Cách thức by pass:
    - Tải lên file hợp lệ: Kẻ tấn công bắt đầu tải lên một file hợp lệ (ví dụ: file .jpg) để vượt qua bước kiểm tra.
    - Thay thế bằng file độc hại: Trong khi hệ thống đang kiểm tra file hợp lệ, kẻ tấn công đồng thời mở một kết nối khác để thay thế file hợp lệ bằng file chứa mã độc (ví dụ: file .php hoặc .js).
    - Thực thi mã độc: Nếu thành công, file chứa mã độc sẽ được lưu trữ và có thể được thực thi trên server.
- Ví Dụ
    - Giả sử hệ thống cho phép upload ảnh hồ sơ người dùng và kiểm tra file upload có đúng định dạng .jpg hay không. Nếu hệ thống không có đồng bộ hóa (synchronization), kẻ tấn công có thể:
    - Bắt đầu tải lên một file .jpg hợp lệ.
    - Đồng thời mở một kết nối khác để thay thế file .jpg với một file .php chứa mã độc ngay sau khi hệ thống kiểm tra xong nhưng chưa kịp lưu trữ.
    - File độc hại .php sẽ được lưu trữ trên server dưới dạng file ảnh nhưng có thể được thực thi như mã PHP.

#### Race conditions in URL-based file uploads
- Đây là một lỗ hổng bảo mật xảy ra khi ứng dụng cho phép người dùng tải file lên server thông qua `URL` thay vì trực tiếp từ máy tính của họ. Khi đó, server sẽ tải file từ `URL` được cung cấp và lưu nó trên hệ thống. **Race condition** xảy ra khi có thể can thiệp vào quá trình tải file này bằng cách thay đổi nội dung của file tại `URL` hoặc chuyển hướng `URL` để trỏ đến file độc hại ngay trước khi server lưu file.
- Cách by pass:
    - Người dùng cung cấp `URL` hợp lệ: Kẻ tấn công cung cấp một `URL` trỏ đến file hợp lệ (ví dụ: một file ảnh hợp lệ) để tải lên.
    - Tấn công race condition: Trong khoảng thời gian server đang tải file từ `URL` và kiểm tra tính hợp lệ của file, kẻ tấn công can thiệp vào `URL` gốc bằng cách:
        - Chuyển hướng `URL`: Thay đổi `URL` để trỏ đến một file độc hại khác, ví dụ như một file PHP hoặc mã độc.
        - Thay thế nội dung file tại `URL`: Cập nhật nội dung file tại `URL` để biến file hợp lệ thành một file chứa mã độc hoặc một script.
    - Server lưu file độc hại: Nếu server không kiểm tra lại file sau khi tải hoặc không đồng bộ hóa quá trình tải và lưu, file độc hại sẽ được lưu trên server và có thể thực thi mã độc.
- Ví dụ:
- Giả sử server cho phép người dùng upload ảnh thông qua `URL`, và ứng dụng tải ảnh từ `URL` và lưu lại trong thư mục của server.

    - Kẻ tấn công cung cấp `URL` trỏ đến một file ảnh hợp lệ: `http://example.com/profile.jpg`.
    - Khi server đang trong quá trình tải file từ `URL`, kẻ tấn công thay đổi profile.jpg tại` http://example.com` để trỏ đến một file PHP chứa mã độc, hoặc chuyển hướng `URL` tới một file độc hại khác.
    - Nếu server không kiểm tra nội dung file sau khi tải về, file độc hại sẽ được lưu và có thể được thực thi.

## Exploiting file upload vulnerabilities without remote code execution

