from website.models import *
from django import template

register = template.Library()


@register.inclusion_tag("partials/footer.html")
def practice(self):
    services = Service.objects.first()

    return {"services": services}
