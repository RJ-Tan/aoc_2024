"""
--- Day 7: Bridge Repair ---

The Historians take you to a familiar rope bridge over a river in the middle of a jungle. The Chief isn't on this side of the bridge, though; maybe he's on the other side?

When you go to cross the bridge, you notice a group of engineers trying to repair it. (Apparently, it breaks pretty frequently.) You won't be able to cross until it's fixed.

You ask how long it'll take; the engineers tell you that it only needs final calibrations, but some young elephants were playing nearby and stole all the operators from their calibration equations! They could finish the calibrations if only someone could determine which test values could possibly be produced by placing any combination of operators into their calibration equations (your puzzle input).

For example:

190: 10 19
3267: 81 40 27
83: 17 5
156: 15 6
7290: 6 8 6 15
161011: 16 10 13
192: 17 8 14
21037: 9 7 18 13
292: 11 6 16 20

Each line represents a single equation. The test value appears before the colon on each line; it is your job to determine whether the remaining numbers can be combined with operators to produce the test value.

Operators are always evaluated left-to-right, not according to precedence rules. Furthermore, numbers in the equations cannot be rearranged. Glancing into the jungle, you can see elephants holding two different types of operators: add (+) and multiply (*).

Only three of the above equations can be made true by inserting operators:

    190: 10 19 has only one position that accepts an operator: between 10 and 19. Choosing + would give 29, but choosing * would give the test value (10 * 19 = 190).
    3267: 81 40 27 has two positions for operators. Of the four possible configurations of the operators, two cause the right side to match the test value: 81 + 40 * 27 and 81 * 40 + 27 both equal 3267 (when evaluated left-to-right)!
    292: 11 6 16 20 can be solved in exactly one way: 11 + 6 * 16 + 20.

The engineers just need the total calibration result, which is the sum of the test values from just the equations that could possibly be true. In the above example, the sum of the test values for the three equations listed above is 3749.

Determine which equations could possibly be true. What is their total calibration result?

"""
calibrations = []
with open("./Day7/day7_input.txt","r",encoding="utf-8") as file:

      for line in file:
            temp = line.split(sep=":")
            temp[0] = int(temp[0])
            temp[1] = list(map(lambda x: int(x), temp[1].strip().split(' ')))

            calibrations.append(tuple(temp))

#Part1
def eval_leftright(nums:list[int], ops:str)->int:
      nums_cp = nums[::-1].copy()
      for op in ops:
            t1 = nums_cp.pop()
            t2 = nums_cp.pop()
            if op == 'x':
                  nums_cp.append(t1*t2)
            elif op == '+':
                  nums_cp.append(t1+t2)
      return nums_cp[0]


def gen_op_combinations(n:int)->list[str]:
      if n == 0:
            return ['']
      smaller_combinations = gen_op_combinations(n-1)
      combinations = []
      for combo in smaller_combinations:
            combinations.append(combo + '+')
            combinations.append(combo + 'x')      
      return combinations

def solution1(inp_mat:list[tuple[int,list[int]]])->int:
      res = 0
      ops_combo_cache:dict[int, list[str]] = dict()
      count = 0
      for target, nums in inp_mat:
            operator_combos = []
            if (len(nums) - 1) in ops_combo_cache:
                  operator_combos = ops_combo_cache[len(nums)-1]
            else:
                  ops_combo_cache[len(nums)-1] = gen_op_combinations(len(nums)-1)
                  operator_combos = ops_combo_cache[len(nums)-1]

            for combo in operator_combos:
                  if eval_leftright(nums, combo) == target:
                        count += 1
                        res += target
                        break

      return res

print(f"The answer for Part1: {solution1(calibrations)}")
#3119088655389

from collections.abc import Callable
from collections import deque

#Part2
def gen_possible_results(nums:list[int], ops:list[Callable[[int,int],int]])->list[int]:
      if len(nums) < 2:
            return set(nums)
      possible_results = [nums[0]]
      for i in range(1,len(nums)):
            temp = []

            while len(possible_results) > 0 and (cur := possible_results.pop()):
                  temp.append(cur*nums[i])
                  temp.append(cur+nums[i])
                  temp.append(int(str(cur)+str(nums[i])))
            possible_results = temp

      return possible_results

def solution2(inp_mat:list[tuple[int,list[int]]])->int:
      res = 0
      operators = [(lambda x,y: x*y), (lambda x,y: x+y), (lambda x, y: int(str(x)+str(y)))]
      for target, nums in inp_mat:
 
            possible_results = gen_possible_results(nums, operators)
            if target in possible_results:
                  res += target
      return res


print(f"The answer for Part2: {solution2(calibrations)}")
#264184041398847