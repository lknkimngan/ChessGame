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
* Bên cạnh đó, giao diện game cũng sẽ hiển thị về quân cờ của người chơi là quân nào, lượt đi của người chơi, thời gian từng người, thông báo chiến thắng, thông báo thua.
Quy tắc để chiến thắng là chiếu bí vua đối phương, bắt vua đối phương hoặc là thời gian kết thúc
![alt text](image-8.png)


## Yêu cầu
* Python 3 <= v3.10.10 (Download from https://www.python.org/downloads/)
## Cách cài đặt 
* $ git clone https://github.com/lknkimngan/ChessGame.git 
* Mở thư mục ChessGame mới cài đặt.
  *  $ python3 -m venv my_env
  *  $ .\my_env\Scripts\activate
## Thực thi chương trình
* Bước 1: Mở terminal và chạy lệnh: ip addr show để lấy địa chỉ IPv4 mà máy đang kết nối.
⇒ Địa chỉ IPv4 của máy sẽ nằm ở dòng inet 192.168.220.128

![alt text](image.png)
* Bước 2: Lấy địa chỉ IP vừa lấy được sau đó dán địa chỉ này vào server = ‘192.168.220.128’ ở file server.py và dòng self.host = ‘192.168.220.128’ ở file client.py. (Địa chỉ IP này sẽ khác trên mỗi máy).
  ![alt text](image-1.png)
![alt text](image-2.png)
*Bước 3: Chạy file server.py. Sau đó, mở thêm 2 terminal khác chạy file game.py
![alt text](image-3.png)
⇒ Sau khi chạy 3 terminal trên, ta được kết quả như sau. Sau đó click để chơi game.
![alt text](image-4.png)
* Bước 4: Chơi game. Khi chơi, ta có thể thấy được đường đi trước đó của đối thủ được đánh dấu bằng vòng tròn màu xanh. Ngoài ra, ta có xem được thời gian chơi game của 2 người chơi. Nếu muốn thoát game, ta cần nhấn phím “q” để thoát game.
  ![alt text](image-5.png)
![alt text](image-6.png)
![alt text](image-7.png)


  
