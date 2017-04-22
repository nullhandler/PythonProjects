# Made by Selva
# Made with ❤ in Selvasoft

import random
import os

# Dictionary of American states and its capital
ques = {'Alabama': 'Montgomery', 'Alaska': 'Juneau', 'Arizona': 'Phoenix',
'Arkansas': 'Little Rock', 'California': 'Sacramento', 'Colorado': 'Denver',
'Connecticut': 'Hartford', 'Delaware': 'Dover', 'Florida': 'Tallahassee',
'Georgia': 'Atlanta', 'Hawaii': 'Honolulu', 'Idaho': 'Boise', 'Illinois':
'Springfield', 'Indiana': 'Indianapolis', 'Iowa': 'Des Moines', 'Kansas':
'Topeka', 'Kentucky': 'Frankfort', 'Louisiana': 'Baton Rouge', 'Maine':
'Augusta', 'Maryland': 'Annapolis', 'Massachusetts': 'Boston', 'Michigan':
'Lansing', 'Minnesota': 'Saint Paul', 'Mississippi': 'Jackson', 'Missouri':
'Jefferson City', 'Montana': 'Helena', 'Nebraska': 'Lincoln', 'Nevada':
'Carson City', 'New Hampshire': 'Concord', 'New Jersey': 'Trenton', 'New\
Mexico': 'Santa Fe', 'New York': 'Albany', 'North Carolina': 'Raleigh',
'North Dakota': 'Bismarck', 'Ohio': 'Columbus', 'Oklahoma': 'Oklahoma City',
'Oregon': 'Salem', 'Pennsylvania': 'Harrisburg', 'Rhode Island': 'Providence',
'South Carolina': 'Columbia', 'South Dakota': 'Pierre', 'Tennessee':
'Nashville', 'Texas': 'Austin', 'Utah': 'Salt Lake City', 'Vermont':
'Montpelier', 'Virginia': 'Richmond', 'Washington': 'Olympia', 'West\
Virginia': 'Charleston', 'Wisconsin': 'Madison', 'Wyoming': 'Cheyenne'}

for i in range(5):      # loop for 5 Quizzes
    quizFile = open('Quiz%s.txt' % str(i+1), 'w') # Creates two files if not available
    ansFile = open('Ans%s.txt' % str(i+1), 'w')
    state = list(ques.keys())
    capitals = list(ques.values())
    for qn in range(4):     #loop for 4 Questions in each quiz
        randomno = random.randint(0, 49)
        randomState = state[randomno]
        correctans = capitals[randomno]
        quizFile.write('What is the capital for %s?\n' % randomState)
        wrongans = random.sample(capitals, 2)
        while correctans in wrongans:           # Dont include a correct answer in wrong answer list
            wrongans = random.sample(capitals, 2)
        choose = wrongans + [correctans]
        random.shuffle(choose)
        print(choose)
        for a in range(0,3):        #loop for 3 choices
            choice = ['A', 'B', 'C']
            quizFile.write('%s. %s\n' % (choice[a], choose[a]))
        ansFile.write(str(qn) + '. ' + correctans + '\n')

    quizFile.close() # Close the opened files
    ansFile.close()







