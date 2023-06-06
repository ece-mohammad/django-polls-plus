from django.http import HttpRequest, HttpResponse
from django.template import loader


def build_page(title: str, body: str, request: HttpRequest) -> str:
    """Build page from given fields (title, body, footer and HttpRequest)"""
    page_template = loader.get_template("polls/base_page.html")
    page_context = {
        "title": title,
        "content": body,
    }

    return page_template.render(page_context, request)

