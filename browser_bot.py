"""
LinkedIn Viral Bot - Browser Automation Engine
Copyright (c) 2022-2026 Ashraf Morningstar
GitHub: https://github.com/AshrafMorningstar/LinkedIn-Viral-Bot

This module provides human-like browser automation for LinkedIn using Playwright.
It handles session management, login persistence, and automated post scheduling.

This project is a personal recreation developed for learning and skill development.
Licensed under the MIT License - see LICENSE file for details.
"""

import time
import random
import os
from playwright.sync_api import sync_playwright
import config


class LinkedInBot:
    """
    Human-Like LinkedIn Browser Automation Bot
    
    This class provides sophisticated browser automation that mimics human behavior
    to safely interact with LinkedIn. It handles login persistence, human-like delays,
    and automated post scheduling while avoiding detection.
    
    Key Features:
        - Session cookie persistence (login once, reuse forever)
        - Human-like random delays between actions
        - Support for both media and text-only posts
        - Automatic scheduling (never posts directly)
        - Robust error handling and fallback selectors
    
    Attributes:
        browser: Playwright browser instance
        context: Browser context with saved cookies
        page: Active browser page
        playwright: Playwright instance
    
    Example:
        >>> bot = LinkedInBot()
        >>> bot.start_session()
        >>> if not bot.is_logged_in():
        ...     bot.login_manual()
        >>> bot.create_text_post("My viral content", "10:00")
        >>> bot.close()
    """
    
    def __init__(self):
        """Initialize the browser automation bot."""
        self.browser = None
        self.context = None
        self.page = None
        self.playwright = None

    def start_session(self):
        """
        Start a browser session with cookie persistence.
        
        This method launches a Chromium browser and loads saved session cookies
        if available. This allows the bot to skip login on subsequent runs,
        making automation faster and more reliable.
        
        The browser is launched in non-headless mode by default for transparency
        and easier debugging. Set config.HEADLESS_MODE = True to run in background.
        """
        self.playwright = sync_playwright().start()
        
        # Launch browser with realistic settings
        self.browser = self.playwright.chromium.launch(
            headless=config.HEADLESS_MODE,
            args=["--start-maximized"]
        )
        
        # Load saved session if available
        if os.path.exists(config.COOKIES_PATH):
            print("🔐 Loading saved session from cookies...")
            self.context = self.browser.new_context(
                storage_state=config.COOKIES_PATH,
                viewport={"width": 1920, "height": 1080}
            )
        else:
            print("🆕 No saved session found. Starting fresh...")
            self.context = self.browser.new_context(
                viewport={"width": 1920, "height": 1080}
            )
        
        self.page = self.context.new_page()
        self.page.goto("https://www.linkedin.com")
        self.human_delay()
    
    def save_session(self):
        """
        Save the current browser session to disk.
        
        This method persists cookies and authentication tokens, allowing
        the bot to skip login on future runs. Called automatically after
        successful manual login.
        """
        self.context.storage_state(path=config.COOKIES_PATH)
        print("💾 Session saved successfully!")

    def human_delay(self, min_seconds=None, max_seconds=None):
        """
        Simulate human-like pause between actions.
        
        This is critical for avoiding detection. Real humans don't click buttons
        instantly - they read, think, and move their mouse. This method adds
        realistic delays between automation steps.
        
        Args:
            min_seconds (int, optional): Minimum delay. Defaults to config.MIN_DELAY
            max_seconds (int, optional): Maximum delay. Defaults to config.MAX_DELAY
        
        Example:
            >>> bot.human_delay(3, 7)  # Wait 3-7 seconds
        """
        if min_seconds is None:
            min_seconds = config.MIN_DELAY
        if max_seconds is None:
            max_seconds = config.MAX_DELAY
            
        sleep_time = random.uniform(min_seconds, max_seconds)
        print(f"⏳ Sleeping for {sleep_time:.2f} seconds...")
        time.sleep(sleep_time)

    def is_logged_in(self):
        """
        Check if the user is currently logged into LinkedIn.
        
        This method looks for elements that only appear when logged in,
        such as the feed identity module. Used to determine if manual
        login is required.
        
        Returns:
            bool: True if logged in, False otherwise
        """
        try:
            # Look for feed element that only appears when logged in
            self.page.wait_for_selector("div.feed-identity-module", timeout=5000)
            print("✅ Already logged in!")
            return True
        except:
            print("❌ Not logged in")
            return False

    def login_manual(self):
        """
        Pause execution for manual login.
        
        On first run, the bot will open LinkedIn and wait for you to log in
        manually. After you log in and press Enter, it saves your session
        so you never have to log in again.
        
        This approach is safer than storing passwords and works with 2FA.
        """
        print("\n" + "="*60)
        print("🔑 MANUAL LOGIN REQUIRED")
        print("="*60)
        print("Please log in to LinkedIn in the browser window.")
        print("After logging in successfully, press Enter here...")
        print("="*60 + "\n")
        
        input("Press Enter after you have logged in: ")
        self.save_session()

    def create_text_post(self, content, schedule_time_str):
        """
        Create and schedule a text-only LinkedIn post.
        
        This method automates the creation of text-only posts when no media
        is available. Perfect for maintaining consistent posting schedules
        with AI-generated content.
        
        Args:
            content (str): The post text content
            schedule_time_str (str): Desired schedule time (currently uses LinkedIn's default)
        
        Example:
            >>> bot.create_text_post("Check out my new blog post!", "10:00")
        """
        print("\n📝 Creating text-only post...")
        self.page.goto("https://www.linkedin.com/feed/")
        self.human_delay()

        print("🖱️  Clicking 'Start a post'...")
        self.page.click("button >> text=Start a post") 
        self.human_delay(2, 4)
        
        # Type the content with human-like typing speed
        print("⌨️  Typing content...")
        self.page.click("div.ql-editor")
        self.page.keyboard.type(content, delay=30)  # 30ms between keystrokes
        self.human_delay()
        
        # Schedule the post
        self._perform_schedule_flow()

    def create_scheduled_post(self, content, media_path, schedule_time_str):
        """
        Create and schedule a LinkedIn post with media attachment.
        
        This method handles the complete workflow for media posts: uploading
        the file, adding caption text, and scheduling for later posting.
        
        Args:
            content (str): The post caption/text
            media_path (str): Absolute path to the media file
            schedule_time_str (str): Desired schedule time
        
        Example:
            >>> bot.create_scheduled_post(
            ...     "Excited to share this!",
            ...     "/path/to/image.jpg",
            ...     "10:00"
            ... )
        """
        print("\n📸 Creating media post...")
        self.page.goto("https://www.linkedin.com/feed/")
        self.human_delay()

        print("🖱️  Clicking 'Start a post'...")
        self.page.click("button >> text=Start a post") 
        self.human_delay(2, 4)

        # Upload media if provided
        if media_path:
            print(f"📤 Uploading media: {os.path.basename(media_path)}...")
            
            with self.page.expect_file_chooser() as fc_info:
                try:
                    # Try primary selector
                    self.page.click("button[aria-label='Add media']")
                except:
                    # Fallback selector
                    self.page.click("button >> text=Media")
            
            file_chooser = fc_info.value
            file_chooser.set_files(media_path)
            self.human_delay(5, 10)  # Wait for upload to complete

            # Click Next if it appears (multi-step upload flow)
            if self.page.is_visible("button >> text=Next"):
                self.page.click("button >> text=Next")
                self.human_delay()

        # Add caption text
        print("⌨️  Adding caption...")
        self.page.click("div.ql-editor")
        self.page.keyboard.type(content, delay=50)
        self.human_delay()

        # Schedule the post
        self._perform_schedule_flow()

    def _perform_schedule_flow(self):
        """
        Internal method to handle the scheduling workflow.
        
        This method contains the logic for finding and clicking LinkedIn's
        schedule button, which can have different selectors depending on
        LinkedIn's current UI. It uses multiple fallback strategies for
        robustness.
        
        Critical: This method ensures posts are NEVER published directly,
        only scheduled for later. This is a key safety feature.
        """
        print("📅 Scheduling post...")
        
        try:
            # Try multiple selectors (LinkedIn UI changes frequently)
            if self.page.is_visible("button[aria-label='Schedule for later']"):
                self.page.click("button[aria-label='Schedule for later']")
            elif self.page.is_visible("button[aria-label='Schedule post']"):
                self.page.click("button[aria-label='Schedule post']")
            else:
                # Fallback: Look for clock icon
                self.page.click("button:has(svg[data-test-icon='clock-small'])")
                
        except Exception as e:
            print(f"⚠️  Failed to find schedule button: {e}")
            print("🛑 Aborting to avoid direct posting (safety measure)")
            return

        self.human_delay()

        # Confirm schedule time (uses LinkedIn's default suggestion)
        if self.page.is_visible("button >> text=Next"): 
            self.page.click("button >> text=Next")
        
        self.human_delay()

        # Final confirmation
        self.page.click("button.share-actions__primary-action") 
        print("✅ Post scheduled successfully!")
        self.human_delay()

    def close(self):
        """
        Close the browser and clean up resources.
        
        Always call this method when done to prevent zombie browser processes.
        """
        if self.browser:
            self.browser.close()
        if self.playwright:
            self.playwright.stop()
        print("🔒 Browser closed")
