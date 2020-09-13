from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin
from rest_framework.authtoken.views import obtain_auth_token
from django.urls import path
from django.conf.urls import include
from core import urls, views
from accountapp.views import user_details, user_details_video
from core.views import CreateVid
urlpatterns = [
    path('admin/', admin.site.urls),

    path('api/', include(urls)),
    path('', views.FPage),
    path('ShowMeApp/', views.ShowMeApp),
    path('Account/', include('accountapp.urls')),
    path('user_details/<id>', user_details, name='user_details'),
    path('user_details_video/<id>', user_details_video, name='user_details_video'),
    path('ShowMeApp/CreateVid/',CreateVid,name='CreateVid')
]

urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
