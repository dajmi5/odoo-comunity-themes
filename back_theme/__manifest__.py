# -*- coding: utf-8 -*-
{
    'name': "Back Theme",

    'summary': """ Custom Settings for Backend """,

    'description': """
    
- Custom Settings for Backend
    """,

    'author': "AWWEA SAS",
    'website': "https://www.awwea.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Theme',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['web_responsive'],
    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/assets.xml',
        'views/config_parameter.xml'
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}