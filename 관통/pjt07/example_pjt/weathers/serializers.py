from rest_framework import serializers
from .models import Weather

# DB에 지정된 필드들만 포장에 관여 : ModelSerializer
# DB 필드 외의 데이터들도 포장에 관여 : Serializer
class WeatherSerializers(serializers.ModelSerializer):
    class Meta:
        model = Weather
        fields = '__all__'