def showstagelist(stages, emotes2stage):
    text = ""
    for icon in stages:
        text += f"{icon} {emotes2stage[icon]}\n"
    return text


def channels_to_str(channel_ids):
    return ', '.join([channel_to_str(x) for x in channel_ids])


def channel_to_str(channel_id):
    return f"<#{channel_id}>"