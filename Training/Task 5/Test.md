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
- Ta tạo một file php và upload thử