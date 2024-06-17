# -*- coding: utf-8 -*-
{
    'name': "new_document_module",
    'summary': "A module which has document and employee many-to-many relation",
    'description': """
        Long description of the module's purpose.
    """,
    'author': "ArbatosPakelis",
    'website': "https://www.yourcompany.com",
    'category': 'Extra Tools',
    'version': '0.1',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/document.xml',
        'views/employee.xml',
        'views/document_filter_wizard.xml',
    ],
    'demo': [],
    'application': True,
    'test': [
        'tests/test_document.py',
    ],
}

