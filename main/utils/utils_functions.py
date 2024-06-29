from django.shortcuts import resolve_url

def get_route_params(route: str = "", request = None):
    url: str = resolve_url(route)
    logout: str = resolve_url("logout")
    signup: str = resolve_url("signup")
    login: str = resolve_url("login")
    blog: str = resolve_url("blog")
    chat: str = resolve_url("chat")
    newpost: str = resolve_url("newpost")
    global_route_name: str = url.split("/")[-1]
    context: dict = {
        "url": url,
        "global_route_name": global_route_name,
        "blog": blog,
        "login": login,
        "signup": signup,
        "chat": chat,
        "newpost": newpost,
    }
    if request:
        context["id"] = request.session.get("id")
        context["logout"] = logout
    return context