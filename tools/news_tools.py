import requests
from config import News_data_api  
import webbrowser


def tell_World_news():
    """
    Fetches top world news headlines and opens the world monitor dashboard.
    Returns news data for the LLM to explain.
    """

    webbrowser.open("https://worldmonitor.app/dashboard")
    url = "https://newsdata.io/api/1/news"

    params = {
        "apikey": News_data_api,
        "language": "en",
        "category": "world"
    }
    try:
        response = requests.get(url, params=params, timeout=10)
        response.raise_for_status()
        data = response.json()
        
        articles = data.get("results", [])[:5] 
        
        news_summary = []
        for article in articles:
            news_summary.append({
                "title": article.get("title"),
                "description": article.get("description"),
                "source": article.get("source_id")
            })
        
        return {
            "status": "success",
            "dashboard_opened": True,
            "news": news_summary
        }
    
    except requests.exceptions.RequestException as e:
        return {
            "status": "error",
            "message": f"Failed to fetch news: {str(e)}"
        }




if __name__ == "__main__":
    result = tell_World_news()
    print(result)