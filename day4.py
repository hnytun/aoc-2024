file1 = open('inputs/day4.txt', 'r')
lines = file1.read().split('\n')

def create_grid(lines):
    grid = []
    for line in lines:
        row = []
        for char in line:
            row.append(char)
        grid.append(row)
    return grid
        
def check(grid,pos,direction):
    if(direction == "left"):
        if(pos[1] != 0):
            return [pos[0],pos[1]-1]
    if(direction == "right"):        
        if(pos[1]+1 < len(grid[0])):
            return [pos[0],pos[1]+1]
    if(direction == "up"):    
        if(pos[0] != 0):
            return [pos[0]-1,pos[1]]
    if(direction == "down"):
        if(pos[0]+1 < len(grid)):
            return [pos[0]+1,pos[1]]
    if(direction == "upleft"):    
        if(pos[1] != 0 and pos[0] != 0):
            return [pos[0]-1,pos[1]-1]
    if(direction == "upright"):    
        if(pos[0] != 0 and pos[1] +1 < len(grid[0])):
            return [pos[0]-1,pos[1]+1]
    if(direction == "downleft"):
        if(pos[0]+1 < len(grid) and pos[1] != 0):
            return [pos[0]+1,pos[1]-1]
    if(direction == "downright"):  
        if(pos[0]+1 < len(grid) and pos[1]+1 < len(grid[0])):
            return [pos[0]+1,pos[1]+1]
    return None

def get_value(grid,pos):
    return grid[pos[0]][pos[1]]

def checkDirection(grid,pos,direction):
    
    checked = check(grid,pos,direction)
    if(checked != None and get_value(grid,checked)) == "M":
        checked = check(grid,checked,direction)
        if(checked != None and get_value(grid,checked)) == "A":
            checked = check(grid,checked,direction)
            if(checked != None and get_value(grid,checked)) == "S":
                return 1
    return 0

def checkAllDirections(grid,pos):
    sum=0
    directions = ["left","right","up","down","upleft","upright","downleft","downright"]
    for direction in directions:   
        sum += checkDirection(grid,[x,y],direction)
    return sum       

def checkCross(grid,pos):
    topleft = check(grid,pos,"upleft")
    topright = check(grid,pos,"upright")
    bottomleft = check(grid,pos,"downleft")
    bottomright = check(grid,pos,"downright")
    
    if(topleft == None or topright == None or bottomleft == None or bottomright == None):
        return False
    
    topleft = grid[topleft[0]][topleft[1]]
    topright = grid[topright[0]][topright[1]]
    bottomleft = grid[bottomleft[0]][bottomleft[1]]
    bottomright = grid[bottomright[0]][bottomright[1]]
    
    if(topleft == "M" and topright == "S" and bottomleft == "M" and bottomright == "S"):
        return True
    elif(topleft == "S" and topright == "S" and bottomleft == "M" and bottomright == "M"):
        return True
    elif(topleft == "M" and topright == "M" and bottomleft == "S" and bottomright == "S"):
        return True
    elif(topleft == "S" and topright == "M" and bottomleft == "S" and bottomright == "M"):
        return True
    else:
        return False
    
grid = create_grid(lines)
sum1=0
sum2=0
for x in range(0,len(grid)):
    for y in range(0,len(grid[0])):
        if(grid[x][y] == "X"):
            sum1 += checkAllDirections(grid,[x,y])
        if(grid[x][y] == "A"):
            if(checkCross(grid,[x,y])):
                sum2+=1

print("part1: ", sum1)      
print("part2: ", sum2)

    
