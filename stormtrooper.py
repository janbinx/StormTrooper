from bs4 import BeautifulSoup
import requests
import csv
from colorama import init, Fore, Back, Style
init(autoreset=True)

def get_subsection(subsection):
    csv_file_name = '{}.csv'.format(subsection)
    with open(csv_file_name, 'w', newline='') as csv_file: # with statement handles both open and close
        csv_writer = csv.writer(csv_file)
        csv_writer.writerow(['Post Title', 'Post Link', 'Author', 'Author Profile', 'Date'])

        if subsection == "home": # one url for the home section
            url = 'http://dailystormer.name'
        else: # another one for all subsections
            url = 'https://dailystormer.name/section/{}/'.format(subsection)
        
        # set header - else you're posing as python/requests, which is not very stealth...
        header = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36'}
        r = requests.get(url, headers=header)
        source = r.content.decode('utf-8') # using .text causes my machine to decode using cp1252, which is wrong
        soup = BeautifulSoup(source, 'lxml')
        
        # home has a row that Jake wants - this doesn't appear in the others sections
        if subsection == "home":
            first = soup.find('li', class_="first-news")
            headline_first = first.h2.a.text
            link_first = first.a["href"]
            author_first = first.find('span', class_="post-meta-author").a.text
            author_first_profile = first.find('span', class_="post-meta-author").a["href"]
            print(headline_first)
            print(link_first)
            csv_writer.writerow([headline_first, link_first, author_first, author_first_profile])        
            # home has articles in 'other-news'-class
            articles = soup.find_all('li', class_="other-news")
        
        else: # all other subsections has atciles in 'item-list'
            articles = soup.find_all('article', class_="item-list")
    
        for article in articles:
            if subsection == "home": # home has the headline in h2
                headline_article = article.h3.a.text
            else:
                headline_article = article.h2.a.text # all other subsections has headline in h2
            link_article = article.a["href"]
            author_article = article.find('span', class_="post-meta-author").a.text
            author_article_profile = article.find('span', class_="post-meta-author").a["href"]
            try:
                article_date = article.find('span', class_="tie-date").text
            except: # these are not present in the home-subsection
                article_date = None
            print(headline_article)
            print(link_article)
            print(author_article)
            print(author_article_profile)
            print(article_date)
            print()
            csv_writer.writerow([headline_article, link_article, author_article, author_article_profile,article_date])
            
def bearjew():
    subsections = ['home', 'world', 'us', 'jewish-problem', 'race-war', 'society', 'insigth']
    for subsection in subsections:
        get_subsection(subsection)
    return None


def engage():
    if input == 1:
        get_subsection('home')
    elif input == 2:
        get_subsection('world')
    elif input == 3:
        get_subsection('us')
    elif input == 4:
        get_subsection('jewish-problem')
    elif input == 5:
        get_subsection('race-war')
    elif input == 6:
        get_articles('society')
    elif input == 7:
        get_articles('insigth')
    elif input == 11:
        bearjew()
    elif input == 0:
        exit()

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
    print(Fore.YELLOW + '    [11]' + Fore.BLUE + ' Unleash the Bear Jew')
    print(Fore.YELLOW + '    [0]' + Fore.BLUE + ' Exit')

menu()
input = int(input())
engage()
print(Fore.BLUE + 'Thanks for hunting Nazis with StormTrooper! Follow me on Twitter @jakecreps.')
print()