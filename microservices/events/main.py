#!/usr/bin/env python3.8

from os import path
from configparser import ConfigParser
import firebase_admin
from firebase_admin import credentials, firestore

from cmc_calendar.data import FirestoreEventsRepository
from cmc_calendar.calendar_ingest import CalendarIngest


def ingest():
    # Load the configuration.
    config_path = path.join(path.dirname(__file__), "configuration.ini")
    config_parser = ConfigParser()
    config_parser.read(config_path)

    # Load Firebase credentials and create client.
    # TODO this won't be necessary once we get Application Default Credentials set up in start.sh
    if not firebase_admin._apps:
        cred = credentials.Certificate(
            "cmc-calendar-297516-firebase-adminsdk-mwugq-e33b3b9a7a.json"
        )
        firebase_admin.initialize_app(cred)

    repository = FirestoreEventsRepository(firestore.client())
    CalendarIngest(config_parser["DEFAULT"], repository).ingest_calendar(False)
