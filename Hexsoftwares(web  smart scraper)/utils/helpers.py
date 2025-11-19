"""
🔧 Utility Functions for Smart Scraper
Helper functions for common tasks
"""

import os
import json
import csv
from datetime import datetime, timedelta
import logging

def get_timestamp(format_type="default"):
    """Get current timestamp in different formats"""
    now = datetime.now()
    
    if format_type == "default":
        return now.strftime("%Y-%m-%d %H:%M:%S")
    elif format_type == "file":
        return now.strftime("%Y%m%d_%H%M%S")
    elif format_type == "readable":
        return now.strftime("%d %B %Y, %I:%M %p")
    else:
        return now.isoformat()

def format_data(data, format_type="text"):
    """Format data for different output types"""
    if format_type == "text":
        if isinstance(data, list):
            return "\n".join([f"• {item}" for item in data])
        elif isinstance(data, dict):
            return "\n".join([f"• {key}: {value}" for key, value in data.items()])
        return str(data)
    
    elif format_type == "json":
        return json.dumps(data, indent=2, ensure_ascii=False)
    
    elif format_type == "csv":
        # This would need to be handled differently based on data structure
        return "CSV format requires specific handling"

def clean_filename(filename):
    """Clean filename by removing invalid characters"""
    invalid_chars = '<>:"/\\|?*'
    for char in invalid_chars:
        filename = filename.replace(char, '_')
    return filename[:100]  # Limit filename length

def calculate_size(filepath):
    """Calculate file size in human readable format"""
    try:
        size_bytes = os.path.getsize(filepath)
        for unit in ['B', 'KB', 'MB', 'GB']:
            if size_bytes < 1024.0:
                return f"{size_bytes:.2f} {unit}"
            size_bytes /= 1024.0
        return f"{size_bytes:.2f} TB"
    except OSError:
        return "Unknown"

def is_file_old(filepath, days=30):
    """Check if file is older than specified days"""
    try:
        file_time = datetime.fromtimestamp(os.path.getmtime(filepath))
        return datetime.now() - file_time > timedelta(days=days)
    except OSError:
        return False

def validate_url(url):
    """Basic URL validation"""
    import re
    regex = re.compile(
        r'^(?:http|ftp)s?://'  # http:// or https://
        r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|'  # domain...
        r'localhost|'  # localhost...
        r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})'  # ...or ip
        r'(?::\d+)?'  # optional port
        r'(?:/?|[/?]\S+)$', re.IGNORECASE)
    return re.match(regex, url) is not None

def progress_bar(iteration, total, length=50):
    """Display progress bar"""
    percent = ("{0:.1f}").format(100 * (iteration / float(total)))
    filled_length = int(length * iteration // total)
    bar = '█' * filled_length + '-' * (length - filled_length)
    return f'|{bar}| {percent}% Complete'

def format_currency(amount, currency="₹"):
    """Format currency amount"""
    try:
        amount = float(amount)
        return f"{currency}{amount:,.2f}"
    except (ValueError, TypeError):
        return f"{currency}0.00"