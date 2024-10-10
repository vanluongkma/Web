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

## HTTP Responses.
- Tương tự **HTTP Requests**, **HTTP Responses** cũng là một **HTTP Message**.
- **HTTP Responses** là kết quả mà server trả về khi ta gửi thành công 1 request.
- Ta có cấu trúc 1 http response cơ bản như sau:

![image](https://github.com/user-attachments/assets/94a41f8d-3013-4928-b95f-5a03a71df3de)
- Như ta thấy dòng đầu của `HTTP Response` là `Status Line` hay dòng trạng thái. Dòng này có cấu trúc như sau: **HTTP-version  - Status Code - Reason Phrase**.
    - **HTTP-version:** Phiên bản HTTP. Bây giờ phiên bản thông dụng nhất là "HTTP/1.1".
    - **Status Code:** Mã phản hồi tiêu chuẩn do máy chủ gửi về. Ví dụ: 200, 301, 500...
    - **Reason Phrase:** Giải thích ngắn gọn về mã phản hồi do máy chủ gửi về.
- Các dòng còn lại là các **Respone Header** bổ sung như:
    - **Content-Type.**
    - **Content-Length.**
    - **Connection: Keep-Alive.**

## HTTP Methods.
- **HTTP Methods** là phương thức mà client gửi request đến server.
- Có một số `HTTP Methods` như sau:

| Phương thức | Mô tả                                                                                                    | An toàn | Bất biến | Hiển thị | Có thể cache |
|------------|----------------------------------------------------------------------------------------------------------|---------|----------|----------|--------------|
| GET        | Lấy tài nguyên                                                                                             | Có      | Có       | Có       | Có          |
| HEAD       | Lấy các thông tin tiêu đề của tài nguyên                                                                    | Có      | Có       | Không     | Có          |
| POST       | Tạo một tài nguyên mới                                                                                     | Không   | Không    | Không     | Không       |
| PUT        | Cập nhật toàn bộ một tài nguyên                                                                             | Không   | Có       | Không     | Không       |
| PATCH      | Cập nhật một phần của tài nguyên                                                                            | Không   | Không    | Không     | Không       |
| DELETE     | Xóa một tài nguyên                                                                                       | Không   | Có       | Không     | Không       |
| OPTIONS    | Mô tả các phương thức HTTP được hỗ trợ bởi tài nguyên                                                     | Có      | Có       | Không     | Có          |
| CONNECT   | Thiết lập một kết nối tunnel đến server                                                                   | Không   | Không    | Không     | Không       |
| TRACE     | Trả về đường dẫn mà request đã đi qua                                                                       | Có      | Có       | Có       | Không       |

## URLs.

- **URL** hay **Uniform Resource Locator** còn gọi là địa chỉ trang web, là một chuỗi ký tự dùng để xác định vị trí của một tài nguyên trên Internet. Tài nguyên này có thể là một trang web, một hình ảnh, một video, hoặc bất kỳ tập tin nào khác có thể được truy cập qua mạng.
- Cấu trúc cơ bản của một URL:
    - **Scheme:** Giao thức truy cập (http, https, ftp, mailto, ...).
    - **Authority:** Phần xác định máy chủ (hostname, port).
    - **Path:** Đường dẫn đến tài nguyên.
    - **Query:** Tham số.
    - **Fragment:** Mỏ neo.
- Chi tiết hơn thì:
![image](https://github.com/user-attachments/assets/790d5ee3-c87a-4e07-8817-47ab645155af)

| Phần | Mô tả | Ví dụ |
|---|---|---|
| **Scheme** | Giao thức truyền thông sử dụng để truy cập tài nguyên. Thường gặp nhất là http (Hypertext Transfer Protocol) và https (Hypertext Transfer Protocol Secure). | http:// |
| **Authority** | Phần xác định máy chủ, bao gồm tên miền và có thể cả cổng. | www.example.com:80 |
|   - **Domain Name** | Tên miền của website. | www.example.com |
|   - **Port** | Cổng mà máy chủ lắng nghe. Nếu không có, cổng mặc định của giao thức sẽ được sử dụng (ví dụ: 80 cho http). | :80 |
| **Path** | Đường dẫn đến tài nguyên trên máy chủ. | /path/to/myfile.html |
| **Query** | Các tham số truyền thêm cho máy chủ, thường được sử dụng để truyền dữ liệu hoặc tùy chỉnh yêu cầu. | ?key1=value1&key2=value2 |
| **Fragment** | Phần mỏ neo, dùng để chỉ định một vị trí cụ thể trên trang. | #SomewhereInTheDocument |
- Vai trò của URL:
    - Xác định duy nhất: Mỗi tài nguyên trên Internet có một URL duy nhất.
    - Dễ nhớ: URL thường được thiết kế để dễ nhớ và liên quan đến nội dung của trang.
    - Truy cập trực tiếp: Bạn có thể nhập URL vào trình duyệt để truy cập trực tiếp đến tài nguyên.

## HTTP Headers
- **HTTP Headers** là những cặp tên-giá trị được gửi từ trình duyệt (hoặc bất kỳ client nào) đến máy chủ web để cung cấp thêm thông tin về yêu cầu và client. Chúng đóng vai trò quan trọng trong việc xác định cách máy chủ xử lý yêu cầu và gửi phản hồi phù hợp.
- Một số Request Headers phổ biến như:
    - **User-Agent:** Xác định trình duyệt hoặc ứng dụng đang gửi yêu cầu.
    - **Accept:** Chỉ định các loại nội dung mà client có thể chấp nhận.
    - **Content-Type**: Xác định loại nội dung của dữ liệu được gửi trong body của yêu cầu.
    - **Authorization:** Chứa thông tin xác thực, thường là token hoặc thông tin đăng nhập.
    - **Cookie:** Chứa các cookie được gửi từ máy chủ trong các yêu cầu trước đó.
    - **Referer:** Chỉ ra trang web đã giới thiệu yêu cầu hiện tại.
    - **If-Modified-Since:** Yêu cầu máy chủ chỉ gửi dữ liệu nếu nó đã được sửa đổi kể từ thời gian được chỉ định.
    - **Cache-Control:** Cung cấp các hướng dẫn về việc cache dữ liệu.

## Cookies.
- **Cookies** là những đoạn văn bản nhỏ được gửi từ một trang web đến trình duyệt của bạn và được lưu trữ trên thiết bị của bạn. Chúng giống như những "tấm thẻ nhớ" nhỏ, giúp các trang web nhớ thông tin về bạn và các hoạt động của bạn trên trang web đó.
- Có hai loại **Cookies** chính:
    - **First-party cookies:** Được tạo bởi trang web bạn đang truy cập.
    - **Third-party cookies:** Được tạo bởi các trang web khác, như công cụ phân tích hoặc quảng cáo, được nhúng vào trang web bạn đang truy cập.
- **Cookies** đùng để:
    - **Lưu trữ thông tin đăng nhập:** Giúp bạn không phải nhập lại mật khẩu mỗi khi truy cập trang web.
    - **Cá nhân hóa trải nghiệm người dùng:** Nhớ các cài đặt của bạn, như ngôn ngữ, font chữ, hoặc các sản phẩm bạn đã xem.
    - **Theo dõi hành vi người dùng:** Giúp các trang web hiểu rõ hơn về cách người dùng tương tác với trang web, từ đó cải thiện trải nghiệm người dùng và hiệu quả của quảng cáo.

## Status Codes.
- **Status Codes** là những **mã số** được trả về từ máy chủ web đến trình duyệt của bạn sau khi request được gửi đi. Chúng cung cấp thông tin về kết quả của yêu cầu đó, cho phép cả máy chủ và trình duyệt hiểu được tình trạng của yêu cầu.
- **Status Codes**được chia thành các nhóm theo chữ số đầu tiên, mỗi nhóm đại diện cho một loại phản hồi khác nhau:
    - **1xx (Thông báo):** Yêu cầu đã được nhận và đang được xử lý.
    - **2xx (Thành công):** Yêu cầu đã được thực hiện thành công. (ví dụ: **200 OK:** Yêu cầu đã được thực hiện thành công.)
    - **3xx (Chuyển hướng):** Để hoàn thành yêu cầu, trình duyệt cần thực hiện một hành động khác (ví dụ: **301 Moved Permanently:** Tài nguyên đã được chuyển đến một URL mới vĩnh viễn).
    - **4xx (Lỗi của Client):** Lỗi xảy ra do yêu cầu từ phía người dùng (ví dụ: **404 Not Found:** Tài nguyên không tìm thấy).
    - **5xx (Lỗi của Server):** Lỗi xảy ra do vấn đề ở phía máy chủ (ví dụ: **500 Internal Server Error:** Máy chủ gặp lỗi trong khi xử lý yêu cầu).

## HTTPS.
- **HTTPS** hay **HyperText Transfer Protocol Secure** là một phiên bản mở rộng của HTTP, giao thức truyền tải siêu văn bản được sử dụng rộng rãi trên Internet để truyền tải dữ liệu giữa máy chủ và trình duyệt. Thực chất, đây chính là giao thức **HTTP** nhưng tích hợp thêm **Chứng chỉ bảo mật SSL** nhằm mã hóa các thông điệp giao tiếp để tăng tính bảo mật. Có thể hiểu, **HTTPS** là phiên bản **HTTP** an toàn, bảo mật hơn.

| Tính năng | HTTP | HTTPS |
|---|---|---|
| **Ý nghĩa** | HyperText Transfer Protocol | HyperText Transfer Protocol Secure |
| **Mục đích** | Truyền tải dữ liệu trên web | Truyền tải dữ liệu trên web một cách **bảo mật** |
| **Mã hóa** | Không | Sử dụng SSL/TLS để mã hóa dữ liệu |
| **Xác thực** | Không xác thực danh tính máy chủ | Xác thực danh tính máy chủ bằng chứng chỉ SSL |
| **Toàn vẹn dữ liệu** | Không đảm bảo dữ liệu không bị thay đổi | Đảm bảo dữ liệu không bị thay đổi trong quá trình truyền |
| **Cổng mặc định** | 80 | 443 |
| **Bảo mật** | Thấp | Cao |
| **SEO** | Thấp hơn | Cao hơn |
| **Ví dụ URL** | http://www.example.com | https://www.example.com |
| **Sử dụng** | Các trang web thông thường | Các trang web yêu cầu bảo mật cao (ví dụ: ngân hàng, thương mại điện tử) |

## HTTP Proxy.
- **HTTP Proxy** là một máy chủ hoạt động như một **trung gian** giữa thiết bị của bạn (ví dụ: máy tính, điện thoại) và các máy chủ trên Internet. Khi bạn gửi một yêu cầu truy cập một trang web, thay vì trực tiếp kết nối đến máy chủ đó, yêu cầu của bạn sẽ được gửi đến máy chủ proxy trước. Máy chủ proxy sẽ xử lý yêu cầu này, sau đó mới chuyển tiếp đến máy chủ đích và trả kết quả về cho bạn.