// description: https://zhenchaogan.gitbook.io/leetcode-solution/leetcode-1570-dot-product-of-two-sparse-vectors
// tags: greedy, object oriented

class SparseVector {
  constructor(vector) {
    this.nonZeroVector = new Map();
    for (let i = 0; i < vector.length; i++) {
      if (vector[i] != 0)
        this.nonZeroVector.set(i, vector[i])
    }
  }

  dotProduct(otherVector) {
    let product = 0
    for (let key of this.nonZeroVector.keys())
      if (otherVector.nonZeroVector.has(key))
        product += this.nonZeroVector.get(key) * otherVector.nonZeroVector.get(key);

    return product;
  }
}

const vec1 = new SparseVector([1, 0, 0, 2, 3]);
const vec2 = new SparseVector([0, 3, 0, 4, 0]);
console.log(vec1.dotProduct(vec2));

// Time complexity: O(n)
// Space complexity: O(n)