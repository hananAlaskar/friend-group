"""An example of how to represent a group of acquaintances in Python."""
import numpy as np

# Your code to go here...

my_group = [{"name": "Jill", "age": 26, "job": "biologist"},
            {"name": "Zalika", "age": 28, "job": "artist"},
            {"name": "John", "age": 27, "job": "writer"},
            {"name": "Nash", "age": 34, "job": "landlord"}]

# print(all_people)

def add_relationship(person_1, person_2, relationship):
    all_people = [person["name"] for person in my_group]

    if (person_1 not in all_people):
        my_group.append({"name": person_1, 'age':0, 'job': None})
    if (person_2 not in all_people):
        my_group.append({"name": person_2, 'age':0, 'job': None})

    for people in my_group:
        if (people["name"] == person_1):
            if(relationship in people):
                people[relationship].append(person_2)
            else:
                people[relationship] = [person_2]
        if (people["name"] == person_2):
            if(relationship in people):
                people[relationship].append(person_1)
            else:
                people[relationship] = [person_1]

def add_relationship2(person_1, person_2, relationship_1, relationship_2):
    all_people = [person["name"] for person in my_group]

    if (person_1 not in all_people):
        my_group.append({"name": person_1, 'age':0, 'job': None})
    if (person_2 not in all_people):
        my_group.append({"name": person_2, 'age':0, 'job': None})

    for people in my_group:
        if (people["name"] == person_1):
            if(relationship_1 in people):
                people[relationship_1].append(person_2)
            else:
                people[relationship_1] = [person_2]
        if (people["name"] == person_2):
            if(relationship_2 in people):
                people[relationship_2].append(person_1)
            else:
                people[relationship_2] = [person_1]


add_relationship("Jill", "Zalika", "friend")
add_relationship("Jill", "Nadira", "friend")
add_relationship("Jill","John","partner")
add_relationship("John", "Nash", "cousin")
add_relationship2("Zalika", "Nash", "landlord", "tennant")
add_relationship2("Zalika", "Grannie", "grandmother", "granddaughter")
print(my_group)

all_people_age = [person["age"] for person in my_group]
#1 the maximum age of people in the group
print('the maximum age of people in the group :', max(all_people_age))

#2 (unfinished)
mean_relationships = np.mean([len(person) -3 for person in my_group ])
print('the average (mean) number of relations among members of the group :', mean_relationships)

#3
subset_age = []
for person in my_group:
    if (len(person) >3):
        subset_age.append(person)

relationship_age = [person["age"] for person in (subset_age)]
print("the maximum age of people in the group that have at least one relation :", max(relationship_age))


#4
subset_friend = []
for person in my_group:
    if ("friend" in person):
        subset_friend.append(person)

friend_age = [person["age"] for person in (subset_age)]
print("the maximum age of people in the group that have at least one friend :", max(friend_age))
