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
for keys in favorite_places.keys():
    fav_places = favorite_places[keys].get('favorite_places')
    wishlist_places = favorite_places[keys].get('wishlist')
    
    print(f"\n{keys.title()}'s Favorite Places Are:")
    for fav_place in fav_places:
        print(f"\t\t\t{fav_place.title()}")

    print(f"\n    And Wishlist Places Are:")
    for wishlist_place in wishlist_places:
        print(f"\t\t\t{wishlist_place.title()}")