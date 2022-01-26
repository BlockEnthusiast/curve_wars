# """Add Address Forms."""
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import (
    DataRequired,
    Email,
    EqualTo,
    Length,
    Optional
)


class AddAddressForm(FlaskForm):
    """User Sign-up Form."""
    address = StringField(
        'Address',
        validators=[DataRequired()]
    )

    nickname = StringField(
        'Nickname',
        validators=[
        ]
    )

    submit = SubmitField('Add Address')
