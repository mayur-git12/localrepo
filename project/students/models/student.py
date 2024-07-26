from odoo import fields, models, api, _
from odoo.exceptions import ValidationError
import base64


class Student(models.Model):
    _name = 'wb.student'
    _description = "This is student profile"

    name = fields.Char("Name", required=True)
    email = fields.Text("Email", required=True)
    school_id = fields.Many2one('wb.school', string="School")
    student_photo = fields.Binary("Image")
    roll_number = fields.Integer("Roll Number")
    School_type = fields.Selection([
        ('primary', 'Primary'),
        ('secondary', 'Secondary')
    ], string="Select Type", )
    habit = fields.Text("Habit")
    height = fields.Float("Height")
    is_enrolled = fields.Boolean("Enrolled", default=True)
    enroll_date = fields.Date("Enrollment Date")
    join_datetime = fields.Datetime("Joining Datetime")
    state = fields.Selection([
        ('draft', 'draft'),
        ('mail_sent', 'Mail sent')
    ], string="Status", default="draft")
    status = fields.Selection([
        ('junior', 'Junior'),
        ('senior', 'Senior')
    ], string="Status")
    course_ids = fields.Many2many('wb.course', string="Courses")

    schooll_id = fields.One2many('wb.school', 'schools_ids', string="More School")

    @api.onchange('School_type')
    def _onchange_school_type(self):
        if self.School_type:
            self.schooll_id = self.env['wb.school'].search([('School_type', '=', self.School_type)])
        else:
            self.schooll_id = False

    def action_send_mail(self):
        report_ref = 'students.student_report_action'
        template_ref = 'students.student_email_template'

        # Fetch the report action using the XML ID
        report_action = self.env.ref(report_ref)
        if report_action:
            # Generate PDF
            pdf_content, _ = report_action._render_qweb_pdf([self.id])

            # Encode the PDF to base64
            report_base64 = base64.b64encode(pdf_content)

            # Create an attachment
            attachment = self.env['ir.attachment'].create({
                'name': 'Student Report - %s.pdf' % self.name,
                'type': 'binary',
                'datas': report_base64,
                'res_model': self._name,
                'res_id': self.id,
                'mimetype': 'application/pdf'
            })

            # Get the email template
            template = self.env.ref(template_ref)
            if template:
                email_template = template.sudo().copy({
                    'attachment_ids': [(6, 0, [attachment.id])]
                })
                email_template.send_mail(self.id, force_send=True)

                # Update the state
                self.state = 'mail_sent'
            else:
                raise ValidationError(_("Email template '%s' not found!" % template_ref))

    @api.model
    def create(self, vals):
        student = super(Student, self).create(vals)
        student._create_res_partner()  # Call on the student instance
        return student

    def _create_res_partner(self):
        partner_vals = {
            'name': self.name,
            'email': self.email,
            'image_1920': self.student_photo,
            'comment': _("Student Profile"),
            'type': 'contact',
        }
        self.env['res.partner'].create(partner_vals)
