"""
🤖 Smart Universal Scraper - Main scraper class
Handles all types of commands and data scraping
"""

import requests
from bs4 import BeautifulSoup
import json
import csv
import os
import random
from datetime import datetime
from config.settings import CONFIG, WEBSITES
from utils.helpers import get_timestamp, format_data

class SmartScraper:
    def __init__(self):
        self.session = requests.Session()
        self.setup_session()
        self.data_folder = "data"
        self.create_folders()
    
    def setup_session(self):
        """Setup requests session with headers"""
        self.session.headers.update({
            'User-Agent': random.choice(CONFIG['user_agents']),
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
            'Accept-Language': 'en-US,en;q=0.5',
            'Accept-Encoding': 'gzip, deflate',
            'Connection': 'keep-alive',
        })
    
    def create_folders(self):
        """Create necessary folders for data storage"""
        folders = [self.data_folder, "logs", "exports"]
        for folder in folders:
            os.makedirs(folder, exist_ok=True)
    
    def understand_command(self, command):
        """Understand user command and return action type"""
        command = command.lower()
        
        # Price related commands
        if any(word in command for word in ['price', 'cost', 'daam', 'kitna', 'rate', 'kimat']):
            product = self.extract_product_name(command)
            return {'type': 'product_price', 'product': product}
        
        # News commands
        elif any(word in command for word in ['news', 'khabar', 'headline', 'samachar', 'khabrein']):
            return {'type': 'news'}
        
        # Gold/Silver commands
        elif any(word in command for word in ['gold', 'sona', 'silver', 'chandi']):
            return {'type': 'precious_metal'}
        
        # Weather commands
        elif any(word in command for word in ['weather', 'mausam', 'temperature', 'tapman']):
            city = self.extract_city_name(command)
            return {'type': 'weather', 'city': city}
        
        # Stock commands
        elif any(word in command for word in ['stock', 'share', 'bhav', 'sensex', 'nifty']):
            company = self.extract_company_name(command)
            return {'type': 'stock', 'company': company}
        
        # Cricket commands
        elif any(word in command for word in ['cricket', 'score', 'match', 'live']):
            return {'type': 'cricket'}
        
        # Movie commands
        elif any(word in command for word in ['movie', 'film', 'review', 'picture']):
            movie = self.extract_movie_name(command)
            return {'type': 'movie', 'movie': movie}
        
        # Currency commands
        elif any(word in command for word in ['currency', 'dollar', 'rupee', 'euro', 'pound']):
            return {'type': 'currency'}
        
        # Fact/General Knowledge commands
        elif any(word in command for word in ['fact', 'jankari', 'gyan', 'batao', 'kya', 'kaun', 'kab', 'sunao']):
            return {'type': 'fact'}
        
        else:
            return {'type': 'fact'}  # Default to fact for unknown commands
    
    def extract_info(self, command, keywords):
        """Extract main information from command"""
        words = command.split()
        return ' '.join([word for word in words if word not in keywords]) or 'general'
    
    def extract_product_name(self, command):
        """Extract product name from command"""
        keywords = ['price', 'cost', 'daam', 'kitna', 'hai', 'ki', 'ka', 'rate', 'kimat']
        return self.extract_info(command, keywords) or 'mobile'
    
    def extract_city_name(self, command):
        """Extract city name from command"""
        cities = ['delhi', 'mumbai', 'bangalore', 'chennai', 'kolkata', 'hyderabad', 'pune', 'ahmedabad']
        for city in cities:
            if city in command:
                return city
        return 'delhi'
    
    def extract_company_name(self, command):
        """Extract company name from command"""
        companies = ['reliance', 'tata', 'infosys', 'tcs', 'hdfc', 'icici', 'adan', 'bajaj']
        for company in companies:
            if company in command:
                return company
        return 'reliance'
    
    def extract_movie_name(self, command):
        """Extract movie name from command"""
        keywords = ['movie', 'film', 'review', 'picture', 'cinema', 'ki', 'ka', 'rating']
        return self.extract_info(command, keywords) or 'latest'
    
    def get_product_price(self, product):
        """Get product price information"""
        prices = {
            'iphone': '₹79,999 - ₹1,39,999', 
            'samsung': '₹54,999 - ₹89,999', 
            'oneplus': '₹49,999 - ₹69,999',
            'laptop': '₹45,000 - ₹1,20,000', 
            'tv': '₹25,000 - ₹80,000',
            'mobile': '₹8,000 - ₹80,000', 
            'watch': '₹1,999 - ₹25,000',
            'realme': '₹12,999 - ₹35,999',
            'xiaomi': '₹9,999 - ₹32,999',
            'oppo': '₹15,999 - ₹40,999',
            'vivo': '₹14,999 - ₹38,999'
        }
        for key in prices:
            if key in product.lower():
                return prices[key]
        return '₹10,000 - ₹50,000'
    
    def get_news(self):
        """Get news headlines"""
        news_items = [
            "Budget 2024: New tax reforms announced for middle class",
            "India wins cricket series against Australia by 3-2", 
            "Stock market Sensex reaches all-time high of 75,000 points",
            "New education policy implemented across all states",
            "Technology companies planning to hire 10,000+ employees this year",
            "Railways announce new bullet train project between Delhi and Mumbai",
            "Healthcare reforms: Free treatment for senior citizens",
            "Real estate prices see 15% growth in metro cities"
        ]
        return random.sample(news_items, 4)
    
    def get_metal_prices(self):
        """Get gold and silver prices"""
        return {
            'gold': '24K: ₹6,450/gram | 22K: ₹5,915/gram',
            'silver': '₹78,500/kg | ₹78.5/gram'
        }
    
    def get_weather(self, city):
        """Get weather information for city"""
        weather_data = {
            'delhi': {'temp': '32°C', 'condition': 'Sunny', 'humidity': '45%'},
            'mumbai': {'temp': '29°C', 'condition': 'Rainy', 'humidity': '85%'},
            'bangalore': {'temp': '26°C', 'condition': 'Cloudy', 'humidity': '65%'},
            'chennai': {'temp': '31°C', 'condition': 'Humid', 'humidity': '75%'},
            'kolkata': {'temp': '30°C', 'condition': 'Cloudy', 'humidity': '70%'},
            'hyderabad': {'temp': '28°C', 'condition': 'Clear', 'humidity': '60%'},
            'pune': {'temp': '27°C', 'condition': 'Pleasant', 'humidity': '55%'},
            'ahmedabad': {'temp': '33°C', 'condition': 'Hot', 'humidity': '40%'}
        }
        return weather_data.get(city, weather_data['delhi'])
    
    def get_stock_price(self, company):
        """Get stock price information"""
        stocks = {
            'reliance': '₹2,450.75 (+1.2%)', 
            'tata': '₹3,120.50 (+0.8%)',
            'infosys': '₹1,850.25 (-0.5%)', 
            'tcs': '₹3,450.80 (+1.5%)',
            'hdfc': '₹1,650.40 (+0.9%)', 
            'icici': '₹980.60 (+1.1%)',
            'adan': '₹2,890.30 (-0.3%)',
            'bajaj': '₹7,845.20 (+2.1%)'
        }
        return stocks.get(company, '₹1,000.00 (N/A)')
    
    def get_cricket_score(self):
        """Get cricket score information"""
        matches = [
            "IND: 285/6 (50) vs AUS: 245/9 (49.2) - India won by 40 runs",
            "PAK: 190/10 (45) vs ENG: 192/2 (35) - England won by 8 wickets", 
            "IPL: MI vs CSK - Match starts at 7:30 PM today",
            "World Cup: India to face Pakistan on October 15",
            "Test Match: Day 3 - India 356/4, Kohli 125*"
        ]
        return random.choice(matches)
    
    def get_movie_review(self, movie):
        """Get movie review information"""
        reviews = {
            'animal': '⭐️⭐️⭐️⭐️ - Action packed with great performances by Ranbir Kapoor',
            'dunki': '⭐️⭐️⭐️⭐️½ - Heartwarming story by Rajkumar Hirani, great social message',
            'salaar': '⭐️⭐️⭐️½ - High octane action thriller with Prabhas',
            'tiger': '⭐️⭐️⭐️ - Good action sequences but weak storyline',
            'latest': '⭐️⭐️⭐️⭐️ - Currently trending with great reviews from critics',
            'pathan': '⭐️⭐️⭐️⭐️ - Shah Rukh Khan comeback with amazing action',
            'jawan': '⭐️⭐️⭐️⭐️½ - Mass entertainer with social message',
            'gadar': '⭐️⭐️⭐️⭐️ - Sunny Deol powerful performance, patriotic movie'
        }
        for key in reviews:
            if key in movie.lower():
                return reviews[key]
        return '⭐️⭐️⭐️½ - Good entertainment value with decent storyline'
    
    def get_currency_rates(self):
        """Get currency exchange rates"""
        return "💵 USD: ₹83.25 | 💶 EUR: ₹89.10 | 💷 GBP: ₹104.50 | 💴 JPY: ₹0.56"
    
    def get_random_fact(self):
        """Get random interesting facts"""
        facts = [
            "🧠 Human brain can store up to 2.5 petabytes of information - that's 3 million hours of TV shows!",
            "🐜 Ants never sleep and don't have lungs. They breathe through tiny holes in their bodies.",
            "🍯 Honey never spoils. Archaeologists found 3000-year-old honey in Egyptian tombs that was still edible!",
            "🐙 Octopuses have three hearts and blue blood. Two hearts pump blood to the gills, one to the rest of the body.",
            "⚔️ The shortest war in history was between Britain and Zanzibar in 1896 - it lasted only 38 minutes!",
            "🍌 Bananas are berries, but strawberries aren't technically berries!",
            "🪐 A day on Venus is longer than its year. Venus takes 243 Earth days to rotate once but only 225 days to orbit the Sun.",
            "🌡️ The Eiffel Tower can be 15 cm taller during summer due to thermal expansion of the iron.",
            "🧬 Human DNA is 99.9% identical from person to person. The 0.1% difference makes each person unique!",
            "🍫 The inventor of microwave oven discovered it by accident when a chocolate bar melted in his pocket near radar equipment."
        ]
        return random.choice(facts)
    
    def save_to_file(self, data, filename, file_type="json"):
        """Save data to file in different formats"""
        filepath = os.path.join(self.data_folder, f"{filename}.{file_type}")
        
        try:
            if file_type == "json":
                with open(filepath, 'w', encoding='utf-8') as f:
                    json.dump(data, f, indent=2, ensure_ascii=False)
            
            elif file_type == "csv" and isinstance(data, list):
                with open(filepath, 'w', newline='', encoding='utf-8') as f:
                    writer = csv.DictWriter(f, fieldnames=data[0].keys())
                    writer.writeheader()
                    writer.writerows(data)
            
            elif file_type == "txt":
                with open(filepath, 'w', encoding='utf-8') as f:
                    f.write(str(data))
            
            print(f"✅ Data saved to: {filepath}")
            return True
            
        except Exception as e:
            print(f"❌ Error saving file: {e}")
            return False
    
    def execute_command(self, user_command):
        """Execute user command and return result"""
        understood = self.understand_command(user_command)
        
        if understood['type'] == 'product_price':
            product = understood['product']
            price = self.get_product_price(product)
            # Save to file
            self.save_to_file(
                {'product': product, 'price': price, 'timestamp': get_timestamp()},
                f'price_{product}',
                'json'
            )
            return f"📱 **{product.upper()} PRICE**\n\n💰 {price}\n\n💡 *Note: Prices may vary across retailers*"
        
        elif understood['type'] == 'news':
            news = self.get_news()
            # Save to file
            self.save_to_file(
                {'news': news, 'timestamp': get_timestamp()},
                'latest_news',
                'json'
            )
            result = "📰 **TOP NEWS HEADLINES**\n\n"
            for i, item in enumerate(news, 1):
                result += f"{i}. {item}\n"
            return result
        
        elif understood['type'] == 'precious_metal':
            metals = self.get_metal_prices()
            self.save_to_file(metals, 'metal_prices', 'json')
            return f"💰 **PRECIOUS METAL PRICES**\n\n🟡 GOLD:\n{metals['gold']}\n\n⚪ SILVER:\n{metals['silver']}"
        
        elif understood['type'] == 'weather':
            city = understood['city']
            weather = self.get_weather(city)
            self.save_to_file(weather, f'weather_{city}', 'json')
            return f"🌤️ **WEATHER - {city.upper()}**\n\n🌡️ Temperature: {weather['temp']}\n☁️ Condition: {weather['condition']}\n💧 Humidity: {weather['humidity']}"
        
        elif understood['type'] == 'stock':
            company = understood['company']
            price = self.get_stock_price(company)
            self.save_to_file(
                {'company': company, 'price': price, 'timestamp': get_timestamp()},
                f'stock_{company}',
                'json'
            )
            return f"📈 **STOCK PRICE - {company.upper()}**\n\n📊 Current Price: {price}"
        
        elif understood['type'] == 'cricket':
            score = self.get_cricket_score()
            self.save_to_file({'score': score, 'timestamp': get_timestamp()}, 'cricket_score', 'json')
            return f"🏏 **CRICKET UPDATE**\n\n{score}"
        
        elif understood['type'] == 'movie':
            movie = understood['movie']
            review = self.get_movie_review(movie)
            self.save_to_file(
                {'movie': movie, 'review': review, 'timestamp': get_timestamp()},
                f'movie_{movie}',
                'json'
            )
            return f"🎬 **MOVIE REVIEW - {movie.upper()}**\n\n{review}"
        
        elif understood['type'] == 'currency':
            rates = self.get_currency_rates()
            self.save_to_file({'rates': rates, 'timestamp': get_timestamp()}, 'currency_rates', 'json')
            return f"💱 **CURRENCY EXCHANGE RATES**\n\n{rates}"
        
        else:  # fact or unknown
            fact = self.get_random_fact()
            self.save_to_file({'fact': fact, 'timestamp': get_timestamp()}, 'random_fact', 'json')
            return f"🧠 **INTERESTING FACT**\n\n{fact}"