
travel_log={    
    "France": ["Paris", "Lille", "Dijon"],
    "Germany": ["Berlin", "Hamburg", "Stuttgart"],
    "Italy": ["Rome", "Milan", "Venice"]
    }

##print the third city in France
print(travel_log["France"][2])

nested_list = ["a", "b", ["c", "d"]]

travel_log2={
    "France":{
        "cities_visited":["Paris", "Lille", "Dijon"],
        "total_visits":12
    },
    "Germany":{
        "cities_visited":["Berlin", "Hamburg", "Stuttgart"],
        "total_visits":5
    },
}

print(travel_log2["Germany"]["cities_visited"][1])
