############
############ ALTHOUGH I GIVE YOU THIS TEMPLATE PROGRAM WITH THE NAME 'skeleton.py', 
############ YOU CAN RENAME IT TO ANYTHING YOU LIKE. HOWEVER, FOR THE PURPOSES OF 
############ THE EXPLANATION IN THESE COMMENTS, I ASSUME THAT THIS PROGRAM IS STILL 
############ CALLED 'skeleton.py'.
############
############ IF YOU WISH TO IMPORT STANDARD MODULES, YOU CAN ADD THEM AFTER THOSE BELOW.
############ NOTE THAT YOU ARE NOT ALLOWED TO IMPORT ANY NON-STANDARD MODULES! TO SEE
############ THE STANDARD MODULES, TAKE A LOOK IN 'validate_before_handin.py'.
############
############ DO NOT INCLUDE ANY COMMENTS ON A LINE WHERE YOU IMPORT A MODULE.
############

import os
import sys
import time
import random

############ START OF SECTOR 0 (IGNORE THIS COMMENT)
############
############ NOW PLEASE SCROLL DOWN UNTIL THE NEXT BLOCK OF CAPITALIZED COMMENTS.
############
############ DO NOT TOUCH OR ALTER THE CODE IN BETWEEN! YOU HAVE BEEN WARNED!
############ BY 'DO NOT TOUCH' I REALLY MEAN THIS. EVEN CHANGING THE SYNTAX, BY
############ ADDING SPACES OR COMMENTS OR LINE RETURNS AND SO ON, COULD MEAN THAT
############ CODES MIGHT NOT RUN WHEN I RUN THEM!
############

def read_file_into_string(input_file, ord_range):
    the_file = open(input_file, 'r') 
    current_char = the_file.read(1) 
    file_string = ""
    length = len(ord_range)
    while current_char != "":
        i = 0
        while i < length:
            if ord(current_char) >= ord_range[i][0] and ord(current_char) <= ord_range[i][1]:
                file_string = file_string + current_char
                i = length
            else:
                i = i + 1
        current_char = the_file.read(1)
    the_file.close()
    return file_string

def remove_all_spaces(the_string):
    length = len(the_string)
    new_string = ""
    for i in range(length):
        if the_string[i] != " ":
            new_string = new_string + the_string[i]
    return new_string

def integerize(the_string):
    length = len(the_string)
    stripped_string = "0"
    for i in range(0, length):
        if ord(the_string[i]) >= 48 and ord(the_string[i]) <= 57:
            stripped_string = stripped_string + the_string[i]
    resulting_int = int(stripped_string)
    return resulting_int

def convert_to_list_of_int(the_string):
    list_of_integers = []
    location = 0
    finished = False
    while finished == False:
        found_comma = the_string.find(',', location)
        if found_comma == -1:
            finished = True
        else:
            list_of_integers.append(integerize(the_string[location:found_comma]))
            location = found_comma + 1
            if the_string[location:location + 5] == "NOTE=":
                finished = True
    return list_of_integers

def build_distance_matrix(num_cities, distances, city_format):
    dist_matrix = []
    i = 0
    if city_format == "full":
        for j in range(num_cities):
            row = []
            for k in range(0, num_cities):
                row.append(distances[i])
                i = i + 1
            dist_matrix.append(row)
    elif city_format == "upper_tri":
        for j in range(0, num_cities):
            row = []
            for k in range(j):
                row.append(0)
            for k in range(num_cities - j):
                row.append(distances[i])
                i = i + 1
            dist_matrix.append(row)
    else:
        for j in range(0, num_cities):
            row = []
            for k in range(j + 1):
                row.append(0)
            for k in range(0, num_cities - (j + 1)):
                row.append(distances[i])
                i = i + 1
            dist_matrix.append(row)
    if city_format == "upper_tri" or city_format == "strict_upper_tri":
        for i in range(0, num_cities):
            for j in range(0, num_cities):
                if i > j:
                    dist_matrix[i][j] = dist_matrix[j][i]
    return dist_matrix

def read_in_algorithm_codes_and_tariffs(alg_codes_file):
    flag = "good"
    code_dictionary = {}   
    tariff_dictionary = {}  
    if not os.path.exists(alg_codes_file):
        flag = "not_exist"  
        return code_dictionary, tariff_dictionary, flag
    ord_range = [[32, 126]]
    file_string = read_file_into_string(alg_codes_file, ord_range)  
    location = 0
    EOF = False
    list_of_items = []  
    while EOF == False: 
        found_comma = file_string.find(",", location)
        if found_comma == -1:
            EOF = True
            sandwich = file_string[location:]
        else:
            sandwich = file_string[location:found_comma]
            location = found_comma + 1
        list_of_items.append(sandwich)
    third_length = int(len(list_of_items)/3)
    for i in range(third_length):
        code_dictionary[list_of_items[3 * i]] = list_of_items[3 * i + 1]
        tariff_dictionary[list_of_items[3 * i]] = int(list_of_items[3 * i + 2])
    return code_dictionary, tariff_dictionary, flag

