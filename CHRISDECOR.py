
if __name__ == "__main__":
  testcases = int(input())
  while(testcases):
    leaves, large, small = map(int,input().split())
    large_count = 0
    small_count = 0
    small_count = small // 3
    if(large >= small_count):
      large = large - small_count
      large_count = large // 2
    else:
      small_count = large
    if((small_count + large_count) >= leaves):
      print("YES")
    else:
      print("NO")
    testcases -= 1
    


"""
Decorating Christmas Tree

You are decorating your Christmas Tree and want to make it beautiful. You consider a Christmas tree beautiful when each leaf of the Christmas Tree is decorated with either one of the following :

    11 large ornament and 33 small ornaments.
    22 large ornaments.

You have XX large ornaments and YY small ornaments. Your Christmas tree consists of NN leaves. Determine if you can make the Christmas tree beautiful by decorating each leaf with either one of the above requirements.
Input Format

    The first line of input will contain a single integer TT, denoting the number of test cases.
    Each test case consists of three space-separated integers, NN, XX and YY, the number of leaves, the number of large ornaments and the number of small ornaments.


URL - https://www.codechef.com/problems/CHRISDECOR
"""
