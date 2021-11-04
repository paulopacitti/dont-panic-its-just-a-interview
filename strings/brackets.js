// description: https://www.hackerrank.com/challenges/balanced-brackets/problem

function isBalanced(s) {
  let reverse = {};
  reverse[")"] = "(";
  reverse["}"] = "{";
  reverse["]"] = "[";
  let close = new Set(["}", "]", ")"]);
  let stack = [];

  for (let i = 0; i < s.length; i++) {
    let current = s.charAt(i);
    if (close.has(current)) {
      let match = stack.pop();
      if (reverse[current] === match)
        continue
      else
        return "NO";
    }
    else
      stack.push(current);
  }
  if(stack.length > 0)
    return "NO";
  else
    return "YES";

}

const s = "[{";
let result = isBalanced(s);
console.log(result);

// Time complexity: O(L), where L is the size of the string
// Space complexity: O(L), because the stack can have all the characters of the string