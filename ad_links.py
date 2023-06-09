import requests
from bs4 import BeautifulSoup
#import TestSinglePage


def get_ad_links():
    links = []
    url_template = 'https://www.olx.pl/motoryzacja/samochody/?page={}'
    for page_num in range(1, 2):
        url = url_template.format(page_num)
        response = requests.get(url)
        soup = BeautifulSoup(response.content, "html.parser")

        links = []

        for div in soup.find_all("div", {"data-cy": "l-card"}):
            link = div.find("a")["href"]
            if '/d/' in link:
                links.append(link)

        for i in range(len(links)):
            links[i] = 'https://www.olx.pl' + links[i]

    return links

    #
    # for link in links:
    #     brand, model, year, mileage, engine_size, horse_power = TestSinglePage.scrapeOlx(link)
    #     results.append((brand, model, year, mileage, engine_size, horse_power))
    #
    # for result in results:
    #     print(result)

print(get_ad_links())