# The default value is evaluated only once. 
# This makes a difference 
# when the default is a mutable object 
# such as a list, dictionary, or instances of most classes.

def f1(a, L=[]):
    L.append(a)
    return L

print(f1(1))
print(f1(2))
print(f1(3))
# This will print
#[1]
#[1, 2]
#[1, 2, 3]



# If you don’t want the default to be shared between subsequent calls, 
# you can write the function like this instead:

def f2(a, L=None):
    if L is None:
        L = []
    L.append(a)
    return L
