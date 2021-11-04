// INCOMPLETE
/*
 * Complete the 'getWays' function below.
 *
 * The function is expected to return a LONG_INTEGER.
 * The function accepts following parameters:
 *  1. INTEGER n
 *  2. LONG_INTEGER_ARRAY c
 */

function getWays(n, c) {
  const memo = new Array(n + 1).fill(0)
  memo[0] = 1;
  for (let i = 0; i < c.length; i++)
    for (let j = c[i]; j <= n; j++)
      memo[j] += memo[j - c[i]];
  return memo[n]
}

let a = [1,2,3]
let n = 4;
console.log(getWays(n, a))


