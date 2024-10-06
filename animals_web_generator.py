import json

def load_data(file_path):
    """Loads the JSON file. """
    with open(file_path, 'r') as handle:
        return json.load(handle)


def create_animal_info(animals_data):
    """ Creates a string with the animals' information,
    and creates a new list for each animal.
    """
    animal_info = ""
    for animal in animals_data:
        animal_info += "<li class='cards__item'>\n"

        if "name" in animal:
            animal_info += f"Name: {animal['name']}<br/>\n"
        if "characteristics" in animal and "diet" in animal['characteristics']:
            animal_info += f"Diet: {animal['characteristics']['diet']}<br/>\n"
        if "locations" in animal and len(animal['locations']) > 0:
            animal_info += f"Location: {animal['locations'][0]}<br/>\n"
        if "characteristics" in animal and "type" in animal['characteristics']:
            animal_info += f"Type: {animal['characteristics']['type']}<br/>\n"

        animal_info += "</li>\n"

    print(animal_info)
    return animal_info


# Loads animal data from JSON.
animals_data = load_data('animals_data.json')

# 1. Read the content of the template.
with open("animals_template.html", "r") as template_file:
    html_template = template_file.read()

# 2. Generate a string with the animals’ data.
animal_info_html = create_animal_info(animals_data)

# 3. Replace __REPLACE_ANIMALS_INFO__ with the generated string.
html_output = html_template.replace("__REPLACE_ANIMALS_INFO__", animal_info_html)

# 4. Write the new HTML content to a new file.
with open("animals.html", "w") as output_file:
    output_file.write(html_output)

