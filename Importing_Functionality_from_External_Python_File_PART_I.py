# -*- coding: utf-8 -*-
"""
Created on Wed Sep 21 21:22:46 2022

@author: Abhik
"""

import random

feet_in_mile=5280
metre_in_kilometre=1000
beatles=["John Lennon","Paul McCartney","George Harrison","Ringo Star"]


def get_file_ext(filename):
    return filename[filename.index(".")+1:]


def roll_dice(num):
    return random.randint(1,num)

    