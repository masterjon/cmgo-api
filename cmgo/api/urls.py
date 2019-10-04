from django.urls import path, re_path
from django.conf.urls import include
from api import views
# from rest_framework_nested import routers
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register(r'slides', views.SlideViewSet)

# router.register(r'categories', views.AnimalCategoryViewSet, base_name='categories')
# router.register(r'markers-categories', views.CategoryMarkerViewSet, base_name='categories_markers')

# category_router = routers.NestedSimpleRouter(router, r'categories', lookup='category')

# category_router.register(r'animal', views.AnimalViewSet, base_name='animal_detail')

urlpatterns = [
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    re_path(r'^', include(router.urls)),
    path('social/', views.Social.as_view(), name="social"),
    path('get-picture-facebook/', views.get_picture_facebook, name='get-picture-facebook'),
    # url(r'activity_dates', views.ActivityDatesViewSet.as_view())
    # url(r'^', include(category_router.urls)),
    # url(r'^related-animals/$', views.RelatedAnimalsView.as_view(), name='related_animals'),
]
