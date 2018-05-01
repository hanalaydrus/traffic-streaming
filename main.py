from flask import Flask, render_template, Response
from queue import Queue
from camera import VideoCamera

app = Flask(__name__)

camera_1 = VideoCamera('/videos/camera_1.mp4')
camera_1.start()

camera_2 = VideoCamera('/videos/camera_2.mp4')
camera_2.start()

camera_3 = VideoCamera('/videos/camera_3.mp4')
camera_3.start()

camera_4 = VideoCamera('/videos/camera_4.mp4')
camera_4.start()

camera_5 = VideoCamera('/videos/camera_5.mp4')
camera_5.start()

camera_6 = VideoCamera('/videos/camera_6.mp4')
camera_6.start()

def gen_1():
    while True:
        frame = camera_1.get_frame()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')

def gen_2():
    while True:
        frame = camera_2.get_frame()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')

def gen_3():
    while True:
        frame = camera_3.get_frame()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')

def gen_4():
    while True:
        frame = camera_4.get_frame()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')
def gen_5():
    while True:
        frame = camera_5.get_frame()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')

def gen_5():
    while True:
        frame = camera_5.get_frame()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')

@app.route('/camera_1')
def video_feed():
    return Response(gen_1(), mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/camera_2')
def video_feed():
    return Response(gen_2(), mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/camera_3')
def video_feed():
    return Response(gen_3(), mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/camera_4')
def video_feed():
    return Response(gen_4(), mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/camera_5')
def video_feed():
    return Response(gen_5(), mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/camera_6')
def video_feed():
    return Response(gen_6(), mimetype='multipart/x-mixed-replace; boundary=frame')
                    
if __name__ == "__main__":
    app.run()