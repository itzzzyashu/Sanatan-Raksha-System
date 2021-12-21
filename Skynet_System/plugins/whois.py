from telethon.tl.functions.users import GetFullUserRequest
from Skynet_System import System, system_cmd


@System.on(system_cmd(pattern=r"whois"))
async def whois(event):
    try:
        to_get = event.pattern_match.group(1)
    except Exception:
        if event.reply:
            replied = await event.get_reply_message()
            to_get = int(replied.sender.id)
        else:
            return
    try:
        to_get = int(to_get)
    except Exception:
        pass
    try:
        data = await System(GetFullUserRequest(to_get))
    except Exception:
        await event.reply("Failed to get data of the user")
        return
    await System.send_message(
        event.chat_id,
        f"╒═══「 **Appraisal results** 」",
        f"\n**• First Name:** `{data.user.last_name}`",
        f"\n**• Last Name:** `{data.user.first_name}`",
        f"\n**• Username:** @{data.user.username}",
        f"\n**• Userlink:** [{data.user.first_name}](tg://user?id={data.user.id})",
        f"\n**• User ID:** `{data.user.id}`",
        f"\n**• About:** {data.about}",
    )


help_plus = """ Here is Help for **Whois** -
`whois` - get data of the user
`uid` - Generate user ID
**Notes:**
`/` `?` `.` `!` are supported prefixes.
**Example:** `/addenf` or `?addenf` or `.addenf`
"""
__plugin_name__ = "whois"
