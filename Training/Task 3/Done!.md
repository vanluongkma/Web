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

# LV5

![image](https://github.com/user-attachments/assets/c49a6ece-8c02-42a8-ac97-0e5490a0bdb0)
- Ở đây mình có khá nhiều file. Do nội dung ít và mình biết pass như thế nào nên mình có thể `cat ./*` để cat toàn bộ file.

![image](https://github.com/user-attachments/assets/9707cf6d-6bda-404e-addc-7bdfdfe85613)

- Tuy nhiên ta có thể làm như sau:

![image](https://github.com/user-attachments/assets/3edc2fb4-82b7-4001-9ea2-5b74f4cde0f0)

> Pass: 4oQYVPkxZOOEOO5pTW81FB8j8lxXGUQw

# LV6

![image](https://github.com/user-attachments/assets/bf0643d9-0231-4392-9100-88d193e54ddd)

- Ta tìm kiếm theo yêu cầu.

![image](https://github.com/user-attachments/assets/723f5270-63df-4510-a530-cc54ab2f56a6)

> Pass: HWasnPhtq9AVKe0dmk45nxy20cvUa6EG

# LV7

![image](https://github.com/user-attachments/assets/6edd6f39-315a-40b2-a153-a102d422132f)
-Tương tự lv6.

![image](https://github.com/user-attachments/assets/65fa6b8d-35fb-4535-924d-4fb207ef54ab)
> Pass: morbNTDkSW6jIlUc0ymOdMaLnOlFVAaj
# LV8
![image](https://github.com/user-attachments/assets/35a3577a-1246-4010-b265-e8699d18bfcb)
- strings | grep thoi.
![image](https://github.com/user-attachments/assets/2b747e4f-9307-4c5a-bdb2-74a3f92d7f90)
> Pass: dfwvzFQi4mU0wfNbFOe9RoWskMLg7eEc