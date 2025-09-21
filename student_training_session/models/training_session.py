# -*- coding: utf-8 -*-
from odoo import models, fields, api
from odoo.exceptions import ValidationError


class TrainingSession(models.Model):
    """Model to manage student training sessions."""
    _name = 'student.training.session'
    _description = 'Student Training Session'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    name = fields.Char('Session Title', required=True, tracking=True)
    trainer_id = fields.Many2one('res.users', string='Trainer',
                                default = lambda self: self.env.uid,
                                required=True, tracking=True,
                                help='Link to the trainer (user)')
    start_date = fields.Date('Start Date', required=True, tracking=True,
                             help='Start date of the training session', default=fields.Date.context_today)
    end_date = fields.Date('End Date', required=True, tracking=True,
                           help='End date of the training session')
    student_ids = fields.Many2many(
        'res.partner',
        string='Students',
        domain=[('is_student', '=', True)],
        tracking=True, help='Students attending the session'
    )
    stage = fields.Selection([
        ('draft', 'Draft'),
        ('ongoing', 'Ongoing'),
        ('completed', 'Completed'),
        ('cancelled', 'Cancelled')
    ], default='draft', copy=False, required=True, tracking=True,
    help='Current stage of the training session')

    attendance_ids = fields.One2many('student.training.attendance', 'session_id',
                                     string='Attendances', help='Attendance records for this session')
    attendance_count = fields.Integer(compute='_compute_attendance_count', string='Attendance Count',
                                      help='Number of attendance records for this session')

    def _compute_attendance_count(self):
        for record in self:
            record.attendance_count = len(record.attendance_ids)


    def action_start_session(self):
        self.ensure_one()
        if self.stage == 'draft':
            # Create attendance records for all students
            attendance_vals = []
            for student in self.student_ids:
                attendance_vals.append({
                    'session_id': self.id,
                    'student_id': student.id,
                    'date': fields.Date.today()
                })
            self.env['student.training.attendance'].create(attendance_vals)
            self.write({'stage': 'ongoing'})

    def action_complete_session(self):
        self.ensure_one()
        if self.stage == 'ongoing':
            self.write({
                'stage': 'completed',
                'end_date': fields.Date.today()
            })

    def action_cancel_session(self):
        self.ensure_one()
        if self.stage in ['draft', 'ongoing']:
            self.write({'stage': 'cancelled'})

    def action_view_attendances(self):
        self.ensure_one()
        return {
            'name': 'Attendances',
            'type': 'ir.actions.act_window',
            'view_mode': 'list,form',
            'res_model': 'student.training.attendance',
            'domain': [('session_id', '=', self.id)],
            'context': {'default_session_id': self.id}
        }

    @api.constrains('start_date', 'end_date')
    def _check_dates(self):
        for record in self:
            if record.start_date and record.end_date:
                if record.start_date > record.end_date:
                    raise ValidationError('End date must be after start date')

    is_user_trainer = fields.Boolean(compute='_compute_is_user_trainer', string='Is User Trainer',
                                     help='Indicates if the current user is the trainer for this session')

    def _compute_is_user_trainer(self):
        for record in self:
            if self.env.uid == record.trainer_id.id:
                record.is_user_trainer = True
            else:
                record.is_user_trainer = False
