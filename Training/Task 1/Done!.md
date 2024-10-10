## The HTTP Protocol.
- **HTTP** hay **HyperText Transfer Protocol** là một giao thức truyền tải siêu văn bản, là nền tảng của `World Wide Web`. Nó cho phép các máy tính (`client`) giao tiếp với nhau qua mạng để truy cập và hiển thị các tài nguyên web như trang web, hình ảnh, video,...
- Nếu không có `HTTP`, `World Wide Web` như chúng ta biết ngày nay sẽ không tồn tại. HTTP là giao thức cho phép truyền dữ liệu qua internet, cho phép người dùng truy cập các trang web và các tài nguyên trực tuyến khác.
- **Cách thức hoạt động:** khi gõ một địa chỉ web vào trình duyệt, trình duyệt sẽ gửi một yêu cầu (`request`) đến máy chủ (`server`) chứa tài nguyên đó thông qua giao thức **HTTP**. Máy chủ sẽ xử lý yêu cầu và gửi lại một phản hồi (`response`) chứa dữ liệu cần thiết. Trình duyệt sẽ nhận phản hồi và hiển thị nội dung lên màn hình.
- Chi tiết hơn thì HTTP hoạt động như sau:
    - HTTP hoạt động dựa trên mô hình khách-chủ.
        - **Client-Server:** 
            - `Client`: Thường là trình duyệt web, gửi yêu cầu đến máy chủ.
            - `Server`: Máy tính lưu trữ các tài nguyên web, nhận yêu cầu và trả về kết quả.
    - Giao tiếp diễn ra qua các cặp yêu cầu và phản hồi:
        - **Requests-Responses** 
            - `Requests` client gửi một yêu cầu đến server, có thể bao gồm:
                - Phương thức: GET, POST, PUT, DELETE, ... (mỗi phương thức có tác động khác nhau đến tài nguyên)
                - URL: Địa chỉ tài nguyên cần truy cập
                - Header: Thông tin bổ sung về yêu cầu
            - `Responses` server xử lý yêu cầu và gửi lại một phản hồi, bao gồm:
                - Status code: Mã trạng thái cho biết kết quả của yêu cầu (ví dụ: 200 OK, 404 Not Found)
                - Header: Thông tin bổ sung về phản hồi
                - Body: Dữ liệu được yêu cầu
    - Ví dụ:
        - Ta nhập địa chỉ trang web: https://www.youtube.com vào trình duyệt.
        - Trình duyệt sẽ gửi request HTTP GET đến máy chủ.
        - Máy chủ sẽ tìm kiếm trang chủ và gửi response chứa mã HTML của trang về trình duyệt.
        - Trình duyệt nhận được mã HTML và hiển thị nội dung trang lên màn hình của bạn.
    - Sơ đồ hoạt động:
![image](https://github.com/user-attachments/assets/00e8852b-d58c-471b-b856-47ebe571031f)
- HTTP tồn tại nhiều ưu và nhược điểm khác nhau:
    - Ưu điểm:
        - Đơn giản và dễ sử dụng: Cấu trúc của HTTP tương đối đơn giản, dễ hiểu và triển khai, giúp các lập trình viên dễ dàng tích hợp vào các ứng dụng của mình.
        - Phổ biến và được hỗ trợ rộng rãi: HTTP được hầu hết các trình duyệt web và máy chủ web hỗ trợ, đảm bảo tính tương thích cao.
        - Linh hoạt: HTTP có thể được sử dụng để truyền tải nhiều loại dữ liệu khác nhau, từ văn bản đến hình ảnh, video, và các loại file khác.
        - Mở và không độc quyền: HTTP là một giao thức mở, không thuộc về bất kỳ tổ chức nào, giúp giảm chi phí và tăng tính cạnh tranh.
    - Nhược điểm:
        - Không bảo mật: HTTP truyền dữ liệu dưới dạng văn bản thuần túy, không được mã hóa, dễ bị nghe lén và đánh cắp thông tin.
        - Không đảm bảo tính toàn vẹn của dữ liệu: Dữ liệu truyền qua HTTP có thể bị thay đổi hoặc làm hỏng trong quá trình truyền tải.
        - Không có cơ chế xác thực: HTTP không có cơ chế xác thực mạnh mẽ, dẫn đến nguy cơ giả mạo.
        - Stateless: HTTP là một giao thức không trạng thái, nghĩa là mỗi yêu cầu đều độc lập và server không lưu trữ thông tin về các yêu cầu trước đó. Điều này có thể dẫn đến việc phải truyền đi nhiều thông tin trùng lặp.

## HTTP Requests.
- **HTTP Requests** hiểu đơn giản như là yêu cầu của `client` gửi lên `server`. Khi đó `server` có nhiệm vụ tìm và xử lý các loại dữ liệu, thông tin, client mong muốn.
- Ta có cấu trúc 1 http request cơ bản như sau:

![image](https://github.com/user-attachments/assets/6f3c9686-c8dd-4007-afd4-7e7825c7209f)
- **Requests line** có cấu trúc như sau: `Request Method - Request URI - HTTP-version`
    - **Request Method:** là yêu cầu của đoạn message, ví dụ : GET, POST, HEAD, OPTIONS.....
    - **Request URI:** là đường dẫn yêu cầu gửi đến. Ví dụ: /doc/test.html
    - **HTTP-version:** phiên bản HTTP. Bây giờ phiên bản thông dụng nhất là "HTTP/1.1"

- Các dòng còn lại từ dòng thứ 2 trở đi của **Request Message** là các **Request Header** bổ sung cho request đó. Ví dụ: Host, User-Agent, Cookie, Accept, Content-Type ...
- **Request header** giúp client có thể gửi yêu cầu lên server. Mỗi yêu cầu sẽ kèm theo các thông số, và các thông số đó được gọi là Header Parameters. Trình duyệt và server sẽ dựa vào các thông số header này để trả dữ liệu và hiển thị dữ liệu cho phù hợp.Tương tự một HTTP Request, header sẽ phân biệt chữ thường và chữ hoa, theo sau đó là dấu “.” và một giá trị.Các thông số mà các bạn có thể gặp khá thường xuyên như:
    - **User-Agent:** cho phép server xác định ứng dụng, hệ điều hành, nhà cung cấp và phiên bản.
    - **Connection:** kiểm soát kết nối mạng. Nói cách khác, cho phép dừng hoặc tiếp tục kết nối sau khi server thực hiện xong yêu cầu.
    - **Cache-Control:** chỉ định chính sách bộ nhớ đệm của trình duyệt.
    - **Accept-Language:** cho biết tất cả các ngôn ngữ (tự nhiên) mà client có thể hiểu được.
- **Request body** cho phép client gừi đến yêu cầu bổ sung cần server thực hiện như: tạo mới hoặc cập nhật dữ liệu mà không thể truyền trên Header Parameters.Thường được sử dụng trong các phương thức Post, Put, Patch.

## HTTP Responses
- Tương tự **HTTP Requests**, **HTTP Responses** cũng là một **HTTP Message**.
