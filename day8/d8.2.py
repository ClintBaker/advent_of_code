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

def find_all_edges(points):
    # for each point identify all edges (push to edges)
    # you only need to go forward
    edges = []

    # for each point
    for i, point in enumerate(points):
        # for each point after current index of point
        for j in range(i,len(points)):
            distance = calculate_distance_sq(point, points[j])
            edges.append([distance, i, j]) # push distance, index of edge 1, index of edge 2
    
    
    return edges

def create_circuits(edges):
    circuits = []
    last_connection_ids = {'a': -1, 'b': -1}
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
                # update our last_connection_x_values to reflect the last connection
                last_connection_ids['a'] = edge[1]
                last_connection_ids['b'] = edge[2]

                #merge circuits 
                circuits[edge1_circuit_found_index].extend(circuits[edge2_circuit_found_index])
                circuits.pop(edge2_circuit_found_index)
        elif edge1_circuit_found_index != -1:
            circuits[edge1_circuit_found_index].append(edge[2])
            last_connection_ids['a'] = edge[1]
            last_connection_ids['b'] = edge[2]
        elif edge2_circuit_found_index != -1:
            circuits[edge2_circuit_found_index].append(edge[1])
            last_connection_ids['a'] = edge[1]
            last_connection_ids['b'] = edge[2]
        else:
            circuits.append([edge[1], edge[2]])
    return last_connection_ids


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
    edges = find_all_edges(data)
    # sort edges
    edges.sort(key=lambda e: e[0])
    last_connection_ids = create_circuits(edges)
    print(data[last_connection_ids['a']][0] * data[last_connection_ids['b']][0])

    # multiply x coords of last two connections
    # how can i identify the last connection





main()