# -*- coding: utf-8 -*-
from odoo import models, fields


class ResPartner(models.Model):
    """Inherit res.partner to add is_student field."""
    _inherit = 'res.partner'

    is_student = fields.Boolean('Is Student', default=False,
                                help='Check if the contact is a student')
