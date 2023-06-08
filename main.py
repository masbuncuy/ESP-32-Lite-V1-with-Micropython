import machine
from time import sleep
import network

blue_fan = machine.Pin(27, machine.Pin.OUT)
red_fan = machine.Pin(23, machine.Pin.OUT)
green_fan = machine.Pin(5, machine.Pin.OUT)
yellow_fan = machine.Pin(18, machine.Pin.OUT)
wlan = network.WLAN(network.STA_IF)
port = 90
state = 0

wlan.active(True)
wlan.connect('Infinix NOTE 8', '123456789')
while not wlan.isconnected():
    pass

ip_address = wlan.ifconfig()[0]
print(ip_address)

url = "http://" + ip_address + ":" + str(port) + "/fan?status=ON"
print("url", url)


def control_fan(status):
    blue_fan.value(status)
    red_fan.value(status)
    green_fan.value(status)
    yellow_fan.value(status)


def send_request(url):
    response = urequests.get(url)
    status = response.text.strip()
    if status == 'ON':
        control_fan(1)
    else:
        control_fan(0)


def start_server():
    import socket
    addr = socket.getaddrinfo('0.0.0.0', port)[0][-1]
    s = socket.socket()
    s.bind(addr)
    s.listen(1)
    print('Server started')
    while True:
        cl, addr = s.accept()
        request = cl.recv(1024)
        request = str(request)
        if '/fan?status=ON' in request:
            control_fan(1)
            state = 1
        elif '/fan?status=OFF' in request:
            control_fan(0)
            state = 0
        if state == 1:
            status = " ON"
        elif state == 0:
            status = " OFF"
        response = "HTTP/1.1 200 OK\n\nFan" + status

        cl.send(response)
        cl.close()


start_server()
