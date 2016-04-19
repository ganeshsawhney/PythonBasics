from __future__ import division
a=int(raw_input())
b=int(raw_input())
tup=divmod(a,b)	#returns tuple
print tup[0],'\n',tup[1]
print divmod(a,b)

# Input (stdin)
# 177
# 10
# Your Output (stdout)
# 17 
# 7
# (17, 7)