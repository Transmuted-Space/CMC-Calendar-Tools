#!/usr/bin/env python3.8

from cmc-calendar.calendar_ingest import CalendarIngest

def ingest():
    CalendarIngest().ingest_calendar(True)
