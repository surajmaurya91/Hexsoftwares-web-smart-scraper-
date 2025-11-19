"""
📝 Logging Configuration for Smart Scraper
Handles all logging activities
"""

import logging
import os
from datetime import datetime

def setup_logger(name="SmartScraper", log_level=logging.INFO):
    """Setup logging configuration"""
    
    # Create logs directory if it doesn't exist
    log_dir = "logs"
    os.makedirs(log_dir, exist_ok=True)
    
    # Log filename with timestamp
    log_file = os.path.join(log_dir, f"scraper_{datetime.now().strftime('%Y%m%d')}.log")
    
    # Create logger
    logger = logging.getLogger(name)
    logger.setLevel(log_level)
    
    # Clear any existing handlers
    logger.handlers.clear()
    
    # Create formatter
    formatter = logging.Formatter(
        '%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S'
    )
    
    # File handler
    file_handler = logging.FileHandler(log_file, encoding='utf-8')
    file_handler.setLevel(log_level)
    file_handler.setFormatter(formatter)
    
    # Console handler
    console_handler = logging.StreamHandler()
    console_handler.setLevel(log_level)
    console_handler.setFormatter(formatter)
    
    # Add handlers to logger
    logger.addHandler(file_handler)
    logger.addHandler(console_handler)
    
    return logger

def log_command(logger, command, response, success=True):
    """Log user commands and responses"""
    if success:
        logger.info(f"Command: '{command}' | Response length: {len(response)}")
    else:
        logger.error(f"Failed command: '{command}' | Error: {response}")

def log_error(logger, error_message, exc_info=False):
    """Log error messages"""
    logger.error(error_message, exc_info=exc_info)

def log_scraping_activity(logger, website, action, details=""):
    """Log scraping activities"""
    logger.info(f"Scraping: {website} | Action: {action} | Details: {details}")

# Create default logger instance
default_logger = setup_logger()