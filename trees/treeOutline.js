class Node {
  constructor(value) {
    this.left = null;
    this.right = null;
    this.value = value;
  }
}

function outline(root) {
  let result = "";
  result = leftView(root.left).split(" ").reverse().join(" ");
  result += root.value;
  result += rightView(root.right);
  return result;
}

// BFS
function leftView(tree) {
  let queue = [];
  let current = tree;
  let result = "";

  queue.unshift(current);
  while(queue.length) {
    let nodesInLevel = queue.length;
    for (let i = 0; i < nodesInLevel; i++) {
      current = queue.pop();
      
      if(i === 0)
        result += " " + current.value;
      if(current.left !== null)
        queue.unshift(current.left);
      if(current.right !== null)
        queue.unshift(current.right);
    }
  }

  return result;
}

// BFS
function rightView(tree) {
  let queue = [];
  let current = tree;
  let result = "";

  queue.unshift(current);
  while(queue.length) {
    let nodesInLevel = queue.length;
    for (let i = 0; i < nodesInLevel; i++) {
      current = queue.pop();
      
      if(i + 1 === nodesInLevel)
        result += " " + current.value;
      if(current.left !== null)
        queue.unshift(current.left);
      if(current.right !== null)
        queue.unshift(current.right);
    }
  }

  return result;
}

let root = new Node(10);
root.left = new Node(2); 
root.right = new Node(3); 
root.left.left = new Node(7); 
root.left.right = new Node(8); 
root.right.right = new Node(15); 
root.right.left = new Node(12); 
root.right.left.left = new Node(20); 
root.left.left.right = new Node(14);
console.log(outline(root));