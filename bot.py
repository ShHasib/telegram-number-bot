 import re
from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, filters, ContextTypes

used_numbers = {}

async def check_number(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text
    user = update.effective_user

    numbers = re.findall(r'\+?\d{7,15}', text)

    if numbers:
        number = numbers[0]

        username = user.username if user.username else user.first_name

        if number in used_numbers:
            used_by = used_numbers[number]
            await update.message.reply_text(f"❌ Already Used by: @{used_by}")
        else:
            used_numbers[number] = username
            await update.message.reply_text("✅ Available")

app = ApplicationBuilder().token("8215918965:AAGn83KeyVMYlPN-cGXEtnLmvmqNUNBT_UY").build()

app.add_handler(MessageHandler(filters.TEXT, check_number))

print("Bot Running...")
app.run_polling()
