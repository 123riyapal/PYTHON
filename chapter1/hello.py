print("hello,world!")
# input("What is your Name?")
''' 
Is a multiple line comment
'''
strs="""hello 
hi 
how are you
"""
name=input()
# print definition
# print(*objects, sep=' ', end='\n', file=None, flush=False) we can change their value accordingly  like line 14 
#print("hello" , input("What is your Name?"))
print("heloo",end='+')
print(f"hello,{name}")

# input take string so if we want to take input as a number than we use type cast
num1 = int( input ())
num2 =int(input ())
SUM=num1+num2
print(SUM)
print(strs)
