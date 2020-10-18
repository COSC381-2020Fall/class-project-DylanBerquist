import pprint
import json
from googleapiclient.discovery import build
import config

my_api_key = config.my_api_key
my_cse_id = config.my_cse_id
my_search_topic = 'No Vacation'

def google_search(search_term, api_key, cse_id, **kwargs):
    service = build("customsearch", "v1", developerKey = api_key)
    res = service.cse().list(q = search_term, cx = cse_id, **kwargs).execute()
    return res['items']

if __name__ == '__main__':
    with open('google_search.json', 'w') as f:
        for i in range(10):
            results = google_search(my_search_topic, my_api_key, my_cse_id, num = 10, start = (i*10))
            json.dump(results, f)
