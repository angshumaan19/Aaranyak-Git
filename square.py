import turtle as t
import time as ti

def square():
    t.begin_fill()
    for line in range(5):
         t.pendown()
         t.forward(100)
         t.right(90)
    t.end_fill()



square()
ti.sleep(5)

