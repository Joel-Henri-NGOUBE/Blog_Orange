from django.shortcuts import resolve_url

def get_route_params(route: str = ""):
    url: str = resolve_url(route)
    global_route_name: str = url.split("/")[-1]
    context: dict = {
        "url": url,
        "global_route_name": global_route_name,
    }
    return context