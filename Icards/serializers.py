from rest_framework import serializers
from .models import Add_category, Add_subcategory, Add_icard


class Add_categorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Add_category            
        fields = '__all__'

class Add_subcategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Add_subcategory          
        fields = '__all__'

class Add_icardSerializer(serializers.ModelSerializer):

    class Meta:
        model =  Add_icard           
        fields = '__all__'