/* Description: https://www.facebook.com/careers/life/sample_interview_questions
 An edit is:
    Inserting one character anywhere in the word (including at the beginning and end)
    Removing one character
    Replacing one character
*/

function oneEditApart(firstWord, secondWord){
  if(Math.abs(firstWord.length - secondWord.length) > 1)
    return false;
  else {
    let differentChars = 0;
    // replace only permitted
    if(firstWord.length === secondWord.length) {
      for(let i=0; i < firstWord.length; i++){
        if(firstWord.charAt(i) != secondWord.charAt(i) && differentChars <= 1)
          differentChars += 1;
      }
      return differentChars <= 1;
    }
    // add or removal (one edit)
    else {
      let i = 0;
      let j = 0;
      while (i < firstWord.length && j < secondWord.length && differentChars <= 1){
        if(firstWord.charAt(i) != secondWord.charAt(j)) {
          differentChars += 1
          if(firstWord.length < secondWord.length) // increment indexes depending of the words size
            j += 1;
          else
            if(firstWord.length > secondWord.length)
              i += 1;
            else {
              i += 1;
              j += 1;
            } 
        }
        else {
          i += 1;
          j += 1;
        }
      } 
    }
    return differentChars <= 1;
  }
}

console.log(oneEditApart('cat', 'ca'));

/*
Time complexity: O(m), where "m" is the length of the longest word;
Space complexity: O(1), no extra space required;
*/