# Hexsoftwares-web-smart-scraper-
# Smart Universal Web Scraper - Your AI-Powered Data Assistant

A powerful, intelligent web scraper that understands natural language commands in both Hindi and English. Get real-time information about products, news, weather, stocks, cricket scores, and more with simple conversational commands.

## ✨ What Makes This Special?

Unlike traditional scrapers that require complex configurations, this tool understands you! Just talk to it naturally:

```
💬 "iphone ka price batao"
💬 "aaj ki news kya hai" 
💬 "delhi ka weather batao"
💬 "cricket score sunao"
```

## 🚀 Quick Start

### Installation

```bash
# Clone the repository
git clone (https://github.com/surajmaurya91/Hexsoftwares-web-smart-scraper)
cd smart-web-scraper

# Install dependencies
pip install -r requirements.txt

# Run the scraper
python main.py
```

### First Time Usage

When you run the scraper, you'll see:

```
🤖 SMART UNIVERSAL SCRAPER
==================================================
Mujhe ye sab commands samajh aate hain:
• Product Prices   • News Updates
• Gold/Silver      • Weather Info 
• Stock Prices     • Cricket Scores
• Movie Reviews    • Currency Rates
• Random Facts     • General Knowledge
==================================================
💬 Aapka command:
```

Try these commands to get started:
- `"iphone price"`
- `"aaj ki news"`
- `"gold price kya hai"`
- `"cricket score"`
- `"kuch interesting batao"`

## 🎯 What Can It Do?

### 🛒 Product Prices
- `"iphone price"` - Get current iPhone prices
- `"laptop kitna hai"` - Check laptop prices
- `"samsung mobile daam"` - Samsung mobile prices
- `"tv cost batao"` - Television prices

### 📰 News & Information  
- `"aaj ki news"` - Today's top news
- `"latest headlines"` - Breaking news
- `"kuch nayi khabar"` - Fresh updates

### 💰 Financial Data
- `"gold price"` - Current gold rates
- `"silver rate kya hai"` - Silver prices
- `"reliance share price"` - Stock prices
- `"dollar rate batao"` - Currency exchange rates

### 🌤️ Weather Information
- `"delhi weather"` - Delhi weather forecast
- `"mumbai ka mausam"` - Mumbai weather
- `"bangalore temperature"` - Bangalore weather

### 🏏 Sports & Entertainment
- `"cricket score"` - Live cricket scores
- `"live match update"` - Match updates
- `"movie review"` - Latest movie reviews

### 🧠 General Knowledge
- `"fact sunao"` - Random interesting facts
- `"kuch interesting batao"` - Fun information
- `"jankari do"` - General knowledge

## 🛠️ Technical Features

- **Natural Language Processing**: Understands mixed Hindi-English commands
- **Multi-Website Support**: Aggregates data from multiple reliable sources
- **Smart Caching**: Redundant requests with cached responses
- **Error Resilience**: Continues working even if some sources fail
- **Data Export**: Automatically saves data in JSON, CSV, and text formats
- **Comprehensive Logging**: Detailed logs for debugging and monitoring

## 📁 Project Structure

```
smart-web-scraper/
├── src/
│   ├── smart_scraper.py      # Main scraper logic
│   ├── news_scraper.py       # News extraction module
│   └── price_scraper.py      # Price comparison engine
├── config/
│   └── settings.py           # All configuration parameters
├── utils/
│   ├── helpers.py            # Utility functions
│   └── logger.py             # Logging configuration
├── data/                     # Auto-saved scraped data
├── logs/                     # Application logs
├── main.py                   # Entry point
├── requirements.txt          # Dependencies
└── README.md                 # This file
```

## 🔧 Advanced Usage

### Custom Command Integration

Want to add your own commands? It's easy! Just extend the `understand_command` method:

```python
def understand_command(self, command):
    command = command.lower()
    
    # Add your custom commands here
    if any(word in command for word in ['flight', 'ticket']):
        return {'type': 'flight_price', 'route': self.extract_route(command)}
    
    # Existing command handling continues...
```

### Data Export Options

All scraped data is automatically saved, but you can also manually export:

```python
scraper.save_to_file(data, 'my_data', 'json')  # JSON format
scraper.save_to_file(data, 'my_data', 'csv')   # CSV format  
scraper.save_to_file(data, 'my_data', 'txt')   # Text format
```

## 🌟 Real-World Examples

Here's what you'll actually see when using the scraper:

```
💬 Aapka command: iphone price

📱 **IPHONE PRICE**

💰 ₹79,999 - ₹1,39,999

💡 Note: Prices may vary across retailers

💬 Aapka command: aaj ki news

📰 **TOP NEWS HEADLINES**

1. Budget 2024: New tax reforms announced for middle class
2. India wins cricket series against Australia by 3-2
3. Stock market Sensex reaches all-time high
4. New education policy implemented across states

💬 Aapka command: gold price kya hai

💰 **PRECIOUS METAL PRICES**

🟡 GOLD:
24K: ₹6,450/gram | 22K: ₹5,915/gram

⚪ SILVER:
₹78,500/kg | ₹78.5/gram
```

## 🤝 Contributing

We love contributions! Here's how you can help:

1. **Fork** the repository
2. **Create** a feature branch (`git checkout -b amazing-feature`)
3. **Commit** your changes (`git commit -m 'Add amazing feature'`)
4. **Push** to the branch (`git push origin amazing-feature`)
5. **Open** a Pull Request

### Development Setup

```bash
# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install development dependencies
pip install -r requirements.txt

# Run tests
python -m pytest tests/
```

## ⚠️ Responsible Usage

This tool is designed for:
✅ Personal use  
✅ Educational purposes  
✅ Research and learning  
✅ Testing and development  

Please respect:
- Website terms of service
- robots.txt files
- Rate limiting policies
- Copyright laws

## 🐛 Troubleshooting

### Common Issues

**Q: I'm getting connection errors**  
A: Check your internet connection and firewall settings. Some networks block scraping.

**Q: Some commands return "currently unavailable"**  
A: Websites change frequently. The scraper includes fallback data when live scraping fails.

**Q: How do I add a new website?**  
A: Update the `WEBSITES` dictionary in `config/settings.py` and implement the scraping logic.

### Debug Mode

Enable detailed logging by setting log level to DEBUG in `utils/logger.py`:

```python
def setup_logger(log_level=logging.DEBUG):  # Change from INFO to DEBUG
```

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🙏 Acknowledgments

- Built with Python's amazing ecosystem
- Thanks to the BeautifulSoup and Requests libraries
- Inspired by the need for accessible web scraping tools

