num=int(raw_input("Enter the number upto which you need to list primes: "))
i = 2
while(i < num):
   j = 2
   while(j <= (i/j)):
      if not(i%j): break
      j = j + 1
   if (j > i/j) : print i, " is prime"
   i = i + 1