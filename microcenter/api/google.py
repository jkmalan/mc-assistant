from oauth2client import client
from googleapiclient.discovery import build

from microcenter import config

credential = client.AccessTokenCredentials(config.GOOGLE_ACCESS_KEY, config.GOOGLE_USER_AGENT)
service = build('calendar', 'v3', credentials=credential)


def get(calendar_id):
    result = service.calendars().get(calendar_id)
    return calendar_wrap(result)


def add(calendar):
    body = {
        'kind': calendar.kind,
        'description': calendar.description,
        'summary': calendar.summary,
        'timezone': calendar.timezone
    }
    service.calendars().insert(body)


class Calendar(object):
    id = ''
    kind = 'calendar#calendar'
    description = ''
    summary = ''
    timezone = ''

    def get(self, event_id):
        result = service.events().get(self.id, event_id)

    def add(self, event):
        body = {
            'id': event.id,
            'kind': event.kind,
            'description': event.description,
            'summary': event.summary,
            'status': event.status,
            'colorId': event.color,
            'location': event.location,
            'start': {
                'date': event.start.date,
                'timeZone': event.start.timezone,
                'dateTime': event.start.datetime
            },
            'end': {
                'date': event.end.date,
                'timeZone': event.end.timezone,
                'dateTime': event.end.datetime
            },
            'creator': event.creator,
            'organizer': event.organizer,
            'attendees': event.attendees,
            'source': {
                'url': event.source.url,
                'title': event.source.title
            },
            'visibility': event.visible,
            'created': event.created_on,
            'updated': event.updated_on
        }
        service.events().insert(self.id, body, sendUpdates=event.updated_notify)


class Event(object):

    id = ''
    kind = 'calendar#event'
    description = ''
    summary = ''
    status = ''
    color = ''
    location = ''
    start = {
        'date': 'yyyy-mm-dd',
        'timezone': 'Continent/Region',
        'datetime': 'yyyy-mm-dd hh:mm:ss'
    }
    end = {
        'date': 'yyyy-mm-dd',
        'timezone': 'Continent/Region',
        'datetime': 'yyyy-mm-dd hh:mm:ss'
    }
    creator = {
        'self': True,
        'displayName': '',
        'email': '',
        'id': ''
    }
    organizer = {
        'self': True,
        'displayName': '',
        'email': '',
        'id': ''
    }
    attendees = []
    source = {
        'url': '',
        'title': ''
    }
    visible = ''
    created_on = ''
    updated_on = ''
    updated_notify = None

    def add_attendee(self, attendee_name, attendee_email, attendee_id):
        attendee = {
            'responseStatus': 'needsAction',
            'displayName': attendee_name,
            'email': attendee_email,
            'id': attendee_id
        }
        self.attendees.append(attendee)


def calendar_wrap(result):
    calendar = Calendar()
    calendar.id = result.id
    calendar.kind = result.kind
    calendar.description = result.description
    calendar.summary = result.summary
    calendar.timezone = result.timeZone
    return calendar


def event_wrap(result):
    event = Event()
    event.id = result.id
    event.kind = result.kind
    event.description = result.description
    event.summary = result.summary
    event.status = result.status
    event.color = result.colorId
    event.location = result.location
    event.start.date = result.start.date
    event.start.timezone = result.start.timeZone
    event.start.datetime = result.start.dateTime
    event.end.date = result.end.date
    event.end.timezone = result.end.timeZone
    event.end.datetime = result.end.dateTime
    event.creator.self = result.creator.self
    event.creator.displayName = result.creator.displayName
    event.creator.email = result.creator.email
    event.creator.id = result.creator.id
    event.organizer.self = result.organizer.self
    event.organizer.displayName = result.organizer.displayName
    event.organizer.email = result.organizer.email
    event.organizer.id = result.organizer.id


    return event
