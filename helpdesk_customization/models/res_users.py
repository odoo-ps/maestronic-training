from odoo import fields, models


class ResUsers(models.Model):
    _inherit = "res.users"

    is_customer_user = fields.Boolean("Customer", default=False)

    def add_remove_user_groups(self):
        """adding group internal user+

        depending on whether they are a customer user. If they are not, they will be added to the internal group+
        else, they will be removed
        """
        internal_plus = self.filtered(lambda x: not x.is_customer_user)
        non_internal_plus = self - internal_plus

        # add or remove group
        internal_plus.groups_id = [(4, self.env.ref('helpdesk_customization.group_user_plus').id)]
        non_internal_plus.groups_id = [(3, self.env.ref('helpdesk_customization.group_user_plus').id), (4, self.env.ref('helpdesk_customization.group_customer').id)]
