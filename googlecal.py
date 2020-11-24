from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
import pickle
from datetime import datetime, timedelta
import datefinder

# users can read/write on the entire calendar
# maybe change to https://www.googleapis.com/auth/calendar.events.readonly 
# so users can just see the events in a calendar
scopes = ['https://www.googleapis.com/auth/calendar']
flow = InstalledAppFlow.from_client_secrets_file("client_secret2.json", scopes=scopes)
# credentials = flow.run_console()

# pickle.dump(credentials, open("token.pkl", "wb"))

credentials = pickle.load(open("token.pkl", "rb"))


service = build("calendar", "v3", credentials=credentials)

calendars = service.calendarList().list().execute()

calendar_id = calendars['items'][0]['id']

# all events on OMH calendar
# result = service.events().list(calendarId=calendar_id).execute()


def add_evt_to_cal(start_time_str, name_evt, business, duration=1, description=None):
    matches = list(datefinder.find_dates(start_time_str))
    if len(matches):
        start_time = matches[0]
        end_time = start_time + timedelta(hours=duration)

    event = {
    'summary': name_evt,
    'location': business,
    'description': description,
    'start': {
        'dateTime': start_time.strftime("%Y-%m-%dT%H:%M:%S"),
        'timeZone': 'America/Chicago',
    },
    'end': {
        'dateTime': end_time.strftime("%Y-%m-%dT%H:%M:%S"),
        'timeZone': 'America/Chicago',
    },
    'recurrence': [
        'RRULE:FREQ=WEEKLY;COUNT=1'
    ],
    'reminders': {
        'useDefault': False,
        'overrides': [
        {'method': 'email', 'minutes': 24 * 60},
        {'method': 'popup', 'minutes': 10},
        ],
    },
    }

    return service.events().insert(calendarId=calendar_id, body=event).execute()

add_evt_to_cal("5 december 10am", "checking python code", "Harvey Yoga")

print("event added!")