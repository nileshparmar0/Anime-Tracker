try:
    # Import necessary modules
    import sys
    import requests
    from bs4 import BeautifulSoup
    import urllib.parse as parse
    import re
    import argparse
except ImportError as e:
    # Handle ImportError and exit if any module is not found
    print('Terminal Error!')
    print(f'System module import error: {e}')
    sys.exit(1)

# BeautifulSoup (bs4) is used for extracting HTML content from web pages

def details(soup):
    """
    Extracts and prints details about the anime from the given BeautifulSoup object.
    """

    # Find the div with the class 'pure-1 md-3-5' which contains the anime summary
    info = soup.find('div', {'class': 'pure-1 md-3-5'})
    # Extract and print the text within the <p> tag of this div
    print("\nAbout the Anime:\n", "\t\t", info.find('p').getText(), "\n")

    # Find the div with the class 'pure-1 md-1-5' which contains the total number of episodes
    total_episodes = soup.find('div', {'class': 'pure-1 md-1-5'})
    # Extract and print the total number of episodes using regex to select only numbers
    print("\nTotal number of episodes:\t",
          re.sub("[^0-9]", "", total_episodes.find('span').getText()))

    # Find the span with the class 'iconYear' which contains the active years of the anime
    active_years = soup.find('span', {'class': 'iconYear'})
    # Print the active years
    print("\nYears Active (From-To):\t", active_years.getText(), "-\n")

    # Find the div with the class 'avgRating' which contains the anime rating
    rating = soup.find('div', {'class': 'avgRating'})
    # Extract and print the rating
    print("Rating: ", rating.find('span').getText())

    # Find the div with the class 'tags' which contains the tags related to the anime
    tags = soup.find('div', {'class': 'tags'})

    # Create a list to store the tags
    tag_list = []
    for _ in range(4):
        tag_list.append(tags.find('ul').getText())

    # Print the tags
    print("\nTags:\n")
    print((tag_list[0].replace("\n", "  ")))

def entry():
    """
    Prompts the user for the anime name, constructs the search URL,
    fetches the HTML content, and parses it using BeautifulSoup.
    """
    print("\nType the complete name of the anime>>\n")
    anime_name = input("Enter the name of the anime: ")
    # Format the anime name for the URL
    anime_name = (" ".join(anime_name.split())).title().replace(" ", "-")

    # Print the formatted anime name
    print("\n")
    print(anime_name)

    # Construct the search URL for the anime on Anime-Planet
    search_url = ("https://www.anime-planet.com/anime/" + anime_name)
    # Send a GET request to the search URL
    source_code = requests.get(search_url)
    # Get the content of the response
    content = source_code.content
    global soup
    # Parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(content, features="html.parser")

    try:
        # Call the details function to extract and print the anime details
        details(soup)
    except AttributeError:
        # Handle the case where the anime information is not found
        print("Anime info not found")

# If the script is run directly, call the entry function
if __name__ == "__main__":
    entry()
