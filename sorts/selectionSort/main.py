
def selectionSortAscending(arr):
  n = len(arr)
  for i in range(n):
    minIndex = i
    for j in range(i+1, n):
      if arr[minIndex] > arr[j]:
        minIndex = j
    arr[i], arr[minIndex] = arr[minIndex], arr[i]
    print(f'i={i} {arr}')
  return arr

def selectionSortDescending(arr):
  n = len(arr)
  for i in range(n):
    maxIndex = i
    for j in range(i+1, n):
      if arr[maxIndex] < arr[j]:
        maxIndex = j
    arr[i], arr[maxIndex] = arr[maxIndex], arr[i]
    print(f'i={i} {arr}')
  return arr
