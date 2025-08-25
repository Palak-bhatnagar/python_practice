import json

# Step 1: Load existing data or create new if file not present
filename = "countries.json"

try:
    with open(filename, "r") as file:
        data = json.load(file)
except FileNotFoundError:
    data = {"countries": []}

# Step 2: Ask user how many countries to add
n = int(input("How many countries do you want to add? "))

for _ in range(n):
    name = input("Enter country name: ")
    capital = input("Enter capital city: ")
    population = int(input("Enter population: "))

    # Add new entry to the list
    data["countries"].append({
        "name": name,
        "capital": capital,
        "population": population
    })

# Step 3: Save updated data back to JSON file
with open(filename, "w") as file:
    json.dump(data, file, indent=4)

print("\n✅ Countries added successfully!\n")

# Step 4: Display all countries
print("Updated Country Details:\n")
for country in data["countries"]:
    print(f"Country: {country['name']}")
    print(f"Capital: {country['capital']}")
    print(f"Population: {country['population']:,}")
    print("-" * 30)
