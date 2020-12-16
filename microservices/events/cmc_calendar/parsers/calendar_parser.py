from html.parser import HTMLParser

class CalendarHTMLParser(HTMLParser):


    def __init__(self):
        super().__init__()
        self.data = []


    def get_data(self):
        return self.data


    def handle_starttag(self, tag, attrs):

        if tag == 'a':
            attr_dict = dict(attrs)

            if 'class' in attr_dict and attr_dict['class'] == 'calendarDayLink' and 'href' in attr_dict:
                    self.data.append(attr_dict['href'])
