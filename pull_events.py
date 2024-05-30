import requests
import os
import base64
from datetime import datetime, timedelta
import pytz
import json

def log_dump(client, token, base_url, realm, event, days):
    url = base_url + "/auth/realms/" + realm + "/protocol/openid-connect/token"
    payload = "grant_type=client_credentials"
    auth_str = client + ":" + token
    basic_hash = base64.b64encode(auth_str.encode()).decode()
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded',
        'Authorization': f'Basic {basic_hash}'
    }

    response = requests.request("POST", url, headers=headers, data=payload)

    token = response.json()['access_token']

    headers = {
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {token}',
    }

    base_url2 = base_url + "/auth/admin/realms/" + realm

    max_val = 100000
    pst = pytz.timezone('US/Pacific')
    t = datetime.now(pst)
    d = timedelta(days=1)
    day = 0
    from_date = t - d
    to_date = t
    print("processing log events...")
    while day < days:
        url = base_url2 + "/events?type=" + event + "&" + "dateFrom=" + from_date.strftime('%Y-%m-%d') + "&dateTo=" + to_date.strftime('%Y-%m-%d') + "&max=" + str(max_val)
        user_resp = requests.request("GET", url, headers=headers)
        if user_resp.status_code == 200:
            with open('events_' + from_date.strftime('%Y-%m-%d') + '.jsonl', 'w') as f:
                res_json = user_resp.json()
                for e in res_json:
                    json.dump(e, f)
                    f.write('\n')
                day += 1
                f.close()
            to_date = from_date
            from_date = from_date - d

if __name__ == '__main__':
    client = os.environ['CLIENT_NAME']
    token = os.environ['CLIENT_TOKEN']
    base_url = os.environ['KEYCLOAK_URL']
    realm = os.environ['KEYCLOAK_REALM']
    event = os.environ['EVENT_NAME']
    days = int(os.environ['DAYS'])
    log_dump(client, token, base_url, realm, event, days)
