import re
from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, filters, ContextTypes

used_numbers = set()

async def check_number(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text

    # নাম্বার খুঁজবে যেকোনো দেশের জন্য
    numbers = re.findall(r'\+?\d{7,15}', text)

    if numbers:
        number = numbers[0]

        if number in used_numbers:
            await update.message.reply_text("❌ Already Used")
        else:
            used_numbers.add(number)
            await update.message.reply_text("✅ Available")

# Bot Token বসাও
app = ApplicationBuilder().token("8215918965:AAGn83KeyVMYlPN-cGXEtnLmvmqNUNBT_UY").build()

# সব টেক্সট মেসেজ চেক করবে
app.add_handler(MessageHandler(filters.TEXT, check_number))

app.run_polling()
