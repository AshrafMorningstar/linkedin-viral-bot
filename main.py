"""
LinkedIn Viral Bot - Main Orchestrator
Copyright (c) 2022-2026 Ashraf Morningstar
GitHub: https://github.com/AshrafMorningstar/LinkedIn-Viral-Bot

This is the main entry point for the LinkedIn Viral Bot. It orchestrates the
complete workflow: media detection, AI content generation, and automated posting.

This project is a personal recreation developed for learning and skill development.
Licensed under the MIT License - see LICENSE file for details.
"""

import os
import time
import schedule
import config
from ai_engine import ViralAI
from media_manager import MediaManager
from browser_bot import LinkedInBot


def job():
    """
    Main automation job - runs the complete posting workflow.
    
    This function executes the full automation cycle:
    1. Check for media files in input_media folder
    2. Generate viral content using AI
    3. Automate LinkedIn posting via browser
    4. Archive processed files
    
    The bot intelligently switches between media posts and text-only posts
    depending on file availability.
    """
    print("\n" + "="*70)
    print("🤖 LINKEDIN VIRAL BOT - AUTOMATION CYCLE STARTED")
    print("="*70)
    
    # Initialize components
    media_mgr = MediaManager()
    media_path = media_mgr.get_next_media()
    ai = ViralAI()
    
    # Determine post type and generate content
    if media_path:
        # ============================================================
        # MEDIA POST WORKFLOW
        # ============================================================
        print(f"\n📁 Media file detected: {os.path.basename(media_path)}")
        
        # Analyze media and determine type
        description = ai.analyze_media(media_path)
        media_type = media_mgr.get_media_type(media_path)
        
        print(f"🎨 Media type: {media_type}")
        print("🤖 Generating viral caption with AI...")
        
        # Generate AI caption
        content = ai.generate_caption(description, media_type)
        
    else:
        # ============================================================
        # TEXT-ONLY POST WORKFLOW
        # ============================================================
        print("\n📝 No media found - generating text-only viral post...")
        content = ai.generate_text_post()
        media_path = None

    # Display generated content
    print("\n" + "-"*70)
    print("📄 GENERATED CONTENT:")
    print("-"*70)
    print(content[:200] + ("..." if len(content) > 200 else ""))
    print("-"*70)

    # ============================================================
    # BROWSER AUTOMATION
    # ============================================================
    bot = LinkedInBot()
    try:
        print("\n🌐 Starting browser automation...")
        bot.start_session()
        
        # Check login status
        if not bot.is_logged_in():
            bot.login_manual()
        
        # Create and schedule the post
        if media_path:
            bot.create_scheduled_post(content, media_path, "10:00")
            # Archive the media file after successful posting
            media_mgr.archive_media(media_path)
        else:
            bot.create_text_post(content, "10:00")
        
        print("\n✅ Automation cycle completed successfully!")
        
    except Exception as e:
        print(f"\n❌ Error during automation: {e}")
        print("💡 Tip: Check your internet connection and LinkedIn login status")
        
    finally:
        bot.close()
    
    print("="*70 + "\n")


def main():
    """
    Main entry point for the LinkedIn Viral Bot.
    
    This function initializes the bot and can be configured to run:
    - Once (for testing or manual triggers)
    - On a schedule (hourly, daily, etc.)
    
    To enable scheduled posting, uncomment the schedule lines below.
    """
    print("\n" + "="*70)
    print("🚀 LINKEDIN VIRAL BOT - STARTED")
    print("="*70)
    print(f"📂 Monitoring: {config.INPUT_MEDIA_DIR}")
    print(f"🤖 AI Provider: {config.AI_PROVIDER}")
    print(f"🧠 AI Model: {config.VIRAL_MODEL}")
    print("="*70 + "\n")
    
    # Run once immediately (for testing/demo)
    job()
    
    # ============================================================
    # SCHEDULED POSTING (OPTIONAL)
    # ============================================================
    # Uncomment the lines below to enable automatic scheduled posting
    # 
    # Example schedules:
    # schedule.every(1).hours.do(job)      # Every hour
    # schedule.every().day.at("10:00").do(job)  # Daily at 10 AM
    # schedule.every().monday.at("09:00").do(job)  # Every Monday at 9 AM
    #
    # while True:
    #     schedule.run_pending()
    #     time.sleep(60)  # Check every minute


if __name__ == "__main__":
    main()
