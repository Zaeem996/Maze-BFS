import time
def enqueue(lst,x):
    lst.append(x)
    return lst
def dequeue(lst):
    return lst.pop(0)
def is_empty(lst):
    if len(lst)==0:
        return True
    else:
        return False
maze1=[["O"," ","#"],["#"," ","#"],["#","X","#"]]

def createMaze2():
    maze = []
    maze.append(["#","#", "#", "#", " ", "#", "#", "#", "#"])
    maze.append(["#"," ", " ", "X", " ", " ", " ", " ", "#"])
    maze.append(["#"," ", "#", "#", " ", "#", "#", " ", "#"])
    maze.append(["#"," ", "#", " ", " ", " ", "#", " ", "#"])
    maze.append(["#"," ", "#", " ", "#", " ", "#", " ", "#"])
    maze.append(["#"," ", "#", " ", "#", " ", "#", " ", "#"])
    maze.append(["#"," ", "#", " ", "#", " ", "#", " ", "#"])
    maze.append(["#"," ", " ", " ", " ", " ", " ", " ", "#"])
    maze.append(["#","#", "#", "#", "#", "#", "#", "O", "#"])

    return maze
maze=createMaze2()
def printMaze(maze, path):# it prints the shortest path present. 
    for k in range(len(maze)):
        for x, pos in enumerate(maze[k]):
            if pos == "O":
                start = x
                bstart=k
    i=start
    j=bstart
    pos=set() #tracks indexing in set
    for move in path:
        if move == "L":           #>>>>>>>>>>>T(O)=2nm+n+m-2+k
            i -= 1
        elif move == "R":
            i += 1
        elif move == "U":
            j -= 1
        else:
            j+=1
        pos.add((j, i))
    
    for j, row in enumerate(maze):
        for i, col in enumerate(row):# looks every single element in maze
            if (j, i) in pos:
                print("+ ",end="")# elements in pos are of shortest path so there it prints "+"
            else:
                print(col + " ",end="")# prints "#" in maze
        print(" ")

def valid(maze, moves): # checks possible movement and return true if path exists
    for k in range(len(maze)):
        for x, pos in enumerate(maze[k]):
            if pos == "O":
                start = x
                bstart=k
    i=start
    j=bstart
    for move in moves:     #>>>>>>>>>>>>>>>>>>>>> T(O)=nm+n+m-2+k
        if move == "L":
            i -= 1

        elif move == "R":
            i += 1
        elif move == "U":
            j -= 1
        else:
            j += 1

        if not(0 <= i < len(maze[0]) and 0 <= j < len(maze)):
            return False
        elif (maze[j][i] == "#"):
            return False

    return True


def findEnd(maze, moves): # iteration for looking if reached end node
    for k in range(len(maze)):
        for x, pos in enumerate(maze[k]):
            if pos == "O":
                start = x
                bstart=k
    i=start
    j=bstart
    for move in moves:# taraverse possible path
        if move == "L":
            i -= 1
        elif move == "R":
            i += 1
        elif move == "U":    #>>>>>>>>>>>>>T(O)=3nm+2n+2m-4+k
            j -= 1
        else:
            j += 1
    if maze[j][i] == "X": #end point condition
        print("Found: " + moves)#returns a string of shortest path
        printMaze(maze, moves)# calling print function
        return True
    return False
t1=time.time()
def maze_sol(maze):#>>>>T(O)=(3nm+2n+2m-4)(nm+n+m-2)
    ways=["U","D","L","R"]
    nums = []# it is a queue used to track all possible routes 
    nums=enqueue(nums,"")
    add = ""
    while not findEnd(maze, add):# exits when end results is found
        add = dequeue(nums)
        #print(add)
        for k in ways:# traverse on all possible child nodes
            put = add + k
            if valid(maze, put): # check all posiible valid movements and track each true path in nums queue
                enqueue(nums,put)
print(maze_sol(maze))
tf=time.time()-t1
print(tf)
