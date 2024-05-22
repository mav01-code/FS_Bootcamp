from rest_framework import serializers
from .models import TodoItem

class listallTodoItemsserializer(serializers.ModelSerializer):
    class Meta:
        model=TodoItem
        fields = '__all__'


class TodoItemCreate(serializers.ModelSerializer):
    class Meta:
        model=TodoItem
        fields = ['title','description','created_at']