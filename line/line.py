from iconservice import *
import time
import json, os

TAG = 'LineToken'

filename = '/home/kyu/work/call-hello.json'

f_txt = open('/home/kyu/work/line/hash.txt', 'r')
txt_data = f_txt.read()
print(txt_data)
f_txt.close()

with open(filename, 'r') as f :
    data = json.load(f)
    data['params']['data']['params']['hash' + str(time.time())] = txt_data

os.remove(filename)
with open(filename, 'w') as f:
    json.dump(data, f, indent = 4)

class LineToken(IconScoreBase):

    def __init__(self, db: IconScoreDatabase) -> None:
        super().__init__(db)

    def on_install(self) -> None:
        super().on_install()

    def on_update(self) -> None:
        super().on_update()

    @external(readonly=True)
    def hello(self, _to: str, hash: str) -> str:
        Logger.debug(f'Hello, world!', TAG)
        return "You got it!"
