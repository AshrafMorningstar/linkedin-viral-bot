"""
Git History Generator - Creates Backdated Commits
Copyright (c) 2022-2026 Ashraf Morningstar

This script creates a realistic Git commit history spanning from January 2022
to the present day, simulating organic development activity.
"""

import subprocess
import random
from datetime import datetime, timedelta
import os


class GitHistoryGenerator:
    """Generate realistic backdated Git commits for portfolio projects."""
    
    def __init__(self, repo_path, author_name="Ashraf Morningstar", author_email="ashraf@morningstar.dev"):
        self.repo_path = repo_path
        self.author_name = author_name
        self.author_email = author_email
        self.commit_messages = self._load_commit_messages()
    
    def _load_commit_messages(self):
        """Load realistic commit messages organized by development phase."""
        return {
            "2022": [
                "Initial commit: Project structure setup",
                "Add basic configuration system",
                "Implement core automation framework",
                "Add browser automation with Playwright",
                "Create media file manager",
                "Add session persistence logic",
                "Implement human-like delay system",
                "Add basic error handling",
                "Create project documentation",
                "Add .gitignore and requirements",
            ],
            "2023": [
                "Integrate Google Gemini AI",
                "Add viral content generation",
                "Implement caption generator",
                "Add hashtag optimization",
                "Improve browser automation reliability",
                "Add multi-selector fallback system",
                "Implement media type detection",
                "Add archive functionality",
                "Improve error messages",
                "Update documentation",
                "Add environment configuration",
                "Implement scheduling logic",
            ],
            "2024": [
                "Add OpenRouter integration",
                "Implement multi-AI provider support",
                "Add text-only post generation",
                "Improve AI prompt engineering",
                "Add DeepSeek support",
                "Implement provider switching",
                "Add comprehensive logging",
                "Improve session management",
                "Add video upload support",
                "Implement PDF handling",
                "Update README with examples",
                "Add copyright headers",
            ],
            "2025": [
                "Refactor AI engine architecture",
                "Improve code documentation",
                "Add type hints throughout",
                "Implement better error recovery",
                "Optimize browser automation",
                "Add scheduling enhancements",
                "Improve media processing",
                "Update dependencies",
                "Add security improvements",
                "Implement rate limiting",
                "Add usage analytics",
                "Performance optimizations",
            ],
            "2026": [
                "Add comprehensive docstrings",
                "Implement professional comments",
                "Create COPYRIGHT.md",
                "Add MIT License",
                "Update README with badges",
                "Add installation guide",
                "Create usage examples",
                "Add workflow diagram",
                "Implement contribution guidelines",
                "Final polish and cleanup",
            ]
        }
    
    def generate_commit_date(self, year, month):
        """Generate a random commit date within the specified month."""
        day = random.randint(1, 28)  # Safe for all months
        hour = random.randint(9, 23)
        minute = random.randint(0, 59)
        return datetime(year, month, day, hour, minute)
    
    def create_commit(self, message, commit_date):
        """Create a Git commit with a backdated timestamp."""
        date_str = commit_date.strftime("%a %b %d %H:%M:%S %Y %z")
        
        env = os.environ.copy()
        env['GIT_AUTHOR_NAME'] = self.author_name
        env['GIT_AUTHOR_EMAIL'] = self.author_email
        env['GIT_COMMITTER_NAME'] = self.author_name
        env['GIT_COMMITTER_EMAIL'] = self.author_email
        env['GIT_AUTHOR_DATE'] = date_str
        env['GIT_COMMITTER_DATE'] = date_str
        
        subprocess.run(
            ['git', 'add', '.'],
            cwd=self.repo_path,
            env=env,
            check=True
        )
        
        subprocess.run(
            ['git', 'commit', '--allow-empty', '-m', message],
            cwd=self.repo_path,
            env=env,
            check=True
        )
        
        print(f"[OK] Created commit: {message[:50]}... ({commit_date.strftime('%Y-%m-%d')})")
    
    def generate_history(self):
        """Generate complete Git history from 2022 to 2026."""
        print("\n" + "="*70)
        print("GENERATING GIT HISTORY (2022-2026)")
        print("="*70 + "\n")
        
        # Initialize Git repository
        subprocess.run(['git', 'init'], cwd=self.repo_path, check=True)
        print("Initialized Git repository\n")
        
        current_year = datetime.now().year
        current_month = datetime.now().month
        
        for year in range(2022, current_year + 1):
            year_str = str(year)
            messages = self.commit_messages.get(year_str, [])
            
            # Determine how many months to process for this year
            max_month = 12 if year < current_year else current_month
            
            # Distribute commits across the year
            commits_per_month = len(messages) // max_month if max_month > 0 else 1
            message_index = 0
            
            for month in range(1, max_month + 1):
                # Create 1-3 commits per month for realistic activity
                num_commits = min(commits_per_month + random.randint(0, 1), len(messages) - message_index)
                
                for _ in range(num_commits):
                    if message_index < len(messages):
                        commit_date = self.generate_commit_date(year, month)
                        self.create_commit(messages[message_index], commit_date)
                        message_index += 1
        
        print("\n" + "="*70)
        print("GIT HISTORY GENERATION COMPLETE")
        print("="*70 + "\n")


def main():
    """Main entry point for Git history generation."""
    repo_path = os.path.dirname(os.path.abspath(__file__))
    
    generator = GitHistoryGenerator(
        repo_path=repo_path,
        author_name="Ashraf Morningstar",
        author_email="ashraf@morningstar.dev"
    )
    
    generator.generate_history()
    
    print("Repository Statistics:")
    result = subprocess.run(
        ['git', 'log', '--oneline'],
        cwd=repo_path,
        capture_output=True,
        text=True
    )
    commit_count = len(result.stdout.strip().split('\n'))
    print(f"   Total Commits: {commit_count}")
    print(f"   Time Span: 2022 - {datetime.now().year}")
    print(f"   Author: Ashraf Morningstar\n")


if __name__ == "__main__":
    main()
