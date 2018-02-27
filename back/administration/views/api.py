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


class ElevesSearchApi(RetrieveAPIView):
    queryset = Eleves.objects.all()
    serializer_class = ElevesSerializer
    lookup_field = 'nom'


class ElevesDeleteApi(DestroyAPIView):
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


class SpecialiteSearchApi(RetrieveAPIView):
    queryset = Specialite.objects.all()
    serializer_class = SpecialiteSerializer
    lookup_field = 'nom'


class SpecialiteDeleteApi(DestroyAPIView):
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


class Specialite_EleveSearchApi(RetrieveAPIView):
    queryset = Specialite_Eleve.objects.all()
    serializer_class = Specialite_EleveSerializer
    lookup_field = 'eleve'


class Specialite_EleveDeleteApi(DestroyAPIView):
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


class Absences_EleveSearchApi(RetrieveAPIView):
    queryset = Absences_Eleve.objects.all()
    serializer_class = Absences_EleveSerializer
    lookup_field = 'eleve'


class Absences_EleveDeleteApi(DestroyAPIView):
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


class ProfSearchApi(RetrieveAPIView):
    queryset = Prof.objects.all()
    serializer_class = ProfSerializer
    lookup_field = 'nom'


class ProfDeleteApi(DestroyAPIView):
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


class Prof_PromotionSearchApi(RetrieveAPIView):
    queryset = Prof_Promotion.objects.all()
    serializer_class = Prof_PromotionSerializer
    lookup_field = 'prof'


class Prof_PromotionDeleteApi(DestroyAPIView):
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


class Absences_ProfSearchApi(RetrieveAPIView):
    queryset = Absences_Prof.objects.all()
    serializer_class = Absences_ProfSerializer
    lookup_field = 'prof'


class Absences_ProfDeleteApi(DestroyAPIView):
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


class CoursSearchApi(RetrieveAPIView):
    queryset = Cours.objects.all()
    serializer_class = CoursSerializer
    lookup_field = 'intitule'


class CoursDeleteApi(DestroyAPIView):
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


class PromotionsSearchApi(RetrieveAPIView):
    queryset = Promotions.objects.all()
    serializer_class = PromotionsSerializer
    lookup_field = 'name'


class PromotionsDeleteApi(DestroyAPIView):
    queryset = Promotions.objects.all()
    serializer_class = PromotionsSerializer
    lookup_field = 'name'
