# -*- coding: utf-8 -*-
"""
Created on Sun Oct  2 17:40:57 2022

@author: paulb
"""

import chess
from chess import engine, pgn

import os
from time import sleep
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


for (root, dirs, files) in os.walk('Chess tournaments'):
    for f in files:
        print(f)
        with open(f'Chess tournaments/{f}', 'rb') as source, open("all games.txt", "ab") as dest:
            dest.write(source.read())
            sleep(1)
            

print('Done')