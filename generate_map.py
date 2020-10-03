'''
This function intended to generate an mxn matrix of nodes to represent possible positions of the ambulance.
The ambulance may move to an adjacent node (diagonals okay, so 8 movement options)
Each node has a predefined position 
Travel time and distance are calculated based on the speed of the 

'''

import numpy as np
from np import random as rd


class Road_Node:
    def __init__(self, x_in=0, y_in=0, traf_in=0):
        self.x = x_in
        self.y = y_in
        self.traffic = traf_in

    def get_data(self):
        print(f'debug/({self.x},{self.y}) with {self.traffic} traffic')


def generate_map(input_m, input_n):
    road_mat = np.zeros((input_m, input_n))
    for x in range(0, input_m):
        for y in range(0, input_n):
            road_mat[x][y] = Road_Node(100*x+40*random.random(),100*y+40*random.random(),random.uniform(0,20))



qq = generate_map(10,10)
print(qq)
