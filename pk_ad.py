def countOnes(row):
  count = 0
  for i in row:
    if i == 1:
      count += 1
  return count


def solve(arr, n, m):
  res = 0
  for i in range(n-1):
    res += countOnes(arr[i])*countOnes(arr[i+1])
  return res



if __name__ == "__main__":
  n = int(input())
  m = int(input())
  arr = [list(map(int, input().split(' '))) for i in range(n)]
  print(solve(arr, n, m))
