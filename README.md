# Notre Dame Football Roster Scraper

A python script that scrapes ND football's roster and prints each players name, number, position, height, weight, class, hometown, and high school.

### Usage:
```bash
python3 roster_scraper.py
```
No command line arguments are needed.


<img width="976" height="1098" alt="image" src="https://github.com/user-attachments/assets/5e103b96-88d5-4303-9182-fe98bdcde16d" />

### Functional Programming and Concurrent Features
*ProcessPoolExecutor().map* from *concurrent.futures* is used to scrape each block of code containing player data concurrently.
Dictionary comprehension is also used twice in organization of player data.
