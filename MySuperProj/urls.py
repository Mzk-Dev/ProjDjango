from django.conf import settings
from django.conf.urls import url
from django.contrib import admin
from django.contrib.auth.views import LogoutView
from django.urls import path

from mysite import views
from mysite.models import Profile
from mysite.views import ProjectView, SignUpView, User_Login, MyLogoutView, HomeDetailView, CommentsDetail, \
    ProfileView
from mysite.views import CompanyList , ProjectList , CompanyDetail
from django.conf.urls.static import static





urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', ProjectView.as_view(),name='index'),
    path('account/signup/', SignUpView.as_view(), name='signup' ),
    path('companys/',CompanyList.as_view(),name='companys'),
    path('project_detail/<int:pk>/', HomeDetailView.as_view(), name='comments'),
    path('project_detail/<int:pk>/allcomments/',CommentsDetail.as_view(),name='allcomments'),
    path('projects/' , ProjectList.as_view(),name='projects'),
    path('company/<int:pk>/',CompanyDetail.as_view(),name='company_detail'),
    # path('comments', Requirement.as_view(), name='requirements'),
    # path('requirement/<int:comment_id>/<str:opition>', UpdateCommentVote.as_view(), name='requirement_comment_vote'),
    path('login/', User_Login.as_view(), name='login'),
    path('logout/', MyLogoutView.as_view(), name='logout'),
    # path('profile/<int:pk>/detail/',UpdProfile.as_view(),name='profiledetail')
    path('profile/',ProfileView.as_view(),name='profile' ),
    url(r'^edit/$', views.edit, name='edit'),

]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,
document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,
document_root=settings.MEDIA_ROOT)



