"""
LinkedIn Viral Bot - Media File Manager
Copyright (c) 2022-2026 Ashraf Morningstar
GitHub: https://github.com/AshrafMorningstar/LinkedIn-Viral-Bot

This module handles media file detection, validation, and archiving for the
LinkedIn automation workflow.

This project is a personal recreation developed for learning and skill development.
Licensed under the MIT License - see LICENSE file for details.
"""

import os
import shutil
import config


class MediaManager:
    """
    Media File Manager for LinkedIn Post Automation
    
    This class manages the lifecycle of media files used in LinkedIn posts,
    including detection, validation, type identification, and archiving after
    successful posting.
    
    Supported Media Types:
        - Images: .jpg, .jpeg, .png, .gif
        - Videos: .mp4
        - Documents: .pdf
    
    Attributes:
        input_dir (str): Directory path for new media files
        archive_dir (str): Directory path for processed media files
    
    Example:
        >>> manager = MediaManager()
        >>> media_path = manager.get_next_media()
        >>> if media_path:
        ...     media_type = manager.get_media_type(media_path)
        ...     # ... process the media ...
        ...     manager.archive_media(media_path)
    """
    
    def __init__(self):
        """
        Initialize the Media Manager and ensure required directories exist.
        
        Creates input_media and archive directories if they don't exist,
        preventing file operation errors during runtime.
        """
        self.input_dir = config.INPUT_MEDIA_DIR
        self.archive_dir = config.ARCHIVE_DIR
        
        # Ensure directories exist
        if not os.path.exists(self.input_dir):
            os.makedirs(self.input_dir)
            print(f"📁 Created input directory: {self.input_dir}")
            
        if not os.path.exists(self.archive_dir):
            os.makedirs(self.archive_dir)
            print(f"📁 Created archive directory: {self.archive_dir}")

    def get_next_media(self):
        """
        Find and return the first supported media file in the input directory.
        
        This method scans the input_media folder and returns the path to the
        first file with a supported extension. Files are processed in the order
        they appear in the directory listing.
        
        Returns:
            str or None: Absolute path to the media file, or None if no media found
        
        Example:
            >>> manager = MediaManager()
            >>> media = manager.get_next_media()
            >>> if media:
            ...     print(f"Found: {media}")
            ... else:
            ...     print("No media files available")
        """
        # Supported file extensions (case-insensitive)
        supported_exts = ('.jpg', '.jpeg', '.png', '.mp4', '.pdf', '.gif')
        
        try:
            files = os.listdir(self.input_dir)
            for file in files:
                if file.lower().endswith(supported_exts):
                    full_path = os.path.join(self.input_dir, file)
                    print(f"📎 Found media file: {file}")
                    return full_path
        except Exception as e:
            print(f"⚠️  Error scanning input directory: {e}")
        
        return None

    def archive_media(self, media_path):
        """
        Move processed media file to the archive directory.
        
        After a post is successfully scheduled, this method moves the media
        file to the archive folder to prevent reprocessing and maintain a
        clean workflow.
        
        Args:
            media_path (str): Absolute path to the media file to archive
        
        Example:
            >>> manager = MediaManager()
            >>> manager.archive_media("/path/to/image.jpg")
            ✅ Archived: image.jpg
        """
        filename = os.path.basename(media_path)
        dest_path = os.path.join(self.archive_dir, filename)
        
        try:
            shutil.move(media_path, dest_path)
            print(f"✅ Archived: {filename}")
        except Exception as e:
            print(f"⚠️  Error archiving {filename}: {e}")

    def get_media_type(self, media_path):
        """
        Identify the type of media file based on its extension.
        
        This classification is used to optimize AI prompts and LinkedIn
        posting strategies for different media types.
        
        Args:
            media_path (str): Path to the media file
        
        Returns:
            str: Media type - "document", "video", or "image"
        
        Example:
            >>> manager = MediaManager()
            >>> media_type = manager.get_media_type("presentation.pdf")
            >>> print(media_type)  # Output: "document"
        """
        extension = media_path.lower()
        
        if extension.endswith('.pdf'):
            return "document"
        elif extension.endswith('.mp4'):
            return "video"
        else:
            return "image"
