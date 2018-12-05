from bs4 import BeautifulSoup
import requests
import csv
from colorama import init, Fore, Back, Style
init(autoreset=True)

#option1
def home():
    source = requests.get('http://dailystormer.name').text

    soup = BeautifulSoup(source, 'lxml')

    csv_file = open('home.csv', 'w')

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

        csv_writer.writerow([headline_other, link_other, author_other, author_other_profile,])
    csv_file.close()
#option2
def world():
    source = requests.get('https://dailystormer.name/section/world/').text

    soup = BeautifulSoup(source, 'lxml')

    csv_file = open('world.csv', 'w')

    csv_writer = csv.writer(csv_file)
    csv_writer.writerow(['Post Title', 'Post Link', 'Author', 'Author Profile', 'Date'])

    for article in soup.find_all('article', class_="item-list"):
        headline_article = article.h2.a.text
        link_article = article.a["href"]
        author_article = article.find('span', class_="post-meta-author").a.text
        author_article_profile = article.find('span', class_="post-meta-author").a["href"]
        article_date = article.find('span', class_="tie-date").text
        print(headline_article)
        print(link_article)
        print(author_article)
        print(author_article_profile)
        print(article_date)
        print()

        csv_writer.writerow([headline_article, link_article, author_article, author_article_profile,article_date])
    csv_file.close()

def us():
    source = requests.get('https://dailystormer.name/section/us/').text

    soup = BeautifulSoup(source, 'lxml')

    csv_file = open('us.csv', 'w')

    csv_writer = csv.writer(csv_file)
    csv_writer.writerow(['Post Title', 'Post Link', 'Author', 'Author Profile', 'Date'])

    for article in soup.find_all('article', class_="item-list"):
        headline_article = article.h2.a.text
        link_article = article.a["href"]
        author_article = article.find('span', class_="post-meta-author").a.text
        author_article_profile = article.find('span', class_="post-meta-author").a["href"]
        article_date = article.find('span', class_="tie-date").text
        print(headline_article)
        print(link_article)
        print(author_article)
        print(author_article_profile)
        print(article_date)
        print()

        csv_writer.writerow([headline_article, link_article, author_article, author_article_profile, article_date])
    csv_file.close()

def jew():
    source = requests.get('https://dailystormer.name/section/jewish-problem/').text

    soup = BeautifulSoup(source, 'lxml')

    csv_file = open('jewishproblem.csv', 'w')

    csv_writer = csv.writer(csv_file)
    csv_writer.writerow(['Post Title', 'Post Link', 'Author', 'Author Profile', 'Date'])

    for article in soup.find_all('article', class_="item-list"):
        headline_article = article.h2.a.text
        link_article = article.a["href"]
        author_article = article.find('span', class_="post-meta-author").a.text
        author_article_profile = article.find('span', class_="post-meta-author").a["href"]
        article_date = article.find('span', class_="tie-date").text
        print(headline_article)
        print(link_article)
        print(author_article)
        print(author_article_profile)
        print(article_date)
        print()

        csv_writer.writerow([headline_article, link_article, author_article, author_article_profile, article_date])
    csv_file.close()

def race():
    source = requests.get('https://dailystormer.name/section/race-war/').text

    soup = BeautifulSoup(source, 'lxml')

    csv_file = open('racewar.csv', 'w')

    csv_writer = csv.writer(csv_file)
    csv_writer.writerow(['Post Title', 'Post Link', 'Author', 'Author Profile', 'Date'])

    for article in soup.find_all('article', class_="item-list"):
        headline_article = article.h2.a.text
        link_article = article.a["href"]
        author_article = article.find('span', class_="post-meta-author").a.text
        author_article_profile = article.find('span', class_="post-meta-author").a["href"]
        article_date = article.find('span', class_="tie-date").text
        print(headline_article)
        print(link_article)
        print(author_article)
        print(author_article_profile)
        print(article_date)
        print()

        csv_writer.writerow([headline_article, link_article, author_article, author_article_profile, article_date])
    csv_file.close()