############
############ HAVE YOU TOUCHED ANYTHING ABOVE? BECAUSE EVEN CHANGING ONE CHARACTER OR
############ ADDING ONE SPACE OR LINE RETURN WILL MEAN THAT THE PROGRAM YOU HAND IN
############ MIGHT NOT RUN PROPERLY!
############
############ THE RESERVED VARIABLE 'input_file' IS THE CITY FILE UNDER CONSIDERATION.
############
############ IT CAN BE SUPPLIED BY SETTING THE VARIABLE BELOW OR VIA A COMMAND-LINE
############ EXECUTION OF THE FORM 'python skeleton.py city_file.txt'. WHEN SUPPLYING
############ THE CITY FILE VIA A COMMAND-LINE EXECUTION, ANY ASSIGNMENT OF THE VARIABLE
############ 'input_file' IN THE LINE BELOW iS SUPPRESSED.
############
############ IT IS ASSUMED THAT THIS PROGRAM 'skeleton.py' SITS IN A FOLDER THE NAME OF
############ WHICH IS YOUR USER-NAME, E.G., 'abcd12', WHICH IN TURN SITS IN ANOTHER
############ FOLDER. IN THIS OTHER FOLDER IS THE FOLDER 'city-files' AND NO MATTER HOW
############ THE NAME OF THE CITY FILE IS SUPPLIED TO THIS PROGRAM, IT IS ASSUMED THAT 
############ THE CITY FILE IS IN THE FOLDER 'city-files'.
############
############ END OF SECTOR 0 (IGNORE THIS COMMENT)

input_file = "AISearchfile175.txt"

############ START OF SECTOR 1 (IGNORE THIS COMMENT)
############
############ PLEASE SCROLL DOWN UNTIL THE NEXT BLOCK OF CAPITALIZED COMMENTS STARTING
############ 'HAVE YOU TOUCHED ...'
############
############ DO NOT TOUCH OR ALTER THE CODE IN BETWEEN! YOU HAVE BEEN WARNED!
############

if len(sys.argv) > 1:
    input_file = sys.argv[1]

############ END OF SECTOR 1 (IGNORE THIS COMMENT)

############ START OF SECTOR 2 (IGNORE THIS COMMENT)
path_for_city_files = os.path.join("..", "city-files")
############ END OF SECTOR 2 (IGNORE THIS COMMENT)

############ START OF SECTOR 3 (IGNORE THIS COMMENT)
path_to_input_file = os.path.join(path_for_city_files, input_file)
if os.path.isfile(path_to_input_file):
    ord_range = [[32, 126]]
    file_string = read_file_into_string(path_to_input_file, ord_range)
    file_string = remove_all_spaces(file_string)
    print("I have found and read the input file " + input_file + ":")
else:
    print("*** error: The city file " + input_file + " does not exist in the city-file folder.")
    sys.exit()

location = file_string.find("SIZE=")
if location == -1:
    print("*** error: The city file " + input_file + " is incorrectly formatted.")
    sys.exit()
    
comma = file_string.find(",", location)
if comma == -1:
    print("*** error: The city file " + input_file + " is incorrectly formatted.")
    sys.exit()
    
num_cities_as_string = file_string[location + 5:comma]
num_cities = integerize(num_cities_as_string)
print("   the number of cities is stored in 'num_cities' and is " + str(num_cities))

comma = comma + 1
stripped_file_string = file_string[comma:]
distances = convert_to_list_of_int(stripped_file_string)

counted_distances = len(distances)
if counted_distances == num_cities * num_cities:
    city_format = "full"
elif counted_distances == (num_cities * (num_cities + 1))/2:
    city_format = "upper_tri"
elif counted_distances == (num_cities * (num_cities - 1))/2:
    city_format = "strict_upper_tri"
else:
    print("*** error: The city file " + input_file + " is incorrectly formatted.")
    sys.exit()

dist_matrix = build_distance_matrix(num_cities, distances, city_format)
print("   the distance matrix 'dist_matrix' has been built.")

