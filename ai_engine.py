"""
LinkedIn Viral Bot - AI Content Generation Engine
Copyright (c) 2022-2026 Ashraf Morningstar
GitHub: https://github.com/AshrafMorningstar/LinkedIn-Viral-Bot

This module provides a unified interface for multiple AI providers (Google Gemini,
OpenAI, DeepSeek, OpenRouter) to generate viral LinkedIn content.

This project is a personal recreation developed for learning and skill development.
Licensed under the MIT License - see LICENSE file for details.
"""

import google.generativeai as genai
import openai
import os
import config


class ViralAI:
    """
    AI Content Generation Engine for LinkedIn Viral Posts
    
    This class provides a unified interface to multiple AI providers, allowing
    seamless switching between Google Gemini, OpenAI, DeepSeek, and OpenRouter
    for generating high-engagement LinkedIn content.
    
    Attributes:
        provider (str): The active AI provider ("gemini", "openai", "openrouter")
        client (openai.OpenAI): OpenAI-compatible client instance
        gemini_model: Google Gemini model instance (if using Gemini)
    
    Example:
        >>> ai = ViralAI()
        >>> caption = ai.generate_caption("A professional headshot", "image")
        >>> text_post = ai.generate_text_post()
    """
    
    def __init__(self):
        """Initialize the AI engine with the configured provider."""
        self.provider = config.AI_PROVIDER
        self.client = None
        self._setup_provider()

    def _setup_provider(self):
        """
        Configure the selected AI provider with API credentials.
        
        This method initializes the appropriate AI client based on the
        AI_PROVIDER setting in config.py. It handles authentication and
        model selection for each supported provider.
        
        Raises:
            Exception: If provider setup fails (logged but not raised)
        """
        try:
            if self.provider == "gemini":
                # Google Gemini setup
                if config.GOOGLE_API_KEY:
                    genai.configure(api_key=config.GOOGLE_API_KEY)
                    self.gemini_model = genai.GenerativeModel(
                        config.VIRAL_MODEL or "gemini-1.5-flash"
                    )
            
            elif self.provider == "openrouter":
                # OpenRouter setup (supports multiple models via OpenAI-compatible API)
                if config.OPENROUTER_API_KEY:
                    self.client = openai.OpenAI(
                        base_url="https://openrouter.ai/api/v1",
                        api_key=config.OPENROUTER_API_KEY,
                    )
            
            elif self.provider == "openai":
                # OpenAI setup
                if config.OPENAI_API_KEY:
                    self.client = openai.OpenAI(api_key=config.OPENAI_API_KEY)
                    
        except Exception as e:
            print(f"⚠️  Error setting up AI provider '{self.provider}': {e}")

    def generate_caption(self, media_description, media_type="image"):
        """
        Generate a viral LinkedIn caption for uploaded media.
        
        This method creates engaging, professional LinkedIn captions optimized
        for maximum engagement. The caption includes hooks, value propositions,
        and relevant hashtags.
        
        Args:
            media_description (str): Description or context of the media file
            media_type (str): Type of media ("image", "video", "document")
        
        Returns:
            str: Generated viral caption ready for LinkedIn posting
        
        Example:
            >>> ai = ViralAI()
            >>> caption = ai.generate_caption(
            ...     "Team celebrating product launch",
            ...     "image"
            ... )
        """
        prompt = f"""
        You are a LinkedIn Viral Content Expert. 
        Create a high-engagement LinkedIn post for a {media_type}.
        
        Context/Description: "{media_description}"
        
        Rules:
        1. Hook the reader immediately.
        2. Use short, punchy lines.
        3. Add value/insight using the context.
        4. End with a question or CTA.
        5. Include 3-5 relevant hashtags.
        6. NO pre-amble (like "Here is the post"). Just the post text.
        """
        return self._generate(prompt)

    def generate_text_post(self):
        """
        Generate a text-only viral LinkedIn post from scratch.
        
        When no media is available, this method creates engaging text-only
        content on trending professional topics. Perfect for maintaining
        consistent posting schedules.
        
        Returns:
            str: Complete text-only LinkedIn post with hooks and hashtags
        
        Example:
            >>> ai = ViralAI()
            >>> post = ai.generate_text_post()
            >>> print(post)
        """
        prompt = """
        You are a LinkedIn Viral Content Expert.
        Create a text-only LinkedIn post that goes viral.
        
        Topic Ideas (Pick one randomly):
        - AI automation trends
        - Productivity hacks for developers
        - The future of work
        - Python programming tips
        - Career growth in Tech
        
        Rules:
        1. Start with a controversial or strong hook.
        2. Tell a brief story or list actionable tips.
        3. Use plenty of whitespace (line breaks).
        4. Keep it under 150 words.
        5. End with a strong CTA.
        6. Include 3 hashtags.
        7. Output ONLY the post content.
        """
        return self._generate(prompt)

    def _generate(self, prompt):
        """
        Internal method to handle AI generation across all providers.
        
        This unified generation method abstracts the differences between
        AI providers, providing a consistent interface regardless of which
        backend is being used.
        
        Args:
            prompt (str): The generation prompt
        
        Returns:
            str: Generated content or error message
        """
        try:
            # Google Gemini generation
            if self.provider == "gemini" and hasattr(self, 'gemini_model'):
                response = self.gemini_model.generate_content(prompt)
                return response.text.strip()
            
            # OpenAI/OpenRouter generation (both use OpenAI-compatible API)
            elif (self.provider == "openrouter" or self.provider == "openai") and self.client:
                model = config.VIRAL_MODEL
                
                # Fallback to default models if not configured
                if not model:
                    model = "openai/gpt-4o-mini" if self.provider == "openrouter" else "gpt-4o"

                response = self.client.chat.completions.create(
                    model=model,
                    messages=[{"role": "user", "content": prompt}],
                )
                return response.choices[0].message.content.strip()
        
        except Exception as e:
            return f"❌ Error with {self.provider}: {e}"
        
        return "❌ Error: AI Provider incorrect or not configured."

    def analyze_media(self, media_path):
        """
        Analyze uploaded media to generate contextual descriptions.
        
        This is a placeholder for future vision AI integration. Currently
        returns a basic description based on filename.
        
        Args:
            media_path (str): Path to the media file
        
        Returns:
            str: Description of the media content
        
        Note:
            Future versions will integrate vision AI for actual image analysis
        """
        # TODO: Integrate vision AI (Gemini Vision, GPT-4 Vision, etc.)
        return f"A professional visual related to {os.path.basename(media_path)}"
