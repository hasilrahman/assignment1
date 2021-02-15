l1=["ab","cd","ef","hr"]
x=map(lambda s:s[0]=='a',l1)
print(list(x))
x=filter(lambda s:s[0]=='a',l1)
print(list(x))
from functools import reduce
def add(x,y):
	return x+y
l1=[12,32,55,54]
print(reduce(add,l1))
