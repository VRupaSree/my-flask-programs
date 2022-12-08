from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField

class AddForm(FlaskForm):

    name = StringField('name of student: ')
    submit = SubmitField('add student:')

class DelForm(FlaskForm):

    id = IntegerField('id no. of the student to remove: ')
    submit = SubmitField('remove student:')

class AddFatherForm(FlaskForm):

    name = StringField('name of father:')
    stu_id = IntegerField('id of student:')
    submit = SubmitField('add student father name:')

