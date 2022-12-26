from typing import Dict
import scraper
import json as _json


def create_events_dict() -> Dict:
    events = {}
    result_data = []
    for data in scraper.get_all_data():
        result_data.append(data)
    events['result_data'] = result_data
    return events


def write_json():
    events = create_events_dict()
    with open(f'data.json', 'w', encoding='utf-8') as f:
        _json.dump(events, f, indent=4, ensure_ascii=False)


