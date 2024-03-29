from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import (CustomUserViewSet, IngredientViewSet, RecipeViewset,
                    SubscribeView, SubscriptionsList, TagViewSet)

router = DefaultRouter()
router.register(r'users', CustomUserViewSet, basename='users')
router.register(r'tags', TagViewSet, basename='tags')
router.register(r'ingredients', IngredientViewSet, basename='ingredients')
router.register(r'recipes', RecipeViewset, basename='recipes')

urlpatterns = [
    path(r'users/subscriptions/', SubscriptionsList.as_view({'get': 'list'})),
    path(r'users/<int:user_id>/subscribe/', SubscribeView.as_view()),
    path('', include(router.urls)),
    path('', include('djoser.urls')),
    path('auth/', include('djoser.urls.authtoken')),
]
