from lxml import etree

xml = """
<head>
    <div>
        <name id="1">杨过</name>
        <name id="2">小龙女</name>
        <div>
            <name id="5">欧阳锋</name>
        </div>
        <div>
            <name id="7">周伯通</name>  
        </div>
        <div>
            <name id="6">洪七公</name> 
        </div>
    </div>
    <span>
        <name id="3">郭靖</name>
        <name id="4">张无忌</name>
    </span>
</head>
"""

tree = etree.XML(xml)

# result = tree.xpath("/head/div/name/text()")   #    text()拿文本
# result = tree.xpath("/head/div//name/text()")  #    //所有后代
# result = tree.xpath("/head/*/name/text()")  #    *任意对象
# result = tree.xpath("/head//name/text()")  #    *任意对象
# [@key = "value"] 属性筛选
div = tree.xpath("/head/div/div")

# print(div)

for d in div:
    result = d.xpath('./name/text()')       # ./ 继续查找
    print(result)                           # @xxxx  拿到属性值

# 网页支持复制xpath
# /html/body/div[3]/h1
# /html/body/div[3]/h1
# //*[@id="J_header_logo_service"]/a[1]