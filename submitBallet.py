#!/usr/local/bin/python3.4
import requests
import json

emails = [

]

def submit_ballet(email):

    url = 'https://embed-216467.secondstreetapp.com/api/form_page_submissions'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.63 Safari/537.36',
        'Content-Type': 'application/json; charset=UTF-8',
        'Cookie': 'i18next=en-US',
        'X-Api-Key': '65032887',
        'X-Organization-Id': '1686',
        'X-Organization-Promotion-Id': '216467',
        'X-Promotion-Id': '166928',
        'X-Referring-Url': 'http://www.popularwoodworking.com/winshop',
        'X-Requested-With': 'XMLHttpRequest',
    }
    cookies = {
        'i18next': 'en-US'
    }
    payload = {
        "form-page-submissions": [
            {
                "referrer": None,
                "form_submission_id": None,
                "fields": [
                    {
                        "field_id": 39,
                        "field_value": email
                    },
                    {
                        "field_id": 41475,
                        "field_value": ""
                    }
                ],
                "form_page_id": 200732,
                "form_id": "171694",
                "next_form_page_id": None,
                "sessions": None,
                "matchup_id": "438147"
            }
        ]
    }

    resp = requests.post(url, data=json.dumps(payload), headers=headers, cookies=cookies)

    print("* status", resp.status_code );
    # print("## headers")
    # print( resp.headers );
    # print("## resp body")
    # print( json.dumps(resp.json(), indent=2));

def main():
    for email in emails:
        print()
        print("Submitting ", email)
        submit_ballet(email)

# Kick this off
main();