############
############ HAVE YOU TOUCHED ANYTHING ABOVE? BECAUSE EVEN CHANGING ONE CHARACTER OR
############ ADDING ONE SPACE OR LINE RETURN WILL MEAN THAT THE PROGRAM YOU HAND IN
############ MIGHT NOT RUN PROPERLY!
############
############ YOU NOW HAVE THE NUMBER OF CITIES STORED IN THE INTEGER VARIABLE 'num_cities'
############ AND THE TWO_DIMENSIONAL MATRIX 'dist_matrix' HOLDS THE INTEGER CITY-TO-CITY 
############ DISTANCES SO THAT 'dist_matrix[i][j]' IS THE DISTANCE FROM CITY 'i' TO CITY 'j'.
############ BOTH 'num_cities' AND 'dist_matrix' ARE RESERVED VARIABLES AND SHOULD FEED
############ INTO YOUR IMPLEMENTATIONS.
############
############ THERE NOW FOLLOWS CODE THAT READS THE ALGORITHM CODES AND TARIFFS FROM
############ THE TEXT-FILE 'alg_codes_and_tariffs.txt' INTO THE RESERVED DICTIONARIES
############ 'code_dictionary' AND 'tariff_dictionary'. DO NOT AMEND THIS CODE!
############ THE TEXT FILE 'alg_codes_and_tariffs.txt' SHOULD BE IN THE SAME FOLDER AS
############ THE FOLDER 'city-files' AND THE FOLDER WHOSE NAME IS YOUR USER-NAME.
############
############ PLEASE SCROLL DOWN UNTIL THE NEXT BLOCK OF CAPITALIZED COMMENTS STARTING
############ 'HAVE YOU TOUCHED ...'
############
############ DO NOT TOUCH OR ALTER THE CODE IN BETWEEN! YOU HAVE BEEN WARNED!
############
############ END OF SECTOR 3 (IGNORE THIS COMMENT)

############ START OF SECTOR 4 (IGNORE THIS COMMENT)
path_for_alg_codes_and_tariffs = os.path.join("..", "alg_codes_and_tariffs.txt")
############ END OF SECTOR 4 (IGNORE THIS COMMENT)

############ START OF SECTOR 5 (IGNORE THIS COMMENT)
code_dictionary, tariff_dictionary, flag = read_in_algorithm_codes_and_tariffs(path_for_alg_codes_and_tariffs)

if flag != "good":
    print("*** error: The text file 'alg_codes_and_tariffs.txt' does not exist.")
    sys.exit()

print("The codes and tariffs have been read from 'alg_codes_and_tariffs.txt':")

############
############ HAVE YOU TOUCHED ANYTHING ABOVE? BECAUSE EVEN CHANGING ONE CHARACTER OR
############ ADDING ONE SPACE OR LINE RETURN WILL MEAN THAT THE PROGRAM YOU HAND IN
############ MIGHT NOT RUN PROPERLY! SORRY TO GO ON ABOUT THIS BUT YOU NEED TO BE 
############ AWARE OF THIS FACT!
############
############ YOU NOW NEED TO SUPPLY SOME PARAMETERS.
############
############ THE RESERVED STRING VARIABLE 'my_user_name' SHOULD BE SET AT YOUR
############ USER-NAME, E.G., "abcd12"
############
############ END OF SECTOR 5 (IGNORE THIS COMMENT)

my_user_name = "jvgw34"

############ START OF SECTOR 6 (IGNORE THIS COMMENT)
############
############ YOU CAN SUPPLY, IF YOU WANT, YOUR FULL NAME. THIS IS NOT USED AT ALL BUT SERVES AS
############ AN EXTRA CHECK THAT THIS FILE BELONGS TO YOU. IF YOU DO NOT WANT TO SUPPLY YOUR
############ NAME THEN EITHER SET THE STRING VARIABLES 'my_first_name' AND 'my_last_name' AT 
############ SOMETHING LIKE "Mickey" AND "Mouse" OR AS THE EMPTY STRING (AS THEY ARE NOW;
############ BUT PLEASE ENSURE THAT THE RESERVED VARIABLES 'my_first_name' AND 'my_last_name'
############ ARE SET AT SOMETHING).
############
############ END OF SECTOR 6 (IGNORE THIS COMMENT)

my_first_name = "Aleksandar"
my_last_name = "Yordanov"

