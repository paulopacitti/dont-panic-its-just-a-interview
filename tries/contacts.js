// INCOMPLETE
// description: https://www.hackerrank.com/challenges/contacts

class Node {
  constructor(key, children){
    this.key = key;
    this.children = {};
    this.count = 1;
  }
}

class Trie {
  constructor(root){
    this.root = new Node("", {});
  }

  insert(key) {
    let index = 1;
    let node = this.root;
    for(index; index < key.length+1; index++) {
      if(!(key.substring(0, index) in node.children))
        node.children[key.substring(0,index)] = new Node(key.substring(0,index), {});
      else
        node.count += 1;
      node = node.children[key.substring(0,index)];
    }
  }
  
  numberOfResults(key){
    let index = 1;
    let node = this.root;
    let count = 0;
    for(index; index < key.length+1; index++) {
      if(key.substring(0,index) in node.children){
        count = node.count;
        node = node.children[key.substring(0,index)];
      }
      else
        return 0;
    }
    return count;
  }
}

function contacts(queries) {
  let trie = new Trie();
  let results = [];
  queries.forEach(query => {
    let [command, argument] = query;
    switch(command){
      case "find":
        results.push(trie.numberOfResults(argument));
        break;
      case "add":
        trie.insert(argument);
        break;
    }
  });
  return results;
}

const test0 = [
  ["add", "hack"],
  ["add", "hackerrank"],
  ["find", "hac"],
  ["find", "hak"],
];
const test1 = [
  ["add", "s"],
  ["add", "ss"],
  ["add", "sss"],
  ["add", "ssss"],
  ["add", "sssss"],
  ["find", "s"],
  ["find", "ss"],
  ["find", "sss"],
  ["find", "ssss"],
  ["find", "sssss"],
  ["find", "ssssss"],
]
console.log(contacts(test0));

// Time complexity:
// Space complexity: s