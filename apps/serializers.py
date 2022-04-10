
from rest_framework import serializers
from .models import Post

class NoteSerializer(serializers.ModelSerializer):

    class Meta:
        model = Post
        read_only_fields = (
            "created_at",
            "updated_at",
        )
        fields = '__all__'