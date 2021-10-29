{
    "name": "Helpdesk Customization",
    # Explain the purpose of the module
    "summary": """
        Additional information on helpdesk.ticket with additional fields related to JIRA.
        """,
    "category": "",
    "version": "14.0.1.0.0",
    "author": "Odoo PS",
    "website": "https://www.odoo.com",
    "license": "OEEL-1",
    # Check depends order uncomment if necessary
    "depends": [
        'helpdesk_repair',
    ],
    # Check data order
    "data": [
        "security/res_groups.xml",
        "security/ir.model.access.csv",
        "security/ir_rule.xml",
        "views/helpdesk_concession.xml",
        "views/helpdesk_ticket.xml",
        "views/repair_order.xml",
        "views/res_users.xml",
        "views/res_partner.xml",
        "views/helpdesk_team.xml",
        "views/helpdesk_category.xml",
        "views/product_template.xml",
        "views/menus.xml",
        "data/server_action.xml",
    ],
    # Only used to link to the analysis / Ps-tech store
    "task_id": [2675153],
}
