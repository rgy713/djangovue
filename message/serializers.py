from rest_framework import serializers
from message.models import Message

from user_info.serializers import UserDescSerializer


class MessageBaseSerializer(serializers.HyperlinkedModelSerializer):

    id = serializers.IntegerField(read_only=True)
    recipient = UserDescSerializer(read_only=True)
    sender = UserDescSerializer(read_only=True)

    default_error_messages = {
        'default': 'No more message here..'
    }

    def check_obj_exists_or_fail(self, model, value, message='default'):
        if not self.default_error_messages.get(message, None):
            message = 'default'

        if not model.objects.filter(id=value).exists() and value is not None:
            self.fail(message, value=value)

class MessageSerializer(MessageBaseSerializer):
    class Meta:
        model = Message
        fields = '__all__'

class MessageDetailSerializer(MessageBaseSerializer):
    id = serializers.IntegerField(read_only=True)
    body_html = serializers.SerializerMethodField()
    toc_html = serializers.SerializerMethodField()

    def get_body_html(self, obj):
        return obj.get_md()[0]

    def get_toc_html(self, obj):
        return obj.get_md()[1]

    class Meta:
        model = Message
        fields = '__all__'
