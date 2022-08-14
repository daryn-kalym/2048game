import random 
class Game2048:
    def __init__(self) -> None:
        self.gamemap = [[0 for i in range(4)] for j in range(4)]
        i,j,k,l = [random.randint(0,3) for p in range(4)]
        self.gamemap[i][j] = 2
        self.gamemap[k][l] = 2
    def __repr__(self) -> str:
        return "{}\n{}\n{}\n{}".format(self.gamemap[0],self.gamemap[1],self.gamemap[2],self.gamemap[3])
    def isAbleToMoveOneStep(self,index,direction):
        # 1 - left
        # 2 - right
        # 3 - up
        # 4 - down
        row = self.gamemap[index[0]] # vertical direction
        idx = index[1] # horizontal direction
        if direction == 1:
            if row[idx-1] == 0 or row[idx] == row[idx-1]:
                return True
        elif direction == 2:
            if row[idx+1] == 0 or row[idx] == row[idx+1]:
                return True
        elif direction == 3:
            if self.gamemap[index[0]-1][index[1]] == 0 or self.gamemap[index[0]-1][index[1]] == self.gamemap[index[0]][index[1]]:
                return True
        elif direction == 4:
            if self.gamemap[index[0]+1][index[1]] == 0 or self.gamemap[index[0]+1][index[1]] == self.gamemap[index[0]][index[1]]:
                return True
        return False
    def create2(self):
        # check if the map is full
        counter = 0
        for i in range(len(self.gamemap)):
            row = self.gamemap[i]
            for j in range(len(row)):
                if self.gamemap[i][j] != 0:
                    counter+=1
        if counter == 16:
            print("----------")
            print("Game over!")
            print("----------")
            exit()

        #check if the game is won
        for i in range(len(self.gamemap)):
            row = self.gamemap[i]
            for j in range(len(row)):
                if self.gamemap[i][j] == 2048:
                    print(self)
                    print("You won the game!")
                    exit()

        #Create new element
        i,j = random.randint(0,3),random.randint(0,3)
        while self.gamemap[i][j] != 0:
            i,j = random.randint(0,3),random.randint(0,3)
        print("Creating 2 at [{},{}]".format(i,j))
        self.gamemap[i][j] = 2
    def moveLeft(self,technical = False):
        if technical:
            self.transform()
        left = 1
        for i in range(len(self.gamemap)):
            row = self.gamemap[i]
            for j in range(1,len(row)):
                if row[j] != 0:
                    k = i
                    l = j
                    while l-1>=0 and self.isAbleToMoveOneStep([k,l],left):
                        if row[l-1] == 0:
                            row[l-1],row[l] = row[l],row[l-1]
                            l -= 1
                        elif row[l-1] == row[l]:
                            row[l-1] += row[l]
                            row[l] = 0
                            break
        if technical:
            self.transform()
        self.create2()
        print("---------")
        print(self)
    def moveRight(self,technical = False):
        if technical:
            self.transform()
        right = 2
        for i in range(len(self.gamemap)):
            row = self.gamemap[i]
            for j in range(len(row)-2,-1,-1):
                if row[j] != 0:
                    k = i
                    l = j
                    while l+1 < len(row) and self.isAbleToMoveOneStep([k,l],right):
                        if row[l+1] == 0:
                            row[l+1],row[l] = row[l],row[l+1]
                            l += 1
                            # break
                        elif row[l+1] == row[l]:
                            row[l+1] += row[l]
                            row[l] = 0
                            break
        if technical:
            self.transform()
        self.create2()
        print("---------")
        print(self)
    def transform(self):
        self.gamemap = [[self.gamemap[j][i] for j in range(len(self.gamemap[i]))] for i in range(len(self.gamemap))]
    def moveUp(self):
        self.moveLeft(technical = True)
    def moveDown(self):
        self.moveRight(technical = True)
g = Game2048()
print(g)
print("---------")
while True:
    next_move = int(input())
    if next_move == 1:
        print("Moving left")
        g.moveLeft()
    elif next_move == 2:
        print("Moving right")
        g.moveRight()
    elif next_move == 3:
        print("Moving up")
        g.moveUp()
    elif next_move == 4:
        print("Moving down")
        g.moveDown()



# while True:
#     q = input("What's the next move?: ")
#     if q == "l":
#         g.moveLeft()
#     elif q == "r":
#         g.moveRight()

# for i in range(100):
#     g.moveDown()