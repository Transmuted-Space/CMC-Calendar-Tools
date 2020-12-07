#!/usr/bin/env python3.8
'''
This is the module for the CalendarIngest tool which provides high level calendar functionality via the command line.
'''

import logging
import requests
import firebase_admin
from firebase_admin import credentials, firestore
from configparser import ConfigParser
from html.parser import HTMLParser
from datetime import date
from .parsers import CalendarHTMLParser, EventHTMLParser, ListViewHTMLParser


class CalendarIngest:
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

        if not firebase_admin._apps:
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


    def ingest_page(self, parser, link, refresh_html_cache=False):
        response = requests.get(link)

        # Handle depending on the response code.
        if response.status_code == 200:

            # Parse the page HTML.
            parser.feed(response.text)

            # Return the parsed data.
            return parser.get_data(), response.text

        elif response.status_code == 404:
            logging.error('URI not found: HTTP status code {}.'.format(response.status_code))
        else:
            logging.error('Unexpected response: HTTP status code {}.'.format(response.status_code))


    def ingest_event_links(self, links, refresh_html_cache=False):        
        for link in links: 

            # Parse out the event ID from the URI suffix.
            event_id = link.replace('/Calendar/EventDetails.aspx?ID=', '')

            # Ingest each event HTML page.
            parsed_data, raw_data = self.ingest_page(
                EventHTMLParser(),
                self.eventsBaseUri + link,
                refresh_html_cache
            )

            # Cache the response if specified.
            if refresh_html_cache:
                with open('cached_html/event-{}.html'.format(event_id), 'w+') as file_handle:
                    file_handle.write(raw_data)

            parsed_data['ID'] = event_id
            self.database.collection('events').add(parsed_data)


    def ingest_calendar(self, refresh_html_cache=False):
        '''
        This function will retrieve an HTML response from the URI and parse the DOM.
        '''

        # Ingest the calendar HTML page.
        parsed_data, raw_data = self.ingest_page(
            CalendarHTMLParser(),
            self.calendarUri,
            refresh_html_cache
        )

        # Cache the response if specified.
        if refresh_html_cache:
            with open('cached_html/calendar-{}.html'.format(date.today()), 'w+') as file_handle:
                file_handle.write(raw_data)

        # Retrieve events list and parse them all.
        self.ingest_event_links(parsed_data, refresh_html_cache=refresh_html_cache)


    def fuzz_events(self):
        '''
        Using the events parsed and added to the database as a starting point 
        this function will fuzz for future or past event IDs.
        '''

        # Instantiate function objects.
        parser = EventHTMLParser()

        # Get the current maximum
        events = self.database.collection('events')
        max_event_id = events.orderBy('ID', Direction.DESCENDING).limit(1)

        # Cap to stop fuzz after 5 consecutive 404s to account for
        # non-contiguous event numbering.
        max_consecutive_404s = 5
        current_404_count = 0

        while current_404_count < max_consecutive_404s:

            # Query the web application for the next possible event.
            response = requests.get(eventQueryBaseUri + max_event_id + 1)

            # Handle depending on the response code.
            if response.status_code == 200:

                # Parse the page HTML.
                parser.feed(response.text)

                # Return the parsed data.
                data = parser.get_data()
                data['ID'] = event_id
                self.database.collection('events').add(parsed_data)

            elif response.status_code == 404:
                current_404_count += 1
            else:
                logging.error('Unexpected response: HTTP status code {}.'.format(response.status_code))