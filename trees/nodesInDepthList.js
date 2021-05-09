/* List of Depths: Given a binary tree, design an algorithm which creates a linked list of all the nodes
    at each depth (e.g., if you have a tree with depth D, you'll have D linked lists).
    [using BFS]
        2
       / \
      /   \
     /     \
    1       3
   / \     / 
  0   7   9  

  Time complexity: O(n)
  Space complexity: O(2n) = O(n)
*/

class Node {
  Node() {
    this.left = null;
    this.right = null;
    this.value = null;
  }
}

function adaptedBfs(node) {
  if(node == null)
    return [];

  let queue = [];
  let list = []
  queue.unshift(node);
  list.push(node)

  while(queue.length > 0) {
    let currentDepth = [];
    let element = queue.pop();
    let children = [element.left, element.right];
    children.forEach(child => {
      if(child != null){
        queue.unshift(child);
        currentDepth.push(child);
      }
    });
    if(currentDepth.length > 0)
      list.push(currentDepth);
  }

  return list;
}

function nodesInDepthList(node) {
  let nodesByDepth = [];
  let list = adaptedBfs(node, nodesByDepth);
  return list;
}

let root = new Node();
root.value = 1;

let a = new Node();
a.value = 2;
let b = new Node();
b.value = 3;

root.left = a;
root.right = b

console.log(nodesInDepthList(root));
