import networkx as nx
import matplotlib.pyplot as plt

print("---- BIENVENIDX A NUESTRO PROGRAMA ----")
message = "Ingrese la sucesión de grados separados por espacio: "

# Reads the sequence separated by space 
s = list(map(int, input(message).split(" "))) # represents the degrees of all nodes
# Creates a copy of the original list
s2 = s.copy() # We will work the Havel-hakimi algorithm with this copy

# Represents one step of the Havel-hakimi algorithm
def execute():
  # sorts the list
  s2.sort(reverse=True);  

  # If the next integer to be deleted is greater than the lenght of the list
  # then we reach the end of the algorithm
  if (s2[0] > len(s2)):
    return False #returns false if we can no longer execute the algorithm

  # Extracts the first element x and substracts -1 to the next x elements 
  first = s2.pop(0)
  for i in range(first): s2[i] -= 1; 
  return True

# Havel-hakimi algorithm
sw = True
# while the length of the list is greater than 2 and sw == True
while (len(s2) > 2 and sw):
  sw = execute()

# -- At this point we can state that the list has 2 elements --

# If ither of the two elements is nonzero or sw == False
if ((s2[0] != 0 or s2[1] != 0) or sw == False):
  print("Lo sentimos, la sucesión ingresada no pertenece a un grafo :(")
else:
  # Creates a empty graph
  G = nx.Graph()
  
  # We add all the nodes (with no connections)
  for i in range(len(s)):
    G.add_node(i) 

  # as long as there are nodes with degree greater than 0
  while (sum(s) > 0): 
    # add edges to all the nodes whose degree > 0
    for i in range(len(s)): # loops the nodes
      for k in range(len(s)): # loops the nodes looking for the other node to be connected
        # we are trying to connect (i, k) where i != k and degree(k) > 0 and degree(i) > 0
        if (k != i and s[k] > 0 and s[i] > 0):
          # if (i, k) or (k, i) already exists, then we continue looking for another k-node
          if ((i, k) in list(G.edges) or (k, i) in list(G.edges)):
            continue
          # we connect the i-node with the k-node
          G.add_edge(i, k)
          # we substract 1 both from degrees(k) and degrees(i)
          s[i] -= 1
          s[k] -= 1
          break
          
  #Code for printing the graph
  #literalmente lo copié y pegué de la documentación, no me pregunten por esto XD
  subax1 = plt.subplot(121)
  nx.draw(G, with_labels=True, font_weight='bold')
  subax2 = plt.subplot(122)
  nx.draw_shell(G, nlist=[range(5, 10), range(5)], with_labels=True, font_weight='bold')
  plt.show() 