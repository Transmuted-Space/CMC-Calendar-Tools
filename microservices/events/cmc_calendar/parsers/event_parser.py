from html.parser import HTMLParser

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
