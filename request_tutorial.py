#Importe the request library
import requests

#Make a request to the desired API and asign it to a variable 
r = requests.get('https://pokeapi.co/api/v2/pokemon/ditto')

#Parse the response using the builtin fuction json() so we can access the inner date of the object
pokemon=r.json()

#The Json decorder return a dictionary wich we can access by naming the Keys inside of it 
pokemon_name=pokemon['name']

#prints the result in console
print(pokemon_name)

#the following example is similar to the previous but using user input to search for a pokemon name given their number
pokemon_number=input('Type in a Pokemon Number to get back their name: ')
response = requests.get(
    'https://pokeapi.co/api/v2/pokemon/'+pokemon_number
)

#prints our the request url to see if we match the api requirements
print(response.url)

#prints our parsed result 
print(response.json()['name'])

