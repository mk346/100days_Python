# nesting dictionaries and lists
countries_visited = [
    {
        "country" : "Kenya",
        "visits" : 20,
        "cities" : ["Nairobi", "Mombasa", "Nakuru"]
    },
    {
        "country" : "Tanzania",
        "visits" : 8,
        "cities" : ["Dareesalam", "Arusha",]
    },
    {
        "country" : "South Africa",
        "visits" : 10,
        "cities" : ["Durban", "Cape Town", "Johannesburg"]
    }
]

def add_country():
    new_country = {}
    new_country['country'] = input("Enter country name: \n")
    new_country['visits'] = int(input("Enter the number of visits: \n"))
    new_country['cities'] = input("Enter the cities visited: \n").split(",")
    countries_visited.append(new_country)
    
add_country()
print(countries_visited)