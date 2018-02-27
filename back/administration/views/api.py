from rest_framework.generics import (
    ListAPIView,
    CreateAPIView,
    UpdateAPIView,
    RetrieveAPIView,
    DestroyAPIView
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


class ElevesUpdateApi(UpdateAPIView):
    queryset = Eleves.objects.all()
    serializer_class = ElevesSerializer
    lookup_field = 'nom'


class ElevesUpdateApi(RetrieveAPIView):
    queryset = Eleves.objects.all()
    serializer_class = ElevesSerializer
    lookup_field = 'nom'


class ElevesUpdateApi(DestroyAPIView):
    queryset = Eleves.objects.all()
    serializer_class = ElevesSerializer
    lookup_field = 'nom'


##############################################################################
# Specialite
##############################################################################


class SpecialiteApi(ListAPIView):
    queryset = Specialite.objects.all()
    serializer_class = SpecialiteSerializer


class SpecialiteCreateApi(CreateAPIView):
    queryset = Specialite.objects.all()
    serializer_class = SpecialiteSerializer


class SpecialiteUpdateApi(UpdateAPIView):
    queryset = Specialite.objects.all()
    serializer_class = SpecialiteSerializer
    lookup_field = 'nom'


class SpecialiteUpdateApi(RetrieveAPIView):
    queryset = Specialite.objects.all()
    serializer_class = SpecialiteSerializer
    lookup_field = 'nom'


class SpecialiteUpdateApi(DestroyAPIView):
    queryset = Specialite.objects.all()
    serializer_class = SpecialiteSerializer
    lookup_field = 'nom'


##############################################################################
# Specialite_Eleve
##############################################################################


class Specialite_EleveApi(ListAPIView):
    queryset = Specialite_Eleve.objects.all()
    serializer_class = Specialite_EleveSerializer


class Specialite_EleveCreateApi(CreateAPIView):
    queryset = Specialite_Eleve.objects.all()
    serializer_class = Specialite_EleveSerializer


class Specialite_EleveUpdateApi(UpdateAPIView):
    queryset = Specialite_Eleve.objects.all()
    serializer_class = Specialite_EleveSerializer
    lookup_field = 'eleve'


class Specialite_EleveUpdateApi(RetrieveAPIView):
    queryset = Specialite_Eleve.objects.all()
    serializer_class = Specialite_EleveSerializer
    lookup_field = 'eleve'


class Specialite_EleveUpdateApi(DestroyAPIView):
    queryset = Specialite_Eleve.objects.all()
    serializer_class = Specialite_EleveSerializer
    lookup_field = 'eleve'


##############################################################################
# Absences_Eleve
##############################################################################


class Absences_EleveApi(ListAPIView):
    queryset = Absences_Eleve.objects.all()
    serializer_class = Absences_EleveSerializer


class Absences_EleveCreateApi(CreateAPIView):
    queryset = Absences_Eleve.objects.all()
    serializer_class = Absences_EleveSerializer


class Absences_EleveUpdateApi(UpdateAPIView):
    queryset = Absences_Eleve.objects.all()
    serializer_class = Absences_EleveSerializer
    lookup_field = 'eleve'


class Absences_EleveUpdateApi(RetrieveAPIView):
    queryset = Absences_Eleve.objects.all()
    serializer_class = Absences_EleveSerializer
    lookup_field = 'eleve'


class Absences_EleveUpdateApi(DestroyAPIView):
    queryset = Absences_Eleve.objects.all()
    serializer_class = Absences_EleveSerializer
    lookup_field = 'eleve'


##############################################################################
# Prof
##############################################################################


class ProfApi(ListAPIView):
    queryset = Prof.objects.all()
    serializer_class = ProfSerializer


class ProfCreateApi(CreateAPIView):
    queryset = Prof.objects.all()
    serializer_class = ProfSerializer


class ProfUpdateApi(UpdateAPIView):
    queryset = Prof.objects.all()
    serializer_class = ProfSerializer
    lookup_field = 'nom'


class ProfUpdateApi(RetrieveAPIView):
    queryset = Prof.objects.all()
    serializer_class = ProfSerializer
    lookup_field = 'nom'


class ProfUpdateApi(DestroyAPIView):
    queryset = Prof.objects.all()
    serializer_class = ProfSerializer
    lookup_field = 'nom'


##############################################################################
# Prof_Promotion
##############################################################################


class Prof_PromotionApi(ListAPIView):
    queryset = Prof_Promotion.objects.all()
    serializer_class = Prof_PromotionSerializer


class Prof_PromotionCreateApi(CreateAPIView):
    queryset = Prof_Promotion.objects.all()
    serializer_class = Prof_PromotionSerializer


class Prof_PromotionUpdateApi(UpdateAPIView):
    queryset = Prof_Promotion.objects.all()
    serializer_class = Prof_PromotionSerializer
    lookup_field = 'prof'


class Prof_PromotionUpdateApi(RetrieveAPIView):
    queryset = Prof_Promotion.objects.all()
    serializer_class = Prof_PromotionSerializer
    lookup_field = 'prof'


class Prof_PromotionUpdateApi(DestroyAPIView):
    queryset = Prof_Promotion.objects.all()
    serializer_class = Prof_PromotionSerializer
    lookup_field = 'prof'


##############################################################################
# Absences_Prof
##############################################################################


class Absences_ProfApi(ListAPIView):
    queryset = Absences_Prof.objects.all()
    serializer_class = Absences_ProfSerializer


class Absences_ProfCreateApi(CreateAPIView):
    queryset = Absences_Prof.objects.all()
    serializer_class = Absences_ProfSerializer


class Absences_ProfUpdateApi(UpdateAPIView):
    queryset = Absences_Prof.objects.all()
    serializer_class = Absences_ProfSerializer
    lookup_field = 'prof'


class Absences_ProfUpdateApi(RetrieveAPIView):
    queryset = Absences_Prof.objects.all()
    serializer_class = Absences_ProfSerializer
    lookup_field = 'prof'


class Absences_ProfUpdateApi(DestroyAPIView):
    queryset = Absences_Prof.objects.all()
    serializer_class = Absences_ProfSerializer
    lookup_field = 'prof'


##############################################################################
# Cours
##############################################################################


class CoursApi(ListAPIView):
    queryset = Cours.objects.all()
    serializer_class = CoursSerializer


class CoursCreateApi(CreateAPIView):
    queryset = Cours.objects.all()
    serializer_class = CoursSerializer


class CoursUpdateApi(UpdateAPIView):
    queryset = Cours.objects.all()
    serializer_class = CoursSerializer
    lookup_field = 'intitule'


class CoursUpdateApi(RetrieveAPIView):
    queryset = Cours.objects.all()
    serializer_class = CoursSerializer
    lookup_field = 'intitule'


class CoursUpdateApi(DestroyAPIView):
    queryset = Cours.objects.all()
    serializer_class = CoursSerializer
    lookup_field = 'intitule'


##############################################################################
# Promotions
##############################################################################


class PromotionsApi(ListAPIView):
    queryset = Promotions.objects.all()
    serializer_class = PromotionsSerializer


class PromotionsCreateApi(CreateAPIView):
    queryset = Promotions.objects.all()
    serializer_class = PromotionsSerializer


class PromotionsUpdateApi(UpdateAPIView):
    queryset = Promotions.objects.all()
    serializer_class = PromotionsSerializer
    lookup_field = 'name'


class PromotionsUpdateApi(RetrieveAPIView):
    queryset = Promotions.objects.all()
    serializer_class = PromotionsSerializer
    lookup_field = 'name'


class PromotionsUpdateApi(DestroyAPIView):
    queryset = Promotions.objects.all()
    serializer_class = PromotionsSerializer
    lookup_field = 'name'
