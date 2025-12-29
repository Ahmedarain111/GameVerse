from django.shortcuts import render
from games.services.rawg import fetch_games

def home_view(request):
    page_size = 20  # number of games per page

    params = {
        "ordering": request.GET.get("sort", "-added"),
        "page": request.GET.get("page", 1),
        "page_size": page_size,
    }

    if platform := request.GET.get("platform"):
        params["platforms"] = platform

    if genre := request.GET.get("genre"):
        params["genres"] = genre

    if date := request.GET.get("release_date"):
        params["dates"] = f"{date},2025-12-31"

    try:
        data = fetch_games(params)
    except Exception:
        data = {"results": [], "count": 0}

    total_pages = (data.get("count", 0) + page_size - 1) // page_size

    context = {
        "games": data.get("results", []),
        "count": data.get("count", 0),
        "page": int(params["page"]),
        "total_pages": total_pages,
    }

    return render(request, "main/home.html", context)
