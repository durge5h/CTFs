msg = "welcome to uiuctf!\nyour super secret flag is: XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
flag = "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
m = int(msg.encode("hex"), 16)
f = int(flag.encode("hex"), 16)

execfile("out.txt")

x, = PolynomialRing(Zmod(n), 'x', implementation='NTL').gens()
poly = (m - f + x)^e - c

r = poly.small_roots(epsilon=1/25, algorithm='fpLLL:proved', fp='rr')[0]
mm = m - f + r
print hex(int(mm)).replace("0x", "").replace("L", "").decode("hex")
