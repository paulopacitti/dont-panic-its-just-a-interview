function spiralArray(n) {
  let square = n*n;
  let spiral = new Array(n);

  for (let index = 0; index < spiral.length; index++)
    spiral[index] = new Array(n).fill(0);
  
  let value = 1;
  let columnDirections = [1, 0, -1, 0];
  let rowDirections = [0, 1, 0, -1];
  let direction = 0;
  let i = 0;
  let j = 0;
  while(value <= square) {
    spiral[i][j] = value;
    i += rowDirections[direction];
    j += columnDirections[direction];
    if(invalidPosition(spiral, i, j)) {
      i -= rowDirections[direction];
      j -= columnDirections[direction];
      direction = (direction+1)%4;
      i += rowDirections[direction];
      j += columnDirections[direction];
    }
    value++;
  }

  return spiral;
}

function invalidPosition(array, row, column) {
  return row < 0 || column < 0 || row >= array.length ||
      column >= array.length || array[row][column] != 0;
}

let result = spiralArray(2);
result.forEach(row => console.log(row));