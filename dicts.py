my_dict = {"city": "Москва", "temperature": "20"}
print(my_dict["city"])
my_dict["temperature"] = 5
print(my_dict["temperature"])
# print(my_dict["country"])
print(my_dict.get("country", "Russia"))
my_dict["date"] = "27.05.2019"
print(len(my_dict))