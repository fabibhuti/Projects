import urllib.request
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, MessageHandler, filters
from rembg import remove
from PIL import Image




# /start command
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    print(f'{update.effective_user.full_name} started the conversation')
    await update.message.reply_text(f'Send Any Image File, And I Will Try To Remove Background From It.')

# / hello command
async def hello(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f'Hello {update.effective_user.first_name}')

# image file
async def process_image(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    print(f'{update.effective_user.full_name} sent an image to remove background')
    try:
        # Retrieve image data from the bot's response
        photo_file = update.message.photo[-1]
        file_id = photo_file.file_id

        # Download the image
        downloaded_file = await context.bot.get_file(file_id)
        image_path = downloaded_file.file_path

        # save in root directory
        urllib.request.urlretrieve(image_path, './braintumor.jpg')
        input_path = './braintumor.jpg'
        output_path = './removed.png'

        img = Image.open(input_path)
        print("Done 0")

        output = remove(img)
        print("Done 1")

        output.save(output_path)
        print("Done 2")
        print(f"Background removed successfully. Image saved to removed.png")

        # Reply the user
        await update.message.reply_photo(open("./removed.png", 'rb'), caption="Your Image Without BG")
        print("Done 3")

    except Exception as e:
        await update.message.reply_text(f"An error occurred: {e}")
        print("Not Done")




if __name__ == "__main__":
    API_KEY = "<Bot API Key from Botfather>"

    app = ApplicationBuilder().token(API_KEY).build()

    app.add_handler(CommandHandler("hello", hello))
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.PHOTO, process_image))

    app.run_polling()