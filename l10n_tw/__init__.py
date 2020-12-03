# -*- coding: utf-8 -*-
# Copyright (C) 2020 Mick Tseng, Odoo Taiwan - suncombo@gmail.com

import babel.core

babel.core.LOCALE_ALIASES['zh'] = 'zh_TW'


def uninstall_hook(cr, registry):
    cr.execute(
        "DELETE FROM ir_model_data WHERE module = 'l10n_tw'"
    )
