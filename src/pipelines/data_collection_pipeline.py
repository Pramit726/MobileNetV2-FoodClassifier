import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'components')))

from data_collection import scrape_images_for_items

# Define global variables
cwd = './Dataset/'
datasets = ['valid/', 'test/', 'train/']
number_of_images = [10, 10, 30]

# Call data collection functions
classes = {
    'Apple': [os.path.join(cwd, dataset, 'Apple') for dataset in datasets],
    'Artichoke': [os.path.join(cwd, dataset, 'Artichoke') for dataset in datasets],
     'Asparagus': [os.path.join(cwd, dataset, 'Asparagus') for dataset in datasets],
    'Avocado': [os.path.join(cwd, dataset, 'Avocado') for dataset in datasets],
    'Bacon': [os.path.join(cwd, dataset, 'Bacon') for dataset in datasets],
    'Banana': [os.path.join(cwd, dataset, 'Banana') for dataset in datasets],
    'Beetroot': [os.path.join(cwd, dataset, 'Beetroot') for dataset in datasets],
    'Bitter Gourd': [os.path.join(cwd, dataset, 'Bitter Gourd') for dataset in datasets],
    'Bottle Gourd': [os.path.join(cwd, dataset, 'Bottle Gourd') for dataset in datasets],
    'Bread': [os.path.join(cwd, dataset, 'Bread') for dataset in datasets],
    'Brinjal': [os.path.join(cwd, dataset, 'Brinjal') for dataset in datasets],
    'Broccoli': [os.path.join(cwd, dataset, 'Broccoli') for dataset in datasets],
    'Butter': [os.path.join(cwd, dataset, 'Butter') for dataset in datasets],
    'Cabbage': [os.path.join(cwd, dataset, 'Cabbage') for dataset in datasets],
    'Capsicum': [os.path.join(cwd, dataset, 'Capsicum') for dataset in datasets],
    'Carrot': [os.path.join(cwd, dataset, 'Carrot') for dataset in datasets],
    'Cauliflower': [os.path.join(cwd, dataset, 'Cauliflower') for dataset in datasets],
    'Cheese': [os.path.join(cwd, dataset, 'Cheese') for dataset in datasets],
    'Chicken': [os.path.join(cwd, dataset, 'Chicken') for dataset in datasets],
    'Chickpeas': [os.path.join(cwd, dataset, 'Chickpeas') for dataset in datasets],
    'Chili Pepper': [os.path.join(cwd, dataset, 'Chili Pepper') for dataset in datasets],
    'Chili Powder': [os.path.join(cwd, dataset, 'Chili Powder') for dataset in datasets],
    'Chowmein Noodles': [os.path.join(cwd, dataset, 'Chowmein Noodles') for dataset in datasets],
    'Cinnamon': [os.path.join(cwd, dataset, 'Cinnamon') for dataset in datasets],
    'Coriander': [os.path.join(cwd, dataset, 'Coriander') for dataset in datasets],
    'Corn': [os.path.join(cwd, dataset, 'Corn') for dataset in datasets],
    'Cornflake': [os.path.join(cwd, dataset, 'Cornflake') for dataset in datasets],
    'Crab Meat': [os.path.join(cwd, dataset, 'Crab Meat') for dataset in datasets],
    'Cucumber': [os.path.join(cwd, dataset, 'Cucumber') for dataset in datasets],
    'Egg': [os.path.join(cwd, dataset, 'Egg') for dataset in datasets],
    'Fish': [os.path.join(cwd, dataset, 'Fish') for dataset in datasets],
    'Garlic': [os.path.join(cwd, dataset, 'Garlic') for dataset in datasets],
    'Ginger': [os.path.join(cwd, dataset, 'Ginger') for dataset in datasets],
    'Green Mint': [os.path.join(cwd, dataset, 'Green Mint') for dataset in datasets],
    'Green Peas': [os.path.join(cwd, dataset, 'Green Peas') for dataset in datasets],
    'Soyabean': [os.path.join(cwd, dataset, 'Soyabean') for dataset in datasets],
    'Ice': [os.path.join(cwd, dataset, 'Ice') for dataset in datasets],
    'Jack Fruit': [os.path.join(cwd, dataset, 'Jack Fruit') for dataset in datasets],
    'Ketchup': [os.path.join(cwd, dataset, 'Ketchup') for dataset in datasets],
    'Kimchi': [os.path.join(cwd, dataset, 'Kimchi') for dataset in datasets],
    'Lemon': [os.path.join(cwd, dataset, 'Lemon') for dataset in datasets],
    'Mayonnaise': [os.path.join(cwd, dataset, 'Mayonnaise') for dataset in datasets],
    'Milk': [os.path.join(cwd, dataset, 'Milk') for dataset in datasets],
    'Drumsticks': [os.path.join(cwd, dataset, 'Drumsticks') for dataset in datasets],
    'Mushroom': [os.path.join(cwd, dataset, 'Mushroom') for dataset in datasets],
    'Mutton': [os.path.join(cwd, dataset, 'Mutton') for dataset in datasets],
    'Okra': [os.path.join(cwd, dataset, 'Okra') for dataset in datasets],
    'Olive Oil': [os.path.join(cwd, dataset, 'Olive Oil') for dataset in datasets],
    'Onion': [os.path.join(cwd, dataset, 'Onion') for dataset in datasets],
    'Spring onion': [os.path.join(cwd, dataset, 'Spring onion') for dataset in datasets],
    'Orange': [os.path.join(cwd, dataset, 'Orange') for dataset in datasets],
    'Spinach': [os.path.join(cwd, dataset, 'Spinach') for dataset in datasets],
    'Paneer': [os.path.join(cwd, dataset, 'Paneer') for dataset in datasets],
    'Papaya': [os.path.join(cwd, dataset, 'Papaya') for dataset in datasets],
    'Pea': [os.path.join(cwd, dataset, 'Pea') for dataset in datasets],
    'Pear': [os.path.join(cwd, dataset, 'Pear') for dataset in datasets],
    'Pointed Gourd': [os.path.join(cwd, dataset, 'Pointed Gourd') for dataset in datasets],
    'Potato': [os.path.join(cwd, dataset, 'Potato') for dataset in datasets],
    'Pumpkin': [os.path.join(cwd, dataset, 'Pumpkin') for dataset in datasets],
    'Radish': [os.path.join(cwd, dataset, 'Radish') for dataset in datasets],
    'Red Beans': [os.path.join(cwd, dataset, 'Red Beans') for dataset in datasets],
    'Red Lentils': [os.path.join(cwd, dataset, 'Red Lentils') for dataset in datasets],
    'Rice': [os.path.join(cwd, dataset, 'Rice') for dataset in datasets],
    'Salt': [os.path.join(cwd, dataset, 'Salt') for dataset in datasets],
    'Sausage': [os.path.join(cwd, dataset, 'Sausage') for dataset in datasets],
    'Seaweed': [os.path.join(cwd, dataset, 'Seaweed') for dataset in datasets],
    'Snake Gourd': [os.path.join(cwd, dataset, 'Snake Gourd') for dataset in datasets],
    'Soy Sauce': [os.path.join(cwd, dataset, 'Soy Sauce') for dataset in datasets],
    'Soya Chunks': [os.path.join(cwd, dataset, 'Soya Chunks') for dataset in datasets],
    'Strawberry': [os.path.join(cwd, dataset, 'Strawberry') for dataset in datasets],
    'Sugar': [os.path.join(cwd, dataset, 'Sugar') for dataset in datasets],
    'Sweet Potato': [os.path.join(cwd, dataset, 'Sweet Potato') for dataset in datasets],
    'Tomato': [os.path.join(cwd, dataset, 'Tomato') for dataset in datasets],
    'Turnip': [os.path.join(cwd, dataset, 'Turnip') for dataset in datasets],
    'Walnut': [os.path.join(cwd, dataset, 'Walnut') for dataset in datasets],
    'Watermelon': [os.path.join(cwd, dataset, 'Watermelon') for dataset in datasets],
    'Wheat': [os.path.join(cwd, dataset, 'Wheat') for dataset in datasets],
    'Yellow Lentils': [os.path.join(cwd, dataset, 'Yellow Lentils') for dataset in datasets],
    'Mango': [os.path.join(cwd, dataset, 'Mango') for dataset in datasets],
    'Pomegranate': [os.path.join(cwd, dataset, 'Pomegranate') for dataset in datasets],
    'Pineapple': [os.path.join(cwd, dataset, 'Pineapple') for dataset in datasets],
    'Kiwi': [os.path.join(cwd, dataset, 'Kiwi') for dataset in datasets]
}

for ingredient, dataset in classes.items():
    for path in dataset:
        substring = path.split('/')[2]
        print(substring)
        if substring == "valid":
            num_images_per_item = number_of_images[0]
        elif substring == "test":
            num_images_per_item = number_of_images[1]
        else:
            num_images_per_item = number_of_images[2]
        scrape_images_for_items(ingredient, path, num_images_per_item)