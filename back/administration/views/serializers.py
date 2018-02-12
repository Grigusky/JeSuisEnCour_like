from rest_framework.serializers import ModelSerializer
from administration.models import *


class ElevesSerializer(ModelSerializer):
    class Meta:
        model = Eleves
        fields = '__all__'


class SpecialiteSerializer(ModelSerializer):
    class Meta:
        model = Specialite
        fields = '__all__'


class Specialite_EleveSerializer(ModelSerializer):
    class Meta:
        model = Specialite_Eleve
        fields = '__all__'


class Absences_EleveSerializer(ModelSerializer):
    class Meta:
        model = Absences_Eleve
        fields = '__all__'


class ProfSerializer(ModelSerializer):
    class Meta:
        model = Prof
        fields = '__all__'


class Prof_PromotionSerializer(ModelSerializer):
    class Meta:
        model = Prof_Promotion
        fields = '__all__'


class Absences_ProfSerializer(ModelSerializer):
    class Meta:
        model = Absences_Prof
        fields = '__all__'


class CoursSerializer(ModelSerializer):
    class Meta:
        model = Cours
        fields = '__all__'


class PromotionsSerializer(ModelSerializer):
    class Meta:
        model = Promotions
        fields = '__all__'
