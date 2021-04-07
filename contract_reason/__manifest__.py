# -*- coding: utf-8 -*-
{
    'name': "Contract reason - How did you know about us?",

#     'summary': """
#         Short (1 phrase/line) summary of the module's purpose, used as
#         subtitle on modules listing or apps.openerp.com""",

    'description': """
         Includes the field, How did you know about us?, in Sales/Contracts. Editable combo with some preset options
    """,

    'author': "Impulzia",
    'website': "http://www.impulzia.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/openerp/addons/base/module/module_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '12.0.0.0.4',

    # any module necessary for this one to work correctly
    'depends': ['base', 'analytic'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'view.xml',
        'res_config_view.xml'
    ],
    # only loaded in demonstration mode
#     'demo': [
#         'demo.xml',
#     ],
}