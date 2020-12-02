#!/usr/bin/env python3.8
'''
This is the module for the CalendarInjest tool which provides high level calendar functionality via the command line.
'''

import requests
from sqlalchemy.orm import declaritive_base
from configparser import ConfigParser
from html.parser import HTMLParser


Base = declaritive_base()


class CalendarInjest:
    '''
    Class encapsulation and functionality for interacting with the calendar API.
    '''

    def __init__(self):
        self.config = ConfigParser()


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
        calendarUri = self.config['DEFAULT']['CalendarUri']

        # Send HTTP request to URI.
        response = requests.get(calendarUri)

        # 


if __name__ == "__main__":
    pass

