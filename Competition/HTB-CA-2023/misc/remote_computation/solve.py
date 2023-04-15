from pwn import *

p = remote('142.93.38.14',30588)

p.recvuntil(b'> ')
p.sendline('1')
data = p.recvuntil(b'> ')

counter = 0
while True:

	que = data.split(b']:')[1].split(b'=')[0].strip()
	print('que - ',que)
	
	
	try:
		ans = eval(que)
		if ans > 1337 or ans < -1337:
			ans = "MEM_ERR"
		else:
			ans = "{:.2f}".format(ans)
	
	except ZeroDivisionError:
		ans = "DVI0_ERR"
	except SyntaxError:
		ans = "SYNTAX_ERR"
	
	info('Anser is - %s' % ans)
	print('counter number %d' % counter)
	counter += 1
	p.sendline(b'{}'.format(ans))
	#p.sendline(ans.encode('utf-8'))
	try:
		data = p.recvuntil(b"> ")
	except EOFError:
		p.interactive()
		exit('-')
	pass
	
