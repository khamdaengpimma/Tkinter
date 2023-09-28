import socket
import pickle

# Tạo thông điệp với các thuộc tính của hình tròn
message = {
    'color': 'red',
    'radius': 50,
    'name': 'Hình tròn đỏ'
}

# Kết nối tới server
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = ('localhost', 2050)  # Địa chỉ và cổng của server

client_socket.connect(server_address)

# Gửi thông điệp tới server
data = pickle.dumps(message)  # Chuyển thông điệp thành dạng pickle
client_socket.send(data)

# Đóng kết nối
client_socket.close()
