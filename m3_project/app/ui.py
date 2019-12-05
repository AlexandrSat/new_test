from objectpack.ui import BaseEditWindow, _create_dict_select_field
from m3_ext.ui import all_components as ext
from django.db import models as django_models
from .models import User
from .controller import observer

class UserAddWindow(BaseEditWindow):

    def _init_components(self):
        super(UserAddWindow, self)._init_components()

        self.field__name = ext.ExtStringField(
            label='Name',
            name='name',
            allow_blank=False,
            anchor='100%'
        )

        self.field__passoword = ext.ExtStringField(
            label='Password',
            name='password',
            allow_blank=False,
            anchor='100%'
        )

        self.field__email = ext.ExtStringField(
            label='E-mail',
            name='email',
            allow_blank=False,
            anchor='100%'
        )

        params = {
            'label': 'Group',
            'name': 'group',
            'anchor': '100%'
        }

        for f in User._meta.fields:
            if isinstance(f, django_models.ForeignKey):
                self.field__group = _create_dict_select_field(f,
                    model_register=observer,
                    **params
                )


    def _do_layout(self):
        super(UserAddWindow, self)._do_layout()
        self.form.items.extend((
            self.field__name,
            self.field__passoword,
            self.field__email,
            self.field__group,
        ))

    def set_params(self, params):
        super(UserAddWindow, self).set_params(params)
        self.height = 'auto'