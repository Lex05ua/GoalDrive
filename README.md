# 🚗 GoalDrive Tracker Bot

**GoalDrive** is a Telegram bot designed to help users (especially aspiring IT professionals) visualize their financial goals, track savings for a car, and calculate the actual "work effort" required to reach the target.

## 🌟 Why this project?
I created this tool to solve a personal challenge: staying motivated while saving for a car. It bridges the gap between raw numbers and the real effort needed, converting car prices into work hours based on target IT salaries.

## 🚀 Features
- **Goal Setting:** Set a target price for your dream car.
- **Progress Tracking:** Add savings and see your progress percentage in real-time.
- **Effort Calculation:** Automatically calculates how many work hours/days are left based on your hourly rate.
- **English Interface:** Built for the international/EU market.

## 🛠 Tech Stack
- **Language:** Python 3.10+
- **Framework:** [Aiogram 3.x](https://docs.aiogram.dev/) (Asynchronous Telegram Bot API)
- **Concepts used:** Separation of concerns (Logic vs Interface), Environment variables, Asynchronous programming.

## 📦 Installation & Setup

## ⚙️ Installation & Setup

1. Clone the repository:
   git clone https://github.com/Lex05ua/GoalDrive.git
   cd GoalDrive

2. Create a virtual environment:
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate

3. Install dependencies:
   pip install -r requirements.txt

4. Configure Environment Variables:
   Create a .env file in the root directory and add your bot token:
   BOT_TOKEN=your_telegram_bot_token_here

5. Run the bot:
   python main.py

---

## 🤖 Bot Commands
- /start - Get welcome message and command list.
- /set_goal [amount] - Define the target car price (e.g., /set_goal 20000).
- /add [amount] - Add your latest savings to the tracker.
- /status - View your detailed progress report and work effort analysis.

---

## 📈 Roadmap
- [ ] Database Integration: Move from in-memory storage to SQLite for persistence.
- [ ] Currency Support: Add automatic conversion between EUR, PLN, and USD.
- [ ] Multi-user Support: Allow multiple users to have independent profiles.
- [ ] Deployment: Host the bot on a VPS (Hetzner/Oracle Cloud) for 24/7 availability.

---

## 👨‍💻 Author
**Oleksii Vielkov**
*Aspiring Python Developer based in the EU.*
[GitHub](https://github.com/Lex05ua)