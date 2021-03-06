# © 2013-2017 Therp BV <http://therp.nl>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).
{
    'name': 'CAMT Format Bank Statements Import',
    'version': '2.0.0',
    'license': 'AGPL-3',
    'author': 'FlectraHQ, Odoo Community Association (OCA), Therp BV',
    'website': 'https://github.com/OCA/bank-statement-import',
    'category': 'Banking addons',
    'depends': [
        'account_bank_statement_import',
    ],
    'data': [
        'views/account_bank_statement_import.xml',
    ],
}
