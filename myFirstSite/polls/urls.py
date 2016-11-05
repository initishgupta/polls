from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static


from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^left-sidebar.html', views.leftSidebar, name='leftSidebar'),
    url(r'^right-sidebar.html', views.rightSidebar, name='rightSidebar'),
    url(r'^index.html', views.index, name='index'),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
