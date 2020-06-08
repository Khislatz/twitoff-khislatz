# web_app/services/basilica_service.py

import os
from dotenv import load_dotenv
import basilica

load_dotenv()

BASILICA_API_KEY = os.getenv("BASILICA_API_KEY", default="OOPS")

connection = basilica.Connection(BASILICA_API_KEY)
print(type(connection)) #> <basilica.Connection object at 0x0140AD70>

# dir(conection) 
# OUTPUT: ['_Connection__encode_image', '__class__', '__delattr__', '__dict__',
#  '__dir__', '__doc__', '__enter__', '__eq__', '__exit__', '__format__', '__ge__', 
# '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', 
# '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', 
# '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', 'adapter', 
# 'embed', 'embed_image','embed_image_file', 'embed_image_files', 'embed_images', 
# 'embed_sentence', 'embed_sentences', 'raw_embed', 'raw_embed_wrapper', 'retry', 
# 'server', 'session']


def basilica_api_client():
    return basilica.Connection(BASILICA_API_KEY)


print(type(connection)) 
sentences = ["Hello world!", "How are you?"]
embeddings = connection.embed_sentences(sentences)

for embed in embeddings:
    print(embed)

# todo: further comparison!