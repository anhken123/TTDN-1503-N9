from odoo import models, fields, api


class VanBanDiVanBanDi(models.Model):
    _name = 'van_ban_didi'
    _description = 'Bảng chứa thông tin văn bảnbản'

    ten_van_ban = fields.Char("ten_van_banban", required=True)
   
