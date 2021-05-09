// description: https://www.educative.io/blog/cracking-top-facebook-coding-interview-questions#questions

function moveZeros(array) {
  readIndex = array.length - 1;
  writeIndex = array.length - 1;

  while(readIndex >= 0){ // until finish moving the non-zero values;
    if(array[readIndex] != 0){
      array[writeIndex] = array[readIndex]; // overwrite the values into the "0" positions;
      writeIndex -= 1;
    }
    readIndex -= 1; // decrements readIndex;
  }

  while(writeIndex >= 0){ // write zeros at the beggining of the array;
    array[writeIndex] = 0;
    writeIndex -= 1;
  }
  return array;
}

console.log(moveZeros([1, 10, 20, 0, 59, 63, 0, 88, 0]))

/*
Time complexity: O(n), where n is the lenght of array
Space complexity: O(1), no extra memory is needed;
*/