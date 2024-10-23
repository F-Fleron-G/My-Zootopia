import data_fetcher


def serialize_animal(animal_obj):
    """Convert an animal object into an HTML formatted string."""
    animal_info = "<li class='cards__item'>\n"

    if "name" in animal_obj:
        animal_info += f"<div class='card__title'>{animal_obj['name']}</div>\n"

    animal_info += "<p class='card__text'>\n"

    if "locations" in animal_obj and len(animal_obj["locations"]) > 0:
        animal_info += f"<strong>Location:</strong> {animal_obj['locations']
        [0]}<br/>\n"
    if "characteristics" in animal_obj:
        if "type" in animal_obj["characteristics"]:
            animal_info += f"<strong>Type:</strong> {animal_obj['characteristics']
            ['type'].capitalize()}<br/>\n"
        if "diet" in animal_obj["characteristics"]:
            animal_info += f"<strong>Diet:</strong> {animal_obj['characteristics']
            ['diet']}<br/>\n"

    animal_info += "</p>\n"
    animal_info += "</li>\n"

    return animal_info


def create_animal_info(animals_data):
    """Generates HTML for the animals list or an error message if no data is
    available.
    """
    if not animals_data or len(animals_data) == 0:
        return ("<h2>No information available. Please search for a different"
                "animal.</h2>")

    animal_info = ""
    for animal in animals_data:
        animal_info += serialize_animal(animal)

    return animal_info


def main():

    animal_name = input("Please enter the name of an animal: ").strip()

    animals_data = data_fetcher.fetches_data(animal_name)

    if animals_data:

        with open("animals_template.html", "r") as template_file:
            html_template = template_file.read()

        animal_info_html = create_animal_info(animals_data)

        html_output = html_template.replace("__REPLACE_ANIMALS_INFO__",
                                            animal_info_html)

        with open("animals.html", "w") as output_file:
            output_file.write(html_output)

        print("A new HTML file has been created: animals.html.")
    else:
        error_message = (f"<h2>Unfortunately, we have no information about '"
                         f"{animal_name}'.</h2>")

        with open("animals_template.html", "r") as template_file:
            html_template = template_file.read()

        html_output = html_template.replace("__REPLACE_ANIMALS_INFO__", error_message)

        with open("animals.html", "w") as output_file:
            output_file.write(html_output)

        print(f"There is no valid data found for '{animal_name}'. Error page created.")


if __name__ == "__main__":
    main()
