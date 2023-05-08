import http.server
import socketserver

PORT = int(input("Введіть порт: "))
class MyHttpRequestHandler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/':
            # Відповідь на запит GЕТ / - повертаємо сторінку з клієнтською частиною
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            with open('index.html', 'rb') as file:
                self.wfile.write(file.read())
        elif self.path.endswith('.css'):
            # Відповідь на запит GЕТ /style.css - повертаємо вміст файлу style.css
            self.send_response(200)
            self.send_header('Content-type', 'text/css')
            self.end_headers()
            with open('style.css', 'rb') as file:
                self.wfile.write(file.read())
        elif self.path.endswith('.js'):
            # Відповідь на запит GЕТ /script.js - повертаємо вміст файлу script.js
            self.send_response(200)
            self.send_header('Content-type', 'text/javascript')
            self.end_headers()
            with open('script.js', 'rb') as file:
                self.wfile.write(file.read())
        elif self.path == "/API":
            # Відповідь на запит GЕТ /API - повертаємо сторінку з API
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            with open('index_api.html', 'rb') as file:
                self.wfile.write(file.read())
        else:
            # Інші запити - повертаємо статус 404
            self.send_response(404)
            self.end_headers()

# Створюємо об'єкт HTTP сервера
with socketserver.TCPServer(("", PORT), MyHttpRequestHandler) as httpd:
    print("Використовується порт:", PORT)
    print(f"Переходьте за посиланням: http://localhost:{PORT}/")
    # Запускаємо сервер
    httpd.serve_forever()