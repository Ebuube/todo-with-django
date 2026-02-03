from datetime import date
from rest_framework import serializers

from todos.models import Todo


class TodoSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Todo
        fields = [
            'id',
            'owner',
            'title',
            'description',
            'is_completed',
            'due_date',
            'created_at',
            'updated_at',
        ]
        read_only_fields = ['id', 'owner', 'created_at', 'updated_at']

    def validate_title(self, value: str) -> str:
        if value is None or not value.strip():
            raise serializers.ValidationError('Title cannot be empty.')
        return value.strip()

    def validate_due_date(self, value):
        '''
        Mirror SSR rules (create vs edit differ).

        Implemented rule:
        - Create: due_date cannot be in the past
        - Update: allow existing past due_date if unchaged
                    but disallow changing it to a past date
        '''
        if value is None:
            return value

        today = date.today()
        is_create = self.instance is None

        if is_create:
            if value < today:
                raise serializers.ValidationError('Due date cannot be in the past')
            return value

        # Update
        # If user is trying to set a past date, only allwo it if it's unchaged from existing
        if value < today:
            current = getattr(self.instance, 'due_date', None)
            if current != value:
                raise serializers.ValidationError('Due date cannot be set to a past date')
        return value
