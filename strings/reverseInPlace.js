function reverseInPlace(word){
  return [...word].reverse().join('');
}

console.log(reverseInPlace('Hello'));