# YiriMirai

> [YiriMirai](https://github.com/YiriMiraiProject/YiriMirai) 的分支。专用于 [QChatGPT](https://github.com/RockChinQ/QChatGPT)。
> PyPI: `yiri-mirai-rc`

<br>

[![PyPI](https://img.shields.io/pypi/v/yiri-mirai-rc)](https://pypi.org/project/yiri-mirai-rc/)
[![Document](https://img.shields.io/badge/document-vercel-brightgreen)](https://yiri-mirai.vercel.app)

一个轻量级、低耦合度的基于 mirai-api-http 的 Python SDK。

**本项目适用于 mirai-api-http 2.0 以上版本**。

## 安装

从 PyPI 安装：

```shell
pip install yiri-mirai-rc
```

## 使用

```python
from mirai import Mirai, FriendMessage, WebSocketAdapter

if __name__ == '__main__':
    bot = Mirai(12345678, adapter=WebSocketAdapter(
        verify_key='your_verify_key', host='localhost', port=6090
    ))

    @bot.on(FriendMessage)
    async def on_friend_message(event: FriendMessage):
        if str(event.message_chain) == '你好':
            await bot.send(event, 'Hello World!')

    bot.run()
```

更多信息参看[文档](https://yiri-mirai.wybxc.cc/)或[文档镜像](https://yiri-mirai.vercel.app)。