############ START OF SECTOR 7 (IGNORE THIS COMMENT)
############
############ YOU NEED TO SUPPLY THE ALGORITHM CODE IN THE RESERVED STRING VARIABLE 'algorithm_code'
############ FOR THE ALGORITHM YOU ARE IMPLEMENTING. IT NEEDS TO BE A LEGAL CODE FROM THE TEXT-FILE
############ 'alg_codes_and_tariffs.txt' (READ THIS FILE TO SEE THE CODES).
############
############ END OF SECTOR 7 (IGNORE THIS COMMENT)

algorithm_code = "AC"

############ START OF SECTOR 8 (IGNORE THIS COMMENT)
############
############ PLEASE SCROLL DOWN UNTIL THE NEXT BLOCK OF CAPITALIZED COMMENTS STARTING
############ 'HAVE YOU TOUCHED ...'
############
############ DO NOT TOUCH OR ALTER THE CODE IN BETWEEN! YOU HAVE BEEN WARNED!
############

if not algorithm_code in code_dictionary:
    print("*** error: the algorithm code " + algorithm_code + " is illegal")
    sys.exit()
print("   your algorithm code is legal and is " + algorithm_code + " -" + code_dictionary[algorithm_code] + ".")

start_time = time.time()

############
############ HAVE YOU TOUCHED ANYTHING ABOVE? BECAUSE EVEN CHANGING ONE CHARACTER OR
############ ADDING ONE SPACE OR LINE RETURN WILL MEAN THAT THE PROGRAM YOU HAND IN
############ MIGHT NOT RUN PROPERLY! SORRY TO GO ON ABOUT THIS BUT YOU NEED TO BE 
############ AWARE OF THIS FACT!
############
############ YOU CAN ADD A NOTE THAT WILL BE ADDED AT THE END OF THE RESULTING TOUR FILE IF YOU LIKE,
############ E.G., "in my basic greedy search, I broke ties by always visiting the first 
############ city found" BY USING THE RESERVED STRING VARIABLE 'added_note' OR LEAVE IT EMPTY
############ IF YOU WISH. THIS HAS NO EFFECT ON MARKS BUT HELPS YOU TO REMEMBER THINGS ABOUT
############ YOUR TOUR THAT YOU MIGHT BE INTERESTED IN LATER. NOTE THAT I CALCULATE THE TIME OF
############ A RUN USING THE RESERVED VARIABLE 'start_time' AND INCLUDE THE RUN-TIME IN 'added_note' LATER.
############
############ IN FACT, YOU CAN INCLUDE YOUR ADDED NOTE IMMEDIATELY BELOW OR EVEN INCLUDE YOUR ADDED NOTE
############ AT ANY POINT IN YOUR PROGRAM: JUST DEFINE THE STRING VARIABLE 'added_note' WHEN YOU WISH
############ (BUT DON'T REMOVE THE ASSIGNMENT IMMEDIATELY BELOW).
############
############ END OF SECTOR 8 (IGNORE THIS COMMENT)

added_note = ""

############ START OF SECTOR 9 (IGNORE THIS COMMENT)
############
############ NOW YOUR CODE SHOULD BEGIN BUT FIRST A COMMENT.
############
############ IF YOU ARE IMPLEMENTING GA THEN:
############  - IF YOU EXECUTE YOUR MAIN LOOP A FIXED NUMBER OF TIMES THEN USE THE VARIABLE 'max_it' TO DENOTE THIS NUMBER
############  - USE THE VARIABLE 'pop_size' TO DENOTE THE SIZE OF YOUR POPULATION (THIS IS '|P|' IN THE PSEUDOCODE)
############
############ IF YOU ARE IMPLEMENTING AC THEN:
############  - IF YOU EXECUTE YOUR MAIN LOOP A FIXED NUMBER OF TIMES THEN USE THE VARIABLE 'max_it' TO DENOTE THIS NUMBER
############  - USE THE VARIABLE 'num_ants' TO DENOTE THE NUMBER OF ANTS (THIS IS 'N' IN THE PSEUDOCODE)
############
############ IF YOU ARE IMPLEMENTING PS THEN:
############  - IF YOU EXECUTE YOUR MAIN LOOP A FIXED NUMBER OF TIMES THEN USE THE VARIABLE 'max_it' TO DENOTE THIS NUMBER
############  - USE THE VARIABLE 'num_parts' TO DENOTE THE NUMBER OF PARTICLES (THIS IS 'N' IN THE PSEUDOCODE)
############
############ DOING THIS WILL MEAN THAT THIS INFORMATION IS WRITTEN WITHIN 'added_note' IN ANY TOUR-FILE PRODUCED.
############ OF COURSE, THE VALUES OF THESE VARIABLES NEED TO BE ACCESSIBLE TO THE MAIN BODY OF CODE.
############ IT'S FINE IF YOU DON'T ADOPT THESE VARIABLE NAMES BUT THIS USEFUL INFORMATION WILL THEN NOT BE WRITTEN TO ANY
############ TOUR-FILE PRODUCED BY THIS CODE.
############
############ END OF SECTOR 9 (IGNORE THIS COMMENT)

