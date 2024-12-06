from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import AccountingViewSet, BusinessViewSet, ModeViewSet, LedgerViewSet, HeadViewSet, TypeViewSet

router = DefaultRouter()
router.register(r'accounting', AccountingViewSet)
router.register(r'businesses', BusinessViewSet)
router.register(r'modes', ModeViewSet)
router.register(r'ledgers', LedgerViewSet)  # Register LedgerViewSet
router.register(r'heads', HeadViewSet)
router.register(r'type', TypeViewSet)

urlpatterns = [
    path('api/', include(router.urls)),  # This includes all the viewsets defined in the router
]
