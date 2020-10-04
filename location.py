"""
This program navigates the map and finds the path in the maze
It then finds the score associated with the path
The higher the score, the more time the ambulance takes to move from the hospital to the house
"""

import numpy as np
from stuff import Node, StackFrontier, Map

def available_move(current_node, city, explored_set, xmax, ymax):
    current_x, current_y = current_node.state
    moves = [
        (current_x, current_y + 1),
        (current_x, current_y - 1),
        (current_x + 1, current_y),
        (current_x - 1, current_y)
    ]
    avail_moves = []
    
    for move in moves:
        x, y = move
    #Check whether the point considered is inside the grid
        if (x >= 0) and (x < xmax) and (y >= 0) and (y < ymax):

        #Check whether the point considered is not in explored_set and it is not a wall
            if (x, y) not in explored_set and city.score(x, y) != 0:
                avail_moves.append((x, y))

    return avail_moves


def solve_best_path(city, xmax, ymax):

    #Initiate values before going to the loop
    initial_node = Node(city.hospital(), -1, -1)
    stack = StackFrontier()
    stack.add_node(initial_node)

    explored_set_state = set()
    explored_set_node = set()

    explored_set_state.add(city.hospital())
    explored_set_node.add(initial_node)

    while True:
        avail_moves = []

        #If the stack is empty, then no solution
        if stack.Empty():
            print('You should use a helicopter')
            return False

        #Obtain the current node
        current_node = stack.remove()

        if current_node.state == city.house():
            path = []
            score = 0

            #Iterate to find the path
            while True:
                x, y = current_node.state
                path.append(current_node.state)

                #Find the score, based on the value of the square on the map
                score += city.score(x, y)

                if current_node.parent == -1:
                    path.reverse()
                    for state in path:
                        print(state)
                    print(score+3)
                    return True
                else:
                    current_node = current_node.parent
            

        explored_set_state.add(current_node.state)
        explored_set_node.add(current_node)

        avail_moves = available_move(current_node, city, explored_set_state, xmax, ymax)
        for move in avail_moves:

            #Update new nodes to the stack
            new_node = Node(move, current_node, -1)
            stack.add_node(new_node)

if __name__ == '__main__':
    solve_best_path(city)

#xmax, ymax = 5, 5
#city = Map(xmax, ymax)
#city.Generate_map(random = False)
#solve_best_path(city)
