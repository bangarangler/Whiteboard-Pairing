function naiveClimbStairs(n) {
  if (n < 0) return 0;
  else if (n == 0) return 1
  else {
    return naiveClimbStairs(n-1) + naiveClimbStairs(n-2) + naiveClimbStairs(n-3)
  }
}

function memoizedClimbStairs(n, cache) {
  if (n < 0) return 0
  else if (n == 0) return 1
  else if (cache[n] > 1) return cache[n]
  else {
    cache[n] = memoizedClimbStairs(n-1, cache) +
               memoizedClimbStairs(n-2, cache) +
               memoizedClimbStairs(n-3, cache)
    return cache[n]
  }
}

console.log(naiveClimbStairs(10))
console.log(naiveClimbStairs(30))
