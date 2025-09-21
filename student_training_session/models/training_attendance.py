# -*- coding: utf-8 -*-
from odoo import models, fields, api


class TrainingAttendance(models.Model):
    """Model to track attendance of students in training sessions."""
    _name = 'student.training.attendance'
    _description = 'Training Session Attendance'
    _rec_name = 'student_id'

    session_id = fields.Many2one('student.training.session', required=True, ondelete='cascade',
                                 help='Link to the training session')
    student_id = fields.Many2one('res.partner', required=True, domain=[('is_student', '=', True)],
                                 help='Link to the student')
    date = fields.Date('Date', required=True, help='Attendance date')
    state = fields.Selection([
        ('present', 'Present'),
        ('absent', 'Absent')
    ], string='Status', default='present', required=True,
    help='Attendance status')
