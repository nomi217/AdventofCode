from itertools import combinations
from collections import defaultdict

def parse_connections(input_text):
    # Create adjacency list representation
    graph = defaultdict(set)
    for line in input_text.strip().split('\n'):
        if line:
            a, b = line.strip().split('-')
            graph[a].add(b)
            graph[b].add(a)
    return graph

def find_connected_triples(graph):
    # Get all possible combinations of three computers
    all_computers = list(graph.keys())
    all_triples = []
    
    # Check each possible triple
    for triple in combinations(all_computers, 3):
        # Check if all pairs in the triple are connected
        if (triple[1] in graph[triple[0]] and 
            triple[2] in graph[triple[0]] and 
            triple[2] in graph[triple[1]]):
            all_triples.append(sorted(triple))
    
    return all_triples

def count_triples_with_t(triples):
    # Count triples containing at least one computer starting with 't'
    t_triples = [triple for triple in triples 
                 if any(comp.startswith('t') for comp in triple)]
    return len(t_triples)

# Read input from file
with open('input.txt', 'r') as file:
    input_text = file.read()

# Process the network
graph = parse_connections(input_text)
triples = find_connected_triples(graph)
t_count = count_triples_with_t(triples)

print(f"Number of triples containing a computer starting with 't': {t_count}")