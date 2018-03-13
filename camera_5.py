from flask import Flask, render_template, Response
from queue import Queue
from camera import VideoCamera

app = Flask(__name__)
camera = VideoCamera('camera_5.mp4')
camera.start()

def gen():
    while True:
        frame = camera.get_frame()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/video_feed')
def video_feed():
    return Response(gen(),
                    mimetype='multipart/x-mixed-replace; boundary=frame')
                    
if __name__ == "__main__":
    app.run()