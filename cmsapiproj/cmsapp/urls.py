from rest_framework.routers import DefaultRouter
from .import views
from django.urls import path, include

#getting the url request from user and route the user to appropriate views

#create a DefaultRouter class instances(obj)
router = DefaultRouter()
#register the url endpoint to each views
router.register(r'departments',views.DepartmentViewSet)
router.register(r'doctors',views.DoctorViewSet)
router.register(r'prescriptions',views.PrescriptionViewSet)
router.register(r'users',views.UserDetailsViewSet)
router.register(r'medicines',views.MedicineViewSet)
router.register(r'labtests',views.LabTestViewSet)
router.register(r'receptionist',views.ReceptionistViewSet)
router.register(r'patient',views.PatientViewSet)
router.register(r'appointments',views.AppointmentViewSet)


#since our register and login views are not viewsets, we need to use the `include` function to include them in the router
#convert the urls to urls patterns

urlpatterns = [
    path("signup/", views.SignupAPIView.as_view(), name="user-signup"),
    path("login/", views.LoginAPIView.as_view(), name="user-login"),
]

urlpatterns += router.urls