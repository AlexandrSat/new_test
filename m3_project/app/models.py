from django.db import models

class ContentType(models.Model):
    name = models.CharField('Type', max_length=50)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Content Types'
        verbose_name_plural = 'Content Types'

class Group(models.Model):
    name = models.CharField('Group', max_length=50)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Group'
        verbose_name_plural = 'Group'


class User(models.Model):
    name = models.CharField('Name', max_length=50)
    password = models.CharField('Password', max_length=50)
    email = models.EmailField('E-mail', max_length=50)
    group = models.ForeignKey(
        'Group',
        verbose_name='Group',
        related_name='group_set',
        null=True, blank=True,
    )

    class Meta:
        verbose_name = 'Users'
        verbose_name_plural = 'Users'


class Permission(models.Model):
    name = models.CharField('Name', max_length=50)
    content_type = models.ForeignKey(
        'ContentType',
        verbose_name='Content Type',
        related_name='contenttype_set',
        null=True, blank=True,
    )
    codename = models.CharField('Codename', max_length=50)

    @property
    def fullname(self):
        return ' | '.join((self.codename, self.content_type.name, self.name))

    class Meta:
        verbose_name = 'Permissions'
        verbose_name_plural = 'Permissions'