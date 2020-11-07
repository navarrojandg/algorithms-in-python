
def bubbleSortAscending(arr):
  n = len(arr)
  for i in range(n):
    print(f'i={i} {arr}')
    for j in range(0, n-i-1):
      if arr[j] > arr[j+1]:
        arr[j], arr[j+1] = arr[j+1], arr[j]
      print(f'  j={j} {arr}')
  return arr

def bubbleSortDescending(arr):
  n = len(arr)
  for i in range(n):
    print(f'i={i} {arr}')
    for j in range(0, n-i-1):
      if arr[j] < arr[j+1]:
        arr[j], arr[j+1] = arr[j+1], arr[j]
      print(f'  j={j} {arr}')
  return arr