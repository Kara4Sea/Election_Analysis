print("Hello World")
counties = ["Arapahoe","Denver","Jefferson"]
counties.append("El Paso")
counties.insert(2, "El Paso")
counties.remove("El Paso")
counties_dict = {}
counties_dict["Arapahoe"] = 422829
counties_dict["Denver"] = 463353
counties_dict["Jefferson"] = 432438
counties_dict.items()
counties_dict.keys()
counties_dict_keys = (['Arapahoe', 'Denver', 'Jefferson'])
counties_dict.values()
counties_dict_values = ([422829, 463353, 432438])
voting_data = []
voting_data.append({"county":"Arapahoe", "registered_voters": 422829})

voting_data.append({"county":"Jefferson", "registered_voters": 432438})

voting_data.insert(1,{"county":"El Paso", "registered_voters": 461149})
voting_data.remove({"county":"Arapahoe", "registered_voters": 422829})
voting_data.insert(2,{"county":"Denver", "registered_voters": 463353})
voting_data.append({"county":"Arapahoe", "registered_voters": 422829})

print(voting_data)