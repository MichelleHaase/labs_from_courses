input = input("Item: ").strip().lower().capitalize()

Enery_from_fruit = {
    "Apple": 130,
    "Avocado": 50,
    "Banana": 110,
    "Cantaloupe": 50,
    "Grapefruit": 60,
    "Grapes": 60,
    "Honeydew melon": 50,
    "Kiwifruit": 90,
    "Lemon": 15,
    "Lime": 20,
    "Nectarine": 60,
    "Orange": 80,
    "Peach": 60,
    "Pear": 100,
    "Pineapple": 50,
    "Plums": 70,
    "Strawberries": 50,
    "Sweet cherries": 100,
    "Tangerine": 50,
    "Watermelon": 80,
}

if input in Enery_from_fruit.keys():
    print(f"Calories: {Enery_from_fruit[input]}")
