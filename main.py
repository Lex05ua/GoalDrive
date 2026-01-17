import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
import logic

# 1. Setup
API_TOKEN = '8281048213:AAExinKV9RzqCD6gJ_TfS6zvGTfvTFRCrtE'
bot = Bot(token=API_TOKEN)
dp = Dispatcher()

user_settings = {
    "goal_price": 0.0,
    "current_savings": 0.0,
    "monthly_deposit": 0.0,
    "hourly_rate": 25.0
}


# 2. Command Handlers
@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    await message.answer(
        "🚗 **Welcome to GoalDrive!**\n\n"
        "I will help you track your car savings.\n"
        "Commands:\n"
        "/set_goal [amount] - Set car price\n"
        "/add [amount] - Add savings\n"
        "/set_monthly [amount] - Your monthly savings\n"
        "/status - Check your progress"
    )


@dp.message(Command("set_goal"))
async def cmd_set_goal(message: types.Message):

    parts = message.text.split()


    if len(parts) < 2:
        await message.answer(
            "⚠️ **You forgot to provide the price!**\n\n"
            "Please send the command and the number in ONE message.\n"
            "Example: `/set_goal 15000`",
            parse_mode="Markdown"
        )
        return

    try:
        # Пробуем превратить второе слово в число
        amount = float(parts[1].replace(',', '.'))  # На случай если введут 15000,5
        user_settings["goal_price"] = amount
        await message.answer(f"✅ Success! Your target car price is now **€{amount:,.2f}**")
    except ValueError:
        # Если вместо числа ввели буквы
        await message.answer("❌ Error: Please provide a valid number (e.g., 15000).")


@dp.message(Command("add"))
async def cmd_add(message: types.Message):
    try:
        amount = float(message.text.split()[1])
        user_settings["current_savings"] += amount

        prog = logic.get_progress_percentage(user_settings["goal_price"], user_settings["current_savings"])
        await message.answer(f"💰 Saved €{amount} more!\nProgress: {prog}%")
    except:
        await message.answer("❌ Usage: /add 500")


@dp.message(Command("status"))
async def cmd_status(message: types.Message):
    goal = user_settings["goal_price"]
    current = user_settings["current_savings"]
    monthly = user_settings["monthly_deposit"]

    if goal == 0:
        await message.answer("Please set your goal price first using /set_goal")
        return

    prog = logic.get_progress_percentage(goal, current)
    effort = logic.get_work_effort(goal, user_settings["hourly_rate"])

    msg = (
        f"📊 **Current Status**\n\n"
        f"Target Price: €{goal}\n"
        f"Saved so far: €{current}\n"
        f"Progress: {prog}%\n\n"
        f"💡 This car costs **{effort['hours']} hours** of your IT work."
    )
    await message.answer(msg)


# 3. Start the bot
async def run():
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(run())