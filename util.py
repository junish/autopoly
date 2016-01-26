# coding: utf-8
# Here your code !

import random
def define_land_id(cls):
    '''usage:
        @define_land_id
        class hogehoge:
    '''
    cls.GO = 0
    cls.A1 = 1
    cls.CC1 = 2
    cls.A2 = 3
    cls.T1 = 4
    cls.R1 = 5
    cls.B1 = 6
    cls.CH1 = 7
    cls.B2 = 8
    cls.B3 =9
    cls.JAIL = 10
    cls.C1 = 11
    cls.U1 = 12
    cls.C2 = 13
    cls.C3 = 14
    cls.R2 = 15
    cls.D1 = 16
    cls.CC2 = 17
    cls.D2 =18
    cls.D3 = 19
    cls.FP = 20
    cls.E1 = 21
    cls.CH2 = 22
    cls.E2 = 23
    cls.E3 = 24
    cls.R3 = 25
    cls.F1 = 26
    cls.F2 = 27
    cls.U2 = 28
    cls.F3 = 29
    cls.G2J = 30
    cls.G1 = 31
    cls.G2 = 32
    cls.CC3 = 33
    cls.G3 = 34
    cls.R4 = 35
    cls.CH3 = 36
    cls.H1 = 37
    cls.T2 = 38
    cls.H2 = 39
    return cls

def dice(m):
    return random.randint(1,m)

   
