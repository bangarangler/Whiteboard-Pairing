function largestContiguousSum(arr) {
  let maxSum = -Infinity;
  let currentSum = 0;

  for (let i = 0; i < arr.length; i++) {
    currentSum += arr[i]
    maxSum = Math.max(maxSum, currentSum)

    if (currentSum < 0) {
      currentSum= 0;
    }
  }

  return maxSum
}


/* Some console.log tests */
console.log(largestContiguousSum([5, -9, 6, -2, 3]));           // should print 7
console.log(largestContiguousSum([1, 23, 90, 0, -9]));          // should print 114
console.log(largestContiguousSum([2, 3, -8, -1, 2, 4, -2, 3])); // should print 7
