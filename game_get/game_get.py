from bs4 import BeautifulSoup
import requests
from selenium import webdriver
from time import sleep


class GameAuto(object):
    def __init__(self):
        self.html = "https://cf.qq.com/web201105/actions.shtml"
        self.user_agent = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 '
                                         '(KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36'}

    def get_activity(self):
        respons = requests.get(self.html)
        respons.encoding = 'gbk'
        html = respons.text
        soup = BeautifulSoup(html, 'html.parser', from_encoding='GBK')
        soup = soup.body
        urls = soup.find_all('a')
        for link in urls:
            print(link.get('href'))

    def shtml_get(self):
        url_list = list()
        broser = webdriver.Firefox()
        broser.get(self.html)
        page_name = self.page_name_get(broser)
        for i in range(1, page_name + 1):
            try:
                urls = self.url_get(broser)
                url_list.extend(urls)
                broser.find_element_by_xpath('//*[@id="hot_next"]').click()
            except Exception as e:
                print(e)
        broser.quit()
        return url_list

    def url_get(self, game_broser):
        url_list = list()
        for i in range(0, 12):
            activity_state = game_broser.find_element_by_xpath(
                '/html/body/div[1]/div[2]/div[2]/div/div/div[2]/div[2]/ul/li[' + str(i +1) + ']/div[3]').get_attribute('class')
            if 'e-status_down' in activity_state:
                break
            url_sub = game_broser.find_element_by_xpath('/html/body/div[1]/div[2]/div[2]/div/div/div[2]/div[2]/ul/li[' + str(i +1) + ']/div[1]/a')
            url = url_sub.get_attribute('href')
            url_list.append(url)
        return url_list

    def page_name_get(self, game_broser):
        page_text = game_broser.find_element_by_xpath('//*[@id="his_total"]').text
        page_number = page_text.split('/')[1]
        return int(page_number)

    def user_log_in(self, web_driver):
        user_name = '893935189'
        user_password = 'zhangjiyue!'
        try:
            web_driver.find_element_by_link_text(u'登录').click()
            web_driver.switch_to_frame('loginIframe')
            web_driver.find_element_by_link_text(u'帐号密码登录').click()
            web_driver.find_element_by_name('u').send_keys(user_name)
            web_driver.find_element_by_id('p').send_keys(user_password)
            # web_driver.find_element_by_id('login_button').click()
        except Exception as e:
            print(e)

    def web_griver(self, url_list):
        broser = webdriver.Firefox()
        for url in url_list:
            broser.get(url)
            self.user_log_in(broser)



if __name__ == '__main__':
    activity_game = GameAuto()
    webs = activity_game.shtml_get()
    activity_game.web_griver(webs)


# html = requests.get('https://cf.qq.com/web201105/actions.shtml').content
# soup = BeautifulSoup(html, 'html.parser', from_encoding='utf-8')
#
# # print(soup.p)