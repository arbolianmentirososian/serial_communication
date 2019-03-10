import json
from urllib.request import urlopen
import os


class Fun:
    absolute_path = '/home/mateo/PycharmProjects/untitled3/venv/learning/results'
    interval = 12

    def __init__(self, url):
        self.url = url

    def read_json(self):
        with urlopen(self.url) as response:
            first = response.read()
            data = json.loads(first.decode('utf-8'))
            return json.dumps(data, indent=2)

    def print_json(self):
        print(self.read_json())

    def save_to_file(self, filename):
        if self.check_path(os.getcwd()):
            with open(filename, 'a') as outputfile:
                outputfile.write(self.read_json()+'\n')
        else:
            os.chdir(self.absolute_path)
            self.check_path(os.getcwd())

    @staticmethod
    def check_path(path):
        if path == Fun.absolute_path:
            return True
        return False
