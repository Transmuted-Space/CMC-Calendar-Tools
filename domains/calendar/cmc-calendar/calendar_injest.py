#!/usr/bin/env python3.8
'''
This is the module for the CalendarInjest tool which provides high level calendar functionality via the command line.
'''

import logging
import requests
from configparser import ConfigParser
from html.parser import HTMLParser


class EventHTMLParser(HTMLParser):
    pass


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
        logging.basicConfig(filename='calendar-injest.log')

        # Load the configuration.
        self.config_parser = ConfigParser()
        self.config_parser.read('configuration.ini')

        # Instanciate HTML parser and logger.
        self.html_parser = CalendarHTMLParser()


    def export_calendar(self):
        '''
        This function will respond with a JSON serilization of events from the calendar.
        '''

        pass


    def subscribe_to_calendar(self):
        '''

        '''
        pass


    def injset_event_links(self, links):
        for link in links:

            # Send HTTP request to URI.
            response = requests.get(calendarUri + link)


    def injest_calendar(self):
        '''
        This function will retrieve an HTML response from the URI and parse the DOM.
        '''

        calendarUri = self.config_parser['DEFAULT']['calendarUri']

        # Send HTTP request to URI.
        response = requests.get(calendarUri)

        # Handle depending on the response code.
        if response.status_code == 200:

            # Feed the response HTML into the parser and parse.
            self.html_parser.feed(response.text)

            # Retrieve events list and parse them all.
            event_links = self.html_parser.get_event_links()
            self.injest_event_links(event_links)

        elif response.status_code == 404:
            logging.error('URI not found: HTTP status code {}.'.format(response.status_code))
        else:
            logging.error('Unexpected response: HTTP status code {}.'.format(response.status_code))
