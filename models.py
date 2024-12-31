from django.db import models

class Patient(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    date_of_birth = models.DateField()
    phone_number = models.CharField(max_length=15)
    email = models.EmailField()
    address = models.TextField()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Doctor(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    specialty = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=15)
    email = models.EmailField()
    office_address = models.TextField()

    def __str__(self):
        return f"Dr. {self.first_name} {self.last_name}"

class Appointment(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name="appointments")
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE, related_name="appointments")
    appointment_date = models.DateTimeField()
    reason_for_visit = models.TextField()

    def __str__(self):
        return f"Appointment with {self.doctor} on {self.appointment_date}"
