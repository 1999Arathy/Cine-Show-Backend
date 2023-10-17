from rest_framework import serializers
from .models import Movie, usermodel
from django.contrib.auth.models import User
from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password

class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = '__all__'

class userSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class RegisterSerializer(serializers.ModelSerializer):
  email = serializers.EmailField(required=True, validators=[UniqueValidator(queryset=User.objects.all())])
  password = serializers.CharField( write_only=True, required=True, validators=[validate_password])
  password2 = serializers.CharField(write_only=True, required=True)
  
  class Meta:
    model = User
    fields = ('username','email','password', 'password2')
    # extra_kwargs = {
    #   'first_name': {'required': True},
    #   'last_name': {'required': True}
    # }
  
  def validate(self, pswd):
    if pswd['password'] != pswd['password2']:
      raise serializers.ValidationError( {"password": "Password fields didn't match."})
    return pswd
  
  def create(self, validated_data):
    user = User.objects.create(
      username=validated_data['username'],
      email=validated_data['email'],
      # first_name=validated_data['first_name'],
      # last_name=validated_data['last_name']
    )
    user.set_password(validated_data['password'])
    user.save()
    return user
  

class BookingSerializer(serializers.ModelSerializer):
   class Meta:
      model = usermodel
      fields  = ('Movie_Name', 'Date', 'Time' , 'Seat_count','User_name')
      def create(self, validated_data):
        show = usermodel.objects.create(
            Movie_Name=validated_data['Movie_Name'],
            Date=validated_data['Date'],
            Time=validated_data['Time'],
            Seat_count=validated_data['Seat_count'],
            User_name = ['User_name']
        )
        show.save()
        return show

class TicketSerializer(serializers.ModelSerializer):
   class  Meta:
      model = usermodel
      fields = '__all__'
    
