from random import choice
from django.shortcuts import render, redirect
import requests, json

# Create your views here.

def home(request):
        cocktail = requests.get('https://www.thecocktaildb.com/api/json/v1/1/random.php').json()
        
        drink_name = cocktail['drinks'][0]['strDrink']
        drink_instructions = cocktail['drinks'][0]['strInstructions']
        drink_pic = cocktail['drinks'][0]['strDrinkThumb']
        drink_ingredient1 = cocktail['drinks'][0]['strIngredient1']
        drink_ingredient2 = cocktail['drinks'][0]['strIngredient2']
        drink_ingredient3 = cocktail['drinks'][0]['strIngredient3']
        drink_ingredient4 = cocktail['drinks'][0]['strIngredient4']
        drink_ingredient5 = cocktail['drinks'][0]['strIngredient5']
        drink_ingredient6 = cocktail['drinks'][0]['strIngredient6']
        drink_ingredient7 = cocktail['drinks'][0]['strIngredient7']
        drink_ingredient8 = cocktail['drinks'][0]['strIngredient8']
        return render(request, 'home.html', {
            'drink_name': drink_name, 
            'drink_instructions': drink_instructions, 
            'drink_pic': drink_pic,
            'drink_ingredient1': drink_ingredient1,
            'drink_ingredient2': drink_ingredient2,
            'drink_ingredient3': drink_ingredient3,
            'drink_ingredient4': drink_ingredient4,
            'drink_ingredient5': drink_ingredient5,
            'drink_ingredient6': drink_ingredient6,
            'drink_ingredient7': drink_ingredient7,
            'drink_ingredient8': drink_ingredient8,
            })

