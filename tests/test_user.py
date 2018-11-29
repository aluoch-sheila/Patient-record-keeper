import unittest
from app.models import User,Record,Patient

class UserModelTest(unittest.TestCase):

    def setUp(self):
        self.new_user = User(password = 'james')

    def test_password_setter(self):
        self.assertTrue(self.new_user.pass_secure is not None)

    def test_no_access_password(self):
            with self.assertRaises(AttributeError):
                self.new_user.password

    def test_password_verification(self):
        self.assertTrue(self.new_user.verify_password('james'))


class RecordModelTest(unittest.TestCase):

    def setUp(self):
        self.new_record = Record(id = 1, record = 'ok', docter = 'oj', patient_id = 1)

    def test_instance(self):
        self.assertTrue(isinstance(self.new_record,Record))

    def test_variables(self):
        self.assertEquals(self.new_record.id,1)
        self.assertEquals(self.new_record.record, 'ok')
        self.assertEquals(self.new_record.docter, 'oj')
        self.assertEquals(self.new_record.patient_id, 1)

    # def test_get_record(self):
    #
    #     self.get_record = Record.get_record(1)
    #     self.assertEquals(self.get_record,[])


class PatientModelTest(unittest.TestCase):

    def setUp(self):
        self.new_patient = Patient(id = 1, patient = 322,user_id = 1)

    def test_instance(self):
        self.assertTrue(isinstance(self.new_patient,Patient))

    def test_variables(self):
        self.assertEquals(self.new_patient.id,1)
        self.assertEquals(self.new_patient.patient, 322)
        self.assertEquals(self.new_patient.user_id, 1)

    # def test_get_patient(self):
    #     self.get_patient = Patient.get_patient(1)
    #     self.assertEquals(self.get_patient, [])
    # def test_save_patient(self):
    # #
    #     self.new_patient.save_patient()
    #     self.assertEquals(self.get_patient, [],date_added)
