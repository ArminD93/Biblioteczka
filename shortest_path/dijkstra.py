#!/usr/bin/env python
# -*- coding: utf-8 -*- 
import sys
import heapq
import settings



class Vertex:
    def __init__(self, node):
        self.id = node
        self.adjacent = {}
        # Ustaw odległość do nieskończoności dla wszystkich węzłów
        self.distance = sys.maxint
        #	Zaznacz wszystkie węzły jako nieodwiedzone       
        self.visited = False  
        # Poprzednik
        self.previous = None

    def add_neighbor(self, neighbor, weight=0):
        self.adjacent[neighbor] = weight



    def get_id(self):
        return self.id

    def get_weight(self, neighbor):
        return self.adjacent[neighbor]

    def set_distance(self, dist):
        self.distance = dist

    def get_distance(self):
        return self.distance

    def set_previous(self, prev):
        self.previous = prev

    def set_visited(self):
        self.visited = True



class Graph:
    def __init__(self):
        self.vert_dict = {}
        self.num_vertices = 0

    def __iter__(self):
        return iter(self.vert_dict.values())

    def add_vertex(self, node):
        self.num_vertices = self.num_vertices + 1
        new_vertex = Vertex(node)
        self.vert_dict[node] = new_vertex
        return new_vertex

    def get_vertex(self, n):
        if n in self.vert_dict:
            return self.vert_dict[n]
        else:
            return None

    def add_edge(self, frm, to, cost = 0):
        if frm not in self.vert_dict:
            self.add_vertex(frm)
        if to not in self.vert_dict:
            self.add_vertex(to)

        self.vert_dict[frm].add_neighbor(self.vert_dict[to], cost)
        self.vert_dict[to].add_neighbor(self.vert_dict[frm], cost)
    
 

        

    def get_vertices(self):
        return self.vert_dict.keys()

    def set_previous(self, current):
        self.previous = current

    def get_previous(self, current):
        return self.previous

def shortest(v, path):
    #Utwórz najkrótszą ścieżkę z v.previous (v.poprzedni)
    if v.previous:
        path.append(v.previous.get_id())
        shortest(v.previous, path)
    return



def dijkstra(aGraph, start, target):
    
    # Ustaw odległość węzła początkowego na zero 
    start.set_distance(0)

    # Wstaw parę krotek ( tuple) do kolejki priorytetów
    unvisited_queue = [(v.get_distance(),v) for v in aGraph]
    heapq.heapify(unvisited_queue)

    while len(unvisited_queue):
        # Wyrzuca wierzchołek o najmniejszej odległości 
        uv = heapq.heappop(unvisited_queue)
        current = uv[1]
        current.set_visited()

        #Dla następnego v.sąsiadującego (v.adjacent)
        for next in current.adjacent:
            # Jeśli odwiedzony to pomiń
            if next.visited:
                continue
            new_dist = current.get_distance() + current.get_weight(next)
            
            if new_dist < next.get_distance():
                next.set_distance(new_dist)
                next.set_previous(current)
                
             
        # Przebuduj stos
        # 1. Pobierz ze stosu każdy element
        while len(unvisited_queue):
            heapq.heappop(unvisited_queue)
        # 2. Umieść wszystkie wierzchołki nieodwiedzone w kolejce
        unvisited_queue = [(v.get_distance(),v) for v in aGraph if not v.visited]
        heapq.heapify(unvisited_queue)
    
      
        
def Dijkstra(frm, to):
        
        g = Graph()

        g.add_vertex('1A')
        g.add_vertex('1B')
        g.add_vertex('1C')
        g.add_vertex('1D')
        g.add_vertex('1E')
    
        g.add_vertex('2A')
        g.add_vertex('2B')
        g.add_vertex('2C')
        g.add_vertex('2D')
        g.add_vertex('2E')
    
        g.add_vertex('3A')
        g.add_vertex('3B')
        g.add_vertex('3C')
        g.add_vertex('3D')
        g.add_vertex('3E')
    
        g.add_vertex('4A')
        g.add_vertex('4B')
        g.add_vertex('4C')
        g.add_vertex('4D')
        g.add_vertex('4E')
    
# ##################################

        pairs = [['1A', '1B', 5], ['1B', '1C', 5],['1C', '1D', 5],['1D', '1E', 5], ['2A', '2B', 5],
					['2B', '2C', 5], ['2C', '2D', 5], ['2D', '2E', 5], ['3A', '3B', 5], ['3B', '3C', 5],
					['3C', '3D', 5], ['3D', '3E', 5], ['4A', '4B', 5], ['4B', '4C', 5], ['4C', '4D', 5],
					['4D', '4E', 5], ['1A', '2A', 23], ['1B', '2B', 23], ['1C', '2C', 23], ['1D', '2D', 23],
					['1E', '2E', 23], ['2A', '3A', 23], ['2B', '3B', 23], ['2C', '3C', 23], ['2D', '3D', 23],
					['2E', '3E', 23], ['3A', '4A', 23], ['3B', '4B', 23], ['3C', '4C', 23], ['3D', '4D', 23],
					['3E', '4E', 23]]
    
        for pair in pairs:
            #print (pair[0], pair[1], pair[2])
            g.add_edge(pair[0], pair[1], pair[2])
    

        dijkstra(g, g.get_vertex(frm), g.get_vertex(to)) 

        target = g.get_vertex(to)
        
        global path
        
        path = [target.get_id()]
        shortest(target, path)
    
        #print 'The shortest path : %s ' %(path[::-1])
       
        
        global listA
         
        listA = path[::-1]
         
        return listA
    




    






               
        
        
