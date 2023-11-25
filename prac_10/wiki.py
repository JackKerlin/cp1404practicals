"""
CP1404 Practical Jack Kerlin
Wiki api
Estimate: 40 minutes
Actual: 30 minutes
"""

import wikipedia
user_search = input("Enter Wikipedia search: ")
while user_search != "":
    try:
        searched_page = wikipedia.page(user_search, auto_suggest=False)
        print(searched_page.title)
        print(searched_page.summary)
        print(searched_page.url)
    except wikipedia.exceptions.DisambiguationError as disambiguation:
        print(disambiguation.options)
    except wikipedia.exceptions.PageError:
        print("Page not found :(")
    user_search = input("Enter Wikipedia search: ")
