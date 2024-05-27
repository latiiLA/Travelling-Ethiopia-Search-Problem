#################################################################
#################################################################
#### 3. Graph representation
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
    "Samara": [("Alamata", 11), ("Fanti Rasu", 7), ("Woldia", 8), ("Gabi Rasu", 10)],
    "Fanti Rasu": [("Samara", 7), ("Kilbet Rasu", 6)],
    "Kilbet Rasu": [("Fanti Rasu", 6)],
    "Lalibela" : [("Sekota", 6), ("Woldia", 7), ("Debre Tabor", 8)],
    "Woldia": [("Lalibela", 7), ("Alamata", 3), ("Samara", 8), ("Dessie", 6)],
    "Debre Tabor": [("Lalibela", 8), ("Bahir Dar", 4), ("Gondar", 6)],
    "Bahir Dar": [("Debre Tabor", 4), ("Finote Selam", 6), ("Injibara", 4), ("Metekel", 11), ("Azezo", 7)],
    "Azezo": [("Bahir Dar", 7), ("Gondar", 1), ("Metema", 7)],
    "Gondar": [("Azezo", 1), ("Metema", 7), ("Debarke", 4), ("Humera", 9), ("Debre Tabor", 6)],
    "Metema": [("Azezo", 7), ("Gondar", 7), ("Kartum", 19)],
    "Gabi Rasu": [("Samara", 10), ("Awash", 5)],
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
    "Mokadisho": [("Gode", 22), ("Moyale", 40)],
    "Dollo": [("Gode", 17), ("Moyale", 18)],
    "Sof Oumer": [("Gode", 23), ("Goba", 6), ("Robe", 23)],
    "Goba": [("Babile", 28), ("Sof Oumer", 6), ("Robe", 18)],
    "Robe": [("Goba", 18), ("Sof Oumer", 23), ("Dodolla", 13), ("Liben", 11)],
    "Liben": [("Robe", 11), ("Moyale", 11)],
    "Dodolla": [("Robe", 13), ("Assasa", 1) , ("Shashemene", 3)],
    "Assasa": [("Dodolla", 1), ("Assella", 4)],
    "Assella": [("Assasa", 4), ("Adama", 4)],
    "Adama": [("Matahara", 3), ("Addis Ababa", 3), ("Batu", 4), ("Assella", 4)],
    "Matahara": [("Adama", 3), ("Awash", 1)],
    "Batu": [("Adama", 4), ("Buta Jirra", 2), ("Shashemene", 3)],
    "Shashemene": [("Batu", 3), ("Dodolla", 3), ("Hawassa", 1), ("Hossana", 7), ("Worabe", 6)],
    "Hawassa": [("Shashemene", 1), ("Dilla", 3)],
    "Dilla": [("Hawassa", 3), ("Bule Hora", 4)],
    "Bule Hora": [("Dilla", 4), ("Yabello", 2)],
    "Yabello": [("Bule Hora", 2), ("Konso", 3), ("Moyale", 6)],
    "Moyale": [("Nairobi", 22), ("Mokadisho", 40), ("Dollo", 18), ("Liben", 11), ("Yabello", 6)],
    "Nairobi": [("Moyale", 22)],
    "Konso": [("Yabello", 3), ("Arba Minch", 4)],
    "Arba Minch": [("Konso", 4), ("Basketo", 10), ("Wolaita Sodo", 4)],
    "Wolaita Sodo": [("Arba Minch", 4), ("Dawro", 6), ("Hossana", 4)],
    "Hossana" : [("Wolaita Sodo", 4), ("Worabe", 2), ("Shashemene", 7), ("Wolkite", 5)],
    "Worabe": [("Hossana", 2), ("Buta Jirra", 2), ("Wolkite", 5), ("Shashemene", 6)],
    "Buta Jirra": [("Batu", 2), ("Worabe", 2), ("Wolkite", 4)],
    "Basketo": [("Arba Minch", 10), ("Bench Maji", 5)],
    "Bench Maji": [("Basketo", 5), ("Juba", 22)],
    "Juba": [("Benchi Maji", 22)],
    "Dawro": [("Wolaita Sodo", 6), ("Bonga", 10)],
    "Bonga": [("Dawro", 10), ("Jimma", 4), ("Mezan Teferi", 4), ("Tepi", 8)],
    "Mezan Teferi": [("Bonga", 4), ("Tepi", 4)],
    "Tepi": [("Mezan Teferi", 4), ("Bonga", 8), ("Gore", 9)],
    "Gore": [("Tepi", 9), ("Bedelle", 6), ("Gambella", 5)],
    "Gambella": [("Gore", 5), ("Dembi Dollo", 4)],
    "Bedelle": [("Gore", 6), ("Jimma", 7), ("Nekemete", 4)],
    "Jimma": [("Bedelle", 7), ("Bonga", 4), ("Wolkite", 8)],
    "Wolkite": [("Jimma", 8), ("Worabe", 5), ("Ambo", 6), ("Hossana", 5), ("Buta Jirra", 4)],
    "Ambo" : [("Wolkite", 6),  ("Addis Ababa", 5), ("Nekemete", 8)],
    "Nekemete" : [("Ambo", 8), ("Bedelle", 4), ("Gimbi", 4)],
    "Gimbi" : [("Nekemete", 4), ("Dembi Dollo", 6), ("Assosa", 8)],
    "Dembi Dollo": [("Gimbi", 6), ("Gambella", 4), ("Assosa", 12)],
    "Assosa": [("Dembi Dollo", 12), ("Gimbi", 8)],
    "Metekel": [("Bahir Dar", 11)],
    "Injibara": [("Bahir Dar", 4), ("Finote Selam", 2)],
    "Finote Selam": [("Injibara", 2), ("Bahir Dar", 6), ("Debre Markos", 3)],
    "Debre Markos": [("Finote Selam", 3), ("Debre Sina", 17), ("Addis Ababa", 13)],
    "Debre Sina": [("Debre Markos", 17), ("Debre Birhan", 2), ("Kemise", 7)],
    "Kemise": [("Debre Sina", 7), ("Dessie", 4)],
    "Dessie": [("Kemise", 4), ("Woldia", 6)],
    "Debre Birhan": [("Debre Sina", 2), ("Addis Ababa", 5)],
    "Addis Ababa": [("Ambo", 5), ("Debre Birhan", 5), ("Adama", 3), ("Debre Markos", 13)]
}

