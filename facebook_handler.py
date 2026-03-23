import requests
from http import cookiejar

class FacebookHandler:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.session = requests.Session()
        self.session.cookies = cookiejar.LWPCookieJar('facebook_cookies.lwp')

    def login(self):
        login_url = 'https://www.facebook.com/login.php'
        payload = {
            'email': self.username,
            'pass': self.password
        }
        response = self.session.post(login_url, data=payload)
        if 'c_user' in self.session.cookies:
            print('Login successful!')
            self.session.cookies.save()
            return True
        else:
            print('Login failed!')
            return False

    def follow(self, user_id):
        follow_url = f'https://www.facebook.com/{user_id}/follow'
        response = self.session.post(follow_url)
        if response.status_code == 200:
            print('Followed successfully!')
        else:
            print('Failed to follow user. Status code:', response.status_code)