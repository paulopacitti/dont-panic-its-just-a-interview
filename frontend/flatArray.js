// question: https://stackoverflow.com/questions/27266550/how-to-flatten-nested-array-in-javascript
function flatten(array) {
  let result = array.reduce((previous, current) => {
    if(Array.isArray(current))
      current = flatten(current); 
    previous = previous.concat(current);
    return previous;
  }, []);
  return result;
}

a = [1,2,3,[3,4,[5],6]];
console.log(flatten(a));