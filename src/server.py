from bottle import route, run, template
from FSM import FSM
import serial
import threading
import time

arduino = serial.Serial("/dev/ttyS0", baudrate=9600)
command = "<N,0>"

def sending_thread():
    print "Thread started"
    while True: 
        arduino.write(command)
        arduino.flush()
        time.sleep(0.05)

thread = threading.Thread(target=sending_thread, args=())
thread.start()

@route('/<comm>')
def index(comm):
    global command
    items = comm.split(',')
    orientation = items[0]
    speed = int(items[1])
    command = FSM(orientation, speed)
    print command
    return template('<b>command: {{comm}} length queue: {{length}}</b>', comm=comm, length = len(comm)) 
 
#This must be it's own IP, not localhost
#run(host='192.168.0.106', port=8080)
run(host='192.168.0.104', port=8080)
