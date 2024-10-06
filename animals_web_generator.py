import json


def load_data(file_path):
    """ Loads the JSON file """
    with open(file_path, 'r') as handle:
        return json.load(handle)


def print_animal_info(animals_data):
    """ Prints each animal's Name, Diet, First Location, and Type (if available) """
    for animal in animals_data:
        if 'name' in animal:
            print(f"Name: {animal['name']}")

        if 'characteristics' in animal and 'diet' in animal['characteristics']:
            print(f"Diet: {animal['characteristics']['diet']}")

        if 'locations' in animal and len(animal['locations']) > 0:
            print(f"Location: {animal['locations'][0]}")

        if 'characteristics' in animal and 'type' in animal['characteristics']:
            print(f"Type: {animal['characteristics']['type']}")

        print()


animals_data = load_data('animals_data.json')

print_animal_info(animals_data)
