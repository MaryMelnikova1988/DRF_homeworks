from rest_framework import serializers

from users.models import User, Payment


# class UserSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     username = serializers.CharField(max_length=100)
#     email = serializers.EmailField()
#
#     def create(self, validated_data):
#         return User.objects.create(**validated_data)
#
#     def update(self, instance, validated_data):
#         instance.username = validated_data.get('username', instance.username)
#         instance.email = validated_data.get('email', instance.email)
#         instance.save()
#         return instance

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = '__all__'

# class PaymentCreateSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Payment
#         fields = ['price','paid_course',]