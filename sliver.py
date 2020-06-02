#!/usr/bin/env python3

from bs4 import BeautifulSoup
import urllib.request as urllib
from datetime import datetime, timedelta
from apiclient.discovery import build
from google.oauth2 import service_account

response = urllib.urlopen('https://www.sliverpizzeria.com/menu-weekly')
html = response.read()
soup = BeautifulSoup(html, features="html.parser")
weekly = soup.find_all("div", {"class": "summary-excerpt"})
telegraph = weekly[:7]
shattuck = weekly[7:14]

scopes = ['https://www.googleapis.com/auth/calendar']
SERVICE_ACCOUNT_FILE = '' ## ENTER PATH TO SERVICE ACCOUNT JSON FILE
SUBJECT = '' ## ENTER CALENDAR ID
credentials = service_account.Credentials.from_service_account_file(SERVICE_ACCOUNT_FILE, scopes=scopes)
delegated_credentials = credentials.with_subject(SUBJECT)
service = build('calendar', 'v3', credentials=delegated_credentials)

calendar_list_entry = {
    'id': '' ## ENTER CALENDAR ID
}

result = service.calendarList().insert(body=calendar_list_entry).execute()

my_calendar = service.calendarList().list().execute()['items'][0]


def createTelegraphEvent(start_time, end_time):
    event_telegraph = {
      'summary': 'Sliver at Telegraph',
      'description': 'Potatoes at Telegraph!',
      'start': {
        'dateTime': start_time.strftime("%Y-%m-%dT%H:%M:%S"),
        'timeZone': 'America/Los_Angeles',
      },
      'end': {
        'dateTime': end_time.strftime("%Y-%m-%dT%H:%M:%S"),
        'timeZone': 'America/Los_Angeles',
      },
      'reminders': {
        'useDefault': False,
        'overrides': [
          {'method': 'email', 'minutes': 24 * 60},
          {'method': 'popup', 'minutes': 10},
        ],
      },
    }
    event = service.events().insert(calendarId='    ## ENTER CALENDAR ID    ', body=event_telegraph).execute()
    # print('Event created: %s' % (event.get('htmlLink')))



def createShattuckEvent(start_time, end_time):
    event_shattuck = {
      'summary': 'Sliver at Shattuck',
      'description': 'Potatoes at Shattuck!',
      'start': {
        'dateTime': start_time.strftime("%Y-%m-%dT%H:%M:%S"),
        'timeZone': 'America/Los_Angeles',
      },
      'end': {
        'dateTime': end_time.strftime("%Y-%m-%dT%H:%M:%S"),
        'timeZone': 'America/Los_Angeles',
      },
      'reminders': {
        'useDefault': False,
        'overrides': [
          {'method': 'email', 'minutes': 24 * 60},
          {'method': 'popup', 'minutes': 10},
        ],
      },
    }
    event = service.events().insert(calendarId='   ## ENTER CALENDAR ID     ', body=event_shattuck).execute()
    # print('Event created: %s' % (event.get('htmlLink')))



for i in range(2,7):
    start_time = datetime.combine(datetime.now().date(),datetime.min.time()) + timedelta(days=(i-1)) + timedelta(hours=11)
    end_time = start_time + timedelta(hours=10)
    if "Roasted Yukon Gold Potatoes" in telegraph[i].text:
        createTelegraphEvent(start_time, end_time)

    if "Roasted Yukon Gold Potatoes" in shattuck[i].text:
        createShattuckEvent(start_time, end_time)
