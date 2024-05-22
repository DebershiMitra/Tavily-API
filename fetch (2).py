from tavily import TavilyClient
import time

def fetch_content(query, key):
    tavily = TavilyClient(api_key=key)
    start_time = time.time()
    response_advanced = tavily.search(query=query, search_depth="advanced", max_results=15)
    end_time = time.time()
    print(f"Time taken: {end_time - start_time:.2f} seconds")

    res = ''
    for result in response_advanced['results']:
        res += result['content']
    return res

