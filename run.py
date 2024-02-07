from algoliasearch.search_client import SearchClient
import params
import helper
import pandas as pd

client = SearchClient.create(params.YourApplicationID, params.YourAPIKEY)
index = client.init_index(params.INDEX)

def main():
    items = []
    page_num = 0
    while True:
        print(f'Page: {page_num}')
        search_params = {
            'page': page_num,
            "hitsPerPage": 100,
        }
        results = index.search('', search_params)
        hits = results['hits']
        print(f'Total hits: {len(hits)}')
        for hit in hits:
            item = helper.extract_data(hit)
            items.append(item)
        if results['page'] == results['nbPages']:
            break
        else:
            page_num += 1
    return items

if __name__ == '__main__':
    items = main()
    df = pd.DataFrame(items)
    df.to_excel('nationalhardwareshow.xlsx', index=False)
    