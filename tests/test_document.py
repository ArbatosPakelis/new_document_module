from odoo.tests import common


class TestDocument(common.TransactionCase):

    def setUp(self):
        super(TestDocument, self).setUp()
        # Create an employee to be used in tests
        self.employee = self.env['new_document_module.employee'].create({
            'name': 'Test Employee',
        })

    def test_create_document(self):
        # Create a document
        document = self.env['new_document_module.document'].create({
            'name': 'Test Document',
            'description': 'This is a test document',
            'company': 'Test Company',
            'creator': 'Test Creator',
            'employee_ids': [(6, 0, [self.employee.id])]
        })
        # Check if the document was created
        self.assertTrue(document)
        self.assertEqual(document.name, 'Test Document')
        self.assertIn(self.employee, document.employee_ids)
        print("TEST WAS RUN")
