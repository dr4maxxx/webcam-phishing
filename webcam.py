import http.server
import socketserver
import threading

PORT = 8080

class MyHandler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        # Envoi de la réponse HTTP
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        
        # Génération du corps de la réponse
        response = "<html><body><form action='/' method='post'>"
        response += "<input type='submit' name='submit' value='Autoriser'>"
        response += "<input type='submit' name='submit' value='Refuser'>"
        response += "</form></body></html>"
        self.wfile.write(response.encode())

    def do_POST(self):
        # Traitement de la demande de l'utilisateur
        if self.headers.get('Content-Length'):
            length = int(self.headers.get('Content-Length'))
            post_data = self.rfile.read(length).decode()
            if 'Autoriser' in post_data:
                # Envoi de la réponse HTTP
                self.send_response(200)
                self.send_header('Content-type', 'text/html')
                self.end_headers()
                
                # Génération du corps de la réponse
                response = "<html><body><p>Accès à la webcam autorisé</p></body></html>"
                self.wfile.write(response.encode())
            elif 'Refuser' in post_data:
                # Envoi de la réponse HTTP
                self.send_response(200)
                self.send_header('Content-type', 'text/html')
                self.end_headers()
                
                # Génération du corps de la réponse
                response = "<html><body><p>Accès à la webcam refusé</p></body></html>"
                self.wfile.write(response.encode())

# Configuration et lancement du serveur
with socketserver.TCPServer(("", PORT), MyHandler) as httpd:
    print("Serveur démarré sur le port", PORT)
    print("Accédez à l'application à l'adresse http://localhost:{}".format(PORT))
    httpd.serve_forever()
