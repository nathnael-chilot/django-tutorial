from rest_framework import serializers
from .models import Comment

class CommentSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.username')

    class Meta:
        model = Comment
        fields = ['id', 'post', 'author', 'body', 'created_at']
        read_only_fields = ['id', 'created_at']

    def validate_body(self, value):
        if not value.strip():
            raise serializers.ValidationError("Comment body cannot be empty.")
        if len(value) > 1000:
            raise serializers.ValidationError("Comment body must be at most 1000 characters.")
        return value