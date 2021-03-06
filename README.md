# pyline_notify

[LINE Notify API Document](https://notify-bot.line.me/doc/ja/) super simple client

# usage

## typical sample

```
#!/usr/bin/env python

from pyline_notify import PyLINENotify

YOUR_LINE_TOKEN = "xxxxxx"
line = PyLINENotify(YOUR_LINE_TOKEN)
res = line.notify("hello world")
if res.is_success():
    print("done")
else:
    print(res.message())
```

## advanced

### stickerId and stickerPackageId

see [here](https://developers.line.biz/ja/docs/messaging-api/sticker-list/)

```
res = line.notify("hello world", stickerPackageId=446, stickerId=1988)
```

### imageFile

```
image_file = "/path/to/image.jpg"
res = line.notify("hello world", imageFile=image_file)

# or 
with open(image_file, "rb") as f:
    res = line.notify("hello world", imageFile=f)
```

# install

```
pip install git+https://github.com/holly/pyline_notify.git
```

# Lincense

MIT.
