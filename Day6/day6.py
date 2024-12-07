"""
--- Day 6: Guard Gallivant ---

The Historians use their fancy device again, this time to whisk you all away to the North Pole prototype suit manufacturing lab... 
in the year 1518! It turns out that having direct access to history is very convenient for a group of historians.

You still have to be careful of time paradoxes, and so it will be important to avoid anyone from 1518 while The Historians search for the Chief. Unfortunately, a 
single guard is patrolling this part of the lab.

Maybe you can work out where the guard will go ahead of time so that The Historians can search safely?

You start by making a map (your puzzle input) of the situation. For example:

....#.....
.........#
..........
..#.......
.......#..
..........
.#..^.....
........#.
#.........
......#...

The map shows the current position of the guard with ^ (to indicate the guard is currently facing up from the perspective of the map). 
Any obstructions - crates, desks, alchemical reactors, etc. - are shown as #.

Lab guards in 1518 follow a very strict patrol protocol which involves repeatedly following these steps:

    If there is something directly in front of you, turn right 90 degrees.
    Otherwise, take a step forward.

Following the above protocol, the guard moves up several times until she reaches an obstacle (in this case, a pile of failed suit prototypes):

....#.....
....^....#
..........
..#.......
.......#..
..........
.#........
........#.
#.........
......#...

Because there is now an obstacle in front of the guard, she turns right before continuing straight in her new facing direction:

....#.....
........>#
..........
..#.......
.......#..
..........
.#........
........#.
#.........
......#...

Reaching another obstacle (a spool of several very long polymers), she turns right again and continues downward:

....#.....
.........#
..........
..#.......
.......#..
..........
.#......v.
........#.
#.........
......#...

This process continues for a while, but the guard eventually leaves the mapped area (after walking past a tank of universal solvent):

....#.....
.........#
..........
..#.......
.......#..
..........
.#........
........#.
#.........
......#v..

By predicting the guard's route, you can determine which specific positions in the lab will be in the patrol path. Including the guard's starting position, 
the positions visited by the guard before leaving the area are marked with an X:

....#.....
....XXXXX#
....X...X.
..#.X...X.
..XXXXX#X.
..X.X.X.X.
.#XXXXXXX.
.XXXXXXX#.
#XXXXXXX..
......#X..

In this example, the guard will visit 41 distinct positions on your map.

Predict the path of the guard. How many distinct positions will the guard visit before leaving the mapped area?
"""
the_map:list[list[str]] = []
with open("day6_input.txt","r",encoding="utf-8") as file:
      for line in file:
            the_map.append(list(line.rstrip('\n')))

#Part1
def solution1(map_mat:list[list[str]])->int:
      map_mat_cp = [row.copy() for row in map_mat]
      map_length = len(map_mat)
      map_width = len(map_mat[0])
      guard_icons_d = {'^':0,'>':1,'v':2,'<':3}
      guard_icons_l = ['^','>','v','<']
      directions = [(-1,0),(0,1),(1,0),(0,-1)]
      guard_locs = []
      visited = set()

      for i in range(map_length):
            for j in range(map_width):
                  if map_mat[i][j] in guard_icons_d:
                        guard_locs.append((i,j))
                        visited.add((i,j))

      while guard_locs != []:
            temp = []
            for i in range(len(guard_locs)):
                  r,c = guard_locs[i]
                  icon = map_mat_cp[r][c]
                  move_r, move_c = directions[guard_icons_d[icon]]
                  if not (0 <= r + move_r < map_length ) or not (0 <= c + move_c < map_width):
                        continue

                  if map_mat_cp[r +move_r][c + move_c] == '#':
                        new_icon = guard_icons_l[(guard_icons_d[icon] + 1)%4]
                        map_mat_cp[r][c] = new_icon
                        temp.append((r,c))
                  else:
                        visited.add((r+move_r, c+move_c))
                        temp.append((r+move_r, c+move_c))
                        map_mat_cp[r][c] = 'X'
                        map_mat_cp[r +move_r][c+move_c] = icon 
            guard_locs = temp
      return len(visited)


test_map = [
      list("....#....."),
      list(".........#"),
      list(".........."),
      list("..#......."),
      list(".......#.."),
      list(".........."),
      list(".#..^....."),
      list("........#."),
      list("#........."),
      list("......#...")]
print(f"The answer for Part1: {solution1(the_map)}")
#4789

