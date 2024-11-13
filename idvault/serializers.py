from rest_framework import serializers
from .models import SAIDRecord

class SAIDRecordSerializer(serializers.ModelSerializer):
    """
    Serializer for the SAIDRecord model.

    This serializer converts instances of the SAIDRecord model into JSON format 
    and validates incoming data for creating or updating SAIDRecord instances.

    Meta:
        model (SAIDRecord): The model that this serializer is based on.
        fields (list): The fields to be included in serialization.
    """

    class Meta:
        model = SAIDRecord
        fields = [
            "id_number",
            "date_of_birth",
            "gender",
            "citizenship_status",
            "search_count",
        ]
