/*
  Given an input array and another array that describes a new index for each element, mutate the input 
  array so that each element ends up in their new index. Discuss the runtime of the algorithm and how 
  you can be sure there won't be any infinite loops.
*/ 

let arr = ["a","b","c","d","e","f"];
let indices = [2, 3, 4, 0, 5, 1];

arr = indices.map((item, index) => {
  return arr[indices.indexOf(index)];
});

console.log(arr);