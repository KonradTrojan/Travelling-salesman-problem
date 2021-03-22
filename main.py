from methods import naive_alhorithm
from methods import matrix
from methods import show_matrix

cordinates = []

plik = open("TSP.txt",'r')

for line in plik:
    cordinates.append(line)
shortest_path = 10000.0
for i in range(1,101):
    for line in open("TSP.txt",'r'):
        cordinates.append(line)
    print(i,end=' ')
    naive_alhorithm(cordinates,i)

#matrix(cordinates)
#show_matrix(matrix(cordinates))
