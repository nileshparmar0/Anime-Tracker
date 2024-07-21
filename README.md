# Anime-Tracker

Anime Information Scraper
This script is designed to extract and display information about a specific anime from the Anime-Planet website. By inputting the name of an anime, the script fetches and displays details such as the summary, total number of episodes, active years, rating, and tags associated with the anime.

Requirements
Before running the script, ensure you have the following Python packages installed:

1. requests
2. beautifulsoup4
3. argparse
4. You can install these packages using pip:

bash code:
pip install requests beautifulsoup4 argparse

Usage:
To run the script, simply execute the following command in your terminal:

bash code: 
python anime_scraper.py
You will be prompted to enter the name of the anime you wish to search for. Ensure that the name is complete and correctly spelled.

Script Details
1. Importing Required Modules:

The script imports necessary modules such as sys, requests, BeautifulSoup from bs4, urllib.parse as parse, re, and argparse.
If there is an error during the import, it prints an error message and exits.

2. Function Definitions:

details(soup): Extracts and prints information about the anime.
It finds and prints the anime summary, total number of episodes, active years, rating, and tags.
entry(): Prompts the user for the anime name, constructs the search URL, fetches the HTML content, and parses it using BeautifulSoup. It then calls the details() function to display the information.

Main Execution:

If the script is run directly, it calls the entry() function.
Example
Here’s an example of how the script works:

1. Run the script:

bash code:
python anime_scraper.py

2. When prompted, enter the name of the anime:

csharp code:
Enter the name of the anime : Attack on Titan

The script will output information about "Attack on Titan" if it is found on Anime-Planet.

Author: Nilesh Parmar