def society():
    source = requests.get('https://dailystormer.name/section/society/').text

    soup = BeautifulSoup(source, 'lxml')

    csv_file = open('society.csv', 'w')

    csv_writer = csv.writer(csv_file)
    csv_writer.writerow(['Post Title', 'Post Link', 'Author', 'Author Profile','Date'])

    for article in soup.find_all('article', class_="item-list"):
        headline_article = article.h2.a.text
        link_article = article.a["href"]
        author_article = article.find('span', class_="post-meta-author").a.text
        author_article_profile = article.find('span', class_="post-meta-author").a["href"]
        article_date = article.find('span', class_="tie-date").text
        print(headline_article)
        print(link_article)
        print(author_article)
        print(author_article_profile)
        print(article_date)
        print()

        csv_writer.writerow([headline_article, link_article, author_article, author_article_profile, article_date])
    csv_file.close()

def insight():
    source = requests.get('https://dailystormer.name/section/insight/').text

    soup = BeautifulSoup(source, 'lxml')

    csv_file = open('insight.csv', 'w')

    csv_writer = csv.writer(csv_file)
    csv_writer.writerow(['Post Title', 'Post Link', 'Author', 'Author Profile', 'Date'])

    for article in soup.find_all('article', class_="item-list"):
        headline_article = article.h2.a.text
        link_article = article.a["href"]
        author_article = article.find('span', class_="post-meta-author").a.text
        author_article_profile = article.find('span', class_="post-meta-author").a["href"]
        article_date = article.find('span', class_="tie-date").text
        print(headline_article)
        print(link_article)
        print(author_article)
        print(author_article_profile)
        print(article_date)
        print()

        csv_writer.writerow([headline_article, link_article, author_article, author_article_profile, article_date])
    csv_file.close()

#engage dashboard
def menu():
    print(Fore.BLUE + """       _____ _                    _______
      / ____| |                  |__   __|
     | (___ | |_ ___  _ __ _ __ ___ | |_ __ ___   ___  _ __   ___ _ __
      \___ \| __/ _ \| '__| '_ ` _ \| | '__/ _ \ / _ \| '_ \ / _ | '__|
      ____) | || (_) | |  | | | | | | | | | (_) | (_) | |_) |  __| |
     |_____/ \__\___/|_|  |_| |_| |_|_|_|  \___/ \___/| .__/ \___|_|
                                                      | |
                                                      |_|              """)

    print(Fore.YELLOW + '                       A DailyStormer OSINT Scraper')
    print(Fore.CYAN + '                          Exports results to csv')
    print()
    print(Fore.YELLOW + ' [!]' + Fore.CYAN + ' Menu')
    print(Fore.YELLOW + '    [1]' + Fore.BLUE + ' Scrape the home page of DailyStormer.name')
    print(Fore.YELLOW + '    [2]' + Fore.BLUE + ' Scrape the world page of DailyStormer.name')
    print(Fore.YELLOW + '    [3]' + Fore.BLUE + ' Scrape the US page of DailyStormer.name')
    print(Fore.YELLOW + '    [4]' + Fore.BLUE + ' Scrape the Jewish Problem page of DailyStormer.name')
    print(Fore.YELLOW + '    [5]' + Fore.BLUE + ' Scrape the Race War page of DailyStormer.name')
    print(Fore.YELLOW + '    [6]' + Fore.BLUE + ' Scrape the Society page of DailyStormer.name')
    print(Fore.YELLOW + '    [7]' + Fore.BLUE + ' Scrape the Insight page of DailyStormer.name')
    print(Fore.YELLOW + '    [8]' + Fore.BLUE + ' Exit')
menu()
input = int(input())
def engage():
    if input == 1:
        home()
    elif input == 2:
        world()
    elif input == 3:
        us()
    elif input == 4:
        jew()
    elif input == 5:
        race()
    elif input == 6:
        society()
    elif input == 7:
        insight()
    elif input == 8:
        exit()
engage()

print(Fore.BLUE + 'Thanks for hunting Nazis with StormTrooper! Follow me on Twitter @jakecreps.')
print()
