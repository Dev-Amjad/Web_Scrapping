from bs4 import BeautifulSoup
import requests
from csv import writer



def get_all_Categories_link(url):
    Home_page = requests.get(url)
    content = Home_page.content
    Home_soup = BeautifulSoup(content, "html.parser")
    categories = Home_soup.find_all('a', class_='bbc-puhg0e e1ibkbh73')
    return categories

def check_For_Video_Section(s):
    if s=="/urdu/media/video":
        return True
    else:
        False

def get_links_of_all_items_on_page(str):
    page = requests.get(str)
    soup = BeautifulSoup(page.text, "html.parser")
    link_soup = soup.select('.bbc-uk8dsi.emimjbx0', )
    links = []
    for i in link_soup:
        links.append(i['href'])

    return links

def get_category_of_the_item(url):
    type=url.text
    return type

def get_data_of_an_item_as_row(url,category):
    row = ['Headline','Category','Story']
    req = requests.get(url)
    soup = BeautifulSoup(req.text, "html.parser")
    try:
        blog = soup.select('.e1j2237y4.bbc-1n11bte.essoxwk0')[0]
        headline = blog.select('.bbc-1pfktyq.essoxwk0')[0].text
        body_soup = blog.select('.bbc-4wucq3.essoxwk0')
    except:
        return row

    body_text = []
    for p in body_soup:
        body_text.append(p.text)

    body_text = ' '.join(body_text)

    row=[headline,type,body_text]
    return row

def parse_and_write_data():

    url = "https://www.bbc.com/urdu"
    categories = get_all_Categories_link(url)

    # Creating a CSV file in which we store the data
    with open('News.csv', 'w', encoding='utf8', newline='') as f:
        theWriter = writer(f)
        header = ['Headline', 'Category', 'Story']
        theWriter.writerow(header)

        for category in categories:
            page_Number = 1
            count_Stories = 0
            not_Hundred = True

            while not_Hundred:

                if check_For_Video_Section(category['href']):
                    break;

                page_link = str(str("https://www.bbc.com") + str(category['href']) + "?page=" + str(page_Number))
                links = get_links_of_all_items_on_page(page_link)

                for link in links:
                    type = get_category_of_the_item(category)
                    row = get_data_of_an_item_as_row(link, type)
                    theWriter.writerow(row)
                    count_Stories += 1
                    print(str(count_Stories))

                    if count_Stories == 100:
                        not_Hundred = False
                        break

                page_Number += 1


    return None









