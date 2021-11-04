class Graph {
  constructor() {
    this.vertices = [];
    this.adjacencyList = {};
  }

  addVertex(vertex) {
    this.vertices.push(vertex);
    this.adjacencyList[vertex] = {};
  }

  upsertEdge(vertex1, vertex2, weight) {
    this.adjacencyList[vertex1][vertex2] = weight;
  }

  dijkstra(source) {
    let distances = {}
    let parents = {}
    let visited = new Set();
    for (let i = 0; i < this.vertices.length; i++) { // INITIALIZE-SINGLE-SOURCE
      if (this.vertices[i] === source)
        distances[source] = 0;
      else
        distances[this.vertices[i]] = Infinity;
      parents[this.vertices[i]] = null;
    }

    let currentVertex = this.vertexWithMinDistance(distances, visited);
    while (currentVertex !== null) {
      let distance = distances[currentVertex]
      for (let neighbor in this.adjacencyList[currentVertex]) {
        let newDistance = distance + this.adjacencyList[neighbor];
        if (distances[neighbor] > newDistance) { // RELAX EDGES
          distances[neighbor] = newDistance;
          parents[neighbor] = currentVertex;
        }
      }
      visited.add(currentVertex);
      currentVertex = this.vertexWithMinDistance(distances, visited);
    }

    console.log(parents);
    console.log(distances);
  }

  vertexWithMinDistance(distances, visited) {
    let minDistance = Infinity;
    let minVertex = null;
    for (let vertex in distances) {
      let distance = distances[vertex];
      if (distance < minDistance && !visited.has(vertex)) {
        minDistance = distance;
        minVertex = vertex;
      }
    }
    return minVertex;
  }
}

let g = new Graph();
g.addVertex("start");
g.addVertex("A");
g.addVertex("B");
g.addVertex("C");

g.upsertEdge("start", "A", 6);
g.upsertEdge("start", "B", 2);
g.upsertEdge("A", "C", 1);
g.upsertEdge("B", "A", 3);
g.upsertEdge("B", "C", 5)
g.dijkstra("start");

// Time complexity: O(V^2)
// Space complexity: O(V)