'''
Improvements based on this paper:
https://www.researchgate.net/publication/228617274_Improved_ant_colony_optimization_algorithm_for_the_traveling_salesman_problems
https://www.cs.ubc.ca/~hutter/previous-earg/EmpAlgReadingGroup/TSP-JohMcg97.pdf
'''
num_ants = 40
num_avoidant_ants = 5 # Num ants must be > num avoidant ants + num scout ants
num_scout_ants = 3
w = 6
rho = 0.4

def get_tour_length(tour):
    cur_len = 0
    for i in range(len(tour)-1):
        cur_len += dist_matrix[tour[i]][tour[i + 1]]
    cur_len += dist_matrix[tour[num_cities - 1]][tour[0]]
    return cur_len

def get_greedy_tour():
    tour = []
    currentCity = 0
    visited = [False] * num_cities
    visited[currentCity] = True
    tour_length = 0

    for i in range(num_cities):
        nearestCity = None
        min_dist = 10 ** 20

        for city in range(num_cities):
            if not visited[city] and dist_matrix[currentCity][city] < min_dist:
                nearestCity = city
                min_dist = dist_matrix[currentCity][city]
        
        if nearestCity != None:
            tour.append(nearestCity)
            visited[nearestCity] = True
            currentCity = nearestCity
            tour_length += min_dist

    tour.append(0)
    tour_length += dist_matrix[currentCity][0]

    return [tour, tour_length]

def two_opt(tour):
    # Based on https://www.cs.ubc.ca/~hutter/previous-earg/EmpAlgReadingGroup/TSP-JohMcg97.pdf
    # And inspired by the C++ code/information provided on the wikipedia page related to 2-opt which is based on this paper: https://en.wikipedia.org/wiki/2-opt
    # There are further improvements to be made by keeping a do not search and neighbours list as described in 3.3
    # However this runs fine up to 535 and implementing that would take far too long.
    best_distance = get_tour_length(tour)
    improvement = True
    while improvement:
        improvement = False
        num_cities = len(tour)
        for i in range(num_cities - 1):
            for j in range(i + 2, num_cities - 2):
                if j - i == 1: # Skip when there is no possibility of crossover
                    continue 
                old_edges = dist_matrix[tour[i]][tour[i + 1]] + dist_matrix[tour[j]][tour[(j + 1) % num_cities]]
                new_edges = dist_matrix[tour[i]][tour[j]] + dist_matrix[tour[i + 1]][tour[(j + 1) % num_cities]]
                delta = new_edges - old_edges
                # Delta solution based on paper.
                if delta < 0:
                    tour[i + 1:j + 1] = tour[i + 1:j + 1][::-1]
                    best_distance += delta
                    improvement = True

    return tour, best_distance

class Ant:
    alpha = 1.5
    beta = 3

    def __init__(self,inital_vertex_index,pheromone_matrix):
        self.tour = [inital_vertex_index]
        self.tabu = [0]
        self.pheromone_matrix = pheromone_matrix

    def _build_probabilites(self,current_index,neighbours):
        # Building probability according to the formula in the lectures
        l_neighbours = len(neighbours)
        # Pre declaring size of neighbours so enough memory is allocated
        pre_probabilities = [0] * l_neighbours
        probabilities = [0] * l_neighbours
        probability_sum = 0
        pheromone_matrix_row = self.pheromone_matrix[current_index]
        for city_index, city_distance in enumerate(neighbours):
            if city_distance == -1:
                pre_probabilities[city_index] = 0
                continue
            
            pheromone_on_edge = pheromone_matrix_row[city_index]
            if pheromone_on_edge < 1e-10: # This is in the case where there is only 1 move with no pheromone
                pheromone_on_edge = 1e-10
            pre_probability = (pheromone_on_edge ** self.alpha) * ((1/(city_distance + 1e-10)) ** self.beta) 
            pre_probabilities[city_index] = (pre_probability)
            probability_sum += pre_probability
        
        for x,i in enumerate(pre_probabilities):
            try:
                probabilities[x] = (i/probability_sum)
            except ZeroDivisionError:
                # For debugging
                print(probabilities)
                print(len(self.tabu),':',len(self.tour))
                print(sorted(self.tabu))
                print(sorted(neighbours))
                exit()
        return probabilities

    def __move(self,tour):
        neighbours = dist_matrix[tour[-1]][:]
        current_position = tour[-1]
        self.tabu.append(current_position)
        # Update neighbours with tabu list.
        for city_visited_index in self.tabu:
            neighbours[city_visited_index] = -1
            
        # Checks if all the neighbours have been visited
        if len(set(neighbours)) == 1:
            return False
        
        probabilites = self._build_probabilites(current_position,neighbours)
        running_total = 0
        # Roulette wheel selection of next neighbour. 
        selection_point = random.random()
        for city_index, probability in enumerate(probabilites):
            running_total += probability
            if running_total >= selection_point:
                self.tour.append(city_index)
                break
        
        return True
    

    def buildSolution(self):
        # Keep moving until unable to.
        while self.__move(self.tour) == True:
            pass
        
        self.tour.append(0)
        tour_cost = get_tour_length(self.tour)
        return (self.tour,tour_cost)

