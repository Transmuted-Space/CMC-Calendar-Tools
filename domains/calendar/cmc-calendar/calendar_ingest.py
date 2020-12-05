#!/usr/bin/env python3.8
'''
This is the module for the CalendarInjest tool which provides high level calendar functionality via the command line.
'''

import logging
import requests
import firebase_admin
from firebase_admin import credentials, firestore
from configparser import ConfigParser
from html.parser import HTMLParser
from datetime import date
from .event import Event


class EventHTMLParser(HTMLParser):


    def __init__(self):
        super().__init__()
        self.harvest_data = False
        self.label = ''
        self.data = {}


    def get_data(self):
        return self.data


    def sanitize_data(self, data):
        data = data.replace('\n', '')
        data = data.replace('\xa0', ' ')
        return data


    def handle_data(self, data):
        if self.harvest_data:
            self.data[self.label] = self.sanitize_data(data)

        self.harvest_data = False


    def handle_starttag(self, tag, attrs):

        if tag == 'span':
            attr_dict = dict(attrs)
            if 'id' in attr_dict and 'EventDetails_lbl' in attr_dict['id']:
                
                # Parse out label name.
                label = attr_dict['id'].replace('EventDetails_lbl', '')
                self.label = label.replace('dnn_ctr781_', '')

                self.harvest_data = True


class CalendarHTMLParser(HTMLParser):


    def __init__(self):
        super().__init__()
        self.event_links = []


    def get_event_links(self):
        return self.event_links


    def handle_starttag(self, tag, attrs):

        if tag == 'a':
            attr_dict = dict(attrs)

            if 'class' in attr_dict and attr_dict['class'] == 'calendarDayLink' and 'href' in attr_dict:
                    self.event_links.append(attr_dict['href'])



class CalendarInjest:
    '''
    Class encapsulation and functionality for interacting with the calendar API.
    '''

    def __init__(self):

        # Configure logger to output to file.
        logging.basicConfig(filename='calendar-ingest.log')

        # Load the configuration.
        self.config_parser = ConfigParser()
        self.config_parser.read('configuration.ini')
        self.calendarUri = self.config_parser['DEFAULT']['calendarUri']
        self.eventsBaseUri = self.config_parser['DEFAULT']['eventsBaseUri']

        # Load Firebase credentials and create client.
        cred = credentials.Certificate('cmc-calendar-297516-firebase-adminsdk-mwugq-e33b3b9a7a.json')
        firebase_admin.initialize_app(cred)
        self.database = firestore.client()


    def export_calendar(self):
        '''
        This function will respond with a JSON serilization of events from the calendar.
        '''

        pass


    def subscribe_to_calendar(self):
        '''

        '''
        pass


    def ingest_event_links(self, links, refresh_html_cache=False):
        event_parser = EventHTMLParser()

        for i, link in enumerate(links):

            # Send HTTP request to URI.
            response = requests.get(self.eventsBaseUri + link)

            # Handle depending on the response code.
            if response.status_code == 200:

                # Cache the response if specified.
                if refresh_html_cache:
                    with open('cached_html/event-{}-{}.html'.format(i, date.today()), 'w+') as file_handle:
                        file_handle.write(response.text)

                # Parse the event page HTML.
                event_parser.feed(response.text)

                data = event_parser.get_data()
                # from pprint import pprint
                # pprint(data)
                self.database.collection('events').add(data)


    def ingest_calendar(self, refresh_html_cache=False):
        '''
        This function will retrieve an HTML response from the URI and parse the DOM.
        '''

        calendar_parser = CalendarHTMLParser()

        # Send HTTP request to URI.
        response = requests.get(self.calendarUri)

        # Handle depending on the response code.
        if response.status_code == 200:

            # Feed the response HTML into the parser and parse.
            calendar_parser.feed(response.text)

            # Cache the response if specified.
            if refresh_html_cache:
                with open('cached_html/calendar-{}.html'.format(date.today()), 'w+') as file_handle:
                    file_handle.write(response.text)

            # Retrieve events list and parse them all.
            event_links = calendar_parser.get_event_links()
            self.ingest_event_links(event_links, refresh_html_cache=refresh_html_cache)

        elif response.status_code == 404:
            logging.error('URI not found: HTTP status code {}.'.format(response.status_code))
        else:
            logging.error('Unexpected response: HTTP status code {}.'.format(response.status_code))
