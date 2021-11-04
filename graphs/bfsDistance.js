// description: https://www.hackerrank.com/challenges/ctci-bfs-shortest-reach/

function processData(input) {
  let lines = input.split("\n");
  let numberOfQueries = parseInt(lines[0]);
  let j = 1;
  for (let i = 0; i < parseInt(numberOfQueries); i++) {
    let [V, E] = lines[j].split(" ").map(e => parseInt(e));
    j += 1;
    let edges = lines.slice(j, j + E).map((line) => {
      let edge = line.split(" ");
      return edge.map((v) => parseInt(v))
    })
    let graph = buildGraph(parseInt(V), edges);
    let start = parseInt(lines[j + E]);
    console.log(printEdges((bfs(graph, start))));
    j += E + 1;
  }
}

function bfs(graph, start) {
  queue = [];
  distances = Array(graph.length).fill(-1);
  distances[start] = 0;
  visited = Array(graph.length).fill(false);
  queue.push(start);
  visited[start] = true;
  while (queue.length > 0) {
    let currentVertex = queue.shift();
    
    graph[currentVertex].forEach(neighbor => {
      if (!visited[neighbor]) {
        if(distances[neighbor] === -1)
          distances[neighbor] = distances[currentVertex] + 6;
        visited[neighbor] = true;
        queue.push(neighbor);
      }
    });    
  }
  return distances;
}

function buildGraph(V, edges) {
  let graph = new Array(V);
  for(let i = 0; i < V+1; i++)
    graph[i] = [];
  for(let i = 0; i < edges.length; i++){
    let vertex = edges[i][0];
    let value = edges[i][1];
    graph[vertex].push(value);
    graph[value].push(vertex);
  }
    
  return graph;
}

function printEdges(array) {
  let result = "";
  array.slice(1, array.length-1).forEach((e) => {
    if(e !== 0) result += e.toString() + " ";
  });
  if(array[array.length-1] !== 0) result += array[array.length-1].toString();
  return result;
}

let s = `1
7 4
1 2
1 3
3 4
2 5
2`;
processData(s);