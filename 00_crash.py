#!/usr/bin/env python3
#Simple Python Fuzzer for Buffer Overflows.

import socket, sys

ip, port = "192.0.0.0", 9999 #change me
command = b"" #any prefix command you need to insert
timeout = 5

payload = b"".join([
    command, b"A" * 10
])

#continuously add more data until program crashes
# s.recv is optional - depending on the program you are fuzzing and so are the line breaks
# if having difficulty feel free to add them after connecting / sending payloads
while True:
    try:
        with socket.socket() as s:
            s.settimeout(timeout)
            s.connect((ip, port))
            s.recv(4096)
            print(f"Fuzzing with {len(payload) - len(command)} bytes")
            s.send(payload + b"\r\n") #send payload plus carriage return
            s.recv(4096)
    except:
        print(f"Fuzzing crashed at {len(payload) - len(command)} bytes")
        sys.exit(0)
    payload += b"B" * 10