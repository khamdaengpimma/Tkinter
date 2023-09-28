import socket
import pickle
import tkinter as tk

# Khởi tạo cửa sổ hiển thị hình tròn
def display_circle(color, radius, name):
    window = tk.Tk()
    window.title("Hình tròn")
    
    canvas = tk.Canvas(window, width=2*radius, height=2*radius)
    canvas.pack()
    
    canvas.create_oval(0, 0, 2*radius, 2*radius, fill=color)
    
    label = tk.Label(window, text=name)
    label.pack()
    
    window.mainloop()

# Khởi tạo server socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = ('localhost',2050)  # Địa chỉ và cổng của server

server_socket.bind(server_address)
server_socket.listen(1)  # Chỉ cho phép một kết nối đồng thời

print("Đang chờ kết nối từ client...")
client_socket, client_address = server_socket.accept()
print(f"Kết nối từ {client_address} đã được thiết lập!")

# Nhận dữ liệu từ client
data = client_socket.recv(1024)
message = pickle.loads(data)  # Giải mã dữ liệu dạng pickle

# Hiển thị hình tròn với các thuộc tính từ thông điệp client
color = message['color']
radius = message['radius']
name = message['name']
display_circle(color, radius, name)

# Đóng kết nối
client_socket.close()
server_socket.close()
