# LV0
- **ssh** vào server.
![image](https://github.com/user-attachments/assets/802c56c3-41dd-44c1-b8d8-848eaafdf749)
- command theo form:
> ssh <username>@<server> -p <port>
- Vậy ta có: 
> ssh bandit0@bandit.labs.overthewire.org -p 2220
- Pass: `bandit0`.
# LV1
![image](https://github.com/user-attachments/assets/97d992d0-8564-4594-b1bb-8191457cd0f4)
- ls và cat flag thôi.

![image](https://github.com/user-attachments/assets/e4985ec3-1100-4393-b5bd-2596bde0b107)

> Pass: ZjLjTmM6FvvyRnrb2rfNWOZOTa6ip5If

| Lệnh  | Mô tả | Ví dụ |
|-------|-------|-------|
| `ls`  | Hiển thị danh sách các tệp và thư mục trong thư mục hiện tại. | `ls -l` hiển thị danh sách chi tiết. |
| `cd`  | Thay đổi thư mục hiện tại. | `cd /home/user` chuyển đến thư mục `/home/user`. |
| `cat` | Hiển thị nội dung của một hoặc nhiều tệp. | `cat file.txt` hiển thị nội dung của tệp `file.txt`. |
| `file`| Xác định loại tệp. | `file file.txt` xác định loại tệp `file.txt`. |
| `du`  | Hiển thị dung lượng ổ đĩa sử dụng bởi các thư mục hoặc tệp. | `du -h` hiển thị dung lượng theo cách dễ đọc. |
| `find`| Tìm kiếm tệp hoặc thư mục dựa trên các tiêu chí. | `find /home -name "*.txt"` tìm các tệp `.txt` trong `/home`. |

# LV2
![image](https://github.com/user-attachments/assets/3b394920-bbd0-4518-9057-72a958333836)

> ssh bandit1@bandit.labs.overthewire.org -p 2220
- ls và thấy file `-`, ta không thể đọc bằng command `cat -`, nên dùng `cat ./-`.

![image](https://github.com/user-attachments/assets/6ecce5ce-7f15-4a10-b7a4-f795102cf09e)
> Pass: 263JGJPfgU6LtdEvgfWU1XP5yac29mFx

# LV3

![image](https://github.com/user-attachments/assets/06e572a2-b1e3-4852-879e-15ae4321b634)

- ls, cat file thôi (dùng tab cho lẹ nha).

![image](https://github.com/user-attachments/assets/001aa1d6-0b5e-4651-8b4f-b2e6878e2c66)

> Pass: MNk8KNH3Usiio41PRUEoDFPqfxLPlSmx

# LV4

![image](https://github.com/user-attachments/assets/dad9608e-9ed1-4fdd-93ee-28c5ad814cf2)

- ls file ẩn bằng `ls -a`.

![image](https://github.com/user-attachments/assets/f530e1fd-dc47-44ed-934f-37ff4b37ef88)

> Pass: 2WmrDFRmJIq3IPxneAaMGhap0pFhF3NJ