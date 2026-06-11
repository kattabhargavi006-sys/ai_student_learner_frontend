import os
from serpapi import GoogleSearch
from dotenv import load_dotenv

load_dotenv()

def web_search(query):

    params = {
        "engine": "google",
        "q": query,
        "api_key": os.getenv("SERPAPI_API_KEY")
    }

    search = GoogleSearch(params)

    results = search.get_dict()

    snippets = []

    if "organic_results" in results:

        for item in results["organic_results"][:5]:

            if "snippet" in item:
                snippets.append(item["snippet"])

    return "\n".join(snippets)