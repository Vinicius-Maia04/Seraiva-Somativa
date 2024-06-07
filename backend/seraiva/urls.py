from .views import *
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register(r'customuser', CustomUserAPIView)
router.register(r'author', AuthorAPIView)
router.register(r'category', CategoryAPIView)
router.register(r'book', BookAPIView)
router.register(r'borrowing', BorrowingAPIView)

urlpatterns = router.urls