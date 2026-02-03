# todos/utils.py
def is_htmx(request) -> bool:
    """Check if the request is an HTMX request."""
    return request.headers.get('HX-Request') == 'true'
