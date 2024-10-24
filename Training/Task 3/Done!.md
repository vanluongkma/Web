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

![image](https://github.com/user-attachments/assets/43b80244-35ca-4e9e-bae1-d485b5614a37)
- Ở lv này ta nhận được 1 file private key của RSA. Lv này không có key hay key chính là file private đó.

![image](https://github.com/user-attachments/assets/9edbd4fd-5113-41c0-9ae8-cd2dabe898ee)
- Tuy nhiên ta cần thay đổi quyền thực thi bằng chmod.
> chmod 700 sshkey.private

- Sau đó ssh lại với ssh.private.
- Join thành công lv 15.

# LV15 
![image](https://github.com/user-attachments/assets/44d60393-57ef-4dff-99ca-32e354c9f5d5)
- Ở LV14 ta đã join được vào lv này.
- Cat pass ở đường dẫn được cung cấp.

![image](https://github.com/user-attachments/assets/0705c241-bd42-4a10-ba17-d0043199d67e)
![image](https://github.com/user-attachments/assets/2eebf09a-fba3-49cc-8c65-8da20ed80b58)
> Pass: 8xCjnmgoKbGLhHFAZlGE5Tmu4M2tKJQo

# LV16

![image](https://github.com/user-attachments/assets/6a392d82-437d-47a6-bd2a-ccd917ca4e54)
> openssl s_client -connect localhost:30001
- Nhập pass lv15.

![image](https://github.com/user-attachments/assets/1aea2de4-8ed2-4753-b097-5360806f5e72)
> Pass: kSkvUpMQ7lBYyCM4GBPvCvT1BfWRy0Dx

# LV17

![image](https://github.com/user-attachments/assets/7a58228a-861a-4c5e-be76-d5ed23fc1c94)

- Sử dụng `nmap` để rò.
> nmap -p- -A <host>

![image](https://github.com/user-attachments/assets/9f8f503c-cf08-41b3-a04d-2a73c15a4971)

- Có 2 cổng xài ssl là `31518` và `31790`.
- Thử từng cổng.
> openssl s_client -ign_eof -connect localhost:31518
> openssl s_client -ign_eof -connect localhost:31790

![image](https://github.com/user-attachments/assets/ecb26fce-d3c9-446c-9d9d-785703bd8228)

- Tương tự ta lại có privatekey.
- Lưu lại để join lv kế.

# LV18
```bash
bandit17@bandit:~$ ls
passwords.new  passwords.old
bandit17@bandit:~$ diff passwords.old passwords.new
42c42
< ktfgBvpMzWKR5ENj26IbLGSblgUG9CzB
---
> x2gLTTjFwMOhQ8oWNbMN362QKxfRqGlO
bandit17@bandit:~$ sort passwords.old passwords.new | uniq -u
ktfgBvpMzWKR5ENj26IbLGSblgUG9CzB
x2gLTTjFwMOhQ8oWNbMN362QKxfRqGlO
bandit17@bandit:~$ cat passwords.new | grep ktfgBvpMzWKR5ENj26IbLGSblgUG9CzB
bandit17@bandit:~$ cat passwords.new | grep x2gLTTjFwMOhQ8oWNbMN362QKxfRqGlO
x2gLTTjFwMOhQ8oWNbMN362QKxfRqGlO
```
> Pass: x2gLTTjFwMOhQ8oWNbMN362QKxfRqGlO

# LV19 
- The password for the next level is stored in a file readme in the homedirectory. Unfortunately, someone has modified .bashrc to log you out when you log in with SSH.

- Use command::
> ssh bandit18@bandit.labs.overthewire.org -p 2220 ls 

```bash
caycon@CayCon:~$ ssh bandit18@bandit.labs.overthewire.org -p 2220 ls
                         _                     _ _ _
                        | |__   __ _ _ __   __| (_) |_
                        | '_ \ / _` | '_ \ / _` | | __|
                        | |_) | (_| | | | | (_| | | |_
                        |_.__/ \__,_|_| |_|\__,_|_|\__|


                      This is an OverTheWire game server.
            More information on http://www.overthewire.org/wargames

bandit18@bandit.labs.overthewire.org's password:
readme
caycon@CayCon:~$ ssh bandit18@bandit.labs.overthewire.org -p 2220 cat readme
                         _                     _ _ _
                        | |__   __ _ _ __   __| (_) |_
                        | '_ \ / _` | '_ \ / _` | | __|
                        | |_) | (_| | | | | (_| | | |_
                        |_.__/ \__,_|_| |_|\__,_|_|\__|


                      This is an OverTheWire game server.
            More information on http://www.overthewire.org/wargames

bandit18@bandit.labs.overthewire.org's password:
cGWpMaKXVwDUNgPAVJbWYuGHVn9zl3j8
```

> Pass: cGWpMaKXVwDUNgPAVJbWYuGHVn9zl3j8

# LV20
- To gain access to the next level, you should use the setuid binary in the homedirectory. Execute it without arguments to find out how to use it. The password for this level can be found in the usual place (/etc/bandit_pass), after you have used the setuid binary.

```bash
bandit19@bandit:~$ ls -la
total 36
drwxr-xr-x  2 root     root      4096 Sep 19 07:08 .
drwxr-xr-x 70 root     root      4096 Sep 19 07:09 ..
-rwsr-x---  1 bandit20 bandit19 14880 Sep 19 07:08 bandit20-do
-rw-r--r--  1 root     root       220 Mar 31  2024 .bash_logout
-rw-r--r--  1 root     root      3771 Mar 31  2024 .bashrc
-rw-r--r--  1 root     root       807 Mar 31  2024 .profile
bandit19@bandit:~$ ./bandit20-do
Run a command as another user.
  Example: ./bandit20-do id
bandit19@bandit:~$ ./bandit20-do ls /etc/bandit_pass
bandit0   bandit11  bandit14  bandit17  bandit2   bandit22  bandit25  bandit28  bandit30  bandit33  bandit6  bandit9
bandit1   bandit12  bandit15  bandit18  bandit20  bandit23  bandit26  bandit29  bandit31  bandit4   bandit7
bandit10  bandit13  bandit16  bandit19  bandit21  bandit24  bandit27  bandit3   bandit32  bandit5   bandit8
bandit19@bandit:~$ ./bandit20-do cat /etc/bandit_pass/bandit20
0qXahG8ZjOVMN9Ghs7iOWsCfZyXOUbYO
bandit19@bandit:~$
```
> Pass: 0qXahG8ZjOVMN9Ghs7iOWsCfZyXOUbYO

# LV21 
- There is a setuid binary in the homedirectory that does the following: it makes a connection to localhost on the port you specify as a commandline argument. It then reads a line of text from the connection and compares it to the password in the previous level (bandit20). If the password is correct, it will transmit the password for the next level (bandit21).
```bash 
bandit20@bandit:~$ echo -n '0qXahG8ZjOVMN9Ghs7iOWsCfZyXOUbYO' | nc -l -p 1234 &
[1] 2222041
bandit20@bandit:~$ ./suconnect 1234
Read: 0qXahG8ZjOVMN9Ghs7iOWsCfZyXOUbYO
Password matches, sending next password
EeoULMCra2q0dSkYj561DX7s1CpBuOBt
bandit20@bandit:~$
```
> Pass: EeoULMCra2q0dSkYj561DX7s1CpBuOBt

# LV22
- A program is running automatically at regular intervals from cron, the time-based job scheduler. Look in /etc/cron.d/ for the configuration and see what command is being executed.
```bash 
bandit21@bandit:~$ cat /usr/bin/cronjob_bandit22.sh
#!/bin/bash
chmod 644 /tmp/t7O6lds9S0RqQh9aMcz6ShpAoZKF7fgv
cat /etc/bandit_pass/bandit22 > /tmp/t7O6lds9S0RqQh9aMcz6ShpAoZKF7fgv
bandit21@bandit:~$ cat /tmp/t7O6lds9S0RqQh9aMcz6ShpAoZKF7fgv
tRae0UfB9v0UzbCdn9cY0gQnds9GF58Q
bandit21@bandit:~$
```
> Pass: tRae0UfB9v0UzbCdn9cY0gQnds9GF58Q

# LV23
- A program is running automatically at regular intervals from cron, the time-based job scheduler. Look in /etc/cron.d/ for the configuration and see what command is being executed.
```bash
bandit22@bandit:~$ cat /usr/bin/cronjob_bandit23.sh
#!/bin/bash

myname=$(whoami)
mytarget=$(echo I am user $myname | md5sum | cut -d ' ' -f 1)

echo "Copying passwordfile /etc/bandit_pass/$myname to /tmp/$mytarget"

cat /etc/bandit_pass/$myname > /tmp/$mytarget
bandit22@bandit:~$ echo I am user bandit23 | md5sum | cut -d ' ' -f 1
8ca319486bfbbc3663ea0fbe81326349
bandit22@bandit:~$ cat /tmp/8ca319486bfbbc3663ea0fbe81326349
0Zf11ioIjMVN551jX3CmStKLYqjk54Ga
bandit22@bandit:~$
```
> Pass: 0Zf11ioIjMVN551jX3CmStKLYqjk54Ga

# LV24
- A program is running automatically at regular intervals from cron, the time-based job scheduler. Look in /etc/cron.d/ for the configuration and see what command is being executed.

> Pass: gb8KRRCsshuZXI0tUuR6ypOFjiZbf3G8

# LV25 
- A daemon is listening on port 30002 and will give you the password for bandit25 if given the password for bandit24 and a secret numeric 4-digit pincode. There is no way to retrieve the pincode except by going through all of the 10000 combinations, called brute-forcing.
- Run code: 
```bash 
for i in {0000..9999}; 
do 
	echo "gb8KRRCsshuZXI0tUuR6ypOFjiZbf3G8 $i"; 
done | nc localhost 30002
```

![image](https://github.com/user-attachments/assets/74f04dd4-20bc-4644-85a0-5f269d2adac3)
> Pass: iCi86ttT4KSNe1armKiwbQNmB3YJP3q4