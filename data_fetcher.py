import requests

API_KEY = "rhPAEnhfQ2zHQ0dQgJJ+9w==s4gOmxkzDVWokPX3"


def fetches_data(animal_name):
    """
    Fetches the animals data for the given 'animal_name' from the API.

    Returns: a list of animals, each animal is a dictionary:
    {
        'name': ...,
        'taxonomy': {...},
        'locations': [...],
        'characteristics': {...}
    }
    """
    url = f"https://api.api-ninjas.com/v1/animals?name={animal_name}"
    headers = {"X-Api-Key": API_KEY}

    response = requests.get(url, headers=headers)

    if response.status_code == 200 and response.json():
        return response.json()
    else:
        print(f"Error: {response.status_code}")
        return None