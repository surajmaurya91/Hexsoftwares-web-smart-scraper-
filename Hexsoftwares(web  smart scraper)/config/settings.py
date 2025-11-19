"""
⚙️ Configuration Settings for Smart Scraper
All configurable parameters in one place
"""

# Main configuration
CONFIG = {
    "app_name": "Smart Universal Scraper",
    "version": "1.0.0",
    "author": "Your Name",
    
    # Request settings
    "request_timeout": 10,
    "retry_attempts": 3,
    "delay_between_requests": 1,
    
    # User agents to rotate
    "user_agents": [
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
        "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:89.0) Gecko/20100101 Firefox/89.0",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.1.1 Safari/605.1.15"
    ],
    
    # Supported commands
    "supported_commands": [
        "price", "news", "weather", "stock", 
        "cricket", "movie", "currency", "fact",
        "gold", "silver", "share", "score"
    ],
    
    # File settings
    "data_retention_days": 30,
    "max_file_size_mb": 10,
    "backup_enabled": True
}

# Website URLs for scraping
WEBSITES = {
    "news": [
        "https://www.bbc.com/hindi",
        "https://timesofindia.indiatimes.com",
        "https://www.ndtv.com"
    ],
    "prices": [
        "https://www.amazon.in",
        "https://www.flipkart.com",
        "https://www.myntra.com"
    ],
    "finance": [
        "https://www.moneycontrol.com",
        "https://www.goldpriceindia.com",
        "https://www.xe.com"
    ],
    "sports": [
        "https://www.espncricinfo.com",
        "https://www.cricbuzz.com"
    ]
}

# City mappings for weather
CITIES = {
    "delhi": {"lat": "28.6139", "lon": "77.2090"},
    "mumbai": {"lat": "19.0760", "lon": "72.8777"},
    "bangalore": {"lat": "12.9716", "lon": "77.5946"},
    "chennai": {"lat": "13.0827", "lon": "80.2707"},
    "kolkata": {"lat": "22.5726", "lon": "88.3639"},
    "hyderabad": {"lat": "17.3850", "lon": "78.4867"},
    "pune": {"lat": "18.5204", "lon": "73.8567"},
    "ahmedabad": {"lat": "23.0225", "lon": "72.5714"}
}

# Product categories
PRODUCT_CATEGORIES = {
    "mobile": ["iphone", "samsung", "oneplus", "realme", "xiaomi", "oppo", "vivo"],
    "laptop": ["dell", "hp", "lenovo", "asus", "acer", "apple"],
    "electronics": ["tv", "headphones", "watch", "camera", "tablet"]
}

# Response templates
RESPONSE_TEMPLATES = {
    "welcome": "🤖 Smart Universal Scraper mein aapka swagat hai!",
    "help": """
🎯 **Available Commands:**
• Product Prices: 'iphone price', 'laptop cost', 'tv daam'
• News Updates: 'news', 'aaj ki khabar', 'headlines'
• Financial: 'gold price', 'silver rate', 'stock price'
• Sports: 'cricket score', 'live match'
• Entertainment: 'movie review', 'film rating'
• General: 'fact', 'jankari', 'kuch interesting batao'
• Weather: 'delhi weather', 'mumbai ka mausam'

Type 'exit' to quit.
    """,
    "error": "❌ Sorry, is command ko process nahi kar paya. Kripya dob try karein.",
    "exit": "👋 Dhanyawaad! Phir milenge!"
}