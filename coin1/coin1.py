from pwn import *

# binary search
url = "pwnable.kr"
port = 9007

r = remote(url, port)
r.recv()
print "Connected to server."

sleep(2)


# find 100 coins
for coin in xrange(100):
	nc = r.recv()
	n = int(nc[2:nc.find("C=")-1])
	c = int(nc[nc.find("C=")+2:-1])
	print n, c

	lower = 0
	upper = n
	size = n/2
	s = ""

	for tries in xrange(c):
		s = ""
		for i in xrange(lower, lower + size):
			s += "{} ".format(i)
			# s = 0 1 2 ... n/2 rounded down
		r.sendline(s)
		res = r.recv()


		# first half
		if res[-2] == "9":
			upper = lower + size
		# second half
		else:
			lower += size 

		size += 1
		size /= 2


	# last try
	s = str(lower)
	r.sendline(s)

	print r.recv()
r.interactive()
