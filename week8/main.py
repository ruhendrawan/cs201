
import json


# Domain model / Business logic
class Listing:
    def __init__(self, id, name, is_sold):
        self.id = id
        self.name = name
        
        # without property, we can do this by defaulting to False
        # self._is_sold : bool = is_sold
        
        # with property, we gain more control
        self.is_sold = is_sold
    
    @property
    def is_sold(self):
        return self._is_sold
    
    @is_sold.setter
    def is_sold(self, value):
        # Since we are using json, 
        # we can't use boolean directly
        # instead we expect 'true' or 'false' string
        if not isinstance(value, str):
            raise ValueError("str expected")
        if value.lower() == 'true':
            self._is_sold = True
        elif value.lower() == 'false':
            self._is_sold = False
        else:
            raise ValueError("true or false expected")
        # if not isinstance(value, bool):
        #     raise ValueError("boolean expected")
        self._is_sold = value

    def __str__(self):
        return f'Listing: {self.id} - {self.name} - {self.is_sold}'


# Data access layer
class ListingRepository:
    def load_listing_from_json(self, json_file):
        listings = []
        with open(json_file, 'r') as file:
            json_data = json.load(file)
            for row in json_data:
                try:
                    listings.append(
                        Listing(
                            row['id'],
                            row['name'],
                            row['is_sold'], 
                            # without property, only 'true' is considered True
                            # row['is_sold'] == 'true', 
                        )
                    )
                except ValueError as ve:
                    # Ignore invalid rows
                    pass
        return listings


# Presentation layer
class ListingView:
    def __init__(self, listings):
        self.listings = listings

    def show(self):
        for listing in self.listings:
            print(listing)    



if __name__ == '__main__':
    repo = ListingRepository()
    listing_data = repo.load_listing_from_json('listings.json')
    view = ListingView(listing_data)
    view.show()