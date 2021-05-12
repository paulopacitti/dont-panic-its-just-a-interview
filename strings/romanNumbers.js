// description: https://www.geeksforgeeks.org/converting-roman-numerals-decimal-lying-1-3999/

const romanDigits = new Map();
romanDigits.set("I", 1);
romanDigits.set("V", 5);
romanDigits.set("X", 10);
romanDigits.set("L", 50);
romanDigits.set("C", 100);
romanDigits.set("D", 500);
romanDigits.set("M", 1000);

function romanToDecimal(word){
  let result = 0;
  let index = 0;
  while(index < word.length) {
    let current = romanDigits.get(word.charAt(index));
    if(index+1 < word.length && current < romanDigits.get(word.charAt(index+1))){
      result += romanDigits.get(word.charAt(index+1)) - current;
      index += 2;
    }
    else {
      result += current;
      index += 1;
    }
  }

  return result;
}

console.log(romanToDecimal("MCMIV"));

/*
  Time complexity: O(n), the length of the word;
  Space complexity: O(1), no extra space is needed;
*/