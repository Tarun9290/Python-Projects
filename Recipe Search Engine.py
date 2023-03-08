#Recipe Search Engine:

#Build a program that can search for recipes from various sources such as websites and books #and display them in a user-friendly way. You can use libraries such as Beautiful Soup and #Requests to accomplish this

import requests
from bs4 import BeautifulSoup

def search_recipes(query):
    """
    This function searches for recipes based on a given query and returns a list of results.
    """
    # Construct the URL for the search query
    url = f"https://www.allrecipes.com/search/results/?wt={query}&sort=re"

    # Send a GET request to the URL and parse the HTML response
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")

    # Extract the recipe titles and URLs from the search results
    results = []
    for article in soup.find_all("article", class_="fixed-recipe-card"):
        title = article.find("h3", class_="fixed-recipe-card__title").text.strip()
        url = article.find("a", class_="fixed-recipe-card__title-link")["href"]
        results.append({"title": title, "url": url})

    return results

# Example usage
results = search_recipes("chicken")
for result in results:
    print(result["title"], result["url"])
