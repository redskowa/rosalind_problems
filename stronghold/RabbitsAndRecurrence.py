def Fibonacci_Loop_Pythonic(months, offsprings):
    parent, child = 1, 1
    for itr in range(months - 1):
        child, parent = parent, parent + (child * offsprings)
    return child

print(Fibonacci_Loop_Pythonic(29,4))


# o - small (children) rabbits. They have to mature and reproduce the next cycle only
# 0 - mature (parents) rabbits. They reproduce and move to next cycle

# Month 1: [o]
# Month 2: [0]
# Month 3: [0 o o]
# Month 4: [0 o o 0 0]
# Month 5: [0 o o 0 o o 0 o o 0 0]

## This is a recursion solution, it is less performant due to the function calls

# def rabbitPairs(numMonths, numOffspring):
#     if numMonths == 1:
#         return 1
#     elif numMonths == 2:
#         return numOffspring

#     oneGen = rabbitPairs(numMonths - 1, numOffspring)
#     twoGen = rabbitPairs(numMonths - 2, numOffspring)

#     if numMonths <= 4:
#         return (oneGen + twoGen)

#     return (oneGen + (twoGen * numOffspring))

# print(rabbitPairs(35, 5))