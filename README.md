# Buffd
Collection of skeleton scripts for doing stack based buffer overflows. 
Each script takes you through a step of exploiting a buffer overflow. 

--------------

Requirements:
Python3, Immunity Debugger with Mona.py in the PyCommands folder, access to a vulnerable executable, Metasploit, and ideally a Windows VM to run the vulnerable program on. 

However the script can be easily modified and the values to enumerate can be found manually or with other tools as well.
Read the comments in each script for a step by step on how to find the values for different variables you need to change. 

--------------

00_Crash - find the amount of bytes that will crash the program.

01_EnumEIP - find the EIP offset

02_Overflow - confirm control of the EIP

03_FindBadChars - generate an initial list of bad characters

04_No_BadCHar - remove bad characters

05_Exploit - generate shell code and exploit

05_ExploitAlt - same as 05 just written differently

-------------
