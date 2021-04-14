// question: https://vimeo.com/357608978
// Description: given a tree, returns the average value for each level
// using DFS

/*
        2
       / \
      /   \
     /     \
    1       3
   / \     / \
  0   7   9   1
 /   / \     / \
2   1   0   8   8
       /
      7
*/

class Node {
  Node() {
    this.left = null;
    this.right = null;
    this.value = null;
  }
}

function collect(node, hash, depth = 0) {
  if(node == null)
    return null;

  if(depth in levels)
    hash[depth].push(node.value);
  else
    hash[depth] = [node.value];

  collect(node.left, hash, depth + 1);
  collect(node.right, hash, depth + 1);
}

function averageByLevel(node) {
  let levels = {};
  collect(node, hash);

  let result = levels.map((element) => {
   let sum = element.reduce((acc, next) => acc+next);
   return (sum/elememt.length);
  });

  return result;
}