from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from mainApp.views import *
from statsApp.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', Home.as_view(), name='home'),
    path('tryouts/', Tryouts.as_view(), name='tryouts'),
    path('about/', About.as_view(), name='about'),
    path('clubs/', ClubsView.as_view(), name='clubs'),
    path('davlatlar/<int:pk>/clubs/', CountryClubView.as_view(), name='country-club'),
    path('transfer/', LatestTransfersView.as_view(), name='transfers'),
    path('players/', PlayerView.as_view(), name='player-list'),
    path('u20/', U20View.as_view(), name='u20'),
    path('club-players/<int:pk>', ClubPlayerView.as_view(), name='club-players'),
    path('stats', Stats.as_view(), name='stats'),
    path('transferlar', TransferView.as_view(), name='transferlar'),
    path('tryouts', Tryouts.as_view(), name='tryouts'),
    path('about/', About.as_view(), name='about'),
    path('150transfers', Transfers150View.as_view(), name='150transfers'),
    path('expenditure/', Top50transfersbyexpendeture.as_view(), name='expenditure'),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
