guitar_data = [
    {
        'id': 1,
        'brand': 'Fender',
        'model': 'Stratocaster',
        'color': 'Sunburst',
        'price': 1200,
        'year': 2020
    },
    {
        'id': 2,
        'brand': 'Gibson',
        'model': 'Les Paul',
        'color': 'Black',
        'price': 1800,
        'year': 2019
    },
    {
        'id': 3,
        'brand': 'Ibanez',
        'model': 'RG550',
        'color': 'Blue',
        'price': 900,
        'year': 2021
    },
    {
        'id': 4,
        'brand': 'PRS',
        'model': 'Custom 24',
        'color': 'Red',
        'price': 2200,
        'year': 2018
    },
    {
        'id': 5,
        'brand': 'Jackson',
        'model': 'Soloist',
        'color': 'White',
        'price': 1500,
        'year': 2022
    },
    {
        'id': 6,
        'brand': 'ESP',
        'model': 'LTD EC-1000',
        'color': 'Black Cherry',
        'price': 1300,
        'year': 2017
    },
    {
        'id': 7,
        'brand': 'Gretsch',
        'model': 'Streamliner',
        'color': 'Green',
        'price': 1000,
        'year': 2023
    },
    {
        'id': 8,
        'brand': 'Taylor',
        'model': '814ce',
        'color': 'Natural',
        'price': 2500,
        'year': 2021
    },
    {
        'id': 9,
        'brand': 'Epiphone',
        'model': 'SG Standard',
        'color': 'Vintage Cherry',
        'price': 600,
        'year': 2020
    },
    {
        'id': 10,
        'brand': 'Yamaha',
        'model': 'Pacificia 112V',
        'color': 'Candy Apple Red',
        'price': 350,
        'year': 2019
    }
]


class GuitarInventory():
    def __init__(self,id,brand,model,color,price,year):
        self.id = id
        self.brand = brand
        self.model = model
        self.color = color
        self.price = price
        self.year = year

    
