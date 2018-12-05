from bs4 import BeautifulSoup
import requests
import csv
from colorama import init, Fore, Back, Style
init(autoreset=True)

print(Fore.BLUE + """   _____ _                    _______
  / ____| |                  |__   __|
 | (___ | |_ ___  _ __ _ __ ___ | |_ __ ___   ___  _ __   ___ _ __
  \___ \| __/ _ \| '__| '_ ` _ \| | '__/ _ \ / _ \| '_ \ / _ | '__|
  ____) | || (_) | |  | | | | | | | | | (_) | (_) | |_) |  __| |
 |_____/ \__\___/|_|  |_| |_| |_|_|_|  \___/ \___/| .__/ \___|_|
                                                  | |
                                                  |_|              """)

print (Fore.MAGENTA + 'A DailyStormer OSINT Scraper')
print (Fore.MAGENTA + 'Exports results to csv')
def stormtrooper():
    source = requests.get('http://dailystormer.name').text

    soup = BeautifulSoup(source, 'lxml')

    csv_file = open('stormtrooper.csv', 'w')

    csv_writer = csv.writer(csv_file)
    csv_writer.writerow(['Post Title', 'Post Link', 'Author', 'Author Profile'])

    first = soup.find('li', class_="first-news")

    def featured():
        headline_first = first.h2.a.text
        link_first = first.a["href"]
        author_first = first.find('span', class_="post-meta-author").a.text
        author_first_profile = first.find('span', class_="post-meta-author").a["href"]
        print(headline_first)
        print(link_first)
        csv_writer.writerow([headline_first, link_first, author_first, author_first_profile])
    featured()


    for other in soup.find_all('li', class_="other-news"):
        headline_other = other.h3.a.text
        link_other = other.a["href"]
        author_other = other.find('span', class_="post-meta-author").a.text
        author_other_profile = other.find('span', class_="post-meta-author").a["href"]
        print(headline_other)
        print(link_other)
        print(author_other)
        print(author_other_profile)
        print()

        csv_writer.writerow([headline_other, link_other, author_other, author_other_profile])
    csv_file.close()
def engage():
    print (Fore.BLUE + '[1] Scrape the home page of DailyStormer.name')
    next_input = input()
    if next_input == "1":
        stormtrooper()
    else:
        engage()
print (Fore.BLUE + '[1] Scrape the home page of DailyStormer.name')
input = input()
if input == "1":
    stormtrooper()
elif input != "1":
    engage()
