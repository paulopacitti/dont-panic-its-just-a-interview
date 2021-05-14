// description: https://www.glassdoor.com/Interview/Given-input-could-be-potentially-more-than-3-keys-in-the-object-above-items-color-red-type-tv-age-18-QTN_2372314.htm
/* Given input:
items = [
  {color: 'red', type: 'tv', age: 18},
  {color: 'silver', type: 'phone', age: 20}
  ...
]
excludes = [
  {k: 'color', v: 'silver'},
  {k: 'type', v: 'tv'},
  ...
]

function excludeItems(items, excludes) {
   excludes.forEach(pair => {
      items = items.filter(item => item[pair.k] === item[pair.v]);
   });
   return items;
}

1. Describe what this function is doing...
The function is 
2. What is wrong with that function?
The function is filtering wrong the "items" object, it should filter comparing
the item[pair.k] with pair.v, not item [pair.v]
3. How would you optimize it ?
*/

function buildMapOfSets(array) {
  let map = new Map();
  for (let element of array) {
    Object.keys(element).forEach((key) =>{
      if (!map.has(key)) {
        map.set(key, new Set())
      }
      map.get(key).add(element[key]);
    })
  }
  return map;
}

function excludeItems(items, excludes) {
  let set = buildMapOfSets(excludes);
  let result = items.filter(element => {
    return !Object.keys(element).some((key) => !set.get("k").has(key) || !set.get("v").has(element[key]));
  });
  return result;
}

let items = [
  {color: 'red', type: 'tv', age: 18},
  {color: 'silver', type: 'phone', age: 20}
];
let excludes = [
  {k: 'color', v: 'silver'},
  {k: 'type', v: 'tv'},
];

console.log(excludeItems(items, excludes));

/*
  Time complexity: O(n*k)
  Space complexity: O(n*k)
*/