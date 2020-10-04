'''
This function intended to generate an mxn matrix of nodes to represent possible positions of the ambulance.
The ambulance may move to an adjacent node (diagonals okay, so 8 movement options)
Each node has a predefined position 
Travel time and distance are calculated based on the speed of the 

'''
import numpy as np


#This file defines all sort of Class objects


class Road_Node():
    def __init__(self, x_in=0, y_in=0, traf_in=0):
        self.x = x_in
        self.y = y_in
        self.traffic = traf_in

class Node():
    def __init__(self, state, parent, action):
        self.state = state 
        self.parent = parent
        self.action = action

    #def get_data(self):
    #    print(f'debug/({self.x},{self.y}) with {self.traffic} traffic')

class StackFrontier():
    def __init__(self):
        self.frontier = []
    
    def Empty(self):

        #Check whether the frontier is empty:
        if self.frontier == []:
            #print('No solution')
            return True
        else:
            return False

    def add_node(self, node):
        self.frontier.append(node)

    def remove(self):

        #Remove and return the last element of frontier
        removed_node = self.frontier.pop()
        return removed_node


class Map():
    def __init__(self, length, width):
        self.length = length
        self.width = width
        self.map = []
        self.hos_x = 0
        self.hos_y = 0
        self.home_x = 4
        self.home_y = 4
    
    def Generate_map(self, random = True):

        if random:
            #Assign random values to the map, such that the value represents the traffic of the map
            for x in range(0, self.width):
                for y in range(0, self.length):
                    self.map[x][y] = np.random.randint(1, 16)

            #Assign random coordinates for house and hospital
            self.hos_x, self.hos_y = np.random.randint(self.width), np.random.randint(self.length)
            self.home_x, self.home_y = np.random.randint(self.width), np.random.randint(self.length)

            #Prevent coordinates of house and hospital to be equal
            while self.home_x == self.hos_x and self.home_y == self.hos_y:
                self.home_x, self.home_y = np.random.randint(self.width), np.random.randint(self.length)

            self.map[self.hos_x][self.hos_y] = -2
            self.map[self.home_x][self.home_y] = -1

        else: #For testing purpose
            self.length, self.width = 5, 5
            self.map = [
                [-2, 1, 1, 1, 1],
                [0, 0, 0, 0, 1],
                [1, 1, 0, 1, 1],
                [1, 0, 0, 0, 0],
                [1, 1, 1, 1, -1]
            ]
            

    def Print(self):
        for i in range(self.width):
            for j in range(self.length):
                print(self.map[i][j], end= ' ')
            print('')
    
    def hospital(self):
        return (self.hos_x, self.hos_y)

    def house(self):
        return (self.home_x, self.home_y)

    def score(self, x, y):
        return self.map[x][y]




