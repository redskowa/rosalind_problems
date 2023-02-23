#import this
import math
from collections import Counter

# ===== Variables and Arithmetic ======#
a = 952
b = 881
#print(a**2 + b**2)


# ===== Strings and Lists ===== #
wordOneStartPos = 73
wordOneEndPos = 83

wordTwoStartPos = 88
wordTwoEndPos = 96

txtStr= "CGjngYkXswUaIhhYSyMJmH8KfXnHX7ICsjs8wXi6eYyA621FMKbrouGOoqUCn1AtGTlHat1GIHydrosaurustMYJcarinatusJXZze1akddrpwEJpsgaaB4ckDulYAAIcpDtw2pgWIPonmLTJU5HxjbREGU4OzbF7dV9."

# Note: End position is not inclusive, we must add one to include it.

# print(f"{txtStr[wordOneStartPos:wordOneEndPos + 1]} {txtStr[wordTwoStartPos:wordTwoEndPos + 1]}")



# ===== Conditions and Loops ===== #

a= 4155
b = 8763

### While solution ###
# x=a
# sum = 0
# while x <= b:
#     if x % 2 != 0:
#         sum += x
#     x += 1
# print(sum)

### Range solution ###
# result = 0

# for x in range(a, b+1):
#     if x % 2 != 0:
#         result += x

### List Comprehension ###
result = sum([x for x in range(a, b+1) if x % 2 != 0])

print(result)


## ===== Reading and Writing ===== ##
outputFile = []

with open("./village/input.txt", "r") as f:
    outputFile = [line for pos, line in enumerate(f.readlines()) if pos % 2 != 0]
    # using list comprehension

with open('./village/out.txt', 'w') as f:
    f.write(''.join([line for line in outputFile]))

## ===== Intro to Python Dictionary ===== ##

txtStr = 'When I find myself in times of trouble Mother Mary comes to me Speaking words of wisdom let it be And in my hour of darkness she is standing right in front of me Speaking words of wisdom let it be Let it be let it be let it be let it be Whisper words of wisdom let it be And when the broken hearted people living in the world agree There will be an answer let it be For though they may be parted there is still a chance that they will see There will be an answer let it be Let it be let it be let it be let it be There will be an answer let it be Let it be let it be let it be let it be Whisper words of wisdom let it be Let it be let it be let it be let it be Whisper words of wisdom let it be And when the night is cloudy there is still a light that shines on me Shine until tomorrow let it be I wake up to the sound of music Mother Mary comes to me Speaking words of wisdom let it be Let it be let it be let it be yeah let it be There will be an answer let it be Let it be let it be let it be yeah let it be Whisper words of wisdom let it be'

# wordCountDict = {}

# for word in txtStr.split(' '):
#     if word in wordCountDict:
#         wordCountDict[word] += 1
#     else:
#         wordCountDict[word] = 1

wordCountDict = Counter(txtStr.split(' '))

for key, value in wordCountDict.items():
    print(key, value)