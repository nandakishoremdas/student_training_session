# -*- coding: utf-8 -*-
#############################################################################
#
#    Author: Nandakishore M(<https://nandakishore.odoo.com/>)
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
{
    'name': 'Student Training Sessions',
    'version': '18.0.1.0.0',
    'category': 'Education',
    'summary': 'Manage student training sessions',
    'description': """
        Manage student training sessions with Session details
    """,
    'maintainer': 'Nandakishore M',
    'company': 'Nandakishore M',
    'website': 'https://nandakishore.odoo.com/',
    'depends': ['base', 'contacts'],
    'data': [
        'security/training_security.xml',
        'security/ir.model.access.csv',

        'views/res_partner_views.xml',
        'views/training_session_views.xml',
        'views/student_training_attendance.xml',

        'reports/report_training_session.xml',
    ],
    'installable': True,
    'application': True,
    'license': 'LGPL-3',
}
