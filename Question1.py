from collections import deque

class GraphSearch:
    def __init__(self, graph, initial_state, goal_state, strategy='BFS'):
        self.graph = graph
        self.initial_state = initial_state
        self.goal_state = goal_state
        self.strategy = strategy

    def bfs(self):
        queue = deque([(self.initial_state, [self.initial_state])])
        visited = set()

        while queue:
            node, path = queue.popleft()

            if node == self.goal_state:
                return path

            if node not in visited:
                visited.add(node)
                for neighbor in self.graph.get(node, []):
                    if neighbor not in visited:
                        queue.append((neighbor, path + [neighbor]))

        return None

    def dfs(self):
        stack = [(self.initial_state, [self.initial_state])]
        visited = set()

        while stack:
            node, path = stack.pop()

            if node == self.goal_state:
                return path

            if node not in visited:
                visited.add(node)
                for neighbor in self.graph.get(node, []):
                    if neighbor not in visited:
                        stack.append((neighbor, path + [neighbor]))

        return None

    def search(self):
        if self.strategy == '1':
            return self.dfs()
        elif self.strategy == '2':
            return self.bfs()
        else:
            raise ValueError("Unsupported search strategy. Use 'BFS' or 'DFS'.")




graph = {
    "Kartum": ["Humera", "Metema"],
    "Humera": ["Kartum", "Gondar", "Shire"],
    "Debarke": ["Gondar", "Shire"],
    "Shire": ["Humera", "Debarke", "Axum"],
    "Axum": ["Shire", "Adwa", "Asmera"],
    "Asmera": ["Axum", "Adigrat"],
    "Adigrat": ["Asmera", "Adwa", "Mekelle"],
    "Adwa": ["Axum", "Adigrat", "Mekelle"],
    "Mekelle": ["Adwa", "Adigrat", "Sekota", "Alamata"],
    "Sekota": ["Mekelle", "Alamata", "Lalibela"],
    "Alamata": ["Mekelle", "Sekota", "Woldia", "Samara"],
    "Samara": ["Alamata", "Fanti Rasu", "Woldia", "Gabi Rasu"],
    "Fanti Rasu": ["Samara", "Kilbet Rasu"],
    "Kilbet Rasu": ["Fanti Rasu"],
    "Lalibela" : ["Sekota", "Woldia", "Debre Tabor"],
    "Woldia": ["Lalibela", "Alamata", "Samara", "Dessie"],
    "Debre Tabor": ["Lalibela", "Bahir Dar"],
    "Bahir Dar": ["Debre Tabor", "Finote Selam", "Injibara", "Metekel", "Azezo"],
    "Azezo": ["Bahir Dar", "Gondar", "Metema"],
    "Gondar": ["Azezo", "Metema", "Debarke", "Humera"],
    "Metema": ["Azezo", "Gondar", "Kartum"],
    "Gabi Rasu": ["Samara", "Awash"],
    "Awash": ["Gabi Rasu", "Matahara", "Chiro"],
    "Chiro": ["Awash", "Dire Dawa"],
    "Dire Dawa": ["Chiro", "Harar"],
    "Harar": ["Dire Dawa", "Babile"],
    "Babile": ["Harar", "Jigjiga"],
    "Jigjiga": ["Babile", "Dega Habur"],
    "Dega Habur": ["Jigjiga", "Goba", "Kebri Dehar"],
    "Kebri Dehar": ["Dega Habur", "Sof Oumer", "Gode", "Werder"],
    "Werder": ["Kebri Dehar"],
    "Gode": ["Kebri Dehar", "Dollo", "Mokadisho"],
    "Mokadisho": ["Gode"],
    "Dollo": ["Gode"],
    "Sof Oumer": ["Kebri Dehar", "Goba", "Bale"],
    "Goba": ["Dega Habur", "Sof Oumer", "Bale"],
    "Bale": ["Goba", "Sof Oumer", "Dodolla", "Liben"],
    "Liben": ["Bale"],
    "Dodolla": ["Bale", "Assasa", "Shashemene"],
    "Assasa": ["Dodolla", "Assella"],
    "Assella": ["Assasa", "Adama"],
    "Adama": ["Matahara", "Addis Ababa", "Batu", "Assella"],
    "Matahara": ["Adama", "Awash"],
    "Batu": ["Adama", "Buta Jirra", "Shashemene"],
    "Shashemene": ["Batu", "Dodolla", "Hawassa", "Hossana"],
    "Hawassa": ["Shashemene", "Dilla"],
    "Dilla": ["Hawassa", "Bule Hora"],
    "Bule Hora": ["Dilla", "Yabello"],
    "Yabello": ["Bule Hora", "Konso", "Moyale"],
    "Moyale": ["Yabello", "Nairobi"],
    "Nairobi": ["Moyale"],
    "Konso": ["Yabello", "Arba Minch"],
    "Arba Minch": ["Konso", "Basketo", "Wolaita Sodo"],
    "Wolaita Sodo": ["Arba Minch", "Dawro", "Hossana"],
    "Hossana" : ["Wolaita Sodo", "Worabe", "Shashemene"],
    "Worabe": ["Hossana", "Buta Jirra", "Wolkite"],
    "Buta Jirra": ["Batu", "Worabe"],
    "Basketo": ["Arba Minch", "Dawro", "Bench Maji", "Mezan Teferi"],
    "Bench Maji": ["Basketo","Juba"],
    "Juba": ["Benchi Maji"],
    "Dawro": ["Basketo", "Wolaita Sodo", "Bonga"],
    "Bonga": ["Dawro", "Jimma", "Mezan Teferi", "Tepi"],
    "Mezan Teferi": ["Bonga", "Basketo", "Tepi"],
    "Tepi": ["Mezan Teferi", "Bonga", "Gore"],
    "Gore": ["Tepi", "Bedelle", "Gambella"],
    "Gambella": ["Gore", "Dembi Dollo"],
    "Bedelle": ["Gore", "Jimma", "Nekemete"],
    "Jimma": ["Bedelle", "Bonga", "Wolkite"],
    "Wolkite": ["Jimma", "Worabe", "Ambo"],
    "Ambo" : ["Wolkite",  "Addis Ababa", "Nekemete"],
    "Nekemete" : ["Ambo", "Bedelle", "Gimbi"],
    "Gimbi" : ["Nekemete", "Dembi Dollo"],
    "Dembi Dollo": ["Gimbi", "Gambella", "Assosa"],
    "Assosa": ["Dembi Dollo", "Metekel"],
    "Metekel": ["Assosa", "Bahir Dar"],
    "Injibara": ["Bahir Dar", "Finote Selam"],
    "Finote Selam": ["Injibara", "Bahir Dar","Debre Markos"],
    "Debre Markos": ["Finote Selam", "Debre Sina"],
    "Debre Sina": ["Debre Markos", "Debre Birhan", "Kemise"],
    "Kemise": ["Debre Sina", "Dessie"],
    "Dessie": ["Kemise", "Woldia"],
    "Debre Birhan": ["Debre Sina", "Addis Ababa"],
    "Addis Ababa": ["Ambo", "Debre Birhan", "Adama"]
}

# Manual initialization
# initial_state = 'Nekemete'
# goal_state = 'Addis Ababa'
# strategy = 'BFS'  # or 'DFS'

# Input from the user
initial_state = input("Enter the initial state: ")
goal_state = input("Enter the goal state: ")
strategy = input("Enter the search strategy: Enter 1 for DFS and Enter 2 for BFS: ")

if initial_state in graph and goal_state in graph and (strategy == "1" or strategy == "2"):
    search = GraphSearch(graph, initial_state, goal_state, strategy)
    path = search.search()
    print(f"Path found using {strategy}: {path}")
else:
    print(f"The input is incorrect. Please check spelling or correct city or correct strategy")
