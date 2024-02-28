import json


class Listing:
    def __init__(self, id, name, is_sold):
        self.id = id
        self.name = name
        self.is_sold : bool = is_sold

    def __str__(self):
        return f'Listing: {self.id} - {self.name} - {self.is_sold}'


def load_listing_from_json(json_file):
    listings = []
    with open(json_file, 'r') as file:
        json_data = json.load(file)
        for row in json_data:
            listings.append(
                Listing(
                    row['id'],
                    row['name'],
                    row['is_sold'] == 'true', 
                )
            )
    return listings


listings = load_listing_from_json('listings.json')


for listing in listings:
    print(listing)
