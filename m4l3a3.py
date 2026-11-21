country_code = { 
    "india": "0043",
    "usa": "00276"
}
print("the country code of india is -")
print(country_code.get("india", "not found"))

print("the country code for japan is -")
print(country_code.get("japan", "not found"))