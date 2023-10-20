# DO NOT MODIFY THIS FILE

#TEST lab1

import os.path
import sys
import json
from haversine import haversine


try:
    assert os.path.exists('tramdata.py')
    assert os.path.exists('tramnetwork.json')
except:
    print('You need to submit both tramdata.py and tramnetwork.json')



with open('tramnetwork.json') as file:
    tramdict = json.load(file)

from tramdata import answer_query

outcome = True


#-----------------------------
#lines_via_stop
try:
    assert answer_query(tramdict, 'via Jaegerdorffsplatsen') == ['3', '9']
except:
    print(f"Error in lines_via_stop via Jaegerdorffsplatsen, your result is {answer_query(tramdict, 'via Jaegerdorffsplatsen')}, but the expected is {['3', '9']}")
    outcome = False

try:
    assert answer_query(tramdict, 'via Aprilgatan') == ['6']
except:
    print(f"Error in lines_via_stop via Aprilgatan, your result is {answer_query(tramdict, 'via Aprilgatan')}, but the expected is {['6']}")
    outcome = False

try:
    assert answer_query(tramdict, 'via Scandinavium') == ['2', '6', '8', '13']
except:
    print(f"Error in lines_via_stop via Scandinavium, your result is {answer_query(tramdict, 'via Scandinavium')}, but the expected is {['2', '6', '8', '13']}")
    outcome = False

try:    
    assert answer_query(tramdict, 'via Botaniska Trädgården') == ['1', '2', '7', '8', '13']
except:
    print(f"Error in lines_via_stop via Botaniska Trädgården, your result is {answer_query(tramdict, 'via Botaniska Trädgården')}, but the expected is {['1', '2', '7', '8', '13']}")
    outcome = False

try:
    assert answer_query(tramdict, 'via Chalmers') == ['6', '7', '8', '10', '13']
except:
    print(f"Error in lines_via_stop via Chalmers, your result is {answer_query(tramdict, 'via Chalmers')}, but the expected is {['6', '7', '8', '10', '13']}")
    outcome = False

#-----------------------------
#lines_between_stops
try:
    assert answer_query(tramdict, 'between Temperaturgatan and Sahlgrenska Huvudentré') == ['6']
except:
    print(f"Error in lines_between_stops between Temperaturgatan and Sahlgrenska Huvudentré, your result is {answer_query(tramdict, 'between Temperaturgatan and Sahlgrenska Huvudentré')}, but the expected is {['6']}")
    outcome = False

try:    
    assert answer_query(tramdict, 'between Domkyrkan and Scandinavium') == ['2', '6']
except:
    print(f"Error in lines_between_stops between Domkyrkan and Scandinavium, your result is {answer_query(tramdict, 'between Domkyrkan and Scandinavium')}, but the expected is {['2', '6']}")
    outcome = False

try:
    assert answer_query(tramdict, 'between Bellevue and Positivgatan') == ['7']
except:
    print(f"Error in lines_between_stops between Bellevue and Positivgatan, your result is {answer_query(tramdict, 'between Bellevue and Positivgatan')}, but the expected is {['7']}")
    outcome = False

try:
    assert answer_query(tramdict, 'between Saltholmen and Medicinaregatan') == ['13']
except:
    print(f"Error in lines_between_stops between Saltholmen and Medicinaregatan, your result is {answer_query(tramdict, 'between Saltholmen and Medicinaregatan')}, but the expected is {['13']}")
    outcome = False

try:
    assert answer_query(tramdict, 'between Saltholmen and Medicinaregatan') == answer_query(tramdict, 'between Medicinaregatan and Saltholmen')
except:
    print(f"Error in lines_between_stops between Saltholmen and Medicinaregatan, your result is {answer_query(tramdict, 'between Saltholmen and Medicinaregatan')}, but the expected is {answer_query(tramdict, 'between Medicinaregatan and Saltholmen')}")
    outcome = False

#-----------------------------
#time_between_stops
try:
    assert answer_query(tramdict, 'time with 3 from Hagakyrkan to Mariaplan') == 16
