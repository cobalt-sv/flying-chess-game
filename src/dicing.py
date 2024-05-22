import sys
import pygame
from pygame.locals import *
from random import randint

pygame.init()

class Dicing(object):
    def __init__(self): # __init__构造函数
        pass



    def dice(self, number): # 判断正确与否
        a = randint(1, number)
        return a

    def playerDice(self, number): # 判断正确与否
        b = randint(0, number)
        return b


