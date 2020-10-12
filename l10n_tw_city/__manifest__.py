# -*- coding: utf-8 -*-
# # Copyright (C) 2020 Mick Tseng, Odoo Taiwan - suncombo@gmail.com

{
    'name': 'Taiwan - City',
    'version': '1.1',
    'category': 'Localizations',
    'description': """
提供台灣縣市及郵遞區號資料，以及調整地址欄位
==============================================================================
    """,
    'depends': [
        'base_address_city',
        'l10n_tw',
    ],
    'data': [
        'data/res.city.csv',
        'views/res_partner_views.xml',
    ],
}
