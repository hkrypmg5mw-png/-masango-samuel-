from django.contrib import admin
from authentication.models import User
from core.models import Facility, AuditLog
from mothers.models import Mother, ANCCheckup
from children.models import Child, GrowthRecord
from vaccinations.models import Vaccine, VaccinationRecord
from appointments.models import Appointment
from notifications.models import SMSNotification, AppNotification
from chat.models import Message

admin.site.register(User)
admin.site.register(Facility)
admin.site.register(AuditLog)
admin.site.register(Mother)
admin.site.register(ANCCheckup)
admin.site.register(Child)
admin.site.register(GrowthRecord)
admin.site.register(Vaccine)
admin.site.register(VaccinationRecord)
admin.site.register(Appointment)
admin.site.register(SMSNotification)
admin.site.register(AppNotification)
admin.site.register(Message)
