from django.conf.urls import url
from objectpack import desktop
from app.controller import controller
from . import actions

def register_urlpatterns():
	"""
	Регистрация конфигурации урлов для приложения
	"""
	return [url(*controller.urlpattern)]

def register_actions():
	"""
	Регистрация экшн-паков
	"""
	return controller.packs.extend([
		actions.UserPack(),
		actions.ContentTypePack(),
		actions.GroupPack(),
		actions.PermissionPack(),
	])

def register_desktop_menu():
	"""
	Регистрация элементов рабочего стола
	"""
	desktop.uificate_the_controller(
		controller
	)