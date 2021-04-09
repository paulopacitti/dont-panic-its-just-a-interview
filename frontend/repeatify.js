// question: https://www.sitepoint.com/5-typical-javascript-interview-exercises/
/* Define a repeatify function on the String object. The function accepts an integer that 
specifies how many times the string has to be repeated. The function returns the string 
repeated the number of times specified. For example:
  console.log('hello'.repeatify(3));
Should print hellohellohello. */
'use strict';
String.prototype.repeatify = String.prototype.repeatify || function(times) {
  let repeatedString = '';
  for(let i=0;i<times; i++){
    repeatedString += this.toString();
  }
  return repeatedString;
};

let a = new String('hi');
console.log(a.repeatify(3));

// Arrow function cannot be used because only "function" has a constructor which binds
// the correct "this". Arrow functions use the global this object;