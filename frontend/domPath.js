/* 
Description: Given two identical DOM tree structures, A and B, and a node from A, find the corresponding node in B 

Example:
<!DOCTYPE html>
<html>
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width">
  <title>Facebook DOM Traversal</title>
</head>
<body>
  <div id="rootA">
    <div>
      <div></div>
    </div>
    
    <div></div>
      
    
    <div>
      <div>
        <div id="nodeA"></div>
        <div></div>
      </div>
    </div>
  </div>
    
  <div id="rootB">
    <div>
      <div></div>
    </div>
    
    <div></div>
    
    <div>
      <div>
        <div id="nodeB"></div>
        <div></div>
      </div>
    </div>
  </div>
</body>
</html> */

let rootA = document.getElementById('rootA');
let rootB = document.getElementById('rootB');
let nodeA = document.getElementById('nodeA');


// find nodeA and then return a reverse a path to it
function findAPath(root, node) {
  const path = [];
  let current = node;

  while(current != root) {
    let parent = current.parentNode;
    let children = Array.from(parent.children);
    path.unshift(children.indexOf(current));
    current = parent;
  }
  return path;
}

function getNode(root, path) {
  let nodeFound = root;
  
  path.forEach((element) => nodeFound = nodeFound.children[element]);
  return nodeFound;
}

function getTwinNode(treeA, treeB, nodeA) {
  let path = findAPath(treeA, nodeA);
  let nodeB = getNode(treeB, path);

  return nodeB;
}

// time complexity????