"""--- Part Two ---

While The Historians begin working around the guard's patrol route, you borrow their fancy device and step outside the lab. From the safety of a supply closet, you time travel through the last few months and record the nightly status of the lab's guard post on the walls of the closet.

Returning after what seems like only a few seconds to The Historians, they explain that the guard's patrol area is simply too large for them to safely search the lab without getting caught.

Fortunately, they are pretty sure that adding a single new obstruction won't cause a time paradox. They'd like to place the new obstruction in such a way that the guard will get stuck in a loop, making the rest of the lab safe to search.

To have the lowest chance of creating a time paradox, The Historians would like to know all of the possible positions for such an obstruction. The new obstruction can't be placed at the guard's starting position - the guard is there right now and would notice.

In the above example, there are only 6 different positions where a new obstruction would cause the guard to get stuck in a loop. The diagrams of these six situations use O to mark the new obstruction, | to show a position where the guard moves up/down, - to show a position where the guard moves left/right, and + to show a position where the guard moves both up/down and left/right.

Option one, put a printing press next to the guard's starting position:

....#.....
....+---+#
....|...|.
..#.|...|.
....|..#|.
....|...|.
.#.O^---+.
........#.
#.........
......#...

Option two, put a stack of failed suit prototypes in the bottom right quadrant of the mapped area:

....#.....
....+---+#
....|...|.
..#.|...|.
..+-+-+#|.
..|.|.|.|.
.#+-^-+-+.
......O.#.
#.........
......#...

Option three, put a crate of chimney-squeeze prototype fabric next to the standing desk in the bottom right quadrant:

....#.....
....+---+#
....|...|.
..#.|...|.
..+-+-+#|.
..|.|.|.|.
.#+-^-+-+.
.+----+O#.
#+----+...
......#...

Option four, put an alchemical retroencabulator near the bottom left corner:

....#.....
....+---+#
....|...|.
..#.|...|.
..+-+-+#|.
..|.|.|.|.
.#+-^-+-+.
..|...|.#.
#O+---+...
......#...

Option five, put the alchemical retroencabulator a bit to the right instead:

....#.....
....+---+#
....|...|.
..#.|...|.
..+-+-+#|.
..|.|.|.|.
.#+-^-+-+.
....|.|.#.
#..O+-+...
......#...

Option six, put a tank of sovereign glue right next to the tank of universal solvent:

....#.....
....+---+#
....|...|.
..#.|...|.
..+-+-+#|.
..|.|.|.|.
.#+-^-+-+.
.+----++#.
#+----++..
......#O..

It doesn't really matter what you choose to use as an obstacle so long as you and The Historians can put it into position without the guard noticing. The important thing is having enough options that you can find one that minimizes time paradoxes, and in this example, there are 6 different positions you could choose.

You need to get the guard stuck in a loop by adding a single new obstruction. How many different positions could you choose for this obstruction?
"""
#Part Two
def causes_loop(map_mat:list[list[str]], obs_loc:tuple)->bool:
      map_mat_cp = [row.copy() for row in map_mat]
      map_length = len(map_mat)
      map_width = len(map_mat[0])
      guard_icons_d = {'^':0,'>':1,'v':2,'<':3}
      guard_icons_l = ['^','>','v','<']
      directions = [(-1,0),(0,1),(1,0),(0,-1)]
      
      res = False
      guard_loc = [map_length,map_width]
      icon = None
      visited = set()

      for i in range(map_length):
            for j in range(map_width):
                  if map_mat[i][j] in guard_icons_d:
                        guard_loc  = i, j
                        icon = map_mat[i][j]
                        visited.add((i,j,icon))
            
            if visited:
                  break

      print(obs_loc)
      while 0 <= guard_loc[0] + directions[guard_icons_d[icon]][0] < map_length and 0 <= guard_loc[1] + directions[guard_icons_d[icon]][1] < map_width:
            move_r, move_c = directions[guard_icons_d[icon]]
            new_loc_r, new_loc_c =  guard_loc[0] + move_r, guard_loc[1] + move_c
            if map_mat_cp[new_loc_r][new_loc_c] == '#' or new_loc_r == obs_loc[0] and new_loc_c == obs_loc[1]:
                  icon = guard_icons_l[(guard_icons_d[icon] + 1)%4]
                  map_mat_cp[guard_loc[0]][guard_loc[1]] = icon
                  visited.add((guard_loc[0],guard_loc[1],icon))

            elif (new_loc_r,new_loc_c,icon) in visited:
                  res = True
                  break
            else:
                  map_mat_cp[new_loc_r][new_loc_c] = icon
                  guard_loc = new_loc_r, new_loc_c
                  visited.add((new_loc_r,new_loc_c,icon))
      
      return res

def solution2(map_mat:list[list[str]])->int:
      map_length = len(map_mat)
      map_width = len(map_mat[0])
      num_positions = 0
      for i in range(map_length):
            for j in range(map_width):
                  if map_mat[i][j] == '.' and causes_loop(map_mat, (i,j)):
                        num_positions += 1
                        
      
      return num_positions

print(f"The answer for Part2: {solution2(the_map)}")
#1304