// description: https://www.geeksforgeeks.org/find-number-of-islands/

function dfs(land, i, j){
  land[i][j] = 0;
  const rowDirections = [0, -1, -1, -1, 0, 1, 1, 1]
  const columnDirections = [1, 1, 0, -1, -1, -1, 0, 1];
  for (let index = 0; index < rowDirections.length; index++) {
    if(!invalidPosition(land, i + rowDirections[index], j + columnDirections[index]) &&
      land[i + rowDirections[index]][j + columnDirections[index]] === 1)
      dfs(land, i + rowDirections[index], j + columnDirections[index])
  }
}

function invalidPosition(land, i, j){
  return i >= land.length || j >= land.length[0] ||
    i < 0 || j < 0;
}

function countIslands(land) {
  let count = 0;
  for (let i = 0; i < land.length; i++) {
    for (let j = 0; j < land[0].length; j++) {
      if(land[i][j] === 1){
        dfs(land, i, j);
        count += 1;
      }
    }
  }

  return count;
}

let M = [
  [ 1, 1, 0, 0, 0],
  [ 0, 1, 0, 0, 1],
  [1, 0, 0, 1, 1],
  [0, 0, 0, 0, 0],
  [1, 0, 1, 0, 1]];
console.log(countIslands(M))

/*
  Time complexity: O(8*(m*n)) -> O(m*n)
  Space complexity: O(m*n)
*/