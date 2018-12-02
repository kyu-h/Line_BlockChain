from iconservice import *
import json, os

TAG = 'LineToken'

filename = '/home/kyu/work/call-hello.json'

with open(filename, 'r') as f :
    data = json.load(f)
    data['params']['data']['params']['hash'] = '0x0000'

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
        return "Hello, " + _to + "\n" + "hash: " + hash

