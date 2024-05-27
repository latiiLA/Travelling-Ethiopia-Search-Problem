
#################################################################
#################################################################
#### 2.1 Graph Representation
#################################################################
#################################################################

graph = {
    "Kartum": [("Humera", 21), ("Metema", 19)],
    "Humera": [("Kartum", 21), ("Gondar", 9), ("Shire", 8)],
    "Debarke": [("Gondar", 4), ("Shire", 7)],
    "Shire": [("Humera", 8), ("Debarke", 7), ("Axum", 2)],
    "Axum": [("Shire", 2), ("Adwa", 1), ("Asmera", 5)],
    "Asmera": [("Axum", 5), ("Adigrat", 9)],
    "Adigrat": [("Asmera", 9), ("Adwa", 4), ("Mekelle", 4)],
    "Adwa": [("Axum", 1), ("Adigrat", 4), ("Mekelle", 7)],
    "Mekelle": [("Adwa", 7), ("Adigrat", 4), ("Sekota", 9), ("Alamata", 5)],
    "Sekota": [("Mekelle", 9), ("Alamata", 6), ("Lalibela", 6)],
    "Alamata": [("Mekelle", 5), ("Sekota", 6), ("Woldia", 3), ("Samara", 11)],
    "Samara": [("Alamata", 11), ("Fanti Rasu", 7), ("Woldia", 8), ("Gabi Rasu", 9)],
    "Fanti Rasu": [("Samara", 7), ("Kilbet Rasu", 6)],
    "Kilbet Rasu": [("Fanti Rasu", 6)],
    "Lalibela" : [("Sekota", 6), ("Woldia", 7), ("Debre Tabor", 8)],
    "Woldia": [("Lalibela", 7), ("Alamata", 3), ("Samara", 8), ("Dessie", 6)],
    "Debre Tabor": [("Lalibela", 8), ("Bahir Dar", 4)],
    "Bahir Dar": [("Debre Tabor", 4), ("Finote Selam", 6), ("Injibara", 4), ("Metekel", 11), ("Azezo", 7)],
    "Azezo": [("Bahir Dar", 7), ("Gondar", 1), ("Metema", 7)],
    "Gondar": [("Azezo", 1), ("Metema", 7), ("Debarke", 4), ("Humera", 9)],
    "Metema": [("Azezo", 7), ("Gondar", 7), ("Kartum", 19)],
    "Gabi Rasu": [("Samara", 9), ("Awash", 5)],
    "Awash": [("Gabi Rasu", 5), ("Matahara", 1), ("Chiro", 4)],
    "Chiro": [("Awash", 4), ("Dire Dawa", 8)],
    "Dire Dawa": [("Chiro", 8), ("Harar", 4)],
    "Harar": [("Dire Dawa", 4), ("Babile", 2)],
    "Babile": [("Harar", 2), ("Goba", 28), ("Jigjiga", 3)],
    "Jigjiga": [("Babile", 3), ("Dega Habur", 5)],
    "Dega Habur": [("Jigjiga", 5), ("Kebri Dehar", 6)],
    "Kebri Dehar": [("Dega Habur", 6), ("Gode", 5), ("Werder", 6)],
    "Werder": [("Kebri Dehar", 6)],
    "Gode": [("Kebri Dehar", 5), ("Dollo", 17), ("Mokadisho", 22), ("Sof Oumer", 23)],
    "Mokadisho": [("Gode", 22)],
    "Dollo": [("Gode", 17)],
    "Sof Oumer": [("Gode", 23), ("Goba", 6), ("Bale", 23)],
    "Goba": [("Babile", 28), ("Sof Oumer", 6), ("Bale", 18)],
    "Bale": [("Goba", 18), ("Sof Oumer", 23), ("Dodolla", 13), ("Liben", 11)],
    "Liben": [("Bale", 11)],
    "Dodolla": [("Bale", 13), ("Assasa", 1) , ("Shashemene", 3)],
    "Assasa": [("Dodolla", 1), ("Assella", 4)],
    "Assella": [("Assasa", 4), ("Adama", 4)],
    "Adama": [("Matahara", 3), ("Addis Ababa", 3), ("Batu", 4), ("Assella", 4)],
    "Matahara": [("Adama", 3), ("Awash", 1)],
    "Batu": [("Adama", 4), ("Buta Jirra", 2), ("Shashemene", 3)],
    "Shashemene": [("Batu", 3), ("Dodolla", 3), ("Hawassa", 1), ("Hossana", 7)],
    "Hawassa": [("Shashemene", 1), ("Dilla", 3)],
    "Dilla": [("Hawassa", 3), ("Bule Hora", 4)],
    "Bule Hora": [("Dilla", 4), ("Yabello", 3)],
    "Yabello": [("Bule Hora", 3), ("Konso", 3), ("Moyale", 6)],
    "Moyale": [("Yabello", 6), ("Nairobi", 22)],
    "Nairobi": [("Moyale", 22)],
    "Konso": [("Yabello", 3), ("Arba Minch", 4)],
    "Arba Minch": [("Konso", 4), ("Basketo", 10), ("Wolaita Sodo", 0)],
    "Wolaita Sodo": [("Arba Minch", 0), ("Dawro", 6), ("Hossana", 4)],
    "Hossana" : [("Wolaita Sodo", 4), ("Worabe", 2), ("Shashemene", 7)],
    "Worabe": [("Hossana", 2), ("Buta Jirra", 2), ("Wolkite", 5)],
    "Buta Jirra": [("Batu", 2), ("Worabe", 2)],
    "Basketo": [("Arba Minch", 10), ("Bench Maji", 5)],
    "Bench Maji": [("Basketo", 5), ("Juba", 22)],
    "Juba": [("Bench Maji", 22)],
    "Dawro": [("Wolaita Sodo", 6), ("Bonga", 10)],
    "Bonga": [("Dawro", 10), ("Jimma", 4), ("Mezan Teferi", 4), ("Tepi", 8)],
    "Mezan Teferi": [("Bonga", 4), ("Tepi", 4)],
    "Tepi": [("Mezan Teferi", 4), ("Bonga", 8), ("Gore", 9)],
    "Gore": [("Tepi", 9), ("Bedelle", 6), ("Gambella", 5)],
    "Gambella": [("Gore", 5), ("Dembi Dollo", 4)],
    "Bedelle": [("Gore", 6), ("Jimma", 7), ("Nekemete", 0)],
    "Jimma": [("Bedelle", 7), ("Bonga", 4), ("Wolkite", 8)],
    "Wolkite": [("Jimma", 8), ("Worabe", 5), ("Ambo", 6)],
    "Ambo" : [("Wolkite", 6),  ("Addis Ababa", 5), ("Nekemete", 9)],
    "Nekemete" : [("Ambo", 9), ("Bedelle", 0), ("Gimbi", 4)],
    "Gimbi" : [("Nekemete", 4), ("Dembi Dollo", 6)],
    "Dembi Dollo": [("Gimbi", 6), ("Gambella", 4), ("Assosa", 12)],
    "Assosa": [("Dembi Dollo", 12)],
    "Metekel": [("Bahir Dar", 11)],
    "Injibara": [("Bahir Dar", 4), ("Finote Selam", 2)],
    "Finote Selam": [("Injibara", 2), ("Bahir Dar", 6), ("Debre Markos", 3)],
    "Debre Markos": [("Finote Selam", 3), ("Debre Sina", 17)],
    "Debre Sina": [("Debre Markos", 17), ("Debre Birhan", 2), ("Kemise", 6)],
    "Kemise": [("Debre Sina", 6), ("Dessie", 4)],
    "Dessie": [("Kemise", 4), ("Woldia", 6)],
    "Debre Birhan": [("Debre Sina", 2), ("Addis Ababa", 5)],
    "Addis Ababa": [("Ambo", 5), ("Debre Birhan", 5), ("Adama", 3)]
}