class AvoidantAnt(Ant):
    # The inspiration for my avoidant ant system comes from https://www.researchgate.net/publication/228617274_Improved_ant_colony_optimization_algorithm_for_the_traveling_salesman_problems
    # I used my own ideas to create another stochiastic mechanism called avoidant ants
    # Avoidant ants will prefer heuristic desirability slightly more than normal ants and have less bias towards pheromone.
    # They will also have a random chance to rechose what node they travel to
    alpha = 1.2
    beta = 3.8
    avoidanceChance = 0.3
    maxAvoidCount = 3 # Keep this always less than the city count.

    def __init__(self, inital_vertex_index, pheromone_matrix):
        super().__init__(inital_vertex_index, pheromone_matrix)
        self.curAvoidCount = 0
    
    def __move(self,tour):
        neighbours = dist_matrix[tour[-1]][:]
        current_position = tour[-1]
        self.tabu.append(current_position)
        for city_visited_index in self.tabu:
            neighbours[city_visited_index] = -1
            
        if len(set(neighbours)) == 1:
            return False
        
        probabilites = self._build_probabilites(current_position,neighbours)
        running_total = 0
        selection_point = random.random()
        avoid_var = random.random()
        for city_index, probability in enumerate(probabilites):
            running_total += probability
            if running_total >= selection_point:
                if avoid_var < AvoidantAnt.avoidanceChance and self.curAvoidCount < AvoidantAnt.maxAvoidCount:
                    # Reroll if conditions met. 
                    probabilites[city_index] = 0
                    n_sum = sum(probabilites)
                    running_total = 0
                    selection_point = random.random() * n_sum
                    for reroll_city_index, reroll_probability in enumerate(probabilites):
                        if reroll_city_index == city_index:
                            continue
                        running_total += reroll_probability
                        if running_total >= selection_point:
                            self.tour.append(reroll_city_index)
                            self.curAvoidCount += 1
                            return True
                else:
                    self.tour.append(city_index)
                    return True
        
        return True

    def buildSolution(self):
        for i in range(AvoidantAnt.maxAvoidCount):
            # Only doing this in the first couple of iterations to remove the chance for not being able to move.
            self.__move(self.tour)

        while self.__move(self.tour) == True:
            pass
        
        self.tour.append(0)
        tour_cost = get_tour_length(self.tour)
        return (self.tour,tour_cost)


class ScoutAnt(Ant):
    # This is the original idea discussed in https://www.researchgate.net/publication/228617274_Improved_ant_colony_optimization_algorithm_for_the_traveling_salesman_problems
    # Providing a stochiastic mechanism for mutation of the best path 
    mutationChance = 1/(2*num_cities) # Decided to base this off n_cities instead of n_paths 

    def __init__(self, tour, best_tour_len):
        self.tour = tour[:-1]
        self.best_tour_len = best_tour_len

    def __mutate(self, tour, mutation_chance, i):
        if random.random() < mutation_chance:
            rand_j = random.randint(i, len(tour) - 1)
            while rand_j == i:
                rand_j = random.randint(i, len(tour) - 1)
            tour[i], tour[rand_j] = tour[rand_j], tour[i]
        return tour
    
    def buildSolution(self):
        for i in range(len(self.tour)-1):
            self.tour = self.__mutate(self.tour, ScoutAnt.mutationChance, i)
        self.tour.append(0)
        tour_cost = get_tour_length(self.tour)
        if tour_cost < self.best_tour_len:
            return (self.tour, tour_cost)
        else:
            return False # Only pass if better, to not overdeposit pheromone


