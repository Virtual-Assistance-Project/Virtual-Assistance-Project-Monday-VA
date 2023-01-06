from rest_framework import serializers
from .models import Schedule, options

class ScheduleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Schedule
        fields = [
            "id",
            "title",
            "type",
            "begans_at",
            "ends_at",
            "routine_weekdays",
            "description",
            "management_id"
        ]
        extra_kwargs={
            "type":{
                "choices": options
            }
        }
        
    def create(self, validated_data):
        return Schedule.objects.create(**validated_data)

    def read(self, instance: Schedule):
        return self.to_representation(instance)

    def update(self, instance: Schedule, validated_data: dict)-> Schedule:
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        
        instance.save()
        return instance
    
    def delete(self, instance: Schedule):
        instance.delete()
        return None