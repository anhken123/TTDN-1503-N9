from odoo import models, fields, api


class VanBanDiVanBanDi(models.Model):
    _name = 'van_ban_di'
    _description = 'Bảng chứa thông tin văn bảnbản'

    ten_van_ban = fields.Char("ten_van_ban", required=True)
   
