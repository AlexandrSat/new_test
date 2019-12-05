from objectpack.actions import ObjectPack, SelectorWindowAction
from objectpack.ui import ModelEditWindow

from .controller import observer
from . import models
from .ui import UserAddWindow

class ContentTypePack(ObjectPack):
    model = models.ContentType
    add_to_desktop = add_to_menu = True
    edit_window = add_window = ModelEditWindow.fabricate(
        model,
        model_register=observer,
    )

    def extend_menu(self, menu):
        return (
            menu.dicts(
                menu.Item('Content Types', self)
            )
        )



class GroupPack(ObjectPack):
    model = models.Group
    add_to_desktop = add_to_menu = True
    edit_window = add_window = ModelEditWindow.fabricate(
        model,
        model_register=observer
    )

    def extend_menu(self, menu):
        return (
            menu.dicts(
                menu.Item('Groups', self)
            )
        )

class PermissionPack(ObjectPack):
    model = models.Permission
    add_to_desktop = add_to_menu = True
    edit_window = add_window = ModelEditWindow.fabricate(
        model,
        model_register=observer,
        field_list=[
            'name',
            'content_type_id',
            'codename',
        ],
    )
    columns = [
        {
            'data_index': 'fullname',
            'header': 'Наименование',
        }
    ]

class UserPack(ObjectPack):
    model = models.User
    add_to_desktop = add_to_menu = True
    #edit_window = add_window = ModelEditWindow.fabricate(
    #     model,
    #     model_register=observer,
    #     field_list=[
    #         'name',
    #         'password',
    #         'email',
    #         'group_id'
    #     ],
    # )

    edit_window = add_window = UserAddWindow 

    columns = [
        {
            'data_index': 'name',
            'header': 'Name',
            'sortable': True,
            'sort_fields': ('name',),
            'filter': {
                'type': 'string',
                'custom_field': ('name',)
            }
        },
        {
            'data_index': 'email',
            'header': 'E-mail',
            'sortable': True,
            'sort_fields': ('email',),
            'filter': {
                'type': 'string',
                'custom_field': ('email',)
            }
        },
        {
            'data_index': 'group',
            'header': 'Group',
        },
    ]
