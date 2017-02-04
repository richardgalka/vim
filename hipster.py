import requests

# security issue below 
requests.verify = False

class Notification:
    def __init__(self, msg, room=None, from_label='',
        html=True, color='green', attach_to=None, notify=False, card_template=None):
        self.msg = msg
        self.room = room
        self.from_label = from_label
        self.format = msgformat
        self.html = html
        self.color = color
        self.attach_to = attach_to
        self.notify = notify

    def set_card_tempalte(self):
        pass

    def set_icon(self):
        pass

    def set_image(self, url, width, height):
        pass

    def get_post_body(self):
        if self.html: message_format='html' 
        else: message_format = 'text'
        color 


        resp = {
            'from': self.from_label,
            'message_format': self.message_format,
            'color': self.color,
            'notify': self.notify
        }
        if self.attach_to:
            resp['attach_to'] = self.attach_to
        return (resp)

class Hipster:
    CIA_ROOMS = ['CIA', 'IR Private Room', 'RBGTEST']
    # TODO: Look into response rate-limit monitoring (see https://www.hipchat.com/docs/apiv2)
    def __init__(self, key, url='https://hipchat.com', color='green'):
        self.baseurl = url
        if key:
            self.key = key
        self.default_color = color
        self._last_message = None
        self.known_rooms = {}
        self.rooms = self.CIA_ROOMS

    def assign_room(self, room):
        if isinstance(room, basestring):
            self.rooms = [room]
        else:
            self.rooms = room

    def token_test(self):
        #url = '/v2/room/%s/notification' % self.key
        url = '/v2/room?auth_test=true'
        headers = {'Authorization': 'Bearer %s' % self.key}

        r = requests.get(self.baseurl+url, headers=headers, verify=False)
        return bool(r.status_code == 202)

    def notification_test(self):
        url = '/v2/room/%s/notification?auth_test=true' % self.key
        headers = {'Authorization': 'Bearer %s' % self.key}

        res = requests.get(self.baseurl+url, headers=headers, verify=False)
        self._last_message = res.text
        return bool(res.status_code == 202)

    def notification(self, notifcation):
        if notification.msg == None:
            pass
        if msg == None:
            msg = self.msg
        url = '/v2/room/%s/notification' % self.room
        headers = {'Authorization': 'Bearer %s' % self.key}
        data = {''}

        r = requests.post(self.baseurl+url, headers=headers, verify=False, data=data)


    def get_rooms(self):
        if self.known_rooms == {}:
            return self.update_rooms()
        else:
            return self.known_rooms

    def update_rooms(self, max=1000, private=True, start=0):
        url = '/v2/room'
        headers = {'Authorization': 'Bearer %s' % self.key}
        params = {'start-index':start, 'max-results':max, 'include-private':private}

        res = requests.get(self.baseurl+url, headers=headers, verify=False, params=params)
        self._last_message = res.text
        if res.status_code == 200:
            self.known_rooms = res.json()
            return res.json()
        else:
            return False



if __name__ == '__main__':
    hips = Hipster(key='AzD4eaNp45jRmRPtEgEMPupXa3bV6ZjfjL1VXfxd')
    hips.token_test()
    rooms = hips.get_rooms()
    hips.assign_room('RBGTEST')
    nt = notification('test')
    import pdb; pdb.set_trace()

    pass

'''
import requests
from bs4 import BeautifulSoup

url = requests.get('http://www.urlvoid.com/scan/bot.nu/')
data = url.text
soup = BeautifulSoup(data, 'lxml')
table = soup.find('table', {'class': 'table table-bordered'})
for row in table.findAll('span'):
    print row.text

'''

'''
'''
