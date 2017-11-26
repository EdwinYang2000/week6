import re
import os
from wechatpy.messages import TextMessage
from wechatpy import create_reply
from qqwry import QQwry

class CommandHandler:
    command = ''

    def check_match(self,message):

        if not isinstance(message, TextMessage):
            return False
        if not message.content.strip().lower().startswith(self.command):
            return False
        return True

class IPLocationHandler(CommandHandler):
    command = "ip"



    def handle(self, message):
        if not self.check_match(message):
            return


        parts = message.content.strip().split()

        if len(parts) == 1 or len(parts) > 2:
            return create_reply('command wrong, correct format ip 123.123.123.123', message)

        ip = parts[1]
        print (ip)

        patterns = r'^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$'

        if not re.match(patterns, ip):
            return create_reply('wrong ip addresss',message)

        file = '/Users/yangedwin/workspace/week6/rmon/qqwry.dat'
        q = QQwry()
        q.load_file(file)
        result = q.lookup(ip)
        print (result)

        if result is None:
            return create_reply('could not find this address',message)
        else:
            return create_reply(result[0],message)
