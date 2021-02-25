### Adjacency list
Adjacency list is a representation of a graph using a list of edges of each node. 

### Breadth First Search (BFS)
The easy way to think how bfs works is, it just searches every unvisited child of the current node. A great way to implement bfs is using a queue. Push an unvisited child whenever you find one and mark it as visited. when there is no unvisited child of the current node, pop the queue and use the poped value as your current node. Do this until the queue is empty.

### Depth First Search (DFS)
As the name suggests you need to explore the deepest holes first. The easy way to get your head around dfs is that whenever you find an unvisited node, you just try to go even deeper from this node. What I am trying to say is you do not stop until you have reached the very bottom. Goodway to implement dfs is using Recursion. Why recursion? Think of every unvisited node as a digging spot and you are the digger. When you find a digging spot you go to the next level by asking yourself to dig. Do this until you reach the deepest point. From there go a level up and see if left any digging spots are left where you haven't dig. As you have to ask yourself to dig every time you find a digging spot that means it is a job for recursion. What should be the base condition you ask? The answer is this recursion doesn't need any.

### Cycle finding
In order to find a cycle in a graph, you should use dfs and try to find out if a visited node that is a child of the current node is the same as the current node's parent or not. If they are not the same and the level of the current node is higher than it's child node. If both hold true then there is a cycle. Why the level of the current node needs to be higher you ask? What we are trying is to find a back edge. The back edge is an edge to the ancestor. So if the level is higher than the child of the node that means the child node was an ancestor and there is a cycle. Why we should use dfs? Because the result of dfs is a tree and the tree doesn’t have a cycle means a different level for each node.


