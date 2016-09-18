from django.core.management.base import BaseCommand
from socket import *
import json
from messages.models import Comments

class Command(BaseCommand):

    def handle(self, *args, **options):
        myHost = ''
        myPort = 50005
        sockobj = socket(AF_INET, SOCK_STREAM)
        sockobj.bind((myHost, myPort))
        sockobj.listen(5)
        while True:
            connection, address = sockobj.accept()
            print('Server connected by', address)
            while True:
                data = connection.recv(1024)
                if not data: break
                info = get_json(data)
                if info:
                    c = Comments(name=info['name'], comment=info['comment'])
                    c.save()
                    connection.send(b'Receive=>' + data)
                else:
                    connection.send(b'Not json=>' + data)
            connection.close()


def get_json(myjson):
    try:
        json_object = json.loads(myjson)
    except(ValueError):
        return False
    return json_object