# -*- coding: utf-8 -*-
# Copyright (C) 2020 Mick Tseng, Odoo Taiwan - suncombo@gmail.com

{
    'name': 'Taiwan - Accounting',
    'author': ['Odoo Taiwan'],
    'website': 'https://www.facebook.com/groups/odoo.taiwan',
    'version': '1.1',
    'category': 'Accounting/Localizations/Account Charts',
    'description': """
這是一個在Odoo管理會計科目表的基礎模組
data/account.account.template.sems.csv 為中小企業會計科目，參考經濟部商業司提供「商業會計項目表」(https://gcis.nat.gov.tw/mainNew/doc/acc_1041222.doc)
此檔案可針對自己會計需要修改後手動匯入，此模組不自動安裝此科目表
==============================================================================
    """,
    'depends': [
        'account',
    ],
    'data': [
        'data/l10n_tw.xml',
        'data/account.account.template.csv',
        'data/l10n_tw_post.xml',
        'data/res.bank.csv',
        'data/res.country.state.csv',
    ],
    'uninstall_hook': 'uninstall_hook',
}
