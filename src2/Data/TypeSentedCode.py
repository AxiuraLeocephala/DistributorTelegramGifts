from pyrogram import enums

SENT_CODE_DESCRIPTIONS = {
    enums.SentCodeType.APP: 'Telegram app',
    enums.SentCodeType.SMS: 'SMS',
    enums.SentCodeType.CALL: 'phone call',
    enums.SentCodeType.FLASH_CALL: 'phone flash call',
    enums.SentCodeType.FRAGMENT_SMS: 'Fragment SMS',
    enums.SentCodeType.EMAIL_CODE: 'email code'
}