#file1 = open('inputs/day2_sample.txt', 'r')
file1 = open('inputs/day2.txt', 'r')
lines = file1.read().split('\n')


def allVariancesValid(line):
    for i in range(1,len(line)):
        variance = abs(int(line[i]) - int(line[i-1]))
        if(variance > 3 or variance < 1):
            return False
    return True


def CheckIfLineIsSafe(line):
    varyingCorrectly = True
    decreasingCorrectly = line == list(reversed(sorted(line, key = lambda x: (int(x)))))
    increasingCorrectly = line == sorted(line, key = lambda x: (int(x)))
    
    if(not allVariancesValid(line)):
        varyingCorrectly = False
  
    return (increasingCorrectly or decreasingCorrectly) and varyingCorrectly

problem_dampener = True     
safe=0

for line in lines:
    original_line = line.split(" ")
    if(CheckIfLineIsSafe(original_line)):
        safe+=1
    elif(problem_dampener):
        new_line = line.split(" ")
        for i in range(0,len(new_line)):
            test_line = new_line.copy()
            test_line.pop(i)
            if(CheckIfLineIsSafe(test_line)):
                safe+=1
                break
            
print(safe)


        
#['4', '5', '6', '9', '12', '15']

#testlineSorted doesnt work?=?

