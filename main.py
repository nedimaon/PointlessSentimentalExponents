import socket
import sys

def main():
    # Создаем сокет
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # Указываем адрес и порт
    host = "192.168.1.1"
    port = 1900

    # Готовим запрос
    request = b"M-SEARCH * HTTP/1.1\r\nHOST: 239.255.255.250:1900\r\nST: ssdp:all\r\nMX: 2\r\nMAN: \"ssdp:discover\"\r\n\r\n"

    # Отправляем запрос
    sock.sendto(request, (host, port))

    # Принимаем ответ
    response, _ = sock.recvfrom(1024)

    # Разбираем ответ
    response_lines = response.decode("utf-8").split("\r\n")

    # Добавляем устройства в список
    for line in response_lines:
        if line.startswith("USN: "):
            usn = line.split(" ")[1]

        if line.startswith("ST: "):
            st = line.split(" ")[1]

        if line.startswith("Location: "):
            location = line.split(" ")[1]

        devices.append({
            "usn": usn,
            "st": st,
            "location": location,
        })

if __name__ == "__main__":
    main()
