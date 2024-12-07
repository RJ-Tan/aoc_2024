"""
--- Day 4: Ceres Search ---

"Looks like the Chief's not here. Next!" One of The Historians pulls out a device and pushes the only button on it. After a brief flash, you recognize the interior of the 
Ceres monitoring station!

As the search for the Chief continues, a small Elf who lives on the station tugs on your shirt; she'd like to know if you could help her with her word search 
(your puzzle input). 
She only has to find one word: XMAS.

This word search allows words to be horizontal, vertical, diagonal, written backwards, or even overlapping other words. 
It's a little unusual, though, as you don't merely need to find one instance of XMAS - you need to find all of them. Here are a few ways XMAS might appear, 
where irrelevant characters have been replaced with .:

..X...
.SAMX.
.A..A.
XMAS.S
.X....

The actual word search will be full of letters instead. For example:

MMMSXXMASM
MSAMXMSMSA
AMXSXMAAMM
MSAMASMSMX
XMASAMXAMM
XXAMMXXAMA
SMSMSASXSS
SAXAMASAAA
MAMMMXMMMM
MXMXAXMASX

In this word search, XMAS occurs a total of 18 times; here's the same word search again, but where letters not involved in any XMAS have been replaced with .:

....XXMAS.
.SAMXMS...
...S..A...
..A.A.MS.X
XMASAMX.MM
X.....XA.A
S.S.S.S.SS
.A.A.A.A.A
..M.M.M.MM
.X.X.XMASX

Take a look at the little Elf's word search. How many times does XMAS appear?
"""
input_mat = [] #2D matrix containing the word search
with open("day4_input.txt", "r", encoding="utf-8") as file:
      for line in file:
            input_mat.append(list(line))

#Part1
def solution(input_mat:list[list[str]]) -> int:
      directions = [(1,0),(1,1),(0,1),(-1,1),(-1,0),(-1,-1),(0,-1),(1,-1)] #UP, UP-RIGHT, RIGHT, DOWN-RIGHT, DOWN, DOWN-LEFT, LEFT, UP-LEFT     
      count = 0
      x_locs = []
      for i in range(len(input_mat)):
            for j in range(len(input_mat[i])):
                  if input_mat[i][j] == 'X':
                        x_locs.append((i,j))

      for loc in x_locs:
            m, n = loc
            for d in directions:

                  if not (0 <= m + d[0]*3 <= len(input_mat) -1 ) or not (0 <= n + d[1]*3 <= len(input_mat[0]) -1 ):
                        continue
                        
                  if input_mat[m+d[0]][n+d[1]] == 'M' and input_mat[m+d[0]*2][n+d[1]*2] == 'A' and input_mat[m+d[0]*3][n+d[1]*3] == 'S':
                        count += 1
      return count

input_mat2 = [
      list("MMMSXXMASM"), 
      list("MSAMXMSMSA"), 
      list("AMXSXMAAMM"),
      list("MSAMASMSMX"),
      list("XMASAMXAMM"),
      list("XXAMMXXAMA"),
      list("SMSMSASXSS"),
      list("SAXAMASAAA"),
      list("MAMMMXMMMM"),
      list("MXMXAXMASX")]

input_mat3 = [
      list("XAMSS"), 
      list("SAAXA"),
      list("SMMXA"),
      list("XAMXA"),]

print(f"Num XMAS found: {solution(input_mat)}")
#Ans: 2454

#Part2
def solution2(input_mat:list[list[int]]) -> int:
      count = 0
      a_locs = []
      diagonals = [(-1,1),(1,1),(1,-1),(-1,-1)]
      #straights = [(-1,0),(0,1),(1,0),(0,-1)]

      for i in range(len(input_mat)):
            for j in range(len(input_mat[i])):
                  if input_mat[i][j] == 'A':
                        a_locs.append((i,j))
      
      for m,n in a_locs:
            usedDgnl = set()
            #usedStrt = set()
            if not (1 <= m < len(input_mat) - 1) or not (1 <= n < len(input_mat[0]) - 1):
                  continue

            for i in range(len(diagonals)):
                  shiftm, shiftn = diagonals[i]
                  oppshiftm, oppshiftn = diagonals[(i+2)%4]
                  if (m+shiftm,n+shiftn) not in usedDgnl and input_mat[m+shiftm][n+shiftn] == 'M' and input_mat[m+oppshiftm][n+oppshiftn] == 'S':
                        usedDgnl.add((m+shiftm,n+shiftn))
                        usedDgnl.add((m+oppshiftm,n+oppshiftn))

            #for i in range(len(straights)):
            #      shiftm, shiftn = straights[i]
            #      oppshiftm, oppshiftn = straights[(i+2)%4]
            #
            #      if (m+shiftm,n+shiftn) not in usedStrt and input_mat[m+shiftm][n+shiftn] == 'M' and input_mat[m+oppshiftm][n+oppshiftn] == 'S':
            #            usedStrt.add((m+shiftm,n+shiftn))
            #            usedStrt.add((m+oppshiftm,n+oppshiftn))
      
            if len(usedDgnl) == 4: 
                  count+=1
        


      return count


print(f"Num X-MAS found: {solution2(input_mat)}")
#Ans: 1858