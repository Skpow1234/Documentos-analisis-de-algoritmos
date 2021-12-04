from node import node
"""
CREATE A FILE AND SEND A WORD INTO IT
"""




# utility function to print huffman
# codes for all symbols in the newly
# created Huffman tree


def printNodes(node, val=''):
	# huffman code for current node
	newVal = val + str(node.huff)

	# if node is not an edge node
	# then traverse inside it
	if(node.left):
		printNodes(node.left, newVal)
	if(node.right):
		printNodes(node.right, newVal)

		# if node is edge node then
		# display its huffman code
	if(not node.left and not node.right):
		file.write(f"{node.symbol} -------- {newVal}\n")


# characters for huffman tree
chars = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
'0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '.', ' ', ',']
freq = []

filename=str(input("Ingrese el nombre del archivo (nombre.extension): "))
f=open(filename,"r")
frase=f.read().rstrip()
f.close
for x in range(len(chars)):
  counter=0
  for i in range(len(frase)):
    if frase[i]==chars[x]:
      counter+=1
  freq.append(counter)

nodes = []

# converting characters and frequencies
# into huffman tree nodes
for x in range(len(chars)):
  if freq[x]!=0:
	  nodes.append(node(freq[x], chars[x]))
numNodos=len(nodes)
while len(nodes) > 1:
	# sort all the nodes in ascending order
	# based on theri frequency
	nodes = sorted(nodes, key=lambda x: x.freq)

	# pick 2 smallest nodes
	left = nodes[0]
	right = nodes[1]

	# assign directional value to these nodes
	left.huff = 0
	right.huff = 1

	# combine the 2 smallest nodes to create
	# new node as their parent
	newNode = node(left.freq+right.freq, left.symbol+right.symbol, left, right)

	# remove the 2 nodes and add their
	# parent as new node among others
	nodes.remove(left)
	nodes.remove(right)
	nodes.append(newNode)

# Huffman Tree is ready!
file = open("decodificacion.txt","w")
file.write("Numero de nodos: "+str(numNodos)+"\n")
file.write("Profundidad maxima del arbol generado: "+str(numNodos)+"\n")
file.write("Simbolo - Codigo\n")
printNodes(nodes[0])
file.close()



