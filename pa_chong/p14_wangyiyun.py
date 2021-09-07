
url = 'https://music.163.com/weapi/comment/resource/comments/get?csrf_token='

# 真实参数
data = {
    'csrf_token': '',
    'cursor': '-1',
    'offset': '0',
    'orderType': '1',
    'pageNo': '1',
    'pageSize': '20',
    'rid': "R_SO_4_1436709403",
    'threadId': "R_SO_4_1436709403"
}

# 处理加密过程

f = '00e0b509f6259df8642dbc35662901477df22677ec152b5ff68ace615bb7b725152b3ab17a876aea8a5aa76d2e417629ec4ee341f56135fccf695280104e0312ecbda92557c93870114af6c9d05c4f7f0c3685b7a46bee255932575cce10b424d813cfe4875d3e82047b97ddef52741d546b8e289dc6935b3ece0462db0a22b8e7'
g = '0CoJUm6Qyw8W8jud'
e = '010001'
i = 'IPoNisWZcCGQG3vS'


def get_encSecKey():
    return "0060a157df26caa727e5816831bde1d0cfa5c7e2279fbf3a8c724545d8cf95d5d3cf48a119d1402044ffcd8239fb6771a9df90b7d5484ac4edc830fe30159facb50cb8dc941f37a97e2734c5b5a803ebbfc40d916c8023209fd9fa58465b3f14b0a47618fba8cdc3be1f248dd8220427d709362e7026707f51e266e0e03125fc"


def get_params(data):
    first = enc_params(data, g)
    secod = enc_params(first, i)
    return secod


def enc_params(data, key):
    

"""
function a(a) {
        var d, e, b = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789", c = "";
        for (d = 0; a > d; d += 1)
            e = Math.random() * b.length,
            e = Math.floor(e),
            c += b.charAt(e);
        return c
    }
    function b(a, b) {
        var c = CryptoJS.enc.Utf8.parse(b)
          , d = CryptoJS.enc.Utf8.parse("0102030405060708")
          , e = CryptoJS.enc.Utf8.parse(a)
          , f = CryptoJS.AES.encrypt(e, c, {
            iv: d,
            mode: CryptoJS.mode.CBC
        });
        return f.toString()
    }
    function c(a, b, c) {
        var d, e;
        return setMaxDigits(131),
        d = new RSAKeyPair(b,"",c),
        e = encryptedString(d, a)
    }
    function d(d, e, f, g) {   d:data   e:010001    f:很长  g:0CoJUm6Qyw8W8jud
        var h = {}
          , i = a(16);
        return h.encText = b(d, g),
        h.encText = b(h.encText, i),
        h.encSecKey = c(i, e, f),
        h
    }
"""