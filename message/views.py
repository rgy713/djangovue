from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from message.models import Message
from rest_framework import viewsets, status
from message.serializers import MessageSerializer
from message.serializers import MessageDetailSerializer

class MessageViewSet(viewsets.ModelViewSet):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
    permission_classes = []
    http_method_names = ['get', 'post', 'delete', ]

    def get_queryset(self):
        queryset = self.queryset
        if self.request.GET.get("user_id"):
            queryset = queryset.filter(sender_id=self.request.GET.get("user_id"))

        return queryset

    def perform_create(self, serializer):
        print("recipient_id", self.request.POST.get("recipient_id"))
        serializer.save(sender=self.request.user, recipient_id=self.request.data["recipient_id"])

    def perform_destroy(self, instance):
        instance.delete()

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)

    def get_serializer_class(self):
        if self.action == 'list':
            return MessageSerializer
        else:
            return MessageDetailSerializer

class MessageReceivedViewSet(viewsets.ModelViewSet):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
    permission_classes = []

    def get_queryset(self):
        queryset = self.queryset
        query_set = queryset.filter(recipient_id=self.request.GET.get("user_id"))
        return query_set

    def perform_create(self, serializer):
        serializer.save(sender=self.request.user)

    def get_serializer_class(self):
        if self.action == 'list':
            return MessageSerializer
        else:
            return MessageDetailSerializer
