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

#lines_via_stop
assert answer_query(tramdict, 'via Jaegerdorffsplatsen') == ['3', '9']
assert answer_query(tramdict, 'via Aprilgatan') == ['6']
assert answer_query(tramdict, 'via Scandinavium') == ['2', '6', '8', '13']
assert answer_query(tramdict, 'via Botaniska Trädgården') == ['1', '2', '7', '8', '13']
assert answer_query(tramdict, 'via Chalmers') == ['6', '7', '8', '10', '13']

#lines_between_stops
assert answer_query(tramdict, 'between Temperaturgatan and Sahlgrenska Huvudentré') == ['6']
assert answer_query(tramdict, 'between Domkyrkan and Scandinavium') == ['2', '6']
assert answer_query(tramdict, 'between Bellevue and Positivgatan') == ['7']
assert answer_query(tramdict, 'between Saltholmen and Medicinaregatan') == ['13']
assert answer_query(tramdict, 'between Saltholmen and Medicinaregatan') == answer_query(tramdict, 'between Medicinaregatan and Saltholmen')

#time_between_stops
assert answer_query(tramdict, 'time with 3 from Hagakyrkan to Mariaplan') == 16
assert answer_query(tramdict, 'time with 5 from Munkebäckstorget to Sankt Sigfrids Plan') == 9
assert answer_query(tramdict, 'time with 7 from Allhelgonakyrkan to Komettorget') == answer_query(tramdict, 'time with 7 from Komettorget to Allhelgonakyrkan') 
assert answer_query(tramdict, 'time with 10 from Wavrinskys Plats to Hjalmar Brantingsplatsen') == 15
assert answer_query(tramdict, 'time with 13 from Scandinavium to Korsvägen') == 1

#distance_between_stops
assert round(answer_query(tramdict, 'distance from Jaegerdorffsplatsen to Tranered'), 3) == 3.003
assert round(answer_query(tramdict, 'distance from Sahlgrenska Huvudentré to Kortedala Torg'), 3) == round(answer_query(tramdict, 'distance from Kortedala Torg to Sahlgrenska Huvudentré'), 3)
assert round(answer_query(tramdict, 'distance from Temperaturgatan to Lackarebäck'), 3) == 10.092
assert round(answer_query(tramdict, 'distance from Rymdtorget Spårvagn to Hagakyrkan'), 3) == 8.841
assert round(answer_query(tramdict, 'distance from Vasaplatsen to Doktor Sydows Gata'), 3) == 2.223

#extra
assert answer_query(tramdict, 'quit') == False
