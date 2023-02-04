from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def index():
    return """
    <html>
        <head>
            <script>
                function handleWebcam() {
                    navigator.mediaDevices.getUserMedia({ video: true })
                        .then(stream => {
                            const video = document.getElementById("webcam");
                            video.srcObject = stream;
                            video.onloadedmetadata = () => {
                                video.play();
                            };
                        });
                }
            </script>
        </head>
        <body>
            <button onclick="handleWebcam()">Autoriser l'accès à la webcam</button>
            <br />
            <video id="webcam" controls></video>
        </body>
    </html>
    """

if __name__ == "__main__":
    app.run(host='0.0.0.0')
