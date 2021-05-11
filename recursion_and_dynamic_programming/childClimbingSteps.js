// recursive top-down approach
function climbStepsRecursive(n){
  if(n === 1)
    return 1;
  if(n === 2)
    return 2;
  if(n === 3)
    return 4;
  else
    return climbStepsRecursive(n-1) + climbStepsRecursive(n-2) + climbStepsRecursive(n-3);
}

// recursive dynamic programming solution, top-down
function climbStepsDP(n, memo){
  if(n === 1)
    return 1;
  if(n === 2)
    return 2;
  if(n === 3)
    return 4;
  if(memo[n-1] === 0)
    memo[n-1] = climbStepsDP(n-1, memo) + climbStepsDP(n-2, memo) + climbStepsDP(n-3, memo)
  return memo[n-1];
}

// dynamic programming solution, bottom-up
function climbStepsIteractive(n){
  const memo = new Array(n).fill(0);
  memo[0] = 1;
  memo[1] = 2;
  memo[2] = 4;
  for (let index = 3; index < memo.length; index++)
    memo[index] = memo[index-1] + memo[index-2] + memo[index - 3]
  return memo[n-1]
}

console.log(climbStepsIteractive(36));
console.log(climbStepsDP(36, new Array(36).fill(0)));
console.log(climbStepsRecursive(36));