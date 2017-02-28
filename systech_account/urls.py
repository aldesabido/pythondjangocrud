
from django.conf.urls import url, handler404,patterns,include
from django.conf import settings as root_settings
from django.conf.urls.static import static

from systech_account.views import crud,common

urlpatterns = [
	url(r'^$', crud.home, name='home'),
	url(r'^crud/$', crud.home, name='home'),
	url(r'^crud/create_dialog/$', crud.create_dialog),
	url(r'^crud/create/$', crud.create),
	url(r'^crud/read/$', crud.read),
	url(r'^crud/edit/$', crud.edit),
	url(r'^crud/delete/(?P<id>[0-9]+)$', crud.delete),
 # 	url(r'^customers/$', customers.redirect_page),
	# url(r'^customer/create_dialog/$', customers.create_dialog),
	# url(r'^customer/create/$', customers.create),
	# url(r'^customer/load_to_edit/(?P<customer_id>[0-9]+)$', customers.load_to_edit),
	# url(r'^customer/read_pagination/$', customers.read_pagination),
	# url(r'^customer/read_generic/$', customers.read_generic),
	# url(r'^customer/read_generic/(?P<customer_id>[0-9]+)$', customers.read_generic),
	# url(r'^customer/read_for_transaction/$', customers.read_for_transaction),
	# url(r'^customer/delete/(?P<customer_id>[0-9]+)$', customers.delete),
]
urlpatterns += static(root_settings.STATIC_URL,document_root=root_settings.STATIC_ROOT)
urlpatterns += static(root_settings.MEDIA_URL,document_root=root_settings.MEDIA_ROOT)
