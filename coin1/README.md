# Coin1
Description:
~~~
Mommy, I wanna play a game!
(if your network response time is too slow, try nc 0 9007 inside pwnable.kr server)

Running at : nc pwnable.kr 9007
~~~

Alright, let's try this.

~~~
$ nc pwnable.kr 9007

	---------------------------------------------------
	-              Shall we play a game?              -
	---------------------------------------------------
	
	You have given some gold coins in your hand
	however, there is one counterfeit coin among them
	counterfeit coin looks exactly same as real coin
	however, its weight is different from real one
	real coin weighs 10, counterfeit coin weighes 9
	help me to find the counterfeit coin with a scale
	if you find 100 counterfeit coins, you will get reward :)
	FYI, you have 30 seconds.
	
	- How to play - 
	1. you get a number of coins (N) and number of chances (C)
	2. then you specify a set of index numbers of coins to be weighed
	3. you get the weight information
	4. 2~3 repeats C time, then you give the answer
	
	- Example -
	[Server] N=4 C=2 	# find counterfeit among 4 coins with 2 trial
	[Client] 0 1 		# weigh first and second coin
	[Server] 20			# scale result : 20
	[Client] 3			# weigh fourth coin
	[Server] 10			# scale result : 10
	[Client] 2 			# counterfeit coin is third!
	[Server] Correct!

	- Ready? starting in 3 sec... -

N=62 C=6
1
10
2
10
3
10
4
10
5
10
6
10
7
Wrong coin!
~~~

From first glance, this looks like something we need to automate. 30 seconds for 100 coins? That's 3.3 coins per second! However, I noticed that C was always equal to `ceil(lg(N))`, which led me to believe that the best way to approach this was binary search! 

Trying multiple coins per line as input:

```
N=519 C=10
1 2 3 4 5
50
6 7 8 9 0
50
...
```

Idea: enter the first `C/2` coins. If the server responds with a value that ends in `9`, we know we are looking at the correct half. Then, we can iterate after changing the limits. If the server responds with a value that ends in a `0`, we are looking at the wrong half, and need to readjust our bounds.

I wrote a [snippet of code](./coin1.py) to perform the binary search and send the data to the server. Running it locally times out because the network is slow. Let's ssh into the pwnable.kr server from a previous challenge, and create the file under `/tmp/` and run it there!

~~~
$ python /tmp/script.py
[+] Opening connection to localhost on port 9007: Done
Connected to server.
478 9
Correct! (0)

...

859 10
Correct! (98)

841 10
Correct! (99)

[*] Switching to interactive mode
Congrats! get your flag
b1NaRy_S34rch1nG_1s_3asy_p3asy

~~~


Flag: `b1NaRy_S34rch1nG_1s_3asy_p3asy`
