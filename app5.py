from xml.etree import ElementTree
from typing import Final
import requests


def main() -> None:
    API_URL: Final[str] = 'https://www.w3schools.com/xml/cd_catalog.xml'
    data = requests.get(API_URL).content
    cds: list[tuple[str, str]] = []

    et = ElementTree.fromstring(data)

    for n in et.findall('CD'):
        artist = n.find('ARTIST').text
        title = n.find('TITLE').text
        cds.append((artist, title))
    print(cds)


if __name__ == '__main__':
    main()
