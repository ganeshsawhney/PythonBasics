'''
All below are tuples
tup1 = ('physics', 'chemistry', 1997, 2000);
tup2 = (1, 2, 3, 4, 5 );
tup3 = "a", "b", "c", "d";

#To write a tuple containing a single value you have to include a comma, even though there is only one value
tup1 = (50,);
'''


tup1 = ('physics', 'chemistry', 1997, 2000);
print "tup1[0]: ", tup1[0]
print "tup1[1:1]: ", tup1[1:1]
print "tup1[1:3]: ", tup1[1:3]
print "tup1[1:5]: ", tup1[1:5]
# tup1[0]:  physics
# tup1[1:1]:  ()
# tup1[1:3]:  ('chemistry', 1997)
# tup1[1:5]:  ('chemistry', 1997, 2000)


'''
Tuples are immutable which means you cannot update or change the values of tuple elements.
'''

tup1 = (12, 34.56);
tup2 = ('abc', 'xyz');
'''
Following action is not valid for tuples 
tup1[0] = 100;
'''
tup3 = tup1 + tup2;
print tup3
#(12, 34.56, 'abc', 'xyz')


'''
Removing individual tuple elements is not possible.
'''
tup = ('physics', 'chemistry', 1997, 2000);
del tup;
print tup
#NameError: name 'tup' is not defined

'''
Tuples respond to the + and * operators much like strings; they mean concatenation and repetition here too, except that the result is a new tuple, not a string.
Python Expression				Results							Description
len((1, 2, 3))					3								Length
(1, 2, 3) + (4, 5, 6)			(1, 2, 3, 4, 5, 6)				Concatenation
('Hi!',) * 4					('Hi!', 'Hi!', 'Hi!', 'Hi!')	Repetition
3 in (1, 2, 3)					True							Membership
for x in (1, 2, 3): print x,	1 2 3							Iteration
'''

L = ('1', '2', '3')
Python Expression		Results			Description
L[2]					'3'				Offsets start at zero
L[-2]					'2'				Negative: count from the right
L[1:]					['2', '3']		Slicing fetches sections


print 'abc', -4.24e93, 18+6.6j, 'xyz'
x, y = 1, 2;
print "Value of x , y : ", x,y
# abc -4.24e+93 (18+6.6j) xyz
# Value of x , y : 1 2


'''
#cmp(tuple1, tuple2)
Compares elements of both tuples.
	
#len(tuple)
Gives the total length of the tuple.
	
#max(tuple)
Returns item from the tuple with max value.
	
#min(tuple)
Returns item from the tuple with min value.
	
#tuple(seq)
Converts a list into tuple.
'''
