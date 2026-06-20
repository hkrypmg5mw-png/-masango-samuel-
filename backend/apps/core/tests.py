from django.test import TestCase
from .sync import smart_merge
from .models import Facility
from django.contrib.auth import get_user_model
from apps.patients.models import Mother
import datetime

User = get_user_model()

class SyncTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testmother', role='MOTHER')
        self.mother = Mother.objects.create(
            user=self.user,
            date_of_birth=datetime.date(1990, 1, 1),
            emergency_contact_name='Contact',
            emergency_contact_phone='12345'
        )

    def test_smart_merge_updates_field(self):
        local_data = {'emergency_contact_name': 'New Contact'}
        updated_mother, fields = smart_merge(local_data, self.mother)
        self.assertEqual(updated_mother.emergency_contact_name, 'New Contact')
        self.assertIn('emergency_contact_name', fields)

    def test_smart_merge_ignores_null(self):
        local_data = {'emergency_contact_name': None, 'emergency_contact_phone': '999'}
        updated_mother, fields = smart_merge(local_data, self.mother)
        self.assertEqual(updated_mother.emergency_contact_name, 'Contact')
        self.assertEqual(updated_mother.emergency_contact_phone, '999')
        self.assertEqual(fields, ['emergency_contact_phone'])
