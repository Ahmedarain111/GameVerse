# GameVerse

**GameVerse** is a full-stack web application that lets users explore and discover detailed information about video games.  
It fetches real-time data from the [RAWG Video Games Database API](https://rawg.io/apidocs), displaying rich game details such as genres, ratings, platforms, and release dates.

---

## 🧩 Features

- 🔍 **Search Games:** Find games by title using RAWG’s vast API.
- 🖼️ **Detailed Game Info:** View game cover, release date, platforms, ratings, and genres.
- 🧠 **Backend Integration:** Django backend handles API requests securely.
- 🎨 **Responsive UI:** Built with HTML, CSS, JavaScript, and Bootstrap.
- 🧱 **Secure API Calls:** RAWG API is accessed through Django to keep the API key private.
- ⚡ **Dynamic Frontend:** JavaScript dynamically loads and displays search results.

---

## 🏗️ Tech Stack

| Layer | Technologies |
|-------|---------------|
| **Frontend** | HTML, CSS, JavaScript, Bootstrap |
| **Backend** | Django (Python) |
| **External API** | [RAWG Video Games Database API](https://rawg.io/apidocs) |
| **Database** | SQLite |

---

## ⚙️ How It Works

1. **User enters a game name** in the search bar.
2. The **frontend** sends the query to the **Django backend** (`/search_games` endpoint).
3. Django **fetches data** from the RAWG API using Python’s `requests` module.
4. The backend **filters and sends JSON** results to the frontend.
5. **JavaScript** dynamically updates the page with game cards and info.
