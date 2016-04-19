list1 = ['physics', "chemistry", 1997, 2000,1,2];
print "list1[0]: ", list1[0]
print "list1[1:1]: ", list1[1:1]
print "list1[1:2]: ", list1[1:2]
print "list1[1:3]: ", list1[1:3]
print "list1[1:5]: ", list1[1:5]

# list1[0]:  physics
# list1[1:1]:  []
# list1[1:2]:  ['chemistry']
# list1[1:3]:  ['chemistry', 1997]
# list1[1:5]:  ['chemistry', 1997, 2000, 1]


print list1[2]
#1997
list1[2] = 2001;
print list1[2]
#2001


list1.append('newelem')
print list1
#['physics', 'chemistry', 2001, 2000, 1, 2, 'newelem']
print list1[6]
#newelem


del list1[2];
print list1
#['physics', 'chemistry', 2000, 1, 2, 'newelem']
print list1[5]
#newelem
print list1[6]
#IndexError: list index out of range

'''
Python Expression				Results						Description
len([1, 2, 3])					3							Length
[1, 2, 3] + [4, 5, 6]			[1, 2, 3, 4, 5, 6]			Concatenation
['Hi!'] * 4						['Hi!','Hi!','Hi!','Hi!']	Repetition
3 in [1, 2, 3]					True						Membership
for x in [1, 2, 3]: print x,	1 2 3						Iteration


L = ['1', '2', '3'] 
Python Expression		Results			Description
L[2]					'3'				Offsets start at zero
L[-2]					'2'				Negative: count from the right
L[1:]					['2', '3']		Slicing fetches sections


Built-in List Functions & Methods:
#cmp(list1, list2)
Compares elements of both lists.

#len(list)
Gives the total length of the list.
	
#max(list)
Returns item from the list with max value.

#min(list)
Returns item from the list with min value.
	
#list(seq)
Converts a tuple into list.

#list.append(obj)
Appends object obj to list
	
#list.count(obj)
Returns count of how many times obj occurs in list
	
#list.extend(seq)
Appends the contents of seq to list
	
#list.index(obj)
Returns the lowest index in list that obj appears
	
#list.insert(index, obj)
Inserts object obj into list at offset index
	
#list.pop(obj=list[-1])
Removes and returns last object or obj from list
	
#list.remove(obj)
Removes object obj from list
	
#list.reverse()
Reverses objects of list in place
	
#list.sort([func])
Sorts objects of list, use compare func if given
'''