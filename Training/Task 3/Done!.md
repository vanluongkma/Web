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

| Lệnh    | Mô tả                                                                 | Ví dụ                                                                 |
|---------|-----------------------------------------------------------------------|-----------------------------------------------------------------------|
| `grep`  | Tìm kiếm một chuỗi hoặc mẫu trong tệp.                                | `grep "password" file.txt` tìm chuỗi "password" trong `file.txt`.      |
| `sort`  | Sắp xếp các dòng trong tệp hoặc đầu vào.                              | `sort file.txt` sắp xếp các dòng trong `file.txt`.                    |
| `uniq`  | Loại bỏ các dòng trùng lặp (thường sử dụng với `sort`).                | `uniq -u file.txt` hiển thị các dòng chỉ xuất hiện một lần.           |
| `strings` | Hiển thị các chuỗi có thể đọc được trong tệp nhị phân.              | `strings binaryfile` hiển thị các chuỗi văn bản trong tệp nhị phân.   |
| `base64`| Mã hóa hoặc giải mã dữ liệu theo định dạng base64.                     | `echo "hello" | base64` mã hóa "hello" thành base64.                  |
| `tr`    | Dịch hoặc xóa các ký tự từ đầu vào tiêu chuẩn.                         | `echo "hello" | tr 'a-z' 'A-Z'` chuyển chữ thường thành chữ hoa.       |
| `tar`   | Lưu trữ nhiều tệp vào một tệp nén (thường dùng với `gzip`).            | `tar -cvf archive.tar file1 file2` tạo tệp lưu trữ `archive.tar`.     |
| `gzip`  | Nén tệp bằng thuật toán gzip.                                          | `gzip file.txt` nén tệp `file.txt` thành `file.txt.gz`.               |
| `bzip2` | Nén tệp bằng thuật toán bzip2.                                         | `bzip2 file.txt` nén tệp `file.txt` thành `file.txt.bz2`.             |
| `xxd`   | Chuyển đổi tệp thành định dạng hex hoặc ngược lại.                     | `xxd file.txt` hiển thị nội dung của `file.txt` dưới dạng hex.        |

