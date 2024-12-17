"""--- Day 11: Plutonian Pebbles ---

The ancient civilization on Pluto was known for its ability to manipulate spacetime, and while The Historians explore their infinite corridors, you've noticed a strange set of physics-defying stones.

At first glance, they seem like normal stones: they're arranged in a perfectly straight line, and each stone has a number engraved on it.

The strange part is that every time you blink, the stones change.

Sometimes, the number engraved on a stone changes. Other times, a stone might split in two, causing all the other stones to shift over a bit to make room in their perfectly straight line.

As you observe them for a while, you find that the stones have a consistent behavior. Every time you blink, the stones each simultaneously change according to the first applicable rule in this list:

    If the stone is engraved with the number 0, it is replaced by a stone engraved with the number 1.
    If the stone is engraved with a number that has an even number of digits, it is replaced by two stones. The left half of the digits are engraved on the new left stone, and the right half of the digits are engraved on the new right stone. (The new numbers don't keep extra leading zeroes: 1000 would become stones 10 and 0.)
    If none of the other rules apply, the stone is replaced by a new stone; the old stone's number multiplied by 2024 is engraved on the new stone.

No matter how the stones change, their order is preserved, and they stay on their perfectly straight line.

How will the stones evolve if you keep blinking at them? You take a note of the number engraved on each stone in the line (your puzzle input).

If you have an arrangement of five stones engraved with the numbers 0 1 10 99 999 and you blink once, the stones transform as follows:

    The first stone, 0, becomes a stone marked 1.
    The second stone, 1, is multiplied by 2024 to become 2024.
    The third stone, 10, is split into a stone marked 1 followed by a stone marked 0.
    The fourth stone, 99, is split into two stones marked 9.
    The fifth stone, 999, is replaced by a stone marked 2021976.

So, after blinking once, your five stones would become an arrangement of seven stones engraved with the numbers 1 2024 1 0 9 9 2021976.

Here is a longer example:

Initial arrangement:
125 17

After 1 blink:
253000 1 7

After 2 blinks:
253 0 2024 14168

After 3 blinks:
512072 1 20 24 28676032

After 4 blinks:
512 72 2024 2 0 2 4 2867 6032

After 5 blinks:
1036288 7 2 20 24 4048 1 4048 8096 28 67 60 32

After 6 blinks:
2097446912 14168 4048 2 0 2 4 40 48 2024 40 48 80 96 2 8 6 7 6 0 3 2

In this example, after blinking six times, you would have 22 stones. After blinking 25 times, you would have 55312 stones!

Consider the arrangement of stones in front of you. How many stones will you have after blinking 25 times?
"""
from time import perf_counter
stones:list[int]
with open("./Day11/day11_input.txt","r", encoding="utf-8") as file:
    stones = [int(num) for num in file.readline().split(sep=' ')]

stones_example1 = [0, 1, 10, 99, 999]

class Stone:
    def __init__(self, val:int):
        self.val = val
        self.prev = None
        self.next = None

def solution1(num_list:list[int], repeat:int)->int:

    def blink(num:int, remain:int)->list[int]:

        if remain == 0:
            return [num]
        
        res = []
        if len(str_num:=str(num)) % 2 == 0:
            left = blink(int(str_num[:len(str_num)//2]), remain=remain-1)
            right = blink(int(str_num[len(str_num)//2:]), remain=remain-1)
            res = [*left, *right]

        elif num == 0:
            res = blink(1, remain=remain-1)
        else:
            res = blink(num*2024, remain=remain-1)
        
        return res
    
    new_num_list = []
    for num in num_list:
        
        generated = blink(num, repeat)
        
        for generated_num in generated:
            new_num_list.append(generated_num)

    return len(new_num_list)

"""print(solution1([125,17], 1))
print(solution1([125,17], 2))
print(solution1([125,17], 3))
print(solution1([125,17], 4))
print(solution1([125,17], 5))
print(solution1([125,17], 25))
"""
time_start = perf_counter()
print(solution1(stones,40))
time_stop = perf_counter()
print(f"Elapsed time: {time_stop-time_start}")

import json
#Part2
def solution2(num_list:list[int], repeat:int)->int:
    """ class Stone:
        def __init__(self, val):
            self.val:int = val
            self.prev:Stone = None
            self.next:Stone = None

    res = 0

    head = Stone(-1)
    tail = Stone(-1)
    head.next = tail
    tail.prev = head
    
    cur = head
    for num in num_list:
        stone = Stone(num)
        old_next = cur.next
        cur.next = stone
        stone.prev = cur
        stone.next = old_next
        old_next.prev = stone
        cur = cur.next

    remain = repeat
    while (remain:=remain - 1) >= 0:

        cur = head
        while (cur:=cur.next) != tail:
            
            if len(str_num:=str(cur.val)) % 2 == 0:
                prev_stone = cur.prev
                next_stone = cur.next
                new_stone1 = Stone(int(str_num[:len(str_num)//2]))
                new_stone2 = Stone(int(str_num[len(str_num)//2:]))

                prev_stone.next = new_stone1
                new_stone1.prev = prev_stone

                new_stone1.next = new_stone2
                new_stone2.prev = new_stone1

                new_stone2.next = next_stone
                next_stone.prev = new_stone2

                cur = new_stone2

            elif cur.val == 0:
                cur.val = 1
            else:
                cur.val = cur.val * 2024

            
    cur = head
    while (cur:=cur.next) != tail:
        res += 1

    return res""" #attempt at using doubly linked list, time ended up worse than the recursive solution

    
    def blink(num:int, remain:int, zero25_cache:list[int] = None)->list[int]:
        if remain == 0:
            return [num]
        res = []
            
        if len(str_num:=str(num)) % 2 == 0:
            left = blink(int(str_num[:len(str_num)//2]), remain-1, zero25_cache)
            right = blink(int(str_num[len(str_num)//2:]), remain-1, zero25_cache)
            res = [*left, *right]

        elif num == 0 and remain > 25 and zero25_cache!= None:
            for cache_num in zero25_cache:
                for blinked_nums in blink(cache_num,remain-25, zero25_cache):
                    res.append(blinked_nums)
        elif num == 0 and remain <= 25:
            res = blink(1, remain-1, zero25_cache)
        else:
            res = blink(num*2024, remain-1, zero25_cache)
       
        return res

    cache = blink(0,25) 
    
    new_num_list = []
    for num in num_list:
        
        generated = blink(num, repeat, cache)
        
        for generated_num in generated:
            new_num_list.append(generated_num)

   
    """    with open('./Day11/data.json', 'w', encoding='utf-8') as f:
        json.dump(blink_cache, f, ensure_ascii=False, indent=4)
    print(new_num_list)"""
    return len(new_num_list)
    
time_start = perf_counter()
print(solution2(stones,40))
time_stop = perf_counter()
print(f"Elapsed time: {time_stop-time_start}")