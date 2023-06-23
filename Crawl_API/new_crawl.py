from requests_html import HTMLSession 

s = HTMLSession()
s.browser

def get_session():
    demo = []
    first_url = "http://stockboard.sbsc.com.vn/apps/StockBoard/SBSC/VN30INDEX.html"
    # Check for access permissions
    # print(r.status_code)
    r = s.get(first_url)
    r.html.render(sleep=3)

    stock_list= ['ACB', 'BCM', 'BID', 'BVH', 'CTG', 'FPT', 'GAS', 'GVR', 'HDB', 'HPG']
    # Check for access permissions
    # print(r.status_code)

    for item in stock_list:
    # Gia khop lenh lien tuc co duoi la 8 || The price of the stock code has the ending of -8
        s_code = r.html.xpath(f'//td[contains(@id,"{item}-8")]')
        price = s_code[0].element.text
        temp = {"stock_code":item, 
        "current_price": price}
        demo.append(temp)

    return demo
