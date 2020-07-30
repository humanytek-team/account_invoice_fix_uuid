# -*- coding: utf-8 -*-
import base64

from odoo import _, api, fields, models


class AccountInvoice(models.Model):
    _inherit = 'account.invoice'

    def _to_base64(self, data):
        return base64.b64decode(data)

    def _fix_uuids(self):
        invoices = self.search([
            ('number', '!=', False),
            ('l10n_mx_edi_cfdi_uuid', '=', ''),
            ('state', '=', 'open'),
            ('type', '=', 'out_invoice'),
        ])

        res = ''

        for r in invoices:
            first_attachment = self.env['ir.attachment'].search(
                [
                    ('res_model', '=', self._name),
                    ('res_id', '=', r.id),
                ],
                order='create_date',
                limit=1,
            )
            if first_attachment.datas_fname[-3:] == 'xml':
                res += '{} {} {}\n'.format(r.number, first_attachment.datas_fname, xml)

        return res
