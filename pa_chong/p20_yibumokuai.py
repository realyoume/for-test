# request.get 同步操作 --》 异步的操作  需要引入aiohttp

import asyncio
import aiohttp

urls = [
    'https://img3.doubanio.com/view/photo/s_ratio_poster/public/p2561716440.webp',
    'https://img2.doubanio.com/view/photo/s_ratio_poster/public/p2372307693.webp',
    'https://img2.doubanio.com/view/photo/s_ratio_poster/public/p511118051.webp',
    'https://img9.doubanio.com/view/photo/s_ratio_poster/public/p457760035.webp'
]


async def download(url):
    # s = aiohttp.ClientSession()  <==> requests
    # request.get()   .post()
    # s.get()  .post()
    name = url.split("/")[-1]
    async with aiohttp.ClientSession() as session:    # with会自动帮你关闭
        async with session.get(url) as resp:
            with open(name, mode='wb') as f:
                f.write(await resp.content.read())      # 读取内容是异步的，需要await挂起
    print(name, 'ok')

    
async def main():
    tasks = []
    for url in urls:
        tasks.append(download(url))
    await asyncio.wait(tasks)


if __name__ == '__main__':
    asyncio.run(main())

