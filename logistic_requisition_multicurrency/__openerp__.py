# -*- coding: utf-8 -*-
#
#
#    Copyright 2015 Camptocamp SA
#    Author: Yannick Vaucher
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
#

{"name": "Logistics Requisition - Multicurrency",
 "summary": "Multicurrency management for logistics requistion",
 "version": "0.1.1",
 "author": "Camptocamp,Odoo Community Association (OCA)",
 "license": "AGPL-3",
 "category": "Purchase Management",
 'complexity': "normal",
 "images": [],
 "website": "http://www.camptocamp.com",
 "depends": ["logistic_budget",
             ],
 "demo": [],
 "data": ['view/logistic_requisition.xml',
          'view/logistic_requisition_line.xml',
          'view/logistic_requisition_source.xml',
          ],
 "test": [],
 'installable': True,
 "auto_install": False,
 }
