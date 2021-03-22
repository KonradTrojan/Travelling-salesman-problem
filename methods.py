import math

# Algorytm ktory rozwiazuje problem komiwojazera w nastepujacy sposob"
# Dla wybranego wierzcholka szuka wierzcholka sasiedniego o najmniejszej drodze(wadze) miedzy nimi
# Przechodzi do niego i powtarza te czynnosc

def naive_alhorithm(cordinates_list,iterator):
    global x_voyager, y_voyager, target_line, target, y_voyager_add, x_voyager_add, sum, x_start, y_start, voyager_start

    voyager = iterator                      #wierzcholek poczatkowy
    for line in cordinates_list:            #przeszkuje plik z wspolrzednymi w poszukiwaniu linii z danym nr miasta
        if int(line.split()[0]) == voyager:
            x_voyager = float(line.split()[1])  #po znalezieniu przydzielam wspolrzedne odpowiedniego miasta
            y_voyager = float(line.split()[2])
            cordinates_list.remove(line)        #usuwam linijke z poczatkowym miastem
            break

    sum = 0                                     #suma drog, jakie przebedziemy w sciezce
    shortest_path = 10432113243.3               #wartosci minimalna z ktore bedziemy porownywac, wyglada tak, bo inaczej nie dzialalo

    for i in range(len(cordinates_list)):
        for line in cordinates_list:            #przeszukuje wszystkie linie w pliku
            x_target = float(line.split()[1])   #przydzielam tymczasowo wspolrzedne przeszkiwanego miasta
            y_target = float(line.split()[2])
            route = length(x_voyager,y_voyager,x_target,y_target)   #licze odleglosc miedzy miastem z listy, a miastem gdzie znajduje sie podroznik
            if route < shortest_path:                               #porownuje, czy wyliczona odleglosc jest mniejsza od najkrotszej odleglosci
                shortest_path = route                               #jesli tak, to wyliczona odleglosc staje sie najkrotsza
                target = float(line.split()[0])                     #zapisuje nr miasta 'celu'
                target_line = line                                  #zapisuje linijke, ktora bedzie trzeba usunac po przejsciu do celu
                x_voyager_add = x_target                            #zmienne pomocnicze do zapisu wspolrzednych
                y_voyager_add = y_target

        x_voyager = x_voyager_add
        y_voyager = y_voyager_add
        cordinates_list.remove(target_line)                         #usuwam z listy linie miasta 'celu' do ktorego doszedlem
        sum += shortest_path                                        #dodaje do sumy drog obecna droge
        shortest_path = 123456.7
    print("Total cost: ",sum)                                       #wypisuje calkowita przebyta droge

def length(x1,y1,x2,y2):            #funkcja liczace wektor odleglosci
    return math.sqrt((x1-x2)*(x1-x2)+(y1-y2)*(y1-y2))

def matrix(cordinates_list):        #funckja tworzaca macierz wag pomiedzy odpowiednimi wierzcholkami
    matrix = []
    for line in cordinates_list:
        matrix_add = []
        x_node = float(line.split()[1])
        y_node = float(line.split()[2])
        for line in cordinates_list:
            x_node_other = float(line.split()[1])
            y_node_other = float(line.split()[2])
            length = math.sqrt((x_node-x_node_other)*(x_node-x_node_other)+(y_node-y_node_other)*(y_node-y_node_other))
            matrix_add.append(length)
        matrix.append(matrix_add)
    return matrix

def show_matrix(matrix):
    plik = open("matrix.txt",'w')
    for line in matrix:
        for element in line:
            plik.write(str(round(element,2)))
            plik.write('\t\t')
        plik.write('\n')
    plik.close()
