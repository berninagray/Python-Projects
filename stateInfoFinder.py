# Programmer: Bernina Gray
# Date 15 Sept 2020
# Purpose: Provides user capability to view state info

# Display welcome message
print("""Welcome to stat info finder.
This program will tell you the information for a state you input.""")

# Declare four lists
# Lists of state names
stateName = [
             'Alabama',
             'Alaska',
             'Arizona',
             'Arkansas',
             'California',
             'Colorado',
             'Connecticut',
             'Delaware',
             'Florida',
             'Georgia',
             'Hawaii',
             'Idaho',
             'Illinois',
             'Indiana',
             'Iowa',
             'Kansas',
             'Kentucky',
             'Louisiana',
             'Maine',
             'Maryland',
             'Massachusetts',
             'Michigan',
             'Minnesota',
             'Mississippi',
             'Missouri',
             'Montana',
             'Nebraska',
             'Nevada',
             'New Hampshire',
             'New Jersey',
             'New Mexico',
             'New York',
             'North Carolina',
             'North Dakota',
             'Ohio',
             'Oklahoma',
             'Oregon',
             'Pennsylvania',
             'Rhode Island',
             'South Carolina',
             'South Dakota',
             'Tennessee',
             'Texas',
             'Utah',
             'Vermont',
             'Virginia',
             'Washington',
             'West Virginia',
             'Wisconsin',
             'Wyoming'
             ]

# List of Capitals
stateCapital = [
                'Montgomery',
                'Juneau',
                'Phoenix',
                'Little Rock',
                'Sacramento',
                'Denver',
                'Hartford',
                'Dover',
                'Tallahassee',
                'Atlanta',
                'Honolulu',
                'Boise',
                'Springfield',
                'Indianapolis',
                'Des Moines',
                'Topeka',
                'Frankfort',
                'Baton Rouge',
                'Augusta',
                'Annapolis',
                'Boston',
                'Lansing',
                'Saint Paul',
                'Jackson',
                'Jefferson City',
                'Helena',
                'Lincoln',
                'Carson City',
                'Concord',
                'Trenton',
                'Santa Fe',
                'Albany',
                'Raleigh',
                'Bismark',
                'Columbus',
                'Oklahoma City',
                'Salem',
                'Harrisburg',
                'Providence',
                'Columbia',
                'Pierre',
                'Nashville',
                'Austin',
                'Salt Lake City',
                'Montpelier',
                'Richmond',
                'Olympia',
                'Charleston',
                'Madison',
                'Cheyenne'
                ]

# List of number of districts
numberOfDistricts = ['7',
                     '1',
                     '9',
                     '4',
                     '53',
                     '7',
                     '5',
                     '1',
                     '27',
                     '14',
                     '2',
                     '2',
                     '18',
                     '9',
                     '4',
                     '4',
                     '6',
                     '6',
                     '2',
                     '8',
                     '9',
                     '14',
                     '8',
                     '4',
                     '9',
                     '1',
                     '3',
                     '4',
                     '2',
                     '12',
                     '3',
                     '27',
                     '14',
                     '1',
                     '16',
                     '5',
                     '5',
                     '18',
                     '2',
                     '7',
                     '1',
                     '9',
                     '36',
                     '4',
                     '1',
                     '11',
                     '10'
                     '3',
                     '8',
                     '1',
                     ]

# List of order state joined the union
stateUnionOrder = ['22',
                   '49',
                   '48',
                   '25',
                   '31',
                   '38',
                   '5',
                   '1',
                   '27',
                   '4',
                   '50',
                   '43',
                   '21',
                   '19',
                   '29',
                   '34',
                   '15',
                   '18',
                   '23',
                   '7',
                   '6',
                   '26',
                   '32',
                   '20',
                   '24',
                   '41',
                   '37',
                   '36',
                   '9',
                   '3',
                   '47',
                   '11',
                   '12',
                   '39',
                   '17',
                   '46',
                   '33',
                   '2',
                   '13',
                   '8',
                   '40',
                   '16',
                   '28',
                   '45',
                   '14',
                   '10',
                   '42',
                   '35',
                   '30',
                   '44',
                  ]

# Ask user for name of a state
selectState = input('Please enter the name of a state: ')

# Lookup the index of that state name
stateindex = stateName.index(selectState.title())

# print (index)

# Use that index to find other data

state = stateName[stateindex]

# Lookup capital of that state
capital = stateCapital[stateindex]
#print (capital)

# Lookup the number of districts
district = numberOfDistricts[stateindex]
# print (district)

# Lookup the order the state joined the union
union = stateUnionOrder[stateindex]
# print (union)
# Display results to user
format = 'The capital of %s is %s, it has %s congressional districts and it is number %s in the the union.'
listItems =(state,capital,district,union)

print (format%listItems)

print ("Thank you for using state finder.")
