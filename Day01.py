'''
 Write a program which will find all such numbers which are divisible by 7
 but are not a multiple of 5, between 2000 and 3200 (both included).
 The numbers obtained should be printed in a comma-separated sequence on a single line.
'''

numbers = []
results = []
for i in range(2000, 3201):
    numbers.append(i)

for num in numbers:
    if num % 7 == 0 and num % 5 !=0:
        results.append(num)

print(results)
