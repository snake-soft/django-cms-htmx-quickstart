import os
from random import randint


def get_random_module():
    class File:
        def __init__(self):
            self.path = None
            self.classpath = None
            self.name = None
            self.size = None

        def read(self):
            with open(self.path, 'r') as file:
                data = file.read()
            data = data.replace('`', r"\`")
            return data

    path = __import__('django').__path__[0]
    djangofiles = []
    for root, _, files in os.walk(path):
        for filename in files:
            file = File()
            file.name = filename
            file.path = os.path.join(root, filename)
            file.size = os.path.getsize(file.path)
            file.classpath = 'django' + file.path[len(path):-3].replace('/', '.')
            file.classpath = file.classpath.lower()
            if file.name.endswith(".py") \
                and file.name != '__init__.py' \
                    and 5000 < file.size < 10000:  # bytes
                djangofiles.append(file)

    while djangofiles:
        random_file = djangofiles[randint(0, len(djangofiles)-1)]
        if random_file.read():
            return random_file
        print(random_file.path)
        djangofiles.remove(random_file)
