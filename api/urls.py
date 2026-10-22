from django.urls import path
from rest_framework.routers import SimpleRouter
from .views import AuthorViewSet, BookViewSet

router = SimpleRouter()
router.register('book', BookViewSet)
router.register('auther', AuthorViewSet)


urlpatterns = router.urls