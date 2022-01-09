"""
LinkedIn Viral Bot - AI-Powered LinkedIn Automation Suite
Copyright (c) 2022-2026 Ashraf Morningstar
GitHub: https://github.com/AshrafMorningstar/LinkedIn-Viral-Bot

This project is a personal recreation developed for learning and skill development.
Original project concepts remain the intellectual property of their respective creators.

Licensed under the MIT License - see LICENSE file for details.
"""

import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# ============================================================================
# AI API CONFIGURATION
# ============================================================================
# Multiple AI providers are supported for maximum flexibility and redundancy
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
DEEPSEEK_API_KEY = os.getenv("DEEPSEEK_API_KEY")
OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")

# ============================================================================
# AI PROVIDER SETTINGS
# ============================================================================
# Default AI provider - Options: "gemini", "openai", "deepseek", "openrouter"
AI_PROVIDER = "openrouter"

# Model selection for content generation
# OpenRouter example: "google/gemini-2.0-flash-lite-preview-02-05:free"
# Gemini example: "gemini-1.5-flash"
# OpenAI example: "gpt-4o-mini"
VIRAL_MODEL = "google/gemini-2.0-flash-lite-preview-02-05:free"

# ============================================================================
# LINKEDIN CREDENTIALS (OPTIONAL)
# ============================================================================
# These are optional - the bot will prompt for manual login on first run
# and save session cookies for subsequent runs
LINKEDIN_USERNAME = os.getenv("LINKEDIN_USERNAME")
LINKEDIN_PASSWORD = os.getenv("LINKEDIN_PASSWORD")

# ============================================================================
# FILE PATHS
# ============================================================================
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
INPUT_MEDIA_DIR = os.path.join(BASE_DIR, "input_media")
ARCHIVE_DIR = os.path.join(BASE_DIR, "archive")
COOKIES_PATH = os.path.join(BASE_DIR, "state.json")

# ============================================================================
# AUTOMATION SETTINGS
# ============================================================================
# Human-like delay ranges (in seconds) to avoid detection
MIN_DELAY = 5  # Minimum delay between actions
MAX_DELAY = 15  # Maximum delay between actions

# Browser automation settings
HEADLESS_MODE = False  # Set to True to run browser in background (not recommended for first run)
