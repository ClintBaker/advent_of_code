# X, Y, Z
# .txt w/ lines -> each line contains X, Y, Z (csv)
# close together according to straight line distance
# connect boxes -> same circuit


# connect together the 1000 pairs of junction boxes which are closest together.  After, what do you get if you multiply the sizes of the three largest circuits?

# ingest data
# identify closest (until we link 1000)
# link closest
# evaluate three largest *

from pathlib import Path
import heapq # minheap (use neg values to create a max-heap)

class DSU: # Disjoint Set Union (Union-Find)
    def __init__(self,n):
        self.parent = list(range(n))
        self.size = [1] * n
    
    def find(self, x):
        while self.parent[x] != x:
            self.parent[x] = self.parent[self.parent[x]]
            x = self.parent[x]
        return x
    
    def union(self, a,b):
        ra = self.find(a)
        rb = self.find(b)
        if ra == rb:
            return False
        if self.size[ra] < self.size[rb]:
            ra,rb = rb,ra
        self.parent[rb] = ra
        self.size[ra] += self.size[rb]
        return True
    def component_sizes(self):
        counts = {}
        for i in range(len(self.parent)):
            r = self.find(i)
            counts[r] = counts.get(r,0) + 1
        return list(counts.values())
    


def ingest_data(filename = 'sample.txt'):
    path = Path(__file__).with_name(filename)
    data = []
    with path.open("r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            data.append([int(field.strip()) for field in line.split(",")])
    return data

def calculate_distance_sq(a, b):
    dx = a[0] - b[0]
    dy = a[1] - b[1]
    dz = a[2] - b[2]
    return dx*dx + dy*dy + dz*dz

def k_smallest_edges(points, k=1000):
    """
    Create a max heap that keeps track of the k smallest edges
    """
    heap = []
    n = len(points)

    # for each set of points
    for i in range(n):
        # iterate through the remaining points and calculate distance between
        for j in range(i + 1, n):
            distance = calculate_distance_sq(points[i], points[j])

            if len(heap) < k:
                heapq.heappush(heap, (-distance, i, j)) # push to heap no matter what if we're less than k
            else:
                if distance < -heap[0][0]: #otherwise, only if our current distance is less than the greatest value in our heap, replace the current max with new edge
                    heapq.heapreplace(heap, (-distance, i, j)) # negative for max instead of min
    # convert back to positive and sort
    edges = [(-neg_dist, i, j) for (neg_dist, i, j) in heap]
    edges.sort(key=lambda t:t[0])
    return edges # we now have the k smallest edges across the entire data set

def jank(edges):
    circuits = []
    for edge in edges:
        edge1_circuit_found_index = -1
        edge2_circuit_found_index = -1 # ty yaba
        for i, circuit in enumerate(circuits):
            if edge[1] in circuit:
                edge1_circuit_found_index = i
            if edge[2] in circuit:
                edge2_circuit_found_index = i
        if edge1_circuit_found_index != -1 and edge2_circuit_found_index != -1:
            # determine if same circuit or not
            if edge1_circuit_found_index == edge2_circuit_found_index:
                #already same circuit keep it moving
                continue
            else:
                #merge circuits
                circuits[edge1_circuit_found_index].extend(circuits[edge2_circuit_found_index])
                circuits.pop(edge2_circuit_found_index)
        elif edge1_circuit_found_index != -1:
            circuits[edge1_circuit_found_index].append(edge[2])
        elif edge2_circuit_found_index != -1:
            circuits[edge2_circuit_found_index].append(edge[1])
        else:
            circuits.append([edge[1], edge[2]])
    return circuits


# cases
# 1. edge1 in a circuit and edge2 not
# 2. edge1 in a circuit and edge2 also in circuit (same circuits)
# 3. edge2 in a circuit edge1 not
# 4. edge1 in a circuit and edge2 also in circuit (different circuits)
# 5. neither in circuit

    return circuits


# take next two pairs
# - if either of the pairs is in an existing list, append to that list



def main():
    # 1. ingest data
    data = ingest_data('input.txt')

    # find 1000 smallest edges
    edges = k_smallest_edges(data, 1000)
    circuits = jank(edges)

    circuits.sort(key=len, reverse=True)
    print(circuits)

    print(len(circuits[0]) * len(circuits[1]) * len(circuits[2]))





main()