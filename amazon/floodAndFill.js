const floodAndFill = (frame, x, y, newColor) => {
  const previousColor = frame[x][y];
  return floodAndFillUtil(frame, x, y, previousColor, newColor);
};

const floodAndFillUtil = (frame, x, y, previousColor, newColor) => {
  let queue = [];
  let visited = Array(frame.length).fill(Array(frame[0].length).fill(false));
  visited.fill(false);
  queue.push([x,y]);
  while(queue.length > 0) {
    let [currentX, currentY] = queue.shift();
    visited[currentX][currentY] = true;
    
    frame[currentX][currentY] = newColor;
    if(onLimits(currentX, currentY-1, frame.length, frame[0].length)
        && !visited[currentX][currentY-1]
        && frame[currentX][currentY-1] === previousColor) 
      queue.push([currentX,currentY-1]);
    if(onLimits(currentX+1, currentY, frame.length, frame[0].length)
        && !visited[currentX+1][currentY]
        && frame[currentX+1][currentY] === previousColor) 
      queue.push([currentX+1,currentY]);
    if(onLimits(currentX+1, currentY+1, frame.length, frame[0].length)
        && !visited[currentX+1][currentY+1]
        && frame[currentX+1][currentY+1] === previousColor) 
      queue.push([currentX+1,currentY+1]);
    if(onLimits(currentX, currentY+1, frame.length, frame[0].length) 
        && !visited[currentX][currentY+1]
        && frame[currentX][currentY+1] === previousColor)  
      queue.push([currentX,currentY+1]);
    if(onLimits(currentX-1, currentY, frame.length, frame[0].length) 
        && !visited[currentX-1][currentY]
        && frame[currentX-1][currentY] === previousColor) 
      queue.push([currentX-1,currentY]);
    if(onLimits(currentX-1, currentY-1, frame.length, frame[0].length)
        && !visited[currentX-1][currentY-1]
        && frame[currentX-1][currentY-1] === previousColor) 
      queue.push([currentX-1,currentY-1]);
  }

  return frame;
};

const onLimits = (x, y, limitX, limitY) => {
  horizontalLimits = (x >= 0 && x < limitX);
  verticalLimits = (y >= 0 && y < limitY);

  return horizontalLimits && verticalLimits;
}


let screen = [
  [1, 1, 1, 1, 1, 1, 1, 1],
  [1, 1, 1, 1, 1, 1, 0, 0],
  [1, 0, 0, 1, 1, 0, 1, 1],
  [1, 2, 2, 2, 2, 0, 1, 0],
  [1, 1, 1, 2, 2, 0, 1, 0],
  [1, 1, 1, 2, 2, 2, 2, 0],
  [1, 1, 1, 1, 1, 2, 1, 1],
  [1, 1, 1, 1, 1, 2, 2, 1],
];
let x = 4, y = 4, newColor = 3;
console.log(floodAndFill(screen, x,y,newColor))

// Time complexity: O(m*n) where m and n are the dimensions of the matrix. (could paint all pixels)
// Space complexity: O(m*n) for visited matrix