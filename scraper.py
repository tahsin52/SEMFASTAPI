import json
from typing import List
import requests
from bs4 import BeautifulSoup
import json as _json


def get_page_length(url) -> int:
    """Get the page length"""
    page = requests.get(str(url))
    soup = BeautifulSoup(page.content, 'html.parser')
    data = soup.find('nav', class_='sds-pagination').find_all('li', class_='sds-pagination__item')

    return len(data)


def _generate_url() -> list:
    """Generate the URL"""
    data = get_page_length('https://www.cars.com/shopping/results/')

    list_url = []

    for i in range(data+1):
        if i == 0:
            url = 'https://www.cars.com/shopping/results/'
            list_url.append(url)
        else:
            url = f'https://www.cars.com/shopping/results/?page=' + str(i)
            list_url.append(url)

    return list_url


def _get_page(url: str) -> BeautifulSoup:
    """Get the page"""
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    return soup

# def get_Transmission():
#     """Get the Transmission"""
#     data_list = []
#     for data in get_all_data():
#         transmissions = data['listing_id']
#         url = f'https://www.cars.com/vehicledetail/{transmissions}/'
#         soup = _get_page(url)
#         transmission = soup.find_all('dd')[5].text
#
#         data_list.append({'listing_id': transmissions, 'transmission': transmission})
#         session.commit()
#     return data_list


def get_all_data() -> List:
    """Get all the data"""
    all_data = []
    for url in _generate_url():
        soup = _get_page(url)
        data = soup.find('div', class_='sds-page-section listings-page')['data-site-activity']
        result = _json.loads(data)['vehicleArray']
        all_data.extend(result)
    return all_data

