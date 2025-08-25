import json

# JSON data
data = {
    "countries": [
        {"name": "India", "capital": "New Delhi", "population": 1428600000},
        {"name": "China", "capital": "Beijing", "population": 1412000000},
        {"name": "United States", "capital": "Washington, D.C.", "population": 339000000},
        {"name": "Indonesia", "capital": "Jakarta", "population": 277500000},
        {"name": "Pakistan", "capital": "Islamabad", "population": 240500000},
        {"name": "Brazil", "capital": "Brasília", "population": 214300000},
        {"name": "Nigeria", "capital": "Abuja", "population": 223800000},
        {"name": "Bangladesh", "capital": "Dhaka", "population": 172500000},
        {"name": "Russia", "capital": "Moscow", "population": 144400000},
        {"name": "Japan", "capital": "Tokyo", "population": 123300000}
    ]
}

# Display in a readable format
print("Country Details:\n")
for country in data["countries"]:
    print(f"Country: {country['name']}")
    print(f"Capital: {country['capital']}")
    print(f"Population: {country['population']:,}")  # formatted with commas
    print("-" * 30)
