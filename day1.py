file1 = open('inputs/day1.txt', 'r')
lines = file1.read().split('\n')

distances=0
left=[]
right=[]
for pair in lines:
    left.append(int(pair.split("   ")[0]))
    right.append(int(pair.split("   ")[1]))
    
left.sort()
right.sort()

for i in range(0,len(left)):
    distance = abs(left[i] - right[i])
    distances+=distance

print("part 1")
print(distances)    

similarities = 0
for i in range(0,len(left)):
    similarity = left[i] * right.count(left[i])
    similarities += similarity
    
print("part 2")
print(similarities)
