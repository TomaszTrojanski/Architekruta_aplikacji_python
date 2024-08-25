from typing import Final
import threading
import logging
import requests

logging.basicConfig(level=logging.INFO)


def get_data_from_api(api_url: str, country: str, storage_dict: dict) -> list:
    data = requests.get(f'{api_url}/search?country={country}')
    if data.status_code != 200:
        raise Exception('Could not retrieve data')
    storage_dict[country] = [university.get('name') for university in data.json()]


def main() -> None:
    API_URL: Final = 'http://universities.hipolabs.com'
    countries = ['Poland', 'Czechia', 'Slovakia', 'Sweden', 'Italy', 'Germany', 'France', 'Spain', 'Ireland',
                 'United Kingdom', 'Croatia', 'United States', 'Portugal', 'Norway', 'Finland']
    tasks = []
    data = {}

    for c in countries:
        task = threading.Thread(target=get_data_from_api, args=(API_URL, c, data))
        tasks.append(task)
        task.start()

    for thread in tasks:
        thread.join()

    print(data)


if __name__ == '__main__':
    main()
