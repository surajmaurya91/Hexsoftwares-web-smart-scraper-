"""
🤖 SMART UNIVERSAL WEB SCRAPER
Main Entry Point - Run this file to start the scraper
"""

import os
import sys

# Add src folder to Python path
sys.path.append(os.path.join(os.path.dirname(__file__), 'src'))

from src.smart_scraper import SmartScraper
from utils.logger import setup_logger

def main():
    """Main function to run the smart scraper"""
    
    # Setup logging
    logger = setup_logger()
    logger.info("🚀 Starting Smart Universal Scraper")
    
    # Create scraper instance
    scraper = SmartScraper()
    
    print("🤖 **SMART UNIVERSAL SCRAPER**")
    print("=" * 50)
    print("Mujhe ye sab commands samajh aate hain:")
    print("• Product Prices   • News Updates")
    print("• Gold/Silver      • Weather Info") 
    print("• Stock Prices     • Cricket Scores")
    print("• Movie Reviews    • Currency Rates")
    print("• Random Facts     • General Knowledge")
    print("=" * 50)
    print("Type 'exit' to quit the program")
    print("=" * 50)
    
    # Main interaction loop
    while True:
        try:
            user_input = input("\n💬 Aapka command: ").strip()
            
            if user_input.lower() in ['exit', 'quit', 'band', 'bye', 'stop']:
                print("👋 Dhanyawaad! Phir milenge!")
                logger.info("Scraper stopped by user")
                break
            
            if not user_input:
                continue
            
            # Execute command and get result
            result = scraper.execute_command(user_input)
            print(f"\n{result}")
            
            # Log the command
            logger.info(f"Command: '{user_input}' | Response: {len(result)} chars")
            
        except KeyboardInterrupt:
            print("\n\n⚠️ Program interrupted by user")
            break
        except Exception as e:
            error_msg = f"❌ Error: {str(e)}"
            print(error_msg)
            logger.error(f"Error in main: {e}")

if __name__ == "__main__":
    main()