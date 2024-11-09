# jobRunner/progressConsumer.py
import json
from channels.generic.websocket import AsyncWebsocketConsumer
from asgiref.sync import async_to_sync


class progressConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()
        print("Connect")
        await self.channel_layer.group_add("progress", self.channel_name)

    async def disconnect(self, close_code):
        print("Disconnect")
        await self.channel_layer.group_discard("progress", self.channel_name)
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
            if message == 'begin_connection':
                await self.send(text_data=json.dumps({
                    'message': 'Waiting for upload'
                }))
            
        # await self.send(text_data=json.dumps({"message": f"Recieved message: {message}"}))
    async def progress_update(self, event): # Custom event handler
        """
        Called when a progress_update event is received from the channel layer.

        Args:
            event (_type_): _description_
        """
        message = event['message']
        await self.send(text_data=json.dumps({
            'message': message
        }))
