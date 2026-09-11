import os
import socket

from app import app


def find_available_port(start_port):
    port = start_port
    while True:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
            if server_socket.connect_ex(("127.0.0.1", port)) != 0:
                return port
        port += 1


if __name__ == "__main__":
    requested_port = int(os.environ.get("PORT", "5001"))
    port = find_available_port(requested_port)
    if port != requested_port:
        print(f"El puerto {requested_port} está ocupado. Usando {port}.")
    print(f"Horizonte disponible en http://127.0.0.1:{port}")
    app.run(debug=True, host="127.0.0.1", port=port, use_reloader=False)
