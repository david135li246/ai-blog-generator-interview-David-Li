def get_mock_seo_data(keyword):
    # Mock SEO data for demonstration purposes
    mock_data = {
        "wireless earbuds": {
            "search_volume": 50000,
            "keyword_difficulty": 30,
            "avg_cpc": 1.20
        },
        "bluetooth headphones": {
            "search_volume": 30000,
            "keyword_difficulty": 25,
            "avg_cpc": 0.90
        },
        "noise cancelling headphones": {
            "search_volume": 20000,
            "keyword_difficulty": 35,
            "avg_cpc": 1.50
        }
    }
    
    return mock_data.get(keyword, {"search_volume": 0, "keyword_difficulty": 0, "avg_cpc": 0})

def fetch_seo_metrics(keyword):
    return get_mock_seo_data(keyword)