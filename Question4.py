#################################################################
#################################################################
#### 4. Graph representation 
#################################################################
#################################################################



graph = {
    "Addis Ababa": ["Ambo", "Buta Jirra", "Adama"],
    "Adama": ["Addis Ababa", "Dire Dawa", "Mojo"],
    "Mojo": ["Kaffa", "Dilla"],
    "Dire Dawa": ["Chiro", "Harar"],
    "Buta Jirra": ["Addis Ababa", "Wolkite", "Worabe"],
    "Wolkite": ["Tepi", "Bench Naji"],
    "Worabe": ["Durame", "Hossana"],
    "Ambo": ["Nekemte", "Gedo"],
    "Nekemte": ["Limu", "Gimbi"],
    "Gedo": ["Shambu", "Fincha"]
}

# Utilities

utilities = {
    "Harar": 10,
    "Chiro": 6,
    "Dilla": 9,
    "Kaffa": 7,
    "Tepi": 6,
    "Bench Naji": 5,
    "Durame": 5,
    "Hossana": 6,
    "Limu": 8,
    "Gimbi": 8,
    "Shambu": 4,
    "Fincha": 5
}


#################################################################
#################################################################
#### 4. Implementation
#################################################################
#################################################################


class MiniMaxSearch:
    def __init__(self, graph, utilities):
        self.graph = graph
        self.utilities = utilities

    def minimax(self, node, depth, maximizing_player):
        if depth == 0 or node not in self.graph:
            return self.utilities.get(node, 0)

        if maximizing_player:
            max_eval = float('-inf')
            for neighbor in self.graph[node]:
                eval = self.minimax(neighbor, depth - 1, False)
                max_eval = max(max_eval, eval)
            return max_eval
        else:
            min_eval = float('inf')
            for neighbor in self.graph[node]:
                eval = self.minimax(neighbor, depth - 1, True)
                min_eval = min(min_eval, eval)
            return min_eval

    def find_best_path(self, start, depth):
        best_value = float('-inf')
        best_path = None

        for neighbor in self.graph[start]:
            path_value = self.minimax(neighbor, depth - 1, False)
            if path_value > best_value:
                best_value = path_value
                best_path = neighbor

        return best_path, best_value
    


# Function Calls

minimax_search = MiniMaxSearch(graph, utilities)
best_path, best_value = minimax_search.find_best_path("Addis Ababa", 3)  # Depth can be adjusted
print(f"Best Path: {best_path}")
print(f"Best Value (Quality of Coffee): {best_value}")
