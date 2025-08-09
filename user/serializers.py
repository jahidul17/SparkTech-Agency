from rest_framework import serializers
from django.contrib.auth.models import User


class RegisterAdminSerializers(serializers.ModelSerializer):
    confirm_password=serializers.CharField(required=True)
    
    class Meta:
        model=User
        fields=['username','first_name','last_name','email','password','confirm_password']
    
    def save(self):
        username=self.validated_data['username']
        first_name=self.validated_data['first_name']
        last_name=self.validated_data['last_name']
        email=self.validated_data['email']
        password=self.validated_data['password']
        password2=self.validated_data['confirm_password']
        
        if password!=password2:
            raise serializers.ValidationError({'error':"Password Doesn't Matched"})
        if User.objects.filter(username=username).exists():
            raise serializers.ValidationError({'error':"Username already exists"})
        if User.objects.filter(email=email).exists():
            raise serializers.ValidationError({'error':"Email Already Exists"})
        
        account=User(username=username,first_name=first_name,last_name=last_name,email=email)
        account.set_password(password)
        account.is_active=True
        account.is_staff=True
        account.save()
        return account
    
    
    
class RegisterUserSerializers(serializers.ModelSerializer):
    confirm_password=serializers.CharField(required=True)
    
    class Meta:
        model=User
        fields=['username','first_name','last_name','email','password','confirm_password']
    
    def save(self):
        username=self.validated_data['username']
        first_name=self.validated_data['first_name']
        last_name=self.validated_data['last_name']
        email=self.validated_data['email']
        password=self.validated_data['password']
        password2=self.validated_data['confirm_password']
        
        
        if password!=password2:
            raise serializers.ValidationError({'error':"Password Doesn't Matched"})
        if User.objects.filter(username=username).exists():
            raise serializers.ValidationError({'error':"Username already exists"})
        if User.objects.filter(email=email).exists():
            raise serializers.ValidationError({'error':"Email Already Exists"})
        
        account=User(username=username,first_name=first_name,last_name=last_name,email=email)
        account.set_password(password)
        account.is_active=True
        account.save()
        return account
    

class UserLoginSerializers(serializers.Serializer):
    username=serializers.CharField(required=True)
    password=serializers.CharField(required=True)


