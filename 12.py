def prims_algorithm(graph, start_vertex=0):
    num_vertices = len(graph)

    # MST set to keep track of vertices included in the MST
    mst_set = set()

    # List to store the edges of the MST
    mst_edges = []

    # List to track the minimum edge weights for each vertex
    min_edge = [float('inf')] * num_vertices
    min_edge[start_vertex] = 0

    # List to store the parent of each vertex in the MST
    parent = [-1] * num_vertices

    while len(mst_set) < num_vertices:
        # Find the vertex with the smallest edge weight not in MST
        min_weight = float('inf')
        u = -1
        for vertex in range(num_vertices):
            if vertex not in mst_set and min_edge[vertex] < min_weight:
                min_weight = min_edge[vertex]
                u = vertex

        if u == -1:
            print("Graph is not connected. MST cannot be formed.")
            return mst_edges

        # Add this vertex to the MST set
        mst_set.add(u)

        # If u is not the start vertex, add the edge (parent[u], u) to the MST
        if parent[u] != -1:
            mst_edges.append((parent[u], u, min_weight))

        # Update the minimum edge weights for neighbors of u
        for v, weight in graph[u]:
            if v not in mst_set and weight < min_edge[v]:
                min_edge[v] = weight
                parent[v] = u

    return mst_edges


def get_graph_input():
    # Get the number of vertices from the user
    num_vertices = int(input("Enter the number of vertices: "))

    # Initialize an empty adjacency list for the graph
    graph = {i: [] for i in range(num_vertices)}

    # Get the number of edges
    num_edges = int(input("Enter the number of edges: "))

    # Get each edge input from the user
    print("Enter each edge in the format: vertex1 vertex2 weight")
    for _ in range(num_edges):
        vertex1, vertex2, weight = map(int, input().split())
        graph[vertex1].append((vertex2, weight))
        graph[vertex2].append((vertex1, weight))

    return graph


if __name__ == "__main__":
    graph = get_graph_input()
    mst = prims_algorithm(graph, start_vertex=0)

    # Print the edges in the MST
    print("\nMinimum Spanning Tree (MST) edges:")
    for u, v, weight in mst:
        print(f"Edge ({u}, {v}) with weight {weight}")