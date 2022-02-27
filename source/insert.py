from pprint import pprint
from sys import api_version
from Google import Create_Service, convert_to_RFC_datetime

def main(assignment, day, month):
    USER_SECRET_FILE = "USER_SECRET_FILE.json"
    API_NAME = "calendar"
    api_version = "v3"
    SCOPES = ["https://www.googleapis.com/auth/calendar"]
    service = Create_Service(USER_SECRET_FILE, API_NAME, api_version , SCOPES)

    print(dir(service))

    request_body = {
        'summary' : 'Homework due dates' # calendar title
    }

    # creating calendar
    response = service.calendars().insert(body=request_body).execute()
    print(response)


    #to delete a calendar
    #service.calendars().delete(calendarid='kp4vd4elble7dek1468o27spf8@group.calendar.google.com').execute()

    # calendar_id = 'kp4vd4elble7dek1468o27spf8@group.calendar.google.com'
    calendar_id = response['id']
    # print(calendar_id)

    # Create an event
    colors = service.colors().get().execute()
    pprint(colors)


    event_request_body = {
    'start': {
        'dateTime': '2022-' + str(month) + ' - ' + str(day) + 'T09:00:00-07:00',
        'timeZone': 'America/Montreal',
    },
    'end': {
        'dateTime': '2022-'+ str(month) +'-' + str(day) + 'T17:00:00-07:00',
        'timeZone': 'America/Montreal',
    },
        'summary': assignment,      # Assignment title
        'colorId' : 5,
        'status' : 'confirmed',
        'transparency' : 'opaque',
        'visibility' : 'private',
        'location' : 'Montreal, QC',
        'organizer' : {
            'id': 'McGill'          # Include Class Code here to identify then class
        }

    }

    response = service.events().insert(  
        calendarId = calendar_id,
        body = event_request_body).execute()

    pprint(response)

# if __name__ == "__main__":
#     inputs = sys.argv[1:4]
#     main(inputs[0], inputs[1], inputs[2])