Basic information
The Python ‘Requests’ library is fantastic for interacting with webpages and APIs through HTTP/1.1 requests. Though it has a few different uses, the Requests library is perfect (and nearly essential) for web scraping, or pulling specific information from websites using scripts & algorithms to automate the process. Based on our research, it seems Requests is almost unanimously lauded as the best option for HTTP request modification thanks to its simplicity, functionality, frequent updates, and widespread popularity-- the Requests website even includes examples that show how difficult it would be for someone to perform its functions without using the library.
Thanks to its up-to-dateness and concise coding features, the Python Requests library is useful in practically any situation that requires parsing information from an HTTP request.
Installation
Python needs to be installed. After python is installed, you should have access to either pip or pip3, which allows us to install the requests library.


Using Pip:
pip install requests

Using Pip3:
Pip3 install requests

Importing the request library
After installing successfully, the library can be included with an import statement, which is recommended to be placed at the top of your .py files.

Example:
<<import statement>>
import requests
<<other import statement>>

<<code>>

**The import statement can also be seen at the top of our example snippets below.



The ‘get’ function
‘Requests’ includes a simple function called ‘get’, which allows you to make a GET request from a website or server by simply typing “requests.get”, followed by a URL. 
	Ex: requests.get(‘https://api.github.com’)

Doing this will elicit a response from the API, which you can easily assign to a variable for parsing.
	Ex: response = requests.get(‘https://api.github.com’)

For added convenience, you can pass parameters to requests.get(), which allows you to modify the results that are returned by the request. 
	Ex: requests.get(‘https://api.github.com’, params={‘q’ : ‘requests+language:python’},)

From here, the user is free to utilize a number of modules that come with Requests for parsing through the GET responses. For example, by using the .content or .text modules, the user can view the payload (the entire response from the GET request) in a more readable format. The user can also utilize the .json() function from the Requests library to convert the response to a dictionary format, so values from the response object can be accessed by their respective key.






Example 1:
#Import the request library
import requests
 
#Make a request to the desired API and assign it to a variable
r = requests.get('https://pokeapi.co/api/v2/pokemon/ditto')
 
#Parse the response using the builtin function json() so we can access the inner date of the object
pokemon=r.json()
 
#The Json decoder return a dictionary wich we can access by naming the Keys inside of it
pokemon_name=pokemon['name']
 
#prints the result in console
print(pokemon_name)
Example 2:
#Import the request library
import requests
 
#the following example is similar to the previous but using user input to search for a pokemon name given their number
pokemon_number=input('Type in a Pokemon Number to get back their name: ')
response = requests.get(
   'https://pokeapi.co/api/v2/pokemon/'+pokemon_number
)
 
 
#prints our the request url to see if we match the api requirements
print(response.url)
 
#prints our parsed result
print(response.json()['name'])
Additional info
Aside from GET, other popular HTTP methods include POST, PUT, DELETE, HEAD, PATCH, and OPTIONS. Requests provides a method, with a similar signature to get(), for each of these HTTP methods.

One other interesting feature of the Requests library is the .request function. This allows the user to view their prepared request in order to inspect exactly what they’re sending/receiving to the server. This is useful for ensuring that the request is properly formatted, which can be particularly valuable when interacting with a site whose format you’re unfamiliar with. Please note that .request needs to be combined with .url or .body in order to return the proper inner element from the response, otherwise it will only return the response code.
