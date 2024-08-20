from rest_framework import serializers
from blog_api.models import Post


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id', 'title', 'author','category','excerpt', 'content', 'status')
        model = Post
