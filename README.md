# 🚀 LinkedIn Viral Bot

<div align="center">

![Python Version](https://img.shields.io/badge/python-3.8%2B-blue)
![License](https://img.shields.io/badge/license-MIT-green)
![Status](https://img.shields.io/badge/status-active-success)
![Contributions](https://img.shields.io/badge/contributions-welcome-brightgreen)

**AI-Powered LinkedIn Automation Suite for Viral Content Creation & Scheduling**

[Features](#-features) • [Installation](#-installation) • [Usage](#-usage) • [Configuration](#-configuration) • [License](#-license)

</div>

---

## 📋 Overview

**LinkedIn Viral Bot** is an intelligent automation tool that combines AI-powered content generation with human-like browser automation to create and schedule engaging LinkedIn posts. Never run out of content ideas or miss optimal posting times again!

### ✨ Key Highlights

- 🤖 **Multi-AI Support**: Integrates with Google Gemini, OpenAI, DeepSeek, and OpenRouter
- 📸 **Media Intelligence**: Automatically processes images, videos, and PDFs
- ✍️ **Text-Only Mode**: Generates viral text posts when no media is available
- 🕐 **Smart Scheduling**: Uses LinkedIn's native scheduler (never posts directly)
- 🔐 **Session Persistence**: Login once, reuse forever with cookie storage
- 🎭 **Human-Like Behavior**: Random delays and realistic interactions to avoid detection

---

## 🎯 Features

### AI Content Generation

- **Viral Caption Generator**: Creates engaging hooks, value propositions, and CTAs
- **Hashtag Optimization**: Automatically includes relevant, high-traffic hashtags
- **Text-Only Posts**: Generates complete posts when no media is available
- **Multi-Provider Support**: Switch between Gemini, OpenAI, DeepSeek, or OpenRouter

### Browser Automation

- **Playwright-Powered**: Reliable, modern browser automation
- **Session Management**: Persistent login with cookie storage
- **Human-Like Delays**: Randomized timing to mimic real user behavior
- **Robust Selectors**: Multiple fallback strategies for UI changes

### Media Handling

- **Supported Formats**: JPG, PNG, GIF, MP4, PDF
- **Auto-Detection**: Scans input folder for new media
- **Smart Archiving**: Moves processed files to archive folder
- **Type Recognition**: Optimizes AI prompts based on media type

---

## 🛠️ Installation

### Prerequisites

- Python 3.8 or higher
- pip (Python package manager)
- Git (for cloning)

### Step 1: Clone the Repository

```bash
git clone https://github.com/AshrafMorningstar/LinkedIn-Viral-Bot.git
cd LinkedIn-Viral-Bot
```

### Step 2: Install Dependencies

```bash
pip install -r requirements.txt
playwright install
```

### Step 3: Configure Environment

```bash
# Copy the example environment file
cp .env.example .env

# Edit .env and add your API keys
# Get keys from:
# - Google Gemini: https://aistudio.google.com/api-keys
# - OpenRouter: https://openrouter.ai/
# - OpenAI: https://platform.openai.com/
```

---

## 🚀 Usage

### Quick Start

1. **Add Media** (optional):

   ```bash
   # Place images/videos in the input_media folder
   cp your-image.jpg input_media/
   ```

2. **Run the Bot**:

   ```bash
   python main.py
   ```

3. **First-Time Login**:
   - The browser will open automatically
   - Log in to LinkedIn manually
   - Press Enter in the terminal
   - Your session will be saved for future runs

### Workflow

```
┌─────────────────┐
│  Check for      │
│  Media Files    │
└────────┬────────┘
         │
    ┌────▼────┐
    │ Found?  │
    └─┬────┬──┘
      │    │
   Yes│    │No
      │    │
┌─────▼──┐ │  ┌──────────────┐
│ Upload │ │  │  Generate    │
│ Media  │ │  │  Text-Only   │
│ + AI   │ │  │  Post with   │
│ Caption│ │  │  AI          │
└────┬───┘ │  └──────┬───────┘
     │     │         │
     └─────┴─────────┘
           │
    ┌──────▼──────┐
    │  Schedule   │
    │  on         │
    │  LinkedIn   │
    └──────┬──────┘
           │
    ┌──────▼──────┐
    │  Archive    │
    │  Media      │
    └─────────────┘
```

---

## ⚙️ Configuration

### AI Provider Selection

Edit `config.py` to choose your AI provider:

```python
AI_PROVIDER = "openrouter"  # Options: "gemini", "openai", "openrouter"
VIRAL_MODEL = "google/gemini-2.0-flash-lite-preview-02-05:free"
```

### Automation Settings

```python
MIN_DELAY = 5   # Minimum seconds between actions
MAX_DELAY = 15  # Maximum seconds between actions
HEADLESS_MODE = False  # Set True to hide browser window
```

### Scheduled Posting (Optional)

Uncomment in `main.py`:

```python
# Post every hour
schedule.every(1).hours.do(job)

# Post daily at 10 AM
schedule.every().day.at("10:00").do(job)

while True:
    schedule.run_pending()
    time.sleep(60)
```

---

## 📁 Project Structure

```
LinkedIn-Viral-Bot/
├── main.py              # Main orchestrator
├── ai_engine.py         # AI content generation
├── browser_bot.py       # Browser automation
├── media_manager.py     # Media file handling
├── config.py            # Configuration
├── requirements.txt     # Dependencies
├── .env.example         # Environment template
├── .gitignore          # Git ignore rules
├── LICENSE             # MIT License
├── COPYRIGHT.md        # Copyright policy
├── README.md           # This file
├── input_media/        # Place media files here
└── archive/            # Processed files moved here
```

---

## 🔒 Security & Privacy

- **API Keys**: Stored in `.env` (never committed to Git)
- **Session Cookies**: Saved locally in `state.json`
- **No Password Storage**: Manual login recommended for security
- **2FA Compatible**: Works with two-factor authentication

---

## ⚠️ Disclaimer

This tool is for **educational purposes** and personal use. Please ensure compliance with:

- LinkedIn's Terms of Service
- Automation policies
- Rate limits and usage guidelines

**The author is not responsible for account restrictions or violations resulting from misuse.**

---

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

---

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

**Copyright (c) 2022-2026 Ashraf Morningstar**

This is a personal recreation developed for learning and skill development. Original project concepts remain the intellectual property of their respective creators.

---

## 🙏 Acknowledgments

- **Playwright** - Modern browser automation
- **Google Gemini** - AI content generation
- **OpenRouter** - Multi-model AI access
- **OpenAI** - GPT models

---

## 📞 Contact

**Ashraf Morningstar**

- GitHub: [@AshrafMorningstar](https://github.com/AshrafMorningstar)
- Project Link: [https://github.com/AshrafMorningstar/LinkedIn-Viral-Bot](https://github.com/AshrafMorningstar/LinkedIn-Viral-Bot)

---

<div align="center">

**⭐ Star this repo if you find it useful!**

Made with ❤️ by Ashraf Morningstar

</div>
