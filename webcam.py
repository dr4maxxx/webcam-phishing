import cv2
import pygame
import socket
import threading

host = ''
port = 5000

def start_server():
    # Initialisation du serveur
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((host, port))
    server.listen(1)
    print("Le serveur est démarré sur l'adresse %s:%s" % (host, port))

    # Acceptation de la connexion client
    client, address = server.accept()
    print("Connexion établie avec %s:%s" % (address[0], address[1]))

    # Réception de l'autorisation de l'utilisateur pour l'accès à la webcam
    permission = client.recv(1024).decode()
    if permission.lower() == 'yes':
        # Initialisation de la webcam
        cap = cv2.VideoCapture(0)
        ret, frame = cap.read()

        # Conversion de l'image en format Pygame
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        frame = pygame.surfarray.make_surface(frame)

        # Envoi de l'image vers l'appareil client
        pygame.image.save(frame, 'received_image.jpg')

        # Fermeture de la webcam et du serveur
        cap.release()
        server.close()
        print("Image reçue avec succès")
    else:
        # Fermeture du serveur
        server.close()
        print("Accès à la webcam refusé")

if __name__ == '__main__':
    # Initialisation de Pygame
    pygame.init()

    # Démarrage du serveur dans un thread séparé
    server_thread = threading.Thread(target=start_server)
    server_thread.start()
