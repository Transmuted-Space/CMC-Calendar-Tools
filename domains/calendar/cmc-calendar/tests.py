#!/usr/bin/env python3.8

from pathlib import Path
import unittest
from unittest.mock import patch
import requests
from .calendar_ingest import CalendarInjest


class Tests(unittest.TestCase):


    def setUp(self):
        self.test_instance = CalendarInjest()


    def test_ingest_event_links(self):

        # Find HTML files in cached directory.
        cached_html_dir = dir(Path('cached_html').rglob('*.html'))

        with patch('requests.get') as mock_request:
            text = ''
            for filename in cached_html_dir:
                if 'event' in filename:
                    file_handle = open(filename, 'r')
                    text = file_handle.read()
                    print(text)

            mock_request.return_value.status_code = 200
            mock_request.return_value.text = text

            self.test_instance.ingest_event_links([''], refresh_html_cache=False)


    def test_ingest_calendar(self):

        # Find HTML files in cached directory.
        cached_html_dir = dir(Path('cached_html').rglob('*.html'))
        
        # If the directory is empty then refresh the cache.
        refresh_html_cache = False
        if not cached_html_dir:
            refresh_html_cache = True

        with patch('requests.get') as mock_request:
            text = ''
            for filename in cached_html_dir:
                if 'calendar' in filename:
                    file_handle = open(filename, 'r')
                    text = file_handle.read()

            mock_request.return_value.status_code = 200
            mock_request.return_value.text = text

            self.test_instance.ingest_calendar(refresh_html_cache=refresh_html_cache)


if __name__ == '__main__':
    unittest.main()
