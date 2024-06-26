# Cờ vua (Python)
Game cờ vua là một trò chơi chiến thuật hai người chơi trên một bảng 8x8 ô vuông, gồm các quân cờ khác nhau và mỗi quân có cách di chuyển riêng biệt. Mục tiêu của trò chơi là chiếu tướng (đưa vua của đối phương vào tình trạng bị tấn công không thể tránh khỏi).
Link github: https://github.com/lknkimngan/ChessGame.git
## Mô tả ứng dụng
* Bàn cờ có màu sắc truyền thống, thường là các ô đen và trắng xen kẽ. Bàn cờ gồm 32 quân cờ được chia đều cho hai bên: trắng và đen. Mỗi bên bao gồm các quân cờ sau đây:
  * 1 Vua: Quân vua có vai trò quan trọng nhất trong game. Mục tiêu của mỗi bên là bảo vệ vua của mình và đồng thời tấn công vua của đối phương.
  * 1 Hậu: Hậu là quân cờ mạnh nhất trong game. Nó có khả năng di chuyển trên các hàng, cột và đường chéo.
  * 2 Xe: Xe có thể di chuyển theo hàng hoặc cột, và nó là quân cờ mạnh khác trong game.
  * 2 Tượng: Tượng có thể di chuyển trên đường chéo và nó là một quân cờ quan trọng trong game.
  *	2 Mã: Mã có thể di chuyển theo hình chữ L. Nó có khả năng nhảy qua các quân cờ khác.
  *	8 Tốt: Tốt là quân cờ yếu nhất, nhưng nó có thể trở thành quân cờ mạnh hơn khi nó tiến đến phần còn lại của bảng.

* Bên cạnh đó, giao diện game cũng sẽ hiển thị về quân cờ của người chơi là quân nào, lượt đi của người chơi, thời gian từng người, thông báo chiến thắng, thông báo thua. Quy tắc để chiến thắng là khi người chơi bên quân nào hết thời gian trước thì bên đó sẽ thua. Ngoài ra, nếu trong quá trình chơi nếu bên nào nhấn nút “q” để thoát trước thì bên đó sẽ là người thua. Bên cạnh đó, bên nào bị chiếu bí trước sẽ là bên thua cuộc.
  
*  Bên cạnh đó, giao diện game cũng sẽ hiển thị về quân cờ của người chơi là quân nào, lượt đi của người chơi, thời gian từng người, thông báo chiến thắng, thông báo thua. Quy tắc để chiến thắng là khi người chơi bên quân nào hết thời gian trước thì bên đó sẽ thua. Ngoài ra, nếu trong quá trình chơi nếu bên nào nhấn nút “q” để thoát trước thì bên đó sẽ là người thua. Bên cạnh đó, bên nào bị chiếu bí trước sẽ là bên thua cuộc.
![alt text](img_readme/image-8.png)


## Yêu cầu
* Python 3 <= v3.10.10 (Download from https://www.python.org/downloads/)
## Cách cài đặt 
  
```bash
 $ git clone https://github.com/lknkimngan/ChessGame.git 
```
* Mở thư mục ChessGame mới cài đặt.
  ```bash
    $ python3 -m venv my_env
   $ .\my_env\Scripts\activate
  ```
## Thực thi chương trình
* Bước 1: Mở terminal và chạy lệnh: ip addr show để lấy địa chỉ IPv4 mà máy đang kết nối.
⇒ Địa chỉ IPv4 của máy sẽ nằm ở dòng inet 192.168.220.128

![alt text](img_readme/image.png)
* Bước 2: Lấy địa chỉ IP vừa lấy được sau đó dán địa chỉ này vào server = ‘192.168.220.128’ ở file server.py và dòng self.host = ‘192.168.220.128’ ở file client.py. (Địa chỉ IP này sẽ khác trên mỗi máy).
  ![alt text](img_readme/image-1.png)
![alt text](img_readme/image-2.png)
*Bước 3: Chạy file server.py. Sau đó, mở thêm 2 terminal khác chạy file game.py
![alt text](img_readme/image-3.png)
⇒ Sau khi chạy 3 terminal trên, ta được kết quả như sau. Sau đó click để chơi game.
![alt text](img_readme/image-4.png)
* Bước 4: Chơi game. Khi chơi, ta có thể thấy được đường đi trước đó của đối thủ được đánh dấu bằng vòng tròn màu xanh. Ngoài ra, ta có xem được thời gian chơi game của 2 người chơi. Nếu muốn thoát game, ta cần nhấn phím “q” để thoát game.
  ![alt text](img_readme/image-5.png)
![alt text](img_readme/image-6.png)
![alt text](img_readme/image-7.png)

## LICENSE
Giấy Phép MIT


Bản quyền (c) 2024 Nguyễn Thị Thu Hà, Lê Kim Ngân, Trương Thị Mai Trinh

Giấy phép được cấp miễn phí cho mọi người nhận được một bản sao của phần mềm này và các tệp tài liệu liên quan (sau đây gọi là "Phần Mềm"), để giao dịch trong Phần Mềm mà không bị ràng buộc, bao gồm mà không giới hạn các quyền
sử dụng, sao chép, sửa đổi, hợp nhất, xuất bản, phân phối, cấp phép con và/hoặc bán các bản sao của Phần Mềm, và cho phép người nhận được Phần Mềm thực hiện điều này, với các điều kiện sau đây:

Thông báo bản quyền trên và thông báo giấy phép này sẽ được bao gồm trong tất cả các bản sao hoặc các phần quan trọng của Phần Mềm.

PHẦN MỀM ĐƯỢC CUNG CẤP "NHƯ CÁC BẢN", KHÔNG CÓ BẢO HÀNH NÀO, RÕ RÀNG HOẶC NGỤ Ý, BAO GỒM NHƯNG KHÔNG GIỚI HẠN BẢO HÀNH VỀ CHẤT LƯỢNG, PHÙ HỢP VỚI MỤC ĐÍCH CỤ THỂ VÀ KHÔNG XÂM PHẠM. TRONG BẤT KỲ TRƯỜNG HỢP NÀO, TÁC GIẢ HOẶC CHỦ SỞ HỮU BẢN QUYỀN KHÔNG CHỊU TRÁCH NHIỆM ĐỐI VỚI BẤT KỲ YÊU CẦU, THIỆT HẠI HOẶC CÁC YÊU CẦU PHÁP LÝ KHÁC, DƯỚI HÌNH THỨC HỢP ĐỒNG, TỘI PHẠM HOẶC KHÁC, PHÁT SINH TỪ, HOẶC TRONG KẾT NỐI VỚI PHẦN MỀM HOẶC VIỆC SỬ DỤNG HOẶC CÁC GIAO DỊCH KHÁC TRONG PHẦN MỀM.

  
