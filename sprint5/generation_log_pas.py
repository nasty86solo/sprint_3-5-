import random
import string


class LoginPasswordGenerator:
    def __init__(self):
        self.email = None
        self.password = None

    def generate(self):
        if self.email is None and self.password is None:
            email_length = random.randint(a:5, b:10)
            self.email = ''.join(random.choices(string.ascii_lowercase + string.digits, k=email_length)) + "@example.com"

            password_lenght = random.randint(a:8, b:12)
            self.password = ''.join(random.choices(string.ascii_letters + string.digits, k=password_lenght))
        return self.email, self.password