from rest_framework import serializers
from . import models


class PostSerializer(serializers.ModelSerializer):

    class Meta:
        fields = ('id', 'author', 'title', 'content', 'created_at', 'updated_at')
        model = models.Post



class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Comment
        fields = ('content', 'author', 'created_at')


class VoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Vote
        fields = '__all__'


class ChoiceSerializer(serializers.ModelSerializer):
    votes = VoteSerializer(many=True, required=False)

    class Meta:
        model = models.Choice
        fields = '__all__'
