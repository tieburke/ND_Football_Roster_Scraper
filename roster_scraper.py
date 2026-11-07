#!/usr/bin/env python3

import requests
import re
import concurrent.futures
import sys

def create_player(row: str) -> [str, dict[str: str]]:
    """
    Returns a tuple with the player name and his attributes as a dictionary
    
    I will run this concurrently later after splitting the html into a block for each player
    """

    # Need the 'player' so that I don't also get coaches
    name = re.search(r'/player/[^<]*<span>([^<]*)<', row)
    
    if not name:
        return None

    # Iterable of all the players attributes
    attributes = re.finditer(r'<span data-v-75a7079f>([^<]*)<', row)
   
    # Order of the attributes
    attribute_keys = ['Number', 'Position', 'Height', 'Weight', 'Class', 'Hometown', 'High School']

    try:
        attribute_dict = {key : next(attributes)[1] for key in attribute_keys}
    except StopIteration:
        return None

    return (name[1], attribute_dict)


def main():
    # Get the site html
    ROSTER_URL = 'https://fightingirish.com/sports/football/roster'
    response = requests.get(ROSTER_URL)

    # All the information for a given player is in these blocks
    player_blocks = re.findall(r'<tbody\b[^>]*>(.*?)</tbody>', response.text, re.DOTALL)

    # Go through these blocks concurrently and create a new dictionary that maps names to attributes
    with concurrent.futures.ProcessPoolExecutor() as executor:
        results = executor.map(create_player, player_blocks)
        player_data = {player[0] : player[1] for player in results if player is not None}

    for player, data in player_data.items():
        print(f'{player}')
        for key, value in data.items():
            print(f'   {key}: {value}')
        print()

if __name__ == '__main__':
    main()
