"""User admin classes."""

#Django
from django.contrib import admin

#models
from users.models import Profile

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
	"""Profile Admin"""
	#Lista de los atributos que mostrara en el admin
	list_display = ('pk','user','phone_number','website','picture')
	#Lista de links que llevan al detalle
	list_display_links = ('pk','user')
	#Lista de editables in situ
	list_editable = ('phone_number','website','picture')
	#Campos en los que se puede buscar
	search_fields = ('user__email','user__username','user__first_name', 'user__last_name','phone_number')
	#Campos por los que se puede filtrar
	list_filter = (
		'user__is_active',
		'user__is_staff',
		'created',
		'modified',
	)