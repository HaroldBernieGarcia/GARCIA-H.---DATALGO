""" HArold Bernie P. Garcia
DATALOG
Feb. 26 , 2020
I have neither received nor provided any help on this (exercice) activity,
nor have I concealed any violation of the Honor Code.
"""
class Airplane:
    def __init__(self):
        self.speed = 0
    def set_speed(self , speed):
        self.speed = speed
    def get_speed(self):
        return self.speed

class Jet(Airplane):
    def __init__(self):
        self.MULTIPLIER = 2
    def set_speed(self , speed):
        super.set_speed(speed * self.MULTIPLIER)
    def accelarate(self):
        super.set_speed(self.get_speed()*2)

class FlyTest():

    biplane = Airplane()
    biplane.set_speed(212)
    print(biplane.get_speed)

    boeing = Jet()
    boeing.set_speed(422)
    print(boeing.get_speed)

    x = 0

    while x < 4:
        boeing.accelarate()
        print(boieng.get_speed())

        if boeing.get_speed() > 5000:
           biplane.set_speed ( biplane.get_speed()* 2)
        else:
            boeing.accelarate()
            x+=1
            print(biplane.get_speed())

FlyTest()

