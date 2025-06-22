from channels.generic.websocket import AsyncWebsocketConsumer
import json

class AlertConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.channel_layer.group_add("alerts", self.channel_name)
        await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard("alerts", self.channel_name)

    async def alert_message(self, event):
        await self.send(text_data=json.dumps(event["message"]))

from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer

class AlertViewSet(viewsets.ModelViewSet):
  

    def perform_create(self, serializer):
        alert = serializer.save(author=self.request.user)
        channel_layer = get_channel_layer()
        async_to_sync(channel_layer.group_send)(
            "alerts",
            {
                "type": "alert_message",
                "message": AlertSerializer(alert).data,
            }
        )
