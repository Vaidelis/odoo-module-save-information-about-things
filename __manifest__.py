# -*- coding: utf-8 -*-
{
    'name': "Save information",

    'summary': """
        Module for saving information about items""",

    'description': """
        Module can save information about items and declare for which company item belongs
    """,

    'author': "Vaidas",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/13.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'security/security.xml',
        'views/save_information.xml',
        'views/information_report_view.xml',
        'report/information_details.xml',
        'report/report.xml',
    ],
}
