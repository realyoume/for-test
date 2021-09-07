# 'http://www.newxue.com/gkmz/sgyy/'
#
import requests
from lxml import etree
import asyncio
import aiohttp
import aiofiles
import re


async def download_one(url):
    name = url.rsplit('/', 1)[1].split('.')[0] + '.txt'

    async with aiohttp.ClientSession() as session:    # with会自动帮你关闭
        async with session.get(url) as resp:
            resp.encoding = 'gb2312'
            html = etree.HTML(await resp.text())
            div = html.xpath('//*[@id="onearcxsbd"]')[0]
            ps = div.xpath('./p')
            
            main_txt = ''
            for p in ps:
                txt = p.xpath('./text()')[0].replace('\r\n\t', '')
                main_txt = main_txt + txt
            
            async with aiofiles.open(name, mode='w', encoding='utf-8') as f:
                await f.write(main_txt)
           
            
async def main(url_list):
    tasks = []
    for url in url_list:
        tasks.append(download_one(url))
    await asyncio.wait(tasks)


if __name__ == '__main__':
    main_url = 'https://www.xyyuedu.com/gdmz/sidamingzhu/sgyy/'
    url_list = []
    with requests.get(main_url) as main_resp:
        main_resp.encoding = 'gb2312'
        html = etree.HTML(main_resp.text)
        ul = html.xpath('/html/body/div[2]/div[3]/div/ul')[0]
        lis = ul.xpath('./li')
        
        for li in lis:
            url = 'https://www.xyyuedu.com' + li.xpath('./a/@href')[0]
            url_list.append(url)

    main_resp.close()
    asyncio.run(main(url_list))
    print('ok')

    


    


