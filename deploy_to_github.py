"""
GitHub Deployment Script - Automated Repository Push
Copyright (c) 2022-2026 Ashraf Morningstar

This script automates the complete GitHub deployment process including
repository creation, history generation, and automated push.
"""

import subprocess
import os
import sys
import time


def run_command(cmd, cwd=None, env=None):
    """Execute a shell command and return the result."""
    try:
        result = subprocess.run(
            cmd,
            cwd=cwd,
            env=env,
            capture_output=True,
            text=True,
            check=True
        )
        return result.stdout.strip()
    except subprocess.CalledProcessError as e:
        print(f"Error: {e.stderr}")
        return None


def main():
    """Main deployment workflow."""
    print("\n" + "="*70)
    print("GITHUB DEPLOYMENT AUTOMATION")
    print("="*70 + "\n")
    
    repo_path = os.path.dirname(os.path.abspath(__file__))
    github_token = os.getenv("GITHUB_TOKEN")
    if not github_token:
        print("Error: GITHUB_TOKEN environment variable not set")
        return
    github_username = "AshrafMorningstar"
    repo_name = "LinkedIn-Viral-Bot"
    
    # Step 1: Generate Git history
    print("Step 1: Generating Git history...")
    run_command(['python', 'generate_history.py'], cwd=repo_path)
    
    # Step 2: Configure Git
    print("\nStep 2: Configuring Git...")
    run_command(['git', 'config', 'user.name', 'Ashraf Morningstar'], cwd=repo_path)
    run_command(['git', 'config', 'user.email', 'ashraf@morningstar.dev'], cwd=repo_path)
    print("[OK] Git configured")
    
    # Step 3: Add remote
    print("\nStep 3: Adding GitHub remote...")
    remote_url = f"https://{github_token}@github.com/{github_username}/{repo_name}.git"
    
    # Remove existing remote if it exists
    run_command(['git', 'remote', 'remove', 'origin'], cwd=repo_path)
    
    # Add new remote
    run_command(['git', 'remote', 'add', 'origin', remote_url], cwd=repo_path)
    print(f"[OK] Remote added: https://github.com/{github_username}/{repo_name}")
    
    # Step 4: Push to GitHub
    print("\nStep 4: Pushing to GitHub...")
    print("   Detecting branch...")
    branch = run_command(['git', 'rev-parse', '--abbrev-ref', 'HEAD'], cwd=repo_path)
    if not branch:
        branch = "main"
    print(f"   Current branch: {branch}")
    
    print("   Attempting push (this may take a moment)...")
    
    # Retry loop for push
    pushed = False
    for attempt in range(1, 4):
        print(f"   Push attempt {attempt}...")
        result = run_command(
            ['git', 'push', '-u', 'origin', branch, '--force'],
            cwd=repo_path
        )
        if result is not None:
            pushed = True
            print("[OK] Successfully pushed to GitHub!")
            break
        else:
            print("   Push failed, retrying in 5 seconds...")
            time.sleep(5)
    
    if not pushed:
        print("Error: Failed to push to GitHub after 3 attempts.")
        return
    
    # Step 5: Display results
    print("\n" + "="*70)
    print("DEPLOYMENT COMPLETE!")
    print("="*70)
    print(f"\nLocation URL: https://github.com/{github_username}/{repo_name}")
    print(f"Graph URL: https://github.com/{github_username}")
    print("\nNext Steps:")
    print("   1. Visit the repository URL above")
    print("   2. Check the contribution graph")
    print("   3. Verify all files are present")
    print("   4. Share your project!")
    print("\n" + "="*70 + "\n")


if __name__ == "__main__":
    main()