# heuristic values

heuristics = {
    "Kartum": 81,
    "Humera": 65,
    "Debarke": 60,
    "Shire": 67,
    "Axum": 66,
    "Asmera": 68,
    "Adigrat": 62,
    "Adwa": 65,
    "Mekelle": 58,
    "Sekota": 59,
    "Alamata": 53,
    "Samara": 42,
    "Fanti Rasu": 49,
    "Kilbet Rasu": 55,
    "Lalibela" : 57,
    "Woldia": 50,
    "Debre Tabor": 52,
    "Bahir Dar": 48,
    "Azezo": 55,
    "Gondar": 56,
    "Metema": 62,
    "Gabi Rasu": 32,
    "Awash": 27,
    "Chiro": 31,
    "Dire Dawa": 31,
    "Harar": 35,
    "Babile": 37,
    "Jigjiga": 40,
    "Dega Habur": 45,
    "Kebri Dehar": 40,
    "Werder": 46,
    "Gode": 35,
    "Mokadisho": 40,
    "Dollo": 18,
    "Sof Oumer": 45,
    "Goba": 40,
    "Robe": 22,
    "Liben": 11,
    "Dodolla": 19,
    "Assasa": 18,
    "Assella": 22,
    "Adama": 23,
    "Matahara": 26,
    "Batu": 19,
    "Shashemene": 16,
    "Hawassa": 15,
    "Dilla": 12,
    "Bule Hora": 8,
    "Yabello": 6,
    "Moyale": 0,
    "Nairobi": 22,
    "Konso": 9,
    "Arba Minch": 13,
    "Wolaita Sodo": 17,
    "Hossana" : 21,
    "Worabe": 22,
    "Buta Jirra": 21,
    "Basketo": 23,
    "Bench Maji": 28,
    "Juba": 50,
    "Dawro": 23,
    "Bonga": 33,
    "Mezan Teferi": 37,
    "Tepi": 41,
    "Gore": 46,
    "Gambella": 51,
    "Bedelle": 40,
    "Jimma": 33,
    "Wolkite": 25,
    "Ambo" : 31,
    "Nekemete" : 39,
    "Gimbi" : 43,
    "Dembi Dollo": 49,
    "Assosa": 51,
    "Metekel": 59,
    "Injibara": 44,
    "Finote Selam": 42,
    "Debre Markos": 39,
    "Debre Sina": 33,
    "Kemise": 40,
    "Dessie": 44,
    "Debre Birhan": 31,
    "Addis Ababa": 26
}


#################################################################
#################################################################
#### 3. Implementation
#################################################################
#################################################################


import heapq

class AStarSearch:
    def __init__(self, graph, heuristics):
        self.graph = graph
        self.heuristics = heuristics

    def a_star_search(self, start, goal):
        # Priority queue: (estimated_total_cost, current_node, current_cost, path)
        pq = [(self.heuristics[start], start, 0, [])]
        visited = set()

        while pq:
            estimated_total_cost, current_node, current_cost, path = heapq.heappop(pq)

            if current_node in visited:
                continue

            visited.add(current_node)
            path = path + [current_node]

            if current_node == goal:
                return path, current_cost

            for neighbor, travel_cost in self.graph[current_node]:
                if neighbor not in visited:
                    total_cost = current_cost + travel_cost
                    estimated_cost = total_cost + self.heuristics[neighbor]
                    heapq.heappush(pq, (estimated_cost, neighbor, total_cost, path))

        return None, float('inf')




# Function Calls


astar = AStarSearch(graph, heuristics)
path, cost = astar.a_star_search("Addis Ababa", "Moyale")
print(f"Path: {path}")
print(f"Total cost: {cost}")

