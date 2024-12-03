import re

#file1 = open('inputs/day3_sample.txt', 'r')
#file1 = open('inputs/day3_sample2.txt', 'r')
file1 = open('inputs/day3.txt', 'r')
input = file1.read()

def get_matches(regex,text):
    matches = re.findall(regex,text)    
    return matches

#mul(11,8) -> 11,8
def parse_mul_match(mul_match):
    return mul_match.replace("(",'').replace(")",'').split("mul")[1].split(",")
        
regex_part1 = "mul\\(\\d*,\\d*\\)"    
matches = get_matches(regex_part1,input)

result=0
for mul in matches:
    mul = parse_mul_match(mul)
    result += int(mul[0])*int(mul[1])
    
print("part1: ", result)

regex_part2 = "do\(\)|don't\(\)|mul\(\d*,\d*\)"
matches = get_matches(regex_part2,input)

do=True
result2=0
for match in matches:
    
    if(match == "do()"):
        do=True
    elif(match == "don't()"):
        do=False
    
    if(match.startswith("mul") and do):
        mul = parse_mul_match(match)
        result2 += int(mul[0])*int(mul[1])
print("part2: ", result2)