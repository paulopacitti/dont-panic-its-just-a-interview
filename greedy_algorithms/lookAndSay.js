// Description: https://www.facebook.com/careers/life/sample_interview_questions

function lookAndSay(n) {
  let currentValue = "1";
  for(let i=1; i < n+1; i++){
    console.log(currentValue);
    currentValue = nextItem(currentValue);
  }
}

function nextItem(input) {
  if(input.length === 1)
    return "1" + input;
  else {
    let result = ""
    let previous = input.charAt(0);
    let count = 1;
    for(let i=1; i <= input.length; i++){
      if(previous !== input.charAt(i) || i === input.length){
        result += count.toString() + previous;
        previous = input.charAt(i);
        count = 1;
      }
      else
        count += 1;
    }
    return result;
  }
}

lookAndSay(10);

/*
Time complexity: O(n), where n is the number of items targeted to be printed;
Space complexity: O(2n) = O(n), worst case is where all the digits are different,
                  so the result string will be twice the size of the input;
*/