except:
    print(f"Error in time_between_stops time with 3 from Hagakyrkan to Mariaplan, your result is {answer_query(tramdict, 'time with 3 from Hagakyrkan to Mariaplan')}, but the expected is {16}")
    outcome = False

try:
    assert answer_query(tramdict, 'time with 5 from Munkebäckstorget to Sankt Sigfrids Plan') == 9
except:
    print(f"Error in time_between_stops time with 5 from Munkebäckstorget to Sankt Sigfrids Plan, your result is {answer_query(tramdict, 'time with 5 from Munkebäckstorget to Sankt Sigfrids Plan')}, but the expected is {9}")
    outcome = False

try:
    assert answer_query(tramdict, 'time with 7 from Allhelgonakyrkan to Komettorget') == answer_query(tramdict, 'time with 7 from Komettorget to Allhelgonakyrkan') 
except:
    print(f"Error in time_between_stops time with 7 from Allhelgonakyrkan to Komettorget, your result is {answer_query(tramdict, 'time with 7 from Allhelgonakyrkan to Komettorget')}, but the expected is {answer_query(tramdict, 'time with 7 from Komettorget to Allhelgonakyrkan')}")
    outcome = False

try:
    assert answer_query(tramdict, 'time with 10 from Wavrinskys Plats to Hjalmar Brantingsplatsen') == 15
except:
    print(f"Error in time_between_stops time with 10 from Wavrinskys Plats to Hjalmar Brantingsplatsen, your result is {answer_query(tramdict, 'time with 10 from Wavrinskys Plats to Hjalmar Brantingsplatsen')}, but the expected is {15}")
    outcome = False

try:
    assert answer_query(tramdict, 'time with 13 from Scandinavium to Korsvägen') == 1
except:
    print(f"Error in time_between_stops time with 13 from Scandinavium to Korsvägen, your result is {answer_query(tramdict, 'time with 13 from Scandinavium to Korsvägen')}, but the expected is {1}")
    outcome = False

#-----------------------------
#distance_between_stops
try:
    assert round(answer_query(tramdict, 'distance from Jaegerdorffsplatsen to Tranered'), 3) == 3.003
except:
    print(f"Error in distance_between_stops distance from Jaegerdorffsplatsen to Tranered, your result is {answer_query(tramdict, 'distance from Jaegerdorffsplatsen to Tranered')}, but the expected is {3.003}")
    outcome = False

try:
    assert round(answer_query(tramdict, 'distance from Sahlgrenska Huvudentré to Kortedala Torg'), 3) == round(answer_query(tramdict, 'distance from Kortedala Torg to Sahlgrenska Huvudentré'), 3)
except:
    print(f"Error in distance_between_stops distance from Sahlgrenska Huvudentré to Kortedala Torg, your result is {answer_query(tramdict, 'distance from Sahlgrenska Huvudentré to Kortedala Torg')}, but the expected is {answer_query(tramdict, 'distance from Kortedala Torg to Sahlgrenska Huvudentré')}")
    outcome = False

try:
    assert round(answer_query(tramdict, 'distance from Temperaturgatan to Lackarebäck'), 3) == 10.092
except:
    print(f"Error in distance_between_stops distance from Temperaturgatan to Lackarebäck, your result is {answer_query(tramdict, 'distance from Temperaturgatan to Lackarebäck')}, but the expected is {10.092}")
    outcome = False

try:
    assert round(answer_query(tramdict, 'distance from Rymdtorget Spårvagn to Hagakyrkan'), 3) == 8.841
except:
    print(f"Error in distance_between_stops distance from Rymdtorget Spårvagn to Hagakyrkan, your result is {answer_query(tramdict, 'distance from Rymdtorget Spårvagn to Hagakyrkan')}, but the expected is {8.841}")
    outcome = False

try:
    assert round(answer_query(tramdict, 'distance from Vasaplatsen to Doktor Sydows Gata'), 3) == 2.223
except:
    print(f"Error in distance_between_stops distance from Vasaplatsen to Doktor Sydows Gata, your result is {answer_query(tramdict, 'distance from Vasaplatsen to Doktor Sydows Gata')}, but the expected is {2.223}")
    outcome = False


#-----------------------------
#final result
assert outcome == True