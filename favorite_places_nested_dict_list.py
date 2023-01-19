#Nested List inside a nested Dictionary
favorite_places = {
    'john' : {
        'favorite_places': ['rome', 'berlin', 'paris'],
        'wishlist': ['holland', 'canada'],
    },
    'michael' : {
        'favorite_places': ['red light district', 'thailand'],
        'wishlist': ['germany', 'italy'],
    }
}
#Looping Through the Dictionary Keys
for keys in favorite_places.keys():
    fav_places = favorite_places.get('favorite_places')
    wishlist_places = favorite_places.get('wishlist')
    
    print(f"\n{keys.title()}'s Favorite Places Are:")
    for fav_place in fav_places: #Looping through the list values inside nested 'favorite_places' Key
        print(f"\t\t\t{fav_place.title()}")

    print(f"\n    And Wishlist Places Are:")
    for wishlist_place in wishlist_places: #Looping through the list values inside nested 'wishlist' Key
        print(f"\t\t\t{wishlist_place.title()}")
