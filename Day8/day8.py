"""--- Day 8: Resonant Collinearity ---

You find yourselves on the roof of a top-secret Easter Bunny installation.

While The Historians do their thing, you take a look at the familiar huge antenna. 
Much to your surprise, it seems to have been reconfigured to emit a signal that makes people 0.1% more likely to buy 
Easter Bunny brand Imitation Mediocre Chocolate as a Christmas gift! Unthinkable!

Scanning across the city, you find that there are actually many such antennas. Each antenna is tuned to a specific frequency 
indicated by a single lowercase letter, uppercase letter, or digit. You create a map (your puzzle input) of these antennas. For example:

............
........0...
.....0......
.......0....
....0.......
......A.....
............
............
........A...
.........A..
............
............

The signal only applies its nefarious effect at specific antinodes based on the resonant frequencies of the antennas. 
In particular, an antinode occurs at any point that is perfectly in line with two antennas of the same frequency - 
but only when one of the antennas is twice as far away as the other. This means that for any pair of antennas with the same 
frequency, there are two antinodes, one on either side of them.

So, for these two antennas with frequency a, they create the two antinodes marked with #:

..........
...#......
..........
....a.....
..........
.....a....
..........
......#...
..........
..........

Adding a third antenna with the same frequency creates several more antinodes. 
It would ideally add four antinodes, but two are off the right side of the map, so instead it adds only two:

..........
...#......
#.........
....a.....
........a.
.....a....
..#.......
......#...
..........
..........

Antennas with different frequencies don't create antinodes; A and a count as different frequencies. 
However, antinodes can occur at locations that contain antennas. In this diagram, the lone antenna with frequency capital A 
creates no antinodes but has a lowercase-a-frequency antinode at its location:

..........
...#......
#.........
....a.....
........a.
.....a....
..#.......
......A...
..........
..........

The first example has antennas with two different frequencies, so the antinodes they create look like this, 
plus an antinode overlapping the topmost A-frequency antenna:

......#....#
...#....0...
....#0....#.
..#....0....
....0....#..
.#....A.....
...#........
#......#....
........A...
.........A..
..........#.
..........#.

Because the topmost A-frequency antenna overlaps with a 0-frequency antinode, there are 14 total unique locations that 
contain an antinode within the bounds of the map.

Calculate the impact of the signal. How many unique locations within the bounds of the map contain an antinode?
"""

#Part1
city_map = []
with open("./Day8/day8_input.txt","r",encoding="utf-8") as file:

      for line in file:
            city_map.append(list(line.strip()))


def solution1(mat:list[list[str]])->int:
      
      antinodes = set()
      antenna_locs:dict[str,list[tuple[int,int]]] = dict()
      inbounds_x = lambda x: 0<= x < len(mat[0])
      inbounds_y = lambda y: 0<= y < len(mat)

      for i in range(len(mat)):
            for j in range(len(mat[i])):
                  if mat[i][j] == '.':
                        continue
                  if mat[i][j] in antenna_locs:
                        antenna_locs[mat[i][j]].append((i,j))
                  else:
                        antenna_locs[mat[i][j]] = [(i,j)]
      
      print(antenna_locs)
      for key in antenna_locs:
            for i in range(len(antenna_locs[key])):
                  for j in range(i+1, len(antenna_locs[key])):
                        ant1 = antenna_locs[key][i]
                        ant2 = antenna_locs[key][j]
                        antinode1 = (ant1[0] + (ant1[0]-ant2[0]), ant1[1] + (ant1[1]  - ant2[1]))
                        antinode2 = (ant2[0] + (ant2[0]-ant1[0]), ant2[1] + (ant2[1]  - ant1[1]))
                        
                        if antinode1 not in antinodes and inbounds_x(antinode1[1]) and inbounds_y(antinode1[0]):
                       
                              antinodes.add(antinode1)

                        if antinode2 not in antinodes and inbounds_x(antinode2[1]) and inbounds_y(antinode2[0]):
            
                              antinodes.add(antinode2)
      #for row in mat:

      #      print(''.join(row))
      return len(antinodes)
test_map = [list("............"),
            list("........0..."),
            list(".....0......"),
            list(".......0...."),
            list("....0......."),
            list("......A....."),
            list("............"),
            list("............"),
            list("........A..."),
            list(".........A.."),
            list("............"),
            list("............")]
print(solution1(city_map))
#Ans: 361

import math
def solution2(mat:list[list[str]])->int:

      antinodes = set()
      antenna_locs:dict[str,list[tuple[int,int]]] = dict()
      inbounds = lambda x: 0<= x[0] < len(mat) and 0<= x[1] < len(mat[0])

      for i in range(len(mat)):
            for j in range(len(mat[i])):
                  if mat[i][j] == '.':
                        continue
                  if mat[i][j] in antenna_locs:
                        antenna_locs[mat[i][j]].append((i,j))
                  else:
                        antenna_locs[mat[i][j]] = [(i,j)]
      
      print(antenna_locs)
      for key in antenna_locs:
            for i in range(len(antenna_locs[key])):
                  for j in range(i+1, len(antenna_locs[key])):
                        ant1 = antenna_locs[key][i]
                        ant2 = antenna_locs[key][j]
                        ant_diff = (ant1[0]-ant2[0], ant1[1]  - ant2[1])
                        gcd = math.gcd(*ant_diff)
                        ant_diff_reduced = (int(ant_diff[0]/gcd),int(ant_diff[1]/gcd))

                        s = 0
                        while inbounds((ant1[0]+s*ant_diff_reduced[0], ant1[1]+s*ant_diff_reduced[1])) or inbounds((ant2[0]-s*ant_diff_reduced[0], ant2[1]-s*ant_diff_reduced[1])):

                              if inbounds((ant1[0]+s*ant_diff_reduced[0], ant1[1]+s*ant_diff_reduced[1])):
                                    antinodes.add((ant1[0]+s*ant_diff_reduced[0], ant1[1]+s*ant_diff_reduced[1]))

                              if inbounds((ant2[0]-s*ant_diff_reduced[0], ant2[1]-s*ant_diff_reduced[1])):
                                    antinodes.add((ant2[0]-s*ant_diff_reduced[0], ant2[1]-s*ant_diff_reduced[1]))
                              
                              s += 1
            print(antinodes)
      for node in list(antinodes):
            mat[node[0]][node[1]] = '#'
      for line in mat:
            print(''.join(line))

      return len(antinodes)

print(solution2(city_map))
#Current: 1124 too low