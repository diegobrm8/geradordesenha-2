import secrets
import string as s
from secrets import SystemRandom as Sr

random = secrets.SystemRandom()

print(''.join(Sr().choices(s.ascii_letters + s.digits + s.punctuation, k=8)))
