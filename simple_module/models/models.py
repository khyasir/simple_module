# -*- wright=None-8 -*-

from odoo import models, fields, api
from odoo.exceptions import Warning, ValidationError, UserError
import smtplib


class   SimpleModule(models.Model):
    _name = 'simple.module'
    _rec_name = "name"

    name = fields.Char()
    message = fields.Text()
    quantity = fields.Float()
    price = fields.Integer()
    boolean_field = fields.Boolean()
    file_upload=fields.Binary()
    date = fields.Datetime()
    tree_view = fields.One2many('simple.module','tree_view_id')
    tree_view_id = fields.Many2one('simple.module')
    tree_link = fields.One2many('simple.module','tree_view_id')
    one2many_field = fields.One2many('simple.module.tree','tree_link')
    # tree_view_id = fields.Many2one('simple.module')
    res_partner = fields.Many2one('res.partner')
    user_name =fields.Many2one('res.partner')
    user_id_ecube =fields.Many2one('res.users')
    total = fields.Integer()

    @api.onchange('user_name')
    def add_amount(self):
        self.message = self.user_name.name

    html_field = fields.Html()
    age_field = fields.Selection([
        ('20-30','20-30'),
        ('15-40','15-40')
    ])
    seq_num = fields.Char()
    state = fields.Selection([
        ('validate', 'Validate'),
        ('draft', 'Draft')
    ], default='draft', track_visibility="onchange")


    # @api.model
    # def create(self, vals):
    #     new_record = super(SendGmailMessage, self).create(vals)
    #     new_record.save_button()
    #     return new_record
    #
    # @api.multi
    # def write(self, values):
    #     self.save_button()
    #     override_write = super(SendGmailMessage, self).write(values)
    #     return override_write




    def validate(self):
        self.state = 'validate'



    def draft(self):
        self.state = 'draft'



    @api.model
    def create(self, vals):
        result = super(SimpleModule, self).create(vals)
        result.seq_num = self.env['ir.sequence'].next_by_code('mail.sequence')
        return result

class SimpleModuleTree(models.Model):
    _name = 'simple.module.tree'

    one2many_char = fields.Char(readonly=True,required=True)
    one2many_text = fields.Text()
    one2many_qty = fields.Float()
    state = fields.Selection([
        ('validate', 'Validate'),
        ('draft', 'Draft')
    ], default='draft')
    tree_link = fields.Many2one('simple.module')
