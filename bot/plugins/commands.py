#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) @AlbertEinsteinTG

from pyrogram import filters, Client
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery
from bot import Translation # pylint: disable=import-error
from bot.database import Database # pylint: disable=import-error

db = Database()

@Client.on_message(filters.command(["start"]) & filters.private, group=1)
async def start(bot, update):
    
    try:
        file_uid = update.command[1]
    except IndexError:
        file_uid = False
    
    if file_uid:
        file_id, file_name, file_caption, file_type = await db.get_file(file_uid)
        
        if (file_id or file_type) == None:
            return
        
        caption = file_caption if file_caption != ("" or None) else ("<code>" + file_name + "</code>")
        
        if file_type == "document":
        
            await bot.send_document(
                chat_id=update.chat.id,
                document = file_id,
                caption = caption,
                parse_mode="html",
                reply_to_message_id=update.message_id,
                reply_markup=InlineKeyboardMarkup(
                    [
                        [
                            InlineKeyboardButton
                                (
                                    '📲JOIN CHANNEL👨🏻‍💻', url="https://t.me/Zeekeralamofficial"
                                )
                        ]
                    ]
                )
            )

        elif file_type == "video":
        
            await bot.send_video(
                chat_id=update.chat.id,
                video = file_id,
                caption = caption,
                parse_mode="html",
                reply_markup=InlineKeyboardMarkup(
                    [
                        [
                            InlineKeyboardButton
                                (
                                    '📲JOIN CHANNEL👨🏻‍💻', url="https://t.me/Zeekeralamofficial"
                                )
                        ]
                    ]
                )
            )
            
        elif file_type == "audio":
        
            await bot.send_audio(
                chat_id=update.chat.id,
                audio = file_id,
                caption = caption,
                parse_mode="html",
                reply_markup=InlineKeyboardMarkup(
                    [
                        [
                            InlineKeyboardButton
                                (
                                    '📲JOIN CHANNEL👨🏻‍💻', url="https://t.me/Zeekeralamofficial"
                                )
                        ]
                    ]
                )
            )

        else:
            print(file_type)
        
        return

    buttons = [[
        InlineKeyboardButton('📲MAIN CHANNEL👨🏻‍💻', url='https://t.me/Zee_Keralam')
    ],[
        InlineKeyboardButton('📲CHANNEL👨🏻‍💻', url='https://t.me/joinchat/5oLHikFN-sA0MDA1'),
        InlineKeyboardButton('📲GROUP👨🏻‍💻', url='https://t.me/joinchat/q8li6l90_KVlYjE1')
    ]'[   
        InlineKeyboardButton('🤕HELP ME🚑', url='https://t.me/Zee_keralambot')
        
    reply_markup = InlineKeyboardMarkup(buttons)
    
    await bot.send_photo(
                chat_id = update.chat.id,
                photo= "https://telegra.ph/file/b18e228ed4a1717d31377.jpg",
                caption=f"<b>എന്റെ പ്രാർത്ഥനങ്ങൾ അഡ്മിന്റെ വാക്കുകൾക്കാണ്</b>\n\n<b>എന്റെ അഡ്മിന്റെ അവകാശമില്ലാതെ എന്നെ ഉപയോഗിക്കാൻ പറ്റില്ല</b>",
    reply_markup=reply_markup,        reply_to_message_id=update.message_id
            )


@Client.on_message(filters.command(["help"]) & filters.private, group=1)
async def help(bot, update):
    buttons = [[
        InlineKeyboardButton('Close 🔐', callback_data='close')
    ]]
    
    reply_markup = InlineKeyboardMarkup(buttons)
    
    await bot.send_message(
        chat_id=update.chat.id,
        text=Translation.HELP_TEXT,
        reply_markup=reply_markup,
        parse_mode="html",
        reply_to_message_id=update.message_id
    )


@Client.on_message(filters.command(["about"]) & filters.private, group=1)
async def about(bot, update):
    
    buttons = [[
        InlineKeyboardButton('Home ⚡', callback_data='start'),
        InlineKeyboardButton('Close 🔐', callback_data='close')
    ]]
    reply_markup = InlineKeyboardMarkup(buttons)
    
    await bot.send_message(
        chat_id=update.chat.id,
        text=Translation.ABOUT_TEXT,
        reply_markup=reply_markup,
        disable_web_page_preview=True,
        parse_mode="html",
        reply_to_message_id=update.message_id
    )
