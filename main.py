class Board:

    def __init__(self):
        # 4 by 4 board
        # self.board is the goal board when first initialized
        self.board = [range(1, 5),
                      range(5, 9),
                      range(9, 13),
                      range(13, 16) + ['*']]
        # self.goal is later used as a comparison to solve the mixed board
        self.goal = []
        for i in self.board:
            self.goal.append(tuple(i))
        self.goal = tuple(self.goal)
        # self.empty is the position of empty block
        self.empty = [3, 3]

def __repr__(self):
    string = ''
    for row in self.board:
        for num in row:
            if len(str(num)) == 1:
                string += '   ' + str(num)
            elif len(str(num)) > 1:
                string += '  ' + str(num)
        string += '\n'
    return string

# Function to print a BFS of graph
def BFS(self, s):
    # Mark all the vertices as not visited
    visited = [False] * (len(self.graph))

    # Create a queue for BFS
    queue = []

    # Mark the source node as visited and enqueue it
    queue.append(s)
    visited[s] = True

    while queue:

        # Dequeue a vertex from queue and print it
        s = queue.pop(0)
        print
        s,

        # Get all adjacent vertices of the dequeued
        # vertex s. If a adjacent has not been visited,
        # then mark it visited and enqueue it
        for i in self.graph[s]:
            if visited[i] == False:
                queue.append(i)
                visited[i] = True

def solve(self):
    start = self.convert_to_tuple(self.board)
    pred = {}
    visited = []
    frontier = Queue.Queue()
    frontier.put(start)

    while frontier.qsize() > 0:
        tmp = frontier.get()

        if tmp == self.goal:
            path = []
            while tmp != start:
                path.append(pred[tmp][1])
                tmp = pred[tmp][0]
            return path[::-1]

        if tmp not in visited:
            visited.append(tmp)
            tmpboard = self.match(tmp)
            tmpboard.move_up()
            if self.convert_to_tuple(tmpboard.board) != tmp:
                frontier.put(self.convert_to_tuple(tmpboard.board))
                if not pred.has_key(self.convert_to_tuple(tmpboard.board)):
                    pred[self.convert_to_tuple(tmpboard.board)] = [tmp, 'up']

            tmpboard = self.match(tmp)
            tmpboard.move_down()
            if self.convert_to_tuple(tmpboard.board) != tmp:
                frontier.put(self.convert_to_tuple(tmpboard.board))
                if not pred.has_key(self.convert_to_tuple(tmpboard.board)):
                    pred[self.convert_to_tuple(tmpboard.board)] = [tmp, 'down']

            tmpboard = self.match(tmp)
            tmpboard.move_right()
            if self.convert_to_tuple(tmpboard.board) != tmp:
                frontier.put(self.convert_to_tuple(tmpboard.board))
                if not pred.has_key(self.convert_to_tuple(tmpboard.board)):
                    pred[self.convert_to_tuple(tmpboard.board)] = [tmp, 'right']

            tmpboard = self.match(tmp)
            tmpboard.move_left()
            if self.convert_to_tuple(tmpboard.board) != tmp:
                frontier.put(self.convert_to_tuple(tmpboard.board))
                if not pred.has_key(self.convert_to_tuple(tmpboard.board)):
                    pred[self.convert_to_tuple(tmpboard.board)] = [tmp, 'left']

    raise Exception('There is no solution.')
