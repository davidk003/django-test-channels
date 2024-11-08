# jobRunner/progressConsumer.py
import json

from channels.generic.websocket import AsyncWebsocketConsumer

class progressConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()

        print("Connect")

    async def disconnect(self, close_code):
        print("Disconnect")
        pass

    async def receive(self, text_data):
        print(text_data)
        try:
            text_data_json = json.loads(text_data)
        except:
            await self.send(text_data=json.dumps({"message": "Message not in json format."}))
            return
        if "message" not in text_data_json:
            await self.send(text_data=json.dumps({"message": "No message field"}))
        else:
            message = text_data_json["message"]


        await self.send(text_data=json.dumps({"message": f"Recieved message: {message}"}))