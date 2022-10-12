contacts = [
    {
        'name': 'Anna', 
        'age': 17,
        'phone': '654987321',
        #UZDEVUUMS: pieraksti vārdnīcā klāt:
        #Annai ir 2020. gada sarkanā Audi ar 2.0 litru dzinēju
        'cars': [
            {
                'brand': 'Audi',
                'year': 2020,
                'color': 'Red',
                'engine': 2.0
            },
            {
                'brand': 'Tesla',
                'year': 2022,
                'color': 'Silver',
                'engine': 50
            }
        ]
    }, 
    {
        'name': 'Oskars', 
        'age': 22,
        'phone': '+371 1234679654',
        'cars': [
            {
                'brand': 'BMW',
                'year': 2018,
                'color': 'Blue',
                'engine': 2.5
            }            
        ]
    }, 
    {
        'name': 'Jenifer', 
        'age': 18,
        'phone': '+1(987)6547852147',
        'cars': [
            {
                'brand': 'BMW',
                'year': 2021,
                'color': 'Black',
                'engine': 1.5
            }            
        ]
    },
    {
        'name': 'Miks', 
        'age': 16,
        'phone': '4658784125'
    }
]

print(contacts[0]['car_year'])

#for contact in contacts:
#    print(contact['name'])
#    print(contact['age'])
#    print(contact['phone'])


