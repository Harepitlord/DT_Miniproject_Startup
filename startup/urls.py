
"""Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path
from startup import views


app_name='startup'
urlpatterns = [
    path('', views.Homepage.as_view(),name='HomePage'),
    path('Home',views.DashBoard.as_view(),name='DashBoard'),
    path('About', views.About.as_view(),name='About'),
    path('Profile', views.Profile.as_view(), name='Profile'),
    path('Signup', views.Signup.as_view(), name='Signup'),
    path('Post',views.Post.as_view(),name='Post'),
    path('CompanyProfile',views.CompanyProfile.as_view(),name='CompanyProfile'),
]
