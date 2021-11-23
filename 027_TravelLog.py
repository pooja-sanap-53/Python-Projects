# Travel Log

'''
INSTRUCTIONS

You are going to write a program that adds to a travel_log.
Write a function that will work with the following line of code to add the entry for Russia to the travel_log.

add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
You've visited Russia 2 times.

You've been to Moscow and Saint Petersburg.

DO NOT modify the travel_log directly. You need to create a function that modifies it.

'''

travel_log = [
{
  "country": "France",
  "visits": 12,
  "cities": ["Paris", "Lille", "Dijon"]
},
{
  "country": "Germany",
  "visits": 5,
  "cities": ["Berlin", "Hamburg", "Stuttgart"]
},
]

def add_new_country(country_name, total_visits, cities_visited):
    new_entry = {}
    new_entry["country"] = country_name
    new_entry["visits"] = total_visits
    new_entry["cities"] = cities_visited
    travel_log.append(new_entry)

add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
print(travel_log)
