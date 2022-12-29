from typing import Dict
import scraper
import json as _json
import scraper


def create_events_dict() -> Dict:
    events = {}
    result_data = []
    for data in scraper.get_all_data():
        result_data.append(data)
    events['result_data'] = result_data
    return events


async def write_json():
    events = create_events_dict()
    for event in events['result_data']:
        url = f'https://www.cars.com/vehicledetail/' + event['listing_id'] + '/'
        soup = scraper._get_page(url)
        transmission = soup.find_all('dd')[5].text
        try:
            event['transmission'] = transmission
        except IndexError:
            continue
        with open(f'data.json', 'w', encoding='utf-8') as f:
            _json.dump(events, f, indent=4, ensure_ascii=False)


