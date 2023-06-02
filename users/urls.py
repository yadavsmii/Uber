from django.urls import path,include
from .views import *

urlpatterns = []

from users.urls import *

urlpatterns += [
    path('get-all-students', GetStudentsView.as_view()),
    path('get-and-save-orders',GetOrdersView.as_view()),
    path('delete-student/<int:pk>',DeleteStudentView.as_view()),
    path('delete-orders/<int:pk>',DeleteOrdersView.as_view()),
    path('students-details-address/<int:pk>',StudentsDetailsAddressView.as_view()),
    path('delete-students-details-address/<int:pk>',DeleteStudentsAddressView.as_view()),
    path('update-students-details/<int:pk>',StudentsUpdateView.as_view()),
]