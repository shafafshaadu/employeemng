from django.urls import path
# from account.views import Regview,ViewEmp,DeleteEmp,EditEmp,Deptview,DepRet,DepDelete,Depedit,
from .views import *
urlpatterns=[
     path('reg/',Regview.as_view(),name='reg'),
     path('vemp/',ViewEmp.as_view(),name='vemp'),
     path('delemp/<int:id>',DeleteEmp.as_view(),name='delemp'),
     path('editemp/<int:id>',EditEmp.as_view(),name='editemp'),
     path('dept/',Deptview.as_view(),name='dept'),
     path('depr/',DepRet.as_view(),name='depret'),
     path('deptdel/<int:id>',DepDelete.as_view(),name='deptdel'),
     path('deptedit/<int:id>',DeptEdit.as_view(),name='deptedit'),
     path('addman/',ManagerReg.as_view(),name='addman'),
     path('viewman/',ManagerList.as_view(),name='viewman'),
     path('delman/<int:id>',DelMen.as_view(),name='delman'),
     path('index/',Index.as_view(),name='index')

]