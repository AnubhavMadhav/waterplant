from rest_framework import serializers
from api.models import Customer


"""class CustomerSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(required=True,allow_blank=False,max_length=255)
    cust_id = serializers.IntegerField(required=True)
    cust_rate = serializers.IntegerField(required=True)
    number_of_jars_taken_in_a_month = serializers.IntegerField(required=True)
    
    def create(self, validated_data):
        
        return Customer.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
       
        instance.name = validated_data.get('name', instance.name)
        instance.cust_id = validated_data.get('cust_id', instance.cust_id)
        instance.cust_rate = validated_data.get('cust_rate', instance.cust_rate)
        instance.number_of_jars_taken_in_a_month = validated_data.get('number_of_jars_taken_in_a_month', instance.number_of_jars_taken_in_a_month)
        instance.save()
        return instance"""
        
        
class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ("name", "cust_id",'cust_rate','number_of_jars_taken_in_a_month')
        
        
"""class TokenSerializer(serializers.Serializer):

    This serializer serializes the token data

    token = serializers.CharField(max_length=255)"""