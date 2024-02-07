import httpx
from time import sleep

def get_address(item: dict, hit):
    eventId = hit['eventEditionExternalId']
    orgId = hit['organisationGuid']
    url = f"https://api.reedexpo.com/v1/organisations/{orgId}/exhibiting-organisations"
    print(f'Scraping address of: {url}')
    querystring = {"eventEditionId":eventId}

    payload = ""
    headers = {
        "cookie": "__cf_bm=4cTeSdK5CqlLDTrDtAfOD2Pruqb0h2ad6tvrGVeS5z4-1706876209-1-AU3bNLMR1LW3gLPWGpSmNoE6MTs%2F7peijAT7PZLAqJzh9rsZnHMOk0E0L3dnV4BGAUcTFelCvF8wUAW7Z7efNYU%3D",
        "authority": "api.reedexpo.com",
        "accept": "application/json",
        "accept-language": "en-US,en;q=0.9",
        "origin": "https://www.nationalhardwareshow.com",
        "referer": "https://www.nationalhardwareshow.com/",
        "sec-ch-ua": '"Not A(Brand";v="99", "Microsoft Edge";v="121", "Chromium";v="121"',
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": '"Windows"',
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "cross-site",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36 Edg/121.0.0.0",
        "x-clientid": "uhQVcmxLwXAjVtVpTvoerERiZSsNz0om",
        "x-correlationid": "ece76209-4a51-4046-840a-26d251a6c030"
    }
    
    for i in range(10):
        try:
            response = httpx.get(url, headers=headers, params=querystring)
            break
        except:
            print('retrying....')
            sleep(5)
    json_data = response.json()['_embedded'][0]
    address = json_data['multilingual'][0]['address']
    for adr in address:
        item[adr] = address[adr]
    return item

def extract_data(hit):
    item = {}
    item['company_name'] = hit['name']
    item['brand_name'] = ', '.join(hit['representedBrands'])
    item['booth_number'] = hit['standReference']
    item['domain'] = hit['website']
    item = get_address(item, hit)
    return item

