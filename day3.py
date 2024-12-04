"""
--- Day 3: Mull It Over ---

"Our computers are having issues, so I have no idea if we have any Chief Historians in stock! You're welcome to check the warehouse, though," says the mildly flustered shopkeeper at the North Pole Toboggan Rental Shop. The Historians head out to take a look.

The shopkeeper turns to you. "Any chance you can see why our computers are having issues again?"

The computer appears to be trying to run a program, but its memory (your puzzle input) is corrupted. All of the instructions have been jumbled up!

It seems like the goal of the program is just to multiply some numbers. It does that with instructions like mul(X,Y), where X and Y are each 1-3 digit numbers. For instance, mul(44,46) multiplies 44 by 46 to get a result of 2024. Similarly, mul(123,4) would multiply 123 by 4.

However, because the program's memory has been corrupted, there are also many invalid characters that should be ignored, even if they look like part of a mul instruction. Sequences like mul(4*, mul(6,9!, ?(12,34), or mul ( 2 , 4 ) do nothing.

For example, consider the following section of corrupted memory:

xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))

Only the four highlighted sections are real mul instructions. Adding up the result of each instruction produces 161 (2*4 + 5*5 + 11*8 + 8*5).

Scan the corrupted memory for uncorrupted mul instructions. What do you get if you add up all of the results of the multiplications?
"""
#Part1
totalSum = 0
inputStr = ""
def isNumeric(c:str):
      return c.isnumeric()

checksVec = [lambda x: x == '(', isNumeric, lambda x: x == ',', isNumeric, lambda x: x == ')']

with open("day3_input.txt","r",encoding="utf-8") as file:
      for line in file:
            inputStr += line

instructionList = inputStr.split(sep='mul')

for instruction in instructionList:

      instrStack = list(instruction[::-1])
      checkId = 0
      num1 = ''
      num2 = ''

      while checkId <= 4 and instrStack != []:
            c = instrStack[-1]

            if checksVec[checkId](c) == True:
       
                  if checkId == 1:
                        num1 += instrStack.pop()
                  elif checkId == 3:
                        num2 += instrStack.pop()
                  else:
                        checkId += 1
                        instrStack.pop()
            elif checkId == 1 or checkId == 3:
                  checkId += 1
            else:
                  break

      if checkId > 4 and num1.isnumeric() and num2.isnumeric():
            totalSum += int(num1) * int(num2)                  


print(f"The total sum for Part One is {totalSum}")
#Ans: 175015740

"""
--- Part Two ---
As you scan through the corrupted memory, you notice that some of the conditional statements are also still intact. 
If you handle some of the uncorrupted conditional statements in the program, you might be able to get an even more accurate result.

There are two new instructions you'll need to handle:

    The do() instruction enables future mul instructions.
    The don't() instruction disables future mul instructions.

Only the most recent do() or don't() instruction applies. At the beginning of the program, mul instructions are enabled.

For example:

xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))

This corrupted memory is similar to the example from before, but this time the mul(5,5) and mul(11,8) instructions are disabled because there is a don't() instruction before them. 
The other mul instructions function normally, including the one at the end that gets re-enabled by a do() instruction.

This time, the sum of the results is 48 (2*4 + 8*5).

Handle the new instructions; what do you get if you add up all of the results of just the enabled multiplications?"""

#PartTwo
inputList = ['d','o','(',')',*list(inputStr)]
currentSubStr = ""
totalSum = 0
while inputList != []:
      
      currentSubStr += inputList.pop() #

      if "don't()" in currentSubStr[::-1]:
      
            currentSubStr = ""

      elif "do()" in currentSubStr[::-1]:

            toDoList = currentSubStr[::-1]
            toDoList = toDoList.split(sep="mul")
      
            for todo in toDoList:

                  todoStack = list(todo[::-1])
                  checkId = 0
                  num1 = ''
                  num2 = ''

                  while checkId <= 4 and todoStack != []:
                        c = todoStack[-1]

                        if checksVec[checkId](c) == True:
                  
                              if checkId == 1:
                                    num1 += todoStack.pop()
                              elif checkId == 3:
                                    num2 += todoStack.pop()
                              else:
                                    checkId += 1
                                    todoStack.pop()
                        elif checkId == 1 or checkId == 3:
                              checkId += 1
                        else:
                              break

                  if checkId > 4 and num1.isnumeric() and num2.isnumeric():
           
                        totalSum += int(num1) * int(num2)        

            currentSubStr = ""


print(f"The total sum for Part Two is: {totalSum}")
#Ans: 112272912 