def evaluate_pheromone(trails_costs,pheromone_matrix,rho):
    for y in range(num_cities):
        for x in range(num_cities):
            pheromone_matrix[y][x] = (1-rho) * pheromone_matrix[y][x]
    pheromone_laid = 1/trails_costs[0][1] + (2*w) * 1/trails_costs[0][1]
    for i in range(len(trails_costs[0][0]) - 1):
        pheromone_matrix[trails_costs[0][0][i]][trails_costs[0][0][i+1]] += pheromone_laid        

    for rank in range(1,w-1):
        pheromone_laid = 1/trails_costs[rank][1] + (w-rank+1) * 1/trails_costs[rank][1]
        for i in range(len(trails_costs[rank][0]) - 1):
            pheromone_matrix[trails_costs[rank][0][i]][trails_costs[rank][0][i+1]] += pheromone_laid
    
    for rank in range(w-1,len(trails_costs)):
        pheromone_laid = 1/trails_costs[rank][1] +  1/trails_costs[rank][1]
        for i in range(len(trails_costs[rank][0]) - 1):
            pheromone_matrix[trails_costs[rank][0][i]][trails_costs[rank][0][i+1]] += pheromone_laid


def ant_colony_system(num_ants,num_avoidant_ants,num_scout_ants):
    greedy_tour = get_greedy_tour()
    best_solution = list(range(1,num_cities))
    random.shuffle(best_solution)
    best_solution.append(0)
    best_solution_cost = get_tour_length(best_solution)
    inital_pheromone = 0.5*w*(num_cities-1) / (greedy_tour[1] * rho) # Still keeping this bound to the number of citites.
    pheromone_matrix = [[inital_pheromone] * num_cities for _ in range(num_cities)]
    start_time = time.time()
    while time.time() - start_time < 55:
        trails_costs = []
        # Construct Ants
        for k in range(((num_ants)-num_scout_ants)-num_avoidant_ants):
            nAnt = Ant(random.randint(1,num_cities-1),pheromone_matrix)
            trails_costs.append(nAnt.buildSolution())
        
        for k in range(num_scout_ants):
            nAnt = ScoutAnt(best_solution,best_solution_cost)
            solution = nAnt.buildSolution()
            if solution == False:
                continue
            else:
                trails_costs.append(solution)

        for k in range(num_avoidant_ants):
            nAnt = AvoidantAnt(random.randint(1,num_cities-1),pheromone_matrix)
            trails_costs.append(nAnt.buildSolution())

        sorted_trails = sorted(trails_costs, key=lambda x: x[1]) # Sort for ranking
        nArr = []
        to_two_opt = 2 #Amount of tours to two-opt
        for i in range(to_two_opt):
            nArr.append(two_opt(sorted_trails[i][0]))

        sorted_trails = [*nArr, *sorted_trails[to_two_opt:]]
        if sorted_trails[0][1] < best_solution_cost:
            best_solution = sorted_trails[0][0]
            best_solution_cost = sorted_trails[0][1]

        evaluate_pheromone(sorted_trails,pheromone_matrix,rho)

    return (best_solution,best_solution_cost)


to_unpack = ant_colony_system(num_ants,num_avoidant_ants,num_scout_ants)
tour_length = to_unpack[1]
tour = to_unpack[0]



############ START OF SECTOR 10 (IGNORE THIS COMMENT)
############
############ YOUR CODE SHOULD NOW BE COMPLETE AND WHEN EXECUTION OF THIS PROGRAM 'skeleton.py'
############ REACHES THIS POINT, YOU SHOULD HAVE COMPUTED A TOUR IN THE RESERVED LIST VARIABLE 'tour', 
############ WHICH HOLDS A LIST OF THE INTEGERS FROM {0, 1, ..., 'num_cities' - 1} SO THAT EVERY INTEGER
############ APPEARS EXACTLY ONCE, AND YOU SHOULD ALSO HOLD THE LENGTH OF THIS TOUR IN THE RESERVED
############ INTEGER VARIABLE 'tour_length'.
############
############ YOUR TOUR WILL BE PACKAGED IN A TOUR FILE OF THE APPROPRIATE FORMAT AND THIS TOUR FILE'S
############ NAME WILL BE A MIX OF THE NAME OF THE CITY FILE, THE NAME OF THIS PROGRAM AND THE
############ CURRENT DATE AND TIME. SO, EVERY SUCCESSFUL EXECUTION GIVES A TOUR FILE WITH A UNIQUE
############ NAME AND YOU CAN RENAME THE ONES YOU WANT TO KEEP LATER.
############
############ DO NOT EDIT ANY TOUR FILE! ALL TOUR FILES MUST BE LEFT AS THEY WERE ON OUTPUT.
############
############ DO NOT TOUCH OR ALTER THE CODE BELOW THIS POINT! YOU HAVE BEEN WARNED!
############

