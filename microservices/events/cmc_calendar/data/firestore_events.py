class FirestoreEventsRepository:
    def __init__(self, database):
        self.database = database

    def get_highest_event_id():
        events = self.database.collection("events")
        return events.orderBy("ID", Direction.DESCENDING).limit(1)

    def add_event(event):
        self.database.collection("events").add(event)
