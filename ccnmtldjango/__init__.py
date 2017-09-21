from paste.script import templates
import pkg_resources


class CcnmtlDjangoTemplate(templates.Template):
    egg_plugins = ["CcnmtlDjangoTemplate"]
    _template_dir = pkg_resources.resource_filename("ccnmtldjango", "template")
    summary = "Columbia CTL Django template"
    required_templates = []
