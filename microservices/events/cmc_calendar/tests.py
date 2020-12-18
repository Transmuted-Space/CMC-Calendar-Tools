#!/usr/bin/env python3.8

from pathlib import Path
import unittest
from unittest.mock import Mock, patch
import requests
from firebase_admin import firestore

from .calendar_ingest import CalendarIngest


class Tests(unittest.TestCase):
    def setUp(self):
        repository = Mock()
        repository.add_event = Mock()
        repository.get_highest_event_id = Mock(return_value=0)
        self.test_instance = CalendarIngest(
            {
                "calendarUri": "https://www.cmc.org/Calendar.aspx",
                "eventsBaseUri": "https://www.cmc.org",
            },
            repository,
        )

    def test_ingest_event_links(self):

        # Find HTML files in cached directory.
        cached_html_dir = Path("cached_html").rglob("*.html")

        with patch("requests.get") as mock_request:
            for filename in cached_html_dir:
                if "event" in str(filename):
                    file_handle = open(filename, "r")
                    text = file_handle.read()
                    file_handle.close()

                    mock_request.return_value.status_code = 200
                    mock_request.return_value.text = text

                    self.test_instance.ingest_event_links(
                        [""], refresh_html_cache=False
                    )

    def test_ingest_calendar(self):

        # Find HTML files in cached directory.
        cached_html_dir = list(Path("cached_html").rglob("*.html"))

        with patch("requests.get") as mock_request:
            text = ""
            for filename in cached_html_dir:
                if "calendar" in str(filename):
                    file_handle = open(filename, "r")
                    text = file_handle.read()
                    file_handle.close()

            mock_request.return_value.status_code = 200
            mock_request.return_value.text = text

            self.test_instance.ingest_calendar(False)


if __name__ == "__main__":
    unittest.main()
