// Three-sum: given a list of sorted numbers, find the three numbers that sum to the target number

function threeSum(array, sum) {
  let result = []
  array.sort((a,b) => a-b);
  for(let i = 0; i < array.length; i++) {
    let left = i + 1;
    let right = array.length - 1;
    while(left < right) {
      if(array[i] + array[left] + array[right] === sum){
        result = result.concat([array[i], array[left], array[right]]);
        return result;
      }

      if(array[i] + array[left] + array[right] < sum)
        left += 1;
      else
        right -= 1;
    }
  }

  return result;
}

console.log(threeSum([12, 3, 4, 1, 6, 9], 24));