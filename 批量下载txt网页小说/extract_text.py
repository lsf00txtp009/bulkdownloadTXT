import requests
from bs4 import BeautifulSoup

base_url = 'https://www.dashenwu.cc/228314/'
extension = '.html'
start_page = 100
end_page = 103

# 定义目标div的ID
div_id = 'content'

# 定义输出文件名
output_file = 'output.txt'

# 发送HTTP请求获取网页内容并提取文字内容
with open(output_file, 'w', encoding='utf-8') as file:
    for page in range(start_page, end_page + 1):
        url = f"{base_url}{page}{extension}"
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        target_div = soup.find('div', id=div_id)
        h1_tag = target_div.find_previous('h1')
        h1_text = h1_tag.get_text() if h1_tag else ""
        content_text = target_div.get_text()
        text_content = f"{h1_text} \n{content_text}"
        file.write(text_content)
        file.write('\n\n')

        url = f"{base_url}{page}_2{extension}"
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        target_div = soup.find('div', id=div_id)
        h1_tag = target_div.find_previous('h1')
        h1_text = h1_tag.get_text() if h1_tag else ""
        content_text = target_div.get_text()
        text_content = f"{h1_text} \n{content_text}"
        file.write(text_content)
        file.write('\n\n')