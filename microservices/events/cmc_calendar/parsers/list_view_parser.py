from html.parser import HTMLParser

class ListViewHTMLParser(HTMLParser):


    def __init__(self):
        super().__init__()
        self.data = []


    def get_data(self):
        return self.data


    def handle_starttag(self, tag, attrs):

        if tag == 'a':
            attr_dict = dict(attrs)

            if 'hreft' in attr_dict and 'EventDeatils.aspx?ID=' in attr_dict['href']:
                    self.data.append(attr_dict['href'])

