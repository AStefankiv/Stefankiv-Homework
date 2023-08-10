# from telegram import Update
# from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
#
#
# async def hello(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
#     await update.message.reply_text(f'Hello {update.effective_user.first_name}')
#
#
# app = ApplicationBuilder().token("5945953214:AAEcfnBgUY5A63qNWl1nKQjPNDurax7dRrs").build()
#
# app.add_handler(CommandHandler("hello", hello))
#
# app.run_polling()
#########################################################################################################


import logging
import datetime
from telegram import Update, ReplyKeyboardMarkup, ReplyKeyboardRemove
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, ConversationHandler, ContextTypes
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from google_auth_oauthlib.flow import InstalledAppFlow

logging.basicConfig(level=logging.INFO)
DATE_INPUT, TIME_INPUT = range(2)

async def hello(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f'Hello {update.effective_user.first_name}')

async def start_booking(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    today = datetime.date.today()
    next_7_days = [today + datetime.timedelta(days=i) for i in range(7)]
    date_options = [date.strftime("%d %B %Y") for date in next_7_days]

    if len(date_options) % 2 != 0:
        date_options.append("")

    context.user_data["date_options"] = date_options

    keyboard = [[date_options[i], date_options[i + 1]] for i in range(0, len(date_options), 2)]
    keyboard.append(["Cancel"])
    reply_markup = ReplyKeyboardMarkup(keyboard, one_time_keyboard=True)

    await update.message.reply_text("Please select a booking date:", reply_markup=reply_markup)
    return DATE_INPUT

async def get_date(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    input_date = update.message.text

    if input_date in context.user_data.get("date_options", []):
        context.user_data["date"] = input_date
        await update.message.reply_text(f"You chose: {input_date}")

        keyboard = [["10 AM", "11 AM", "12 PM", "1 PM", "2 PM", "3 PM", "4 PM", "5 PM", "6 PM"], ["Cancel"]]
        reply_markup = ReplyKeyboardMarkup(keyboard, one_time_keyboard=True)
        await update.message.reply_text("Please select a booking time:", reply_markup=reply_markup)
        return TIME_INPUT
    else:
        await update.message.reply_text("Invalid option. Please select a valid date option from the provided list.")
        return DATE_INPUT

SCOPES = ["https://www.googleapis.com/auth/calendar.events"]

def get_credentials():
    flow = InstalledAppFlow.from_client_secrets_file("credentials.json", SCOPES)
    flow.redirect_uri = "http://localhost:5000"
    credentials = flow.run_local_server(port=0)
    return credentials

async def get_time(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    time = update.message.text
    context.user_data["time"] = time
    chosen_date = context.user_data.get("date", "Unknown")

    try:
        event_summary = f"Lesson with {update.effective_user.first_name}"
        start_time = datetime.datetime.strptime(f"{chosen_date} {time}", "%d %B %Y %I %p")
        end_time = start_time + datetime.timedelta(hours=1)  # Assuming each lesson is 1 hour

        credentials = get_credentials()
        service = build("calendar", "v3", credentials=credentials)

        event = {
            "summary": event_summary,
            "start": {"dateTime": start_time.strftime("%Y-%m-%dT%H:%M:%S")},
            "end": {"dateTime": end_time.strftime("%Y-%m-%dT%H:%M:%S")},
        }

        event = service.events().insert(calendarId="primary", body=event).execute()

        print("Event created: %s" % (event.get("htmlLink")))

    except HttpError as err:
        print(f"An error occurred: {err}")

    zoom_link = "https://us06web.zoom.us/j/8182736518?pwd=U2E0bEp3alduWFFqbkF1THdrWDNhUT09"
    meeting_id = "818 273 6518"
    passcode = "11111"
    message = (
        f"Your lesson will be on {chosen_date.capitalize()} at {time}.\n"
        f"Here's the Zoom link: {zoom_link}.\n"
        f"Meeting ID: {meeting_id}, Passcode: {passcode}."
    )
    await update.message.reply_text(message, reply_markup=ReplyKeyboardRemove())
    return ConversationHandler.END


def cancel(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    update.message.reply_text("Booking canceled.", reply_markup=ReplyKeyboardRemove())

app = ApplicationBuilder().token("5945953214:AAEcfnBgUY5A63qNWl1nKQjPNDurax7dRrs").build()

app.add_handler(CommandHandler("hello", hello))
app.add_handler(CommandHandler("cancel", cancel))

booking_date_handler = ConversationHandler(
    entry_points=[CommandHandler('book', start_booking)],
    states={
        DATE_INPUT: [MessageHandler(None, get_date)],
        TIME_INPUT: [MessageHandler(None, get_time)],
    },
    fallbacks=[CommandHandler('cancel', cancel)],
)
app.add_handler(booking_date_handler)

if __name__ == "__main__":
    app.run_polling()