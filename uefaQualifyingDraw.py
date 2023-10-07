import random
from html import escape

winterVenue = ['Belarus', 'Estonia', 'Faroe Islands', 'Finland', 'Iceland', 'Latvia', 'Lithuania', 'Norway']

excessiveTravelAZE = ['Gibraltar', 'Iceland', 'Portugal']
excessiveTravelISL = ['Cyprus', 'Georgia', 'Israel']
excessiveTravelKAZ = ['Andorra', 'England', 'France', 'Gibraltar', 'Iceland', 'Malta', 'Northern Ireland', 'Portugal',
                      'Republic of Ireland', 'Scotland', 'Spain', 'Wales']


def winterVenueCheck(group, winterVenue):
    # Check if any group has more than two countries from winterVenue
    winter_count = sum(1 for country in group if country in winterVenue)
    if winter_count <= 2:
        return 0
    else:
        return 1


def excessiveTravel(group, excessiveTravel):
    excessive_count = sum(1 for country in new_group if country in excessiveTravel)
    if excessive_count <= 1:
        return 0
    else:
        return 1


def prohibitedClashesCheck(new_group):
    if "Armenia" in new_group and "Azerbaijan" in new_group:
        return 1
    if "Spain" in new_group and "Gibraltar" in new_group:
        return 1
    if "Serbia" in new_group and "Kosovo" in new_group:
        return 1
    if "Kosovo" in new_group and "Bosnia and Herzegovina" in new_group:
        return 1
    if "Belarus" in new_group and "Ukraine" in new_group:
        return 1
    else:
        return 0


def validGroup(new_group):
    if prohibitedClashesCheck(new_group) == 1:
        return 1
    if winterVenueCheck(new_group, winterVenue) == 1:
        return 1
    if "Azerbaijan" in new_group and excessiveTravel(new_group, excessiveTravelAZE) == 1:
        return 1
    if "Iceland" in new_group and excessiveTravel(new_group, excessiveTravelISL) == 1:
        return 1
    if "Kazakhstan" in new_group and excessiveTravel(new_group, excessiveTravelKAZ) == 1:
        return 1
    else:
        return 0


while True:
    groups = {}

    listNL = ['Spain', 'Croatia', 'Netherlands', 'Italy']
    list1 = ['Denmark', 'Portugal', 'Belgium', 'Hungary', 'Switzerland', 'Poland']
    list2 = ['France', 'Austria', 'Czechia', 'England', 'Wales', 'Israel', 'Bosnia and Herzegovina', 'Serbia',
             'Scotland', 'Finland']
    list3 = ['Ukraine', 'Iceland', 'Norway', 'Slovenia', 'Republic of Ireland', 'Albania', 'Montenegro', 'Romania',
             'Sweden', 'Armenia']
    list4 = ['Georgia', 'Greece', 'Turkiye', 'Kazakhstan', 'Luxembourg', 'Azerbaijan', 'Kosovo', 'Bulgaria',
             'Faroe Islands', 'North Macedonia']
    list5 = ['Slovakia', 'Northern Ireland', 'Cyprus', 'Belarus', 'Lithuania', 'Gibraltar', 'Estonia', 'Latvia',
             'Moldova', 'Malta']
    list6 = ['Andorra', 'San Marino', 'Liechtenstein']

    # Repeat the process 10 times to create 10 allocations
    for group_number in range(1, 11):
        # Initialize a new list for the group
        new_group = []
        if group_number < 5:
            # Randomly select one country from each list and add it to the new list
            country1 = random.choice(listNL)
            country2 = random.choice(list2)
            country3 = random.choice(list3)
            country4 = random.choice(list4)
            country5 = random.choice(list5)

            # Add the selected countries to the new list
            new_group.extend([country1, country2, country3, country4, country5])

            # Remove the selected countries from the original lists
            listNL.remove(country1)
            list2.remove(country2)
            list3.remove(country3)
            list4.remove(country4)
            list5.remove(country5)

        elif group_number >= 5 and group_number < 8:

            country1 = random.choice(list1)
            country2 = random.choice(list2)
            country3 = random.choice(list3)
            country4 = random.choice(list4)
            country5 = random.choice(list5)

            # Add the selected countries to the new list
            new_group.extend([country1, country2, country3, country4, country5])

            # Remove the selected countries from the original lists
            list1.remove(country1)
            list2.remove(country2)
            list3.remove(country3)
            list4.remove(country4)
            list5.remove(country5)

        else:
            # Randomly select one country from each list and add it to the new list
            country1 = random.choice(list1)
            country2 = random.choice(list2)
            country3 = random.choice(list3)
            country4 = random.choice(list4)
            country5 = random.choice(list5)
            country6 = random.choice(list6)

            # Add the selected countries to the new list
            new_group.extend([country1, country2, country3, country4, country5, country6])

            # Remove the selected countries from the original lists
            list1.remove(country1)
            list2.remove(country2)
            list3.remove(country3)
            list4.remove(country4)
            list5.remove(country5)
            list6.remove(country6)

        if validGroup(new_group) == 0:
            groups[f'group{group_number}'] = new_group
        else:
            continue

    # If there are 10 valid groups, break the loop
    if len(groups) == 10:
        break

with open('groups.html', 'w') as html_file:
    html_file.write("<!DOCTYPE html>\n<html>\n<head>\n")
    html_file.write('<link rel="stylesheet" href="style1.css">\n')
    html_file.write("</head>\n<body>\n")

    group_letters = [chr(ord('A') + i) for i in range(len(groups))]

    for group_letter, (group_name, group) in zip(group_letters, groups.items()):
        html_file.write(f'<h1>Group {group_letter}</h1>\n<ul>\n')
        for country in group:
            html_file.write(f'<li>{escape(country)}</li>\n')
        html_file.write('</ul>\n')

    html_file.write('</body>\n</html>\n')

print('Created groups have been saved to "groups.html" file.')
