# -*- coding: utf-8 -*-
#############################################################################
#
#    Cybrosys Technologies Pvt. Ltd.
#
# Copyright (C) 2023-TODAY Cybrosys Technologies(<https://www.cybrosys.com>).
# Author: Cybrosys Techno Solutions (Contact :odoo@cybrosys.com)
#
#    You can modify it under the terms of the GNU AFFERO
#    GENERAL PUBLIC LICENSE (AGPL v3), Version 3.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU AFFERO GENERAL PUBLIC LICENSE (AGPL v3) for more details.
#
#    You should have received a copy of the GNU AFFERO GENERAL PUBLIC LICENSE
#    (AGPL v3) along with this program.
#    If not, see <http://www.gnu.org/licenses/>.
#
#############################################################################
from odoo import models, fields


class ProductProduct(models.Model):
    """Field to hide the product variant in website"""
    _inherit = 'product.product'

    website_hide_variants = fields.Boolean("Hide on Website",
                                           help="Check right if you want to "
                                                "hide the variant in your "
                                                "website")

    def product_read(self, data):
        if data.get('id', False):
            prod_id = int(data.get('id'))
            product = self.sudo().browse(prod_id).read(["website_hide_variants"])
            return product
