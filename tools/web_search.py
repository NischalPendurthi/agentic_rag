import requests

def web_search(query):
    # Replace with your Bing API key
    subscription_key = "your_bing_api_key"
    search_url = "https://api.bing.microsoft.com/v7.0/search"
    headers = {"Ocp-Apim-Subscription-Key": subscription_key}
    params = {"q": query, "count": 3}
    response = requests.get(search_url, headers=headers, params=params)
    response.raise_for_status()
    results = response.json()
    snippets = [item["snippet"] for item in results.get("webPages", {}).get("value", [])]
    return "\n".join(snippets) if snippets else "No results found."