# LV9
![image](https://github.com/user-attachments/assets/7ee60bab-36fe-4007-9f85-24dee77781b3)
- Sort duy nhất là được.

![image](https://github.com/user-attachments/assets/39d408df-5c7c-4c30-bb30-6908ab50dfc0)
> Pass: 4CKMh1JI91bUIZZPXDqGanal4xvAg0JM

# LV10
![image](https://github.com/user-attachments/assets/1ab31849-07ad-43c8-8e56-4b791a3baee0)
- grep =

![image](https://github.com/user-attachments/assets/d8433efb-a379-44a1-9aa9-4a9a74e84393)
> Pass: FGUW5ilLVJrxX9kMYMmlN4MgbpfMiqey

# LV11
![image](https://github.com/user-attachments/assets/192d3ea3-ba23-4c1a-a279-a392b148cea9)

- Decode base64.

![image](https://github.com/user-attachments/assets/c21bfa70-7478-4ac1-9199-32439a03fad3)
> Pass: dtR173fZKb0RRsDFSGsg2RWnpNVj3qRr

# LV12
![image](https://github.com/user-attachments/assets/55ab388b-b19b-4cfc-a6eb-e55a49215417)

- ROT 13.

![image](https://github.com/user-attachments/assets/f87b5308-3dbc-4654-bcb7-fd494bb8a99e)
> Pass: 7x16WNeHIi5YkIhWsfFIqoognUTyj9Q4

- Decode bên ngoài cho dễ nha:)))) ([link](https://kt.gy/tools.html#conv/)).

# LV13
![image](https://github.com/user-attachments/assets/e1e453a8-9a4b-4e2a-94cc-6696f7d077eb)

- Tạo file và di chuyển.

![image](https://github.com/user-attachments/assets/9f9053b8-c45e-43ad-8230-cde74630b162)
- Revert hexdump: ` xxd -r hexdump_data zip`
- Unzip: `

```bash
bandit12@bandit:/tmp/tmp.w5z9YoI2Yt$ xxd -r hexdump_data zip
bandit12@bandit:/tmp/tmp.w5z9YoI2Yt$ mv zip tar.gz
bandit12@bandit:/tmp/tmp.w5z9YoI2Yt$ ls
hexdump_data  tar.gz
bandit12@bandit:/tmp/tmp.w5z9YoI2Yt$ gzip -d tar.gz
bandit12@bandit:/tmp/tmp.w5z9YoI2Yt$ ls
hexdump_data  tar
bandit12@bandit:/tmp/tmp.w5z9YoI2Yt$ mv tar bzip2.bz2
bandit12@bandit:/tmp/tmp.w5z9YoI2Yt$ lls
Command 'lls' not found, but there are 16 similar ones.
bandit12@bandit:/tmp/tmp.w5z9YoI2Yt$ ls
bzip2.bz2  hexdump_data
bandit12@bandit:/tmp/tmp.w5z9YoI2Yt$ bzip2 -d bzip2.bz2
bandit12@bandit:/tmp/tmp.w5z9YoI2Yt$ ls
bzip2  hexdump_data
bandit12@bandit:/tmp/tmp.w5z9YoI2Yt$ mv bzip2 gzip.gz
bandit12@bandit:/tmp/tmp.w5z9YoI2Yt$ gzip -d gzip.gz
bandit12@bandit:/tmp/tmp.w5z9YoI2Yt$ ls
gzip  hexdump_data
bandit12@bandit:/tmp/tmp.w5z9YoI2Yt$ mv gzip tar.tar
bandit12@bandit:/tmp/tmp.w5z9YoI2Yt$ tar -xf tar.tar
bandit12@bandit:/tmp/tmp.w5z9YoI2Yt$ ls
data5.bin  hexdump_data  tar.tar
bandit12@bandit:/tmp/tmp.w5z9YoI2Yt$ tar -xf data5.bin
bandit12@bandit:/tmp/tmp.w5z9YoI2Yt$ ls
data5.bin  data6.bin  hexdump_data  tar.tar
bandit12@bandit:/tmp/tmp.w5z9YoI2Yt$ tar -xf data6.bin
bandit12@bandit:/tmp/tmp.w5z9YoI2Yt$ ls
data5.bin  data6.bin  data8.bin  hexdump_data  tar.tar
bandit12@bandit:/tmp/tmp.w5z9YoI2Yt$ tar -xf data7.bin
tar: data7.bin: Cannot open: No such file or directory
tar: Error is not recoverable: exiting now
bandit12@bandit:/tmp/tmp.w5z9YoI2Yt$ tar -xf data8.bin
bandit12@bandit:/tmp/tmp.w5z9YoI2Yt$ ls
data5.bin  data6.bin  data8.bin  hexdump_data  tar.tar
bandit12@bandit:/tmp/tmp.w5z9YoI2Yt$ tar -xf data6.bin
bandit12@bandit:/tmp/tmp.w5z9YoI2Yt$ ls
data5.bin  data6.bin  data8.bin  hexdump_data  tar.tar
bandit12@bandit:/tmp/tmp.w5z9YoI2Yt$ tar -xf data6.bin.out
tar: data6.bin.out: Cannot open: No such file or directory
tar: Error is not recoverable: exiting now
bandit12@bandit:/tmp/tmp.w5z9YoI2Yt$ bzip2 -d data6.bin
bzip2: Can't guess original name for data6.bin -- using data6.bin.out
bandit12@bandit:/tmp/tmp.w5z9YoI2Yt$ tar -xf data6.bin.out
bandit12@bandit:/tmp/tmp.w5z9YoI2Yt$ xxd data8.bin
00000000: 1f8b 0808 dfcd eb66 0203 6461 7461 392e  .......f..data9.
00000010: 6269 6e00 0bc9 4855 2848 2c2e 2ecf 2f4a  bin...HU(H,.../J
00000020: 51c8 2c56 70f3 374d 2977 2b4e 3648 4e4a  Q.,Vp.7M)w+N6HNJ
00000030: f4cc f430 c8b0 f032 4a0d cd2e 362a 4b09  ...0...2J...6*K.
00000040: 7129 77cc e302 003e de32 4131 0000 00    q)w....>.2A1...
bandit12@bandit:/tmp/tmp.w5z9YoI2Yt$ mv data8.bin data8.gz
bandit12@bandit:/tmp/tmp.w5z9YoI2Yt$ gzip -d data8.gz
bandit12@bandit:/tmp/tmp.w5z9YoI2Yt$ cat data8
The password is FO5dwFsc0cbaIiH0h8J2eUks2vdTDwAn
bandit12@bandit:/tmp/tmp.w5z9YoI2Yt$
```

> Pass: FO5dwFsc0cbaIiH0h8J2eUks2vdTDwAn

# LV14
![image](https://github.com/user-attachments/assets/150a07aa-693e-4cfc-8895-3dd44f05a277)