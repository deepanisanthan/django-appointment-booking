from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action
from .models import Patient, Doctor, Appointment
from .serializers import PatientSerializer, DoctorSerializer, AppointmentSerializer

class PatientViewSet(viewsets.ModelViewSet):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer

class DoctorViewSet(viewsets.ModelViewSet):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer

class AppointmentViewSet(viewsets.ModelViewSet):
    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer

    @action(detail=True, methods=['get'])
    def patient_appointments(self, request, pk=None):
        """Retrieve appointments for a specific patient."""
        patient = self.get_object()
        appointments = patient.appointments.all()
        serializer = AppointmentSerializer(appointments, many=True)
        return Response(serializer.data)