end_time = time.time()
elapsed_time = round(end_time - start_time, 1)

if algorithm_code == "GA":
    try: max_it
    except NameError: max_it = None
    try: pop_size
    except NameError: pop_size = None
    if added_note != "":
        added_note = added_note + "\n"
    added_note = added_note + "The parameter values are 'max_it' = " + str(max_it) + " and 'pop_size' = " + str(pop_size) + "."

if algorithm_code == "AC":
    try: max_it
    except NameError: max_it = None
    try: num_ants
    except NameError: num_ants = None
    if added_note != "":
        added_note = added_note + "\n"
    added_note = added_note + "The parameter values are 'max_it' = " + str(max_it) + " and 'num_ants' = " + str(num_ants) + "."

if algorithm_code == "PS":
    try: max_it
    except NameError: max_it = None
    try: num_parts
    except NameError: num_parts = None
    if added_note != "":
        added_note = added_note + "\n"
    added_note = added_note + "The parameter values are 'max_it' = " + str(max_it) + " and 'num_parts' = " + str(num_parts) + "."
    
added_note = added_note + "\nRUN-TIME = " + str(elapsed_time) + " seconds.\n"

flag = "good"
length = len(tour)
for i in range(0, length):
    if isinstance(tour[i], int) == False:
        flag = "bad"
    else:
        tour[i] = int(tour[i])
if flag == "bad":
    print("*** error: Your tour contains non-integer values.")
    sys.exit()
if isinstance(tour_length, int) == False:
    print("*** error: The tour-length is a non-integer value.")
    sys.exit()
tour_length = int(tour_length)
if len(tour) != num_cities:
    print("*** error: The tour does not consist of " + str(num_cities) + " cities as there are, in fact, " + str(len(tour)) + ".")
    sys.exit()
flag = "good"
for i in range(0, num_cities):
    if not i in tour:
        flag = "bad"
if flag == "bad":
    print("*** error: Your tour has illegal or repeated city names.")
    sys.exit()
check_tour_length = 0
for i in range(0, num_cities - 1):
    check_tour_length = check_tour_length + dist_matrix[tour[i]][tour[i + 1]]
check_tour_length = check_tour_length + dist_matrix[tour[num_cities - 1]][tour[0]]
if tour_length != check_tour_length:
    flag = print("*** error: The length of your tour is not " + str(tour_length) + "; it is actually " + str(check_tour_length) + ".")
    sys.exit()
print("You, user " + my_user_name + ", have successfully built a tour of length " + str(tour_length) + "!")
len_user_name = len(my_user_name)
user_number = 0
for i in range(0, len_user_name):
    user_number = user_number + ord(my_user_name[i])
alg_number = ord(algorithm_code[0]) + ord(algorithm_code[1])
tour_diff = abs(tour[0] - tour[num_cities - 1])
for i in range(0, num_cities - 1):
    tour_diff = tour_diff + abs(tour[i + 1] - tour[i])
certificate = user_number + alg_number + tour_diff
local_time = time.asctime(time.localtime(time.time()))
output_file_time = local_time[4:7] + local_time[8:10] + local_time[11:13] + local_time[14:16] + local_time[17:19]
output_file_time = output_file_time.replace(" ", "0")
script_name = os.path.basename(sys.argv[0])
if len(sys.argv) > 2:
    output_file_time = sys.argv[2]
output_file_name = script_name[0:len(script_name) - 3] + "_" + input_file[0:len(input_file) - 4] + "_" + output_file_time + ".txt"

f = open(output_file_name,'w')
f.write("USER = {0} ({1} {2}),\n".format(my_user_name, my_first_name, my_last_name))
f.write("ALGORITHM CODE = {0}, NAME OF CITY-FILE = {1},\n".format(algorithm_code, input_file))
f.write("SIZE = {0}, TOUR LENGTH = {1},\n".format(num_cities, tour_length))
f.write(str(tour[0]))
for i in range(1,num_cities):
    f.write(",{0}".format(tour[i]))
f.write(",\nNOTE = {0}".format(added_note))
f.write("CERTIFICATE = {0}.\n".format(certificate))
f.close()
print("I have successfully written your tour to the tour file:\n   " + output_file_name + ".")

############ END OF SECTOR 10 (IGNORE THIS COMMENT)
