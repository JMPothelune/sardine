from random import random, randint
c.bpm = 120
ct = 0

@swim
def test(delay=0.5, iter=0):
    global ct
    ct += 0.5
    if ct % 2.5 == 0:
        S('bd').out()
        S('jvbass', n=randint(1,20)).out()
    if ct % 3.5 == 0:
        S('cp', n=randint(1,20)).out()
        S('jvbass', n=randint(1,20)).out()
    if ct % 0.5 == 0:
        S('hh', amp=0.4).out()
    cs(test, delay=0.5, iter=iter+1)


hush()
