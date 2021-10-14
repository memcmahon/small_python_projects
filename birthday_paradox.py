import datetime, random

def getBirthdays(numberOfBirthdays):
    """Returns a list of n random date objects for birthdays."""
    birthdays = []

    for i in range(numberOfBirthdays):
        startOfYear = datetime.date(2001, 1, 1)
        randomNumberOfDays = datetime.timedelta(random.randint(0,364))
        birthday = startOfYear + randomNumberOfDays
        birthdays.append(birthday)

    return birthdays

def getMatch(birthdays):
    """Returns the date object of a buirthday that occurs more than once in the birthday list"""
    if len(birthdays) == len(set(birthdays)):
        return None

    for i, birthdayA in enumerate(birthdays):
        for j, birthdayB in enumerate(birthdays[i + 1:]):
            if birthdayA == birthdayB:
                return birthdayA


print('''Welcome to the Birthday Paradox

The Birthday Paradox shows us that in a group of N people,
the odds that two of them have matching birthdays is
surprisingly large.

This program does a Monte Carlo simulation (repeated random
simulations) to explore this concept.

(It's not actually a paradox, it's just a surprising result)''')

MONTHS = ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec')

while True:
    print('How many birthdays shall I generate? (Max 100)')
    response = input('> ')
    if response.isdecimal() and (0 < int(response) <= 100):
        numBDays = int(response)
        break

print()

print('Here are', numBDays, 'birthdays:')
birthdays = getBirthdays(numBDays)
for i, birthday in enumerate(birthdays):
    if i != 0:
        print(', ', end='')

    monthName = MONTHS[birthday.month -1]
    dateText = '{} {}'.format(monthName, birthday.day)
    print(dateText, end='')

print()
print()

match = getMatch(birthdays)

print('In this simulation, ', end='')
if match != None:
    monthName = MONTHS[match.month - 1]
    dateText = '{} {}'.format(monthName, birthday.day)
    print('multiple people have a birthday on, ', dateText)
else:
    print('there are no matching birthdays.')

print()

print('Generating', numBDays, 'random birthdays 100,000 times...')
input('Press Enter to begin...')

simMatch = 0
for i in range(100_000):
    if i % 10_000 == 0:
        print(i, 'simulations run...')
    birthdays = getBirthdays(numBDays)
    if getMatch(birthdays) != None:
        simMatch += 1

print('100,000 simulations run.')

probability = round(simMatch / 100_000 * 100, 2)
print('Out of 100,000 simulations of', numBDays, 'people, there was a')
print('matching birthday in that group', simMatch, 'times. This means')
print('that', numBDays, 'people have a', probability, '% chance of')
print('having a matching birthday in their group')

