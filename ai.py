import time
import random
import io
import sys

class key:
    def key(self):
        return "10jifn2eonvgp1o2ornfdlf-1230"

class ai:
    def __init__(self):
        t = 10
        start_time = 0

    class state:
        def __init__(self, a, b, a_fin, b_fin):
            self.a = a
            self.b = b
            self.a_fin = a_fin
            self.b_fin = b_fin
            self.repeat = False

    def move(self, a, b, a_fin, b_fin, t):
        state = self.state(a, b, a_fin, b_fin)
        self.t = t * 0.01
        result = self.minimax(8, state = state)
        return result

        # below is the given + modified testing code this does not run
        f = open('time.txt', 'a') #append to time.txt so that you can see running time for all moves.
        # Make sure to clean the file before each of your experiment
        for d in [3, 5, 7, 9, 11, 13, 15]: #You should try more
            f.write('depth = '+str(d)+'\n')
            t_start = time.time()
            self.minimax(depth = d, state = state)
            f.write(str(time.time()-t_start)+'\n')
        f.close()


    def minimax(self, depth, state):
        # wrapper for the  minimax algorithm
        self.start_time = time.time()

        # v approaches the max value of the state
        # v <- max_value(state, -infinity, +infinity)
        v, index = self.max_value(state, -sys.maxsize - 1, sys.maxsize, depth, -1)
        iterator = index
        while (state.a[iterator] == 0):
            iterator = abs(iterator + 1 % 6)
        return index

    def max_value (self, state, alpha, beta, depth, last_index) :
        # inputs: current state in the game
        # a, the value of the best alternative for MAX along the path to state
        # b, the value of the best alternative for MIN along the path to state

        # if Terminal-Test(state) then return Utility(state)
        if (self.terminal_state(state, depth)):
            return (self.get_utility(state, "a"), last_index)

        # v <- -inf
        v = -sys.maxsize - 1
        index = -1

        # generate successors
        children = self.generate_successors(state, "a")

        # for a, s in Successors(state), do
        for child in children:
            curr_state = child[0]
            value = 0
            curr_index = 0
            # v <- Max(v, min_value(s, a, b))

            if (curr_state.repeat == True):
                print("double turn")
                value, curr_index = self.max_value(curr_state, alpha, beta, depth, child[1])
            else:
                value, curr_index = self.min_value(curr_state, alpha, beta, depth - 1, child[1])

            if (value > v):
                index = child[1]
            v = max(v, value)

            # if v >= b then return v (cutoff)
            if v >= beta:
                return (v, index)
            # a <- Max(a, v)
            alpha = max(alpha, v)

        # return v and index
        return (v, index)

    def min_value (self, state, alpha, beta, depth, last_index) :
        # inputs: current state in the game
        # alpha, the value of the best alternative for MAX along the path to state
        # beta, the value of the best alternative for MIN along the path to state

        # if Terminal-Test(state) then return Utility(state)
            # check if game is over or out of time
            # return state: a_fin - b_fin
        if (self.terminal_state(state, depth)):
            return (self.get_utility(state, "b"), last_index)
        # v <- +inf
        v = sys.maxsize
        index = -1
        # generate successors
        children = self.generate_successors(state, "b") # but for the other player!
        # for a, s in Successors(state), do
        for child in children:
            curr_state = child[0]
            value= 0
            curr_index = 0
            # v <- Min(v, max_value(s, a, b))
            if (curr_state.repeat == True):
                print("double turn")
                value, curr_index = self.min_value(curr_state, alpha, beta, depth, child[1])
            else:
                value, curr_index = self.max_value(curr_state, alpha, beta, depth - 1, child[1])
            if (value < v):
                index = child[1]
            v = min(v, value)
            # if v <= a then return v (cutoff)
            if v <= alpha:
                return (v, index)
            # b <- Min(b, v)
            beta = min(beta, v)

        # return v and index
        return (v, index)

    def get_utility(self, state, player):
        # heuristic function
        # of marbles in mine - # of marbles in hers
        a_count = 0
        b_count = 0
        for i in range (5):
            if (i < 4):
                a_count += state.a[i]
                b_count += state.b[i]
            if (i >= 4):
                if (state.a[i] > 0):
                    a_count += 1 + state.a[i]

                if (state.a[i] > 0):
                    b_count += 1 + state.b[i]
        utility = (a_count - b_count)
        # number of stones in the Kalah
        utility += 100 * (state.a_fin - state.b_fin)
        return utility

    def generate_successors(self, state, player):
        # generates all successor for player
        # only pick buckets with non zero items
        # return an array of tuples(state, index_chosen)
        children = []

        if player == "a":
            for i in range (6):
                if (state.a[i] != 0):
                    curr_state = self.make_successor_state_a(i, state)
                    children.append((curr_state, i))
        if player == "b":
            for i in range (6):
                num = state.b[i]
                if (num != 0):
                    children.append((self.make_successor_state_b(i, state), i))
        return children

    def make_successor_state_a(self, i, state) :
        # generates a successor for player a given the index to move
        curr_state = self.state(state.a.copy(), state.b.copy(), state.a_fin,
                        state.b_fin)
        num = state.a[i]
        curr_state.a[i] = 0
        index = 0
        for j in range (num):
            j += 1
            index = (j + i) % 13
            if (index < 6):
                curr_state.a[index] += 1
            if (index == 6):
                curr_state.a_fin += 1
            if (index > 6 and index < 13):
                index -= 7
                curr_state.b[index] += 1

        # if the last stone lands in an empty hole
        if (index >= 0 and index <= 5 and curr_state.a[index] == 1 and
            curr_state.b[abs(index - 5)] != 0):
            curr_state.a_fin += curr_state.b[abs(index - 5)] + 1
            curr_state.a[index] = 0
            curr_state.b[abs(index - 5)] = 0
        # handles case where there are no stones remaining on one side
        count = 0
        for k in range (6):
            if curr_state.a[k] == 0:
                count += 1
        if (count == 6):
            for k in range (6):
                state.b_fin += curr_state.b[k]
                curr_state.b[k] = 0
        if (index == 6):
            curr_state.repeat == True
        return curr_state

    def make_successor_state_b(self, i, state):
        # generates a successor for player b given the index to move
        curr_state = self.state(state.a.copy(), state.b.copy(), state.a_fin,
                        state.b_fin)
        num = state.b[i]
        curr_state.b[i] = 0

        for j in range (num):
            j += 1
            index = (j + i) % 13
            if (index < 6):
                curr_state.b[index] += 1
            if (index == 6):
                curr_state.b_fin += 1
            if (index > 6 and index < 13):
                index -= 7
                curr_state.a[index] += 1

        # if the last stone lands in an empty hole
        if (index >= 0 and index <= 5 and curr_state.b[index] == 1 and
            curr_state.a[abs(index - 5)] != 0):
            # get opponent's stones
            curr_state.b_fin += curr_state.a[abs(index - 5)] + 1
            curr_state.a[abs(index - 5)] = 0
            curr_state.b[index] = 0

        # handles case where there are no stones remaining on one side
        count = 0
        for k in range (6):
            if curr_state.b[k] == 0:
                count += 1
        if (count == 6):
            for k in range (6):
                state.a_fin += curr_state.a[k]
                curr_state.a[k] = 0
        if (index == 6):
            curr_state.repeat == True
        return curr_state

    def terminal_state(self, state, depth):
        # checks termainal state including a winner, timeout, or max depth
        if (state.a_fin > 36) or (state.b_fin > 36):
            return True
        end = time.time()
        elapsed_time = end - self.start_time
        if (elapsed_time >= self.t):
            print("TIMEOUT")
            return True
        if (depth <= 0):
            return True
        return False
