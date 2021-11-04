// question: https://stackoverflow.com/questions/27266550/how-to-flatten-nested-array-in-javascript
function flattenRecursive(array) {
  let result = array.reduce((previous, current) => {
    if(Array.isArray(current))
      current = flattenRecursive(current); 
    previous = previous.concat(current);
    return previous;
  }, []);
  return result;
}

function flattenIterative(array) {
  let result = [];
  let value;
  while(array.length) {
    value = array.shift();
    if(Array.isArray(value))
      array = value.concat(array); // concats the inner array at the end of the input
    else
      result.push(value);
  }
  return result;
}

a = [1,2,3,[3,4,[5],6], 7];
console.log(a.flat(Infinity));
console.log(flattenRecursive(a));
console.log(flattenIterative(a))