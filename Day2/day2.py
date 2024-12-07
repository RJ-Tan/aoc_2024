"""
--- Day 2: Red-Nosed Reports ---

Fortunately, the first location The Historians want to search isn't a long walk from the Chief Historian's office.

While the Red-Nosed Reindeer nuclear fusion/fission plant appears to contain no sign of the Chief Historian, the engineers there run up to you as soon as they see you. 
Apparently, they still talk about the time Rudolph was saved through molecular synthesis from a single electron.

They're quick to add that - since you're already here - they'd really appreciate your help analyzing some unusual data from the Red-Nosed reactor. 
You turn to check if The Historians are waiting for you, but they seem to have already divided into groups that are currently searching every corner of the facility. 
You offer to help with the unusual data.

The unusual data (your puzzle input) consists of many reports, one report per line. 
Each report is a list of numbers called levels that are separated by spaces. For example:

7 6 4 2 1
1 2 7 8 9
9 7 6 2 1
1 3 2 4 5
8 6 4 4 1
1 3 6 7 9

This example data contains six reports each containing five levels.

The engineers are trying to figure out which reports are safe. 
The Red-Nosed reactor safety systems can only tolerate levels that are either gradually increasing or gradually decreasing. 
So, a report only counts as safe if both of the following are true:

    The levels are either all increasing or all decreasing.
    Any two adjacent levels differ by at least one and at most three.

In the example above, the reports can be found safe or unsafe by checking those rules:

    7 6 4 2 1: Safe because the levels are all decreasing by 1 or 2.
    1 2 7 8 9: Unsafe because 2 7 is an increase of 5.
    9 7 6 2 1: Unsafe because 6 2 is a decrease of 4.
    1 3 2 4 5: Unsafe because 1 3 is increasing but 3 2 is decreasing.
    8 6 4 4 1: Unsafe because 4 4 is neither an increase or a decrease.
    1 3 6 7 9: Safe because the levels are all increasing by 1, 2, or 3.

So, in this example, 2 reports are safe.

Analyze the unusual data from the engineers. How many reports are safe?

"""
#Part1
dataMat = []
numSafe = 0
with open("day2_input.txt","r", encoding="utf-8") as file:
      for line in file:
            cur = line.rstrip("\n").split(sep=" ")
            dataMat.append(list(map(lambda x: int(x),cur)))

for report in dataMat:
      isSafe = True
      assumption1 = (lambda x,y: x <= y) if report[0] < report[-1] else (lambda x, y: x >= y)      
      assumption2 = (lambda x,y: 1 <= abs(x-y) <= 3)

      for i in range(len(report)-1):
            if not assumption1(report[i],report[i+1]) or not assumption2(report[i],report[i+1]):
                  isSafe = False
                  break

      if isSafe:
            numSafe += 1
print(f"The number of safe reports are {numSafe}")

#Part2
numSafe = 0 

def isMajorityIncreasing(nums:list[int]):
      count = 0
      for i in range(len(nums)-1):
            if nums[i] <= nums[i+1]:
                  count += 1
      
      return count > len(nums)/2

for report in dataMat:
      assumption1 = (lambda x,y: x <= y) if isMajorityIncreasing(report) else (lambda x, y: x >= y)    
      assumption2 = (lambda x,y: 1 <= abs(x-y) <= 3)
      potentiallyUnsafe = []
      isSafe = True
      safeCheck1 = True
      safeCheck2 = True

      for i in range(len(report)-1):
            if not assumption1(report[i],report[i+1]) or not assumption2(report[i],report[i+1]):
                  potentiallyUnsafe.append([*report[:i],*report[i+1:]])
                  potentiallyUnsafe.append([*report[:i+1],*report[i+2:]])
                  isSafe = False
                  break
      
      if potentiallyUnsafe:
            for i in range(len(potentiallyUnsafe[0])-1):
                  if not assumption1(potentiallyUnsafe[0][i],potentiallyUnsafe[0][i+1]) or not assumption2(potentiallyUnsafe[0][i],potentiallyUnsafe[0][i+1]):
                        safeCheck1 = False
                        break
            for i in range(len(potentiallyUnsafe[1])-1):
                  if not assumption1(potentiallyUnsafe[1][i],potentiallyUnsafe[1][i+1]) or not assumption2(potentiallyUnsafe[1][i],potentiallyUnsafe[1][i+1]):
                        safeCheck2 = False
                        break

      if isSafe or safeCheck1 or safeCheck2:
            numSafe += 1
      
print(f"The number of safe reports are {numSafe}")