import requests


def load_data(animal_name):
    """Fetches data from the API for the given animal name."""
    url = f"https://api.api-ninjas.com/v1/animals?name={animal_name}"

    headers = {
        "X-Api-Key": "rhPAEnhfQ2zHQ0dQgJJ+9w==s4gOmxkzDVWokPX3"
    }

    response = requests.get(url, headers=headers)

    # Checks the return status and returns JSON data.
    if response.status_code == 200:
        return response.json()
    else:
        print(f"There's an error: {response.status_code}")
        return None


def serialize_animal(animal_obj):
    """Convert an animal object into an HTML formatted string."""
    animal_info = "<li class='cards__item'>\n"

    if "name" in animal_obj:
        animal_info += f"<div class='card__title'>{animal_obj['name']}</div>\n"

    animal_info += "<p class='card__text'>\n"

    if "locations" in animal_obj and len(animal_obj["locations"]) > 0:
        animal_info += f"<strong>Location:</strong> {animal_obj['locations'][0]}<br/>\n"
    if "characteristics" in animal_obj:
        if "type" in animal_obj["characteristics"]:
            animal_info += f"<strong>Type:</strong> {animal_obj['characteristics']['type'].capitalize()}<br/>\n"
        if "diet" in animal_obj["characteristics"]:
            animal_info += f"<strong>Diet:</strong> {animal_obj['characteristics']['diet']}<br/>\n"

    animal_info += "</p>\n"
    animal_info += "</li>\n"

    return animal_info


def create_animal_info(animals_data):
    """Compile HTML for multiple animals from a data list."""
    animal_info = ""
    for animal in animals_data:
        animal_info += serialize_animal(animal)
    return animal_info


def main():

    animal_name = input("Please enter the name of an animal: ").strip()

    animals_data = load_data(animal_name)

    # Checks if the API returned data.
    if animals_data:

        with open("animals_template.html", "r") as template_file:
            html_template = template_file.read()

        animal_info_html = create_animal_info(animals_data)

        html_output = html_template.replace("__REPLACE_ANIMALS_INFO__", animal_info_html)

        with open("animals.html", "w") as output_file:
            output_file.write(html_output)

        print("A new HTML file has been created: animals.html.")
    else:
        print("Failed to fetch animal data from the API.")


if __name__ == "__main__":
    main()
