from typing import Dict
import json as _json


def get_all_data_services() -> Dict:
    """Get all the data"""
    with open('data.json', encoding='utf-8') as f:
        data = _json.load(f)
    return data['result_data']


def get_list_data():
    """Get one data"""
    with open('data.json', encoding='utf-8') as f:
        data = _json.load(f)
        data_list = []
        for result in data['result_data']:
            data_list.append(result)
    return data_list

