import telebot
from datetime import datetime, timedelta
from persiantools.jdatetime import JalaliDate

# توکن ربات تلگرام خود را اینجا قرار دهید
TOKEN = '7130317382:AAH2uIe4IiXXsjPCJS61sH-Zqmo95ytmTqk'
bot = telebot.TeleBot(TOKEN)

# جمله‌های انگیزشی مختلف
inspirational_quotes = [
    "از همین امروز شروع کن، نتیجه‌ای که دیروز می‌خواستی فردا داشته باشی.",
    "هر روز، فرصتی برای شروع مسیری جدید است.",
    "بزرگترین انگیزه برای ادامه کار، آغاز کردن آن است.",
    "همیشه بهترین زمان برای شروع، الان است.",
    "پیشرفت کوچک، همیشه بهتر از انجام کاری ایده‌آل است.",
]

def get_remaining_time(target_date, current_date):
    # محاسبه مدت زمان باقی‌مانده
    remaining_time = target_date - current_date
    days_remaining = remaining_time.days
    hours_remaining, seconds_remaining = divmod(remaining_time.seconds, 3600)
    minutes_remaining, seconds_remaining = divmod(seconds_remaining, 60)
    
    return days_remaining, hours_remaining, minutes_remaining, seconds_remaining

@bot.message_handler(commands=['start'])
def welcome(message):
    bot.reply_to(message, "سلام! خوش آمدید. برای ادامه، دستور /erfan را اجرا کنید.")

@bot.message_handler(commands=['erfan'])
def erfan(message):
    # تاریخ معین را اینجا تنظیم کنید (فرضاً تاریخ 1403/01/01)
    target_date = JalaliDate(1403, 2, 6).to_gregorian()
    current_date = datetime.now()
    
    # تبدیل تاریخ معین به شیء datetime
    target_date = datetime(target_date.year, target_date.month, target_date.day)
    
    # محاسبه مدت زمان باقی‌مانده بر حسب روز، ساعت، دقیقه و ثانیه
    days_remaining, hours_remaining, minutes_remaining, seconds_remaining = get_remaining_time(target_date, current_date)
    
    # نمایش نتیجه به کاربر
    message_text = (
        f"روزشمار بر حسب ماه و روز: {days_remaining // 31} ماه و {days_remaining % 31} روز و "
        f"{hours_remaining} ساعت {minutes_remaining} دقیقه و {seconds_remaining} ثانیه باقی مانده است.\n"
        
        f"روزشمار بر حسب روز: {days_remaining} روز، "
        f"{hours_remaining} ساعت، {minutes_remaining} دقیقه و {seconds_remaining} ثانیه باقی مانده است.\n"
        
        f"روز شمار بر حسب دقیقه: {days_remaining * 24 * 60 + hours_remaining * 60 + minutes_remaining} دقیقه "
        f"و {seconds_remaining} ثانیه باقی مانده است.\n"
        
        f"روزشمار بر حسب ثانیه: {days_remaining * 24 * 60 * 60 + hours_remaining * 60 * 60 + minutes_remaining * 60 + seconds_remaining} ثانیه باقی مانده است."
    )
    
    # اضافه کردن فاصله و استکیر بین جواب‌ها
    message_text += "\n" + "=" * 30 + "\n\n"
    
    # انتخاب و نمایش جمله انگیزشی
    message_text += inspirational_quotes[divmod(current_date.hour, 24)[0]]
    
    bot.reply_to(message, message_text)

bot.polling()
