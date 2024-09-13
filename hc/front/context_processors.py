from __future__ import annotations

from django.conf import settings
from django.http import HttpRequest


def branding(request: HttpRequest) -> dict[str, str | None]:
    return {
        "site_name": settings.SITE_NAME,
        "site_logo_url": settings.SITE_LOGO_URL,
    }

def show_documentation(request: HttpRequest)-> dict[str, bool]:
    return {'show_doc': settings.SHOW_DOC}

def show_footer(request: HttpRequest)-> dict[str, bool]:
    return {'show_footer': settings.SHOW_FOOTER}