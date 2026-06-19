s=3
if (type(s) is int):
    print("true")
else:
    print("false")

c=6.3

if (type(c) is not float):
    print("true")
else:
    print("false")

t=20
u=20

if (t is u):
    print("t & u have the same identity")

u=30

if (t is not u):
    print("t & u have different identity")