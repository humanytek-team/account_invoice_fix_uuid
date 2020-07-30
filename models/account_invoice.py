# -*- coding: utf-8 -*-
import base64
import importlib


from odoo import _, api, fields, models


class AccountInvoice(models.Model):
    _inherit = 'account.invoice'

    def _import(self, module):
        return importlib.import_module(module)

    def _to_base64(self, data):
        return base64.b64decode(data)
