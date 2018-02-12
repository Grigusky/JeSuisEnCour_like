from rest_framework.generics import (
    ListAPIView,
    CreateAPIView
)
from administration.models import *
from .serializers import *


###############################################################################
# Eleves
###############################################################################


class ElevesApi(ListAPIView):
    queryset = Eleves.objects.all()
    serializer_class = ElevesSerializer


class ElevesCreateApi(CreateAPIView):
    queryset = Eleves.objects.all()
    serializer_class = ElevesSerializer


##############################################################################
# Specialite
##############################################################################


class SpecialiteApi(ListAPIView):
    queryset = Specialite.objects.all()
    serializer_class = SpecialiteSerializer


class SpecialiteCreateApi(CreateAPIView):
    queryset = Specialite.objects.all()
    serializer_class = SpecialiteSerializer


##############################################################################
# Specialite_Eleve
##############################################################################


class Specialite_EleveApi(ListAPIView):
    queryset = Specialite_Eleve.objects.all()
    serializer_class = Specialite_EleveSerializer


class Specialite_EleveCreateApi(CreateAPIView):
    queryset = Specialite_Eleve.objects.all()
    serializer_class = Specialite_EleveSerializer


##############################################################################
# Absences_Eleve
##############################################################################


class Absences_EleveApi(ListAPIView):
    queryset = Absences_Eleve.objects.all()
    serializer_class = Absences_EleveSerializer


class Absences_EleveCreateApi(CreateAPIView):
    queryset = Absences_Eleve.objects.all()
    serializer_class = Absences_EleveSerializer


##############################################################################
# Prof
##############################################################################


class ProfApi(ListAPIView):
    queryset = Prof.objects.all()
    serializer_class = ProfSerializer


class ProfCreateApi(CreateAPIView):
    queryset = Prof.objects.all()
    serializer_class = ProfSerializer


##############################################################################
# Prof_Promotion
##############################################################################


class Prof_PromotionApi(ListAPIView):
    queryset = Prof_Promotion.objects.all()
    serializer_class = Prof_PromotionSerializer


class Prof_PromotionCreateApi(CreateAPIView):
    queryset = Prof_Promotion.objects.all()
    serializer_class = Prof_PromotionSerializer


##############################################################################
# Absences_Prof
##############################################################################


class Absences_ProfApi(ListAPIView):
    queryset = Absences_Prof.objects.all()
    serializer_class = Absences_ProfSerializer


class Absences_ProfCreateApi(CreateAPIView):
    queryset = Absences_Prof.objects.all()
    serializer_class = Absences_ProfSerializer


##############################################################################
# Cours
##############################################################################


class CoursApi(ListAPIView):
    queryset = Cours.objects.all()
    serializer_class = CoursSerializer


class CoursCreateApi(CreateAPIView):
    queryset = Cours.objects.all()
    serializer_class = CoursSerializer


##############################################################################
# Promotions
##############################################################################


class PromotionsApi(ListAPIView):
    queryset = Promotions.objects.all()
    serializer_class = PromotionsSerializer


class PromotionsCreateApi(CreateAPIView):
    queryset = Promotions.objects.all()
    serializer_class = PromotionsSerializer
