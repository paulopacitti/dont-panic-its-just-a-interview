/*
  Given a grid of characters output a decoded message. The message for the following would be IROCKA. 
  (diagonally down right and diagonally up right if you can't go further .. you continue doing this)

  I B C A L K A 
  D R F C A E A
  G H O E L A D
*/

function isValid(array, i) {
  return i >= 0 && i < array.length;
}

function decode(array) {
  let result = "";
  let verticalDirections = [1, -1];
  let i = 0;
  let j = 0;
  let direction = 0;

  while(j < array[0].length) {
    if(isValid(array, i)) {
      result += array[i][j];
      j += 1;
    }
    else {
      direction = (direction + 1) % 2;
      i += verticalDirections[direction];
    }
    i += verticalDirections[direction];
  }

  return result;
}

let encrypted = [
  "IBCALKA".split(""),
  "DRFCAEA".split(""),
  "G H O E L A D".split(" "),
];

console.log(decode(encrypted));
/*
  Time complexity: O(n), where n is the number of columns
  Space complexity: O(n), string with n characters, where n is the number of columns
*/