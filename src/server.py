from bottle import route, run, template
import serial

arduino = serial.Serial("/dev/ttyS0", baudrate=9600)

@route('/<comm>')
def index(comm):
    arduino.write(comm)
    print arduino.read(len(comm))
    return template('<b>command: {{comm}} length queue: {{length}}</b>', comm=comm, length = len(comm)) 
 
#This must be it's own IP, not localhost
run(host='192.168.0.106', port=8080)
