from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

class Translation(object):



    START_TEXT = """
Hey {} 

I am Telegram Most Powerful Media Encoder Bot

I can Encode Any Video or File in Negligible Quality

Use Help Command to Know How to Use me

Made By @Vedant_Vn
"""
    HELP_TEXT = """
Recommended
➠ Just Send Me Media To Get Started

Delete Thumbnail
➠ Send /dthumb To Delete Thumbnail

Set Thumbnail
➠ Reply To Photo With /sthumb To Save Thumbnail

Settings
➠ Use /settings Command To Check Settings

Made With By @AnimeSigma_Network
"""
    ABOUT_TEXT = """
🤖 My Name : Media-Encoder-Bot\n
🚦 Version : <a href='https://telegram.me/tellybots_4u'>2.0</a>\n
💫 Source Code : <a href='https://t.me/tellybots_digital'>Click Here</a>\n
🗃️ Library : <a href='https://pyrogram.org'>Click Here</a>\n
👲 Developer : <a href='https://telegram.me/tellybots_4u'>TellyBots_4u</a>\n
📦 Last Updated : <a href='https://telegram.me/tellybots_4u'>[ 15-Dec-21 ] 15:00 PM</a>"""

    START_BUTTONS = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('Anime Channel', url='https://telegram.me/AnimeSigma'),
        InlineKeyboardButton('💬 Support Group', url='https://telegram.me/NarutoRobot_support')
        ],[
        InlineKeyboardButton('❔ Help', callback_data='help'),
        InlineKeyboardButton('⛔ Close', callback_data='close')
        ]]
    )
    HELP_BUTTONS = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('🏡 Home', callback_data='home'),
        InlineKeyboardButton('👲 About', callback_data='about'),
        InlineKeyboardButton('⛔ Close', callback_data='close')
        ]]
    )
    ABOUT_BUTTONS = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('🏡 Home', callback_data='home'),
        InlineKeyboardButton('❔ Help', callback_data='help'),
        InlineKeyboardButton('⛔ Close', callback_data='close')
        ]]
    )
    BUTTONS = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('⛔ Close', callback_data='close')
        ]]
    )
