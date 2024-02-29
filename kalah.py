#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 27 11:14:37 2024

@author: piripuz
"""
import numpy as np

class Kalah:
    def __init__(self, p0_name="player_0", p1_name="player_1", width=6):
        self.p = [p0_name, p1_name]
        self.table = np.ones((2, width), dtype=int)*4
        self.dep = np.zeros((2))
        self.curr_player = 0           
    def move(self, cell):
        self.curr_player = 1 - self.curr_player
        num_ball = self.table[self.curr_player, cell]
        self.table[self.curr_player, cell] = 0
        self.red(cell, num_ball, self.curr_player)
    def red(self, cell, num_ball, player):
        if num_ball == 0:
            if self.table[player, cell] == 1:
                self.dep[self.curr_player] += self.table[1 - player, cell] + 1
                self.table[player, cell] = 0
                self.table[1 - player, cell] = 0
                print(f"{self.p[self.curr_player]} gained some balls!!")
                return
            else:
                print("Niente")
                return
        if player == 0:
            if (cell != 0):
                target = cell - 1
                self.table[player, target] += 1
                self.red(target, num_ball - 1, player)
            else:
                self.dep[0] += 1
                self.red(-1, num_ball - 1, 1)
        if player == 1:
            if (cell != 5):
                target = cell + 1
                self.table[player, target] += 1
                self.red(target, num_ball - 1, player)
            else:
                self.dep[1] += 1
                self.red(6, num_ball - 1, 0)
    
    def finished(self):
        return (max(self.dep) > 18 or np.min(np.max(self.table, axis=1), axis=0) == 0)
    
