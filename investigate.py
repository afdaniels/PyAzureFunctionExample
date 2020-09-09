import requests
from bs4 import BeautifulSoup
from urllib3 import ProxyManager, PoolManager, make_headers
import json
import time
import logging
from .Utils.data_access import *
from .Utils.tag_finders import *


def start():
    url = ''

    some_data = get_some_data()

    for data in some_data:
        retries = 12
        status = 200

        while True:
            retries = retries - 1
            r = requests.get(url+some_data['column1'])

            logging.info(str(retries) + ' Status : ' + str(r.status_code))

            if r.status_code == 200:
                break
            if retries == 0:
                break
            time.sleep(.4)

        content = r.content
        soup = BeautifulSoup(content,features="html.parser")

        if r.status_code == 200:
            name = find_name(soup)
            address = find_address(soup)
        elif r.status_code == 404:
            logging.info('404 code')
        else:
            notes = 'complete failure'

        data = {'Columns1': name, 'Notes': address}

        logging.info(data)

        insert_some_data(data)
        
        time.sleep(4)

    return 'worked'

