from django.urls import path
from .views import SAIDFormView, SAIDResultView
from django.views.generic import RedirectView

# URL patterns for the SA ID Validation application
urlpatterns = [
    path(
        "", 
        RedirectView.as_view(url='validate-sa-id/', permanent=False), 
        name="home"
    ),
    path(
        "validate-sa-id/", 
        SAIDFormView.as_view(), 
        name="validate-sa-id"
    ),
    path(
        "sa-id-result/<int:pk>/", 
        SAIDResultView.as_view(), 
        name="sa-id-result"
    ),
]
