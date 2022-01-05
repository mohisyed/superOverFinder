import requests
from bs4 import BeautifulSoup
import re

cricketbuzz = "https://www.cricbuzz.com/"


def user_input():
    x = input("What year do u want to search for: ")
    return x


def get_links(user_input):
    cricketbuzz_input = "https://www.cricbuzz.com/cricket-scorecard-archives/" + user_input
    r_cricketbuzz = requests.get(cricketbuzz_input)
    soup = BeautifulSoup(r_cricketbuzz.text, "html.parser")

    today_div = soup.findAll("div", {"class": "cb-col-84 cb-col"})
    urls = re.findall(r'"(/cricket-series/\S*)"', str(today_div))
    return urls


def find_super_overs(urls):
    outcomes = []

    for url in urls:
        response = requests.get(cricketbuzz + url)
        html_file = BeautifulSoup(response.content, "html.parser")
        total_outcome = html_file.findAll("a", {"class": "cb-text-complete"})
        title = html_file.findAll("a", {"class", "text-hvr-underline"})
        for i in range(len(total_outcome)):
            outcomes.append(title[i].text + " : " + total_outcome[i].text)
            print(title[i].text + " : " + total_outcome[i].text)
    return outcomes


def super_over_counter(outcomes):
    super_over = []
    for item in outcomes:
        if 'super over' in item.lower():
            super_over.append(item)
    print(super_over)
    print(len(super_over))


super_over_counter(find_super_overs(get_links(user_input())))
