#!/usr/bin/env python3.8
'''
This is the module for the CalendarInjest tool which provides high level calendar functionality via the command line.
'''

import logging
import requests
from configparser import ConfigParser
from html.parser import HTMLParser


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
        self.html_parser = HTMLParser()


    def export_calendar(self):
        '''
        This function will respond with a JSON serilization of events from the calendar.
        '''

        pass


    def subscribe_to_calendar(self):
        '''

        '''
        pass


    def injest_calendar(self):
        '''
        This function will retrieve an HTML response from the URI and parse the DOM.
        '''

        calendarUri = self.config_parser['DEFAULT']['calendarUri']

        # Send HTTP request to URI.
        response = requests.get(calendarUri)

        # 
        if response.status_code == 200:
            self.html_parser.feed(response.text)
        else:
            pass


if __name__ == "__main__":
    pass

