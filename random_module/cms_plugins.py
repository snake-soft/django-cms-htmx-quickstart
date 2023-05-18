from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from cms.models.pluginmodel import CMSPlugin
from django.utils.translation import gettext_lazy as _


@plugin_pool.register_plugin
class CodeRunnerPlugin(CMSPluginBase):
    model = CMSPlugin
    render_template = "random_module/code_runner.html"
    cache = True
    name = _("Code Runner")
