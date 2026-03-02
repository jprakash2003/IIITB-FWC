from machine import Pin
import time

# 7-segment pins
a = Pin(2, Pin.OUT)
b = Pin(3, Pin.OUT)
c = Pin(4, Pin.OUT)
d = Pin(5, Pin.OUT)
e = Pin(6, Pin.OUT)
f = Pin(7, Pin.OUT)
g = Pin(8, Pin.OUT)

# For COMMON ANODE display

def show_1():
    a.value(1)
    b.value(0)
    c.value(0)
    d.value(1)
    e.value(1)
    f.value(1)
    g.value(1)

def show_0():
    a.value(0)
    b.value(0)
    c.value(0)
    d.value(0)
    e.value(0)
    f.value(0)
    g.value(1)

while True:
    for A in [0,1]:
        for B in [0,1]:
            for C in [0,1]:

                # NAND logic
                Y = not (A and B and C)

                print("A=",A,"B=",B,"C=",C,"Output=",Y)

                if Y == 1:
                    show_1()
                else:
                    show_0()

                time.sleep(2)