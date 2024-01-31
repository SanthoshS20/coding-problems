import math 

if __name__ == "__main__":
  testcases = int(input())
  while(testcases):
    boss, d1, d2, d3, time = map(int,input().split())
    d1_hits = math.ceil(boss / d1)
    d2_hits = 0
    if(boss > (d2 * time)):
      d2_hits = time + math.ceil((boss - (d2 * time)) / d3)
    else:
      d2_hits = math.ceil(boss / d2)
    if(d1_hits <= d2_hits):
      print(d1_hits)
    else:
      print(d2_hits)
    testcases -= 1


"""
Weapon Choice

Chef is playing a videogame, and is now at a boss fight.
The boss has HH health.

Chef has two weapons with him:

    First, a gun that does XX damage every hit.
    Second, a laser that does Y1Y1​ damage every hit.
    However, after the KK-th time it's used, the laser's output drops; and it will then do only Y2Y2​ damage every hit (Y2<Y1Y2​<Y1​).

Chef must choose exactly one of the two weapons to fight the boss, and cannot change once the fight begins.
What's the minimum number of hits he needs to defeat the boss?

The boss will be defeated once Chef inflicts at least HH damage to it in total.

URL - https://www.codechef.com/problems/WEPCH

"""
