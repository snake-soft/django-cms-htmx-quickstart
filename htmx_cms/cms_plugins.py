from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from cms.models.pluginmodel import CMSPlugin
from django.utils.translation import gettext_lazy as _
from djangocms_frontend.contrib.link.cms_plugins import LinkPlugin
from .forms import HtmxLinkForm


@plugin_pool.register_plugin
class HtmxOnlyPlugin(CMSPluginBase):
    module = _('Htmx')
    name = _('Htmx only content')
    allow_children = True
    render_template = "htmx_cms/plugins/htmx_only.html"


@plugin_pool.register_plugin
class NonHtmxOnlyPlugin(CMSPluginBase):
    model = CMSPlugin
    module = _('Htmx')
    name = _('Non Htmx only content')
    allow_children = True
    render_template = "htmx_cms/plugins/non_htmx_only.html"
