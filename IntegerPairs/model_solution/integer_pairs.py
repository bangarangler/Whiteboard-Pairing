'''
Integer Pairs
favoring memory efficiency over time efficiency
O(n log n) runtime due to sorting
with O(1) space
'''

# def integerPairs(arr, k):
  # found_pair = False
  # arr.sort()
  # first = 0
  # last = len(arr) - 1

  # while first < last:
    # sum = arr[first] + arr[last]

    # if sum == k:
      # print(str(arr[first]) + ', ' + str(arr[last]))
      # first += 1
      # last -= 1
      # found_pair = True
    # else:
      # if sum < k:
        # first += 1
      # else:
        # last -= 1
  # if not found_pair:
    # print('No pairs found')

'''
Integer Pairs
trades time efficiency for space efficiency
O(n) runtime with O(n) space
'''

def integerPairs(arr, k):
  found_pair = False
  hash = {}

  for elem in arr:
    if k - elem in hash:
      print(elem, k - elem)
      found_pair = True
    else:
      hash[elem] = True
  if not found_pair:
    print("No pairs found")


# Some basic tests
integerPairs([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 11)   # should print '1, 10', '2, 9', '3, 8', '4, 7', '5, 6'
print('---------------')
integerPairs([5, 5, 4], 12)                         # should print 'No pairs found'
print('---------------')
integerPairs([99, 45, 38, 1, 68, 78], 100)          # should print '1, 99'
