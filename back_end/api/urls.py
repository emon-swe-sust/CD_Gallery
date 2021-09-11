from django.urls import path, include
from .views import apiOverview

urlpatterns = [

    path('', apiOverview, name="api-overview"),

    path('accounts/', include('accounts.urls'))

]