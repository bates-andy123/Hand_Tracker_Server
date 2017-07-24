from bottle import route, run, template
from FSM import FSM
import serial

arduino = serial.Serial("/dev/ttyS0", baudrate=9600)

@route('/<comm>')
def index(comm):
    items = comm.split(',')
    orientation = items[0]
    speed = int(items[1])
    fsm = FSM(orientation, speed)
    #arduino.write(fsm)
    print fsm
    return template('<b>command: {{comm}} length queue: {{length}}</b>', comm=comm, length = len(comm)) 
 
#This must be it's own IP, not localhost
#run(host='192.168.0.106', port=8080)
run(host='192.168.1.85', port=8080)
