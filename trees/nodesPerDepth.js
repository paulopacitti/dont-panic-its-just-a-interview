// description: https://www.educative.io/blog/cracking-top-facebook-coding-interview-questions#questions


class Node {
  Node() {
    this.left = null;
    this.right = null;
    this.value = null;
  }
}

function bfs(root){
  const queue = [];
  console.log(' ' + root.value.toString());
 
  queue.unshift(root);
  while(queue.length > 0){
    let depth = [];
    let current = queue.pop();
    let children = [current.left, current.right];
    children.forEach((child) => {
      if(child != null) {
        queue.unshift(child);
        depth.push(child.value);
      }
    });
    if(depth.length > 0) {
      let result = '';
      depth.forEach(e => result += (' ' + e.toString()));
      console.log(result);
    }
  }
}

let root = new Node();
root.value = 1;

let a = new Node();
a.value = 2;
let b = new Node();
b.value = 3;

let c = new Node();
c.value = 4;
b.left = c;

root.left = a;
root.right = b

bfs(root);

/*
  Time complexity: O(n)
  Space complexity: O(2n) = O(n)
*/