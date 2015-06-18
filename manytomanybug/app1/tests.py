from django.test import TestCase
from manytomanybug.app1.models import FormA, FormB
from manytomanybug.app2.models import Upload

# Create your tests here.

class BugTestCase(TestCase):

    def test_wrong_table_queried(self):
        upload = Upload.objects.create(text="test")

        form = FormA.objects.create(name="form 1")
        form.signature.add(upload)

        query = form.signature.all().query

        # Our form is an instance of FormA
        self.assertTrue(isinstance(form, FormA))
        # The table for FormA is 'app1_forma'
        self.assertEqual(form._meta.db_table, 'app1_forma')

        # The table name of FormA is not in the produced query
        self.assertFalse('app1_forma' in query.tables)

        # However the table FormB is used instead
        self.assertTrue('app1_formb' in query.tables)