# NOTES   
# Bedelle to Nekemete cost value is not given in the figure--- Therefore 0(zero) is taken
# Arbaminch to Nekemete const value is not given in the figure--- Therefore 0(zero) is taken



#################################################################
#################################################################
#### 2.2 Implementation
#################################################################
#################################################################

from queue import PriorityQueue

def uniform_cost_search(graph, start, goal):
    frontier = PriorityQueue()
    frontier.put((0, start))
    came_from = {}
    cost_so_far = {start: 0}

    while not frontier.empty():
        current_cost, current_node = frontier.get()

        if current_node == goal:
            break

        for neighbor, cost in graph[current_node]:
            new_cost = cost_so_far[current_node] + cost
            if neighbor not in cost_so_far or new_cost < cost_so_far[neighbor]:
                cost_so_far[neighbor] = new_cost
                priority = new_cost
                frontier.put((priority, neighbor))
                came_from[neighbor] = current_node

    path = [goal]
    while goal != start:
        goal = came_from[goal]
        path.append(goal)
    path.reverse()
    return path



# Function Calls

start = 'Addis Ababa'
goal = 'Lalibela'

path = uniform_cost_search(graph, start, goal)
print("Result for 2.2 sub question")
print(f"Path from {start} to {goal}: {path}\n\n")





#################################################################
#################################################################
#### 2.3 Implementation
#################################################################
#################################################################

import heapq

class MultiGoalUCS:
    def __init__(self, graph):
        self.graph = graph

    def uniform_cost_search(self, start, goals):
        # Priority queue: (cost, current_node, path, visited_cities, visited_goals)
        pq = [(0, start, [], set(), set())]
        all_goals = set(goals)
        visited = {}

        while pq:
            current_cost, current_node, path, visited_cities, visited_goals = heapq.heappop(pq)

            if current_node in visited_cities or (current_node, frozenset(visited_goals)) in visited:
                continue

            visited[(current_node, frozenset(visited_goals))] = current_cost
            path = path + [current_node]
            visited_cities = visited_cities | {current_node}
            if current_node in all_goals:
                visited_goals = visited_goals | {current_node}

            if visited_goals == all_goals:
                return path, current_cost

            for neighbor, travel_cost in self.graph[current_node]:
                new_cost = current_cost + travel_cost
                new_visited_goals = visited_goals.copy()
                if neighbor in all_goals:
                    new_visited_goals = new_visited_goals | {neighbor}
                
                if (neighbor, frozenset(new_visited_goals)) not in visited or new_cost < visited.get((neighbor, frozenset(new_visited_goals)), float('inf')):
                    heapq.heappush(pq, (new_cost, neighbor, path, visited_cities, new_visited_goals))

        return None, float('inf')


# Function Calls

goals = ["Axum", "Gondar", "Lalibela", "Babile", "Jimma", "Bale", "Sof Oumer", "Arba Minch"] # Defined in the question

ucs = MultiGoalUCS(graph)
path, cost = ucs.uniform_cost_search("Addis Ababa", goals)
print("Result for 2.3 sub question")
print(f"Path: {path}")
print(f"Total cost: {cost}")