from django.urls import include, path
from django.contrib import admin

urlpatterns = [

	
    path('polls/', include('polls.urls')),
    path('admin/', admin.site.urls),
    path('HanksBank3/', include('HanksBank3.urls')),


    


]
#urlpatterns = patterns('', url(r'^hello, 'HanksBank3.views.hello'), 
#	url(r'^admin/', include(admin.site.urls)),
#	)
