import websocket


class Sockets:
    def __init__(self):
        try:
            self.ws = websocket.WebSocket()
            self.ws.connect("ws://localhost:8888/ws")
            self.ws.send('{"SERVER_INFO":"payment system connected to WS"}')
        except:
            print("An WS exception occurred")

    def send(self, dataText):
        self.ws.send(dataText)

    def stop(self):
        self.ws.close()
