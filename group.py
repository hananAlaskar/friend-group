"""An example of how to represent a group of acquaintances in Python."""

# Your code to go here...

my_group = [{"name": "Jill", "age": 26, "job": "biologist"},
            {"name": "Zalika", "age": 28, "job": "artist"},
            {"name": "John", "age": 27, "job": "writer"},
            {"name": "Nash", "age": 34, "job": "landlord"}]

# print(all_people)

def add_relationship(person_1, person_2, relationship):
    all_people = [person["name"] for person in my_group]

    if (person_1 not in all_people):
        my_group.append({"name": person_1})
    if (person_2 not in all_people):
        my_group.append({"name": person_2})

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


add_relationship("Jill", "Zalika", "friend")
add_relationship("Jill", "Nadira", "friend")
add_relationship("Jill","John","partner")
print(my_group)