# 导入库
import os
import codecs
import time
import analysis
from selenium import webdriver
# 浏览驱动器路径

'''driver = webdriver.Chrome(chromedriver)
driver.get("https://movie.douban.com/subject/2264216/comments?status=P")
driver.find_element_by_xpath('//*[@id="comments"]/div[1]/div[2]/p/span/text()')'''

# 获取摘要信息
def getFilmReview(film):
    global films
    try:
        # 新建文件夹及文件
        basePathDirectory = "DouBan_FilmReviews"
        if not os.path.exists(basePathDirectory):
            os.makedirs(basePathDirectory)

        # 浏览驱动器路径
        chromedriver = 'C:\Program Files (x86)\Google\Chrome\Application\chromedriver'
        os.environ["webdriver.chrome.driver"] = chromedriver
        driver = webdriver.Chrome(chromedriver)
        # 打开网页
        driver.get("https://search.douban.com/movie/subject_search?search_text={}".format(film))
        time.sleep(2)
        link=driver.find_element_by_class_name('title-text')
        url=link.get_attribute('href')
        films=link.text

        baiduFile = os.path.join(basePathDirectory, films+".txt")
        # 若文件不存在则新建，若存在则追加写入
        if not os.path.exists(baiduFile):
            info = codecs.open(baiduFile, 'w', 'utf-8')
        else:
            info = codecs.open(baiduFile, 'a', 'utf-8')

        for k in range(50):
            time.sleep(1)
            driver.get(url+"comments?start={}".format(k))
            try:
                # 自动搜索
                for i in range(21):
                    elem = driver.find_element_by_xpath('//*[@id="comments"]/div[{}]/div[2]/p/span'.format(i + 1))
                    print(elem.text)
                    info.writelines(elem.text + '\r\n')
            except Exception as e:
                print('Error:', e)

    except Exception as e:
        print('Error:', e)

    finally:
        print('\n')
        driver.close()
    analysis.analysis(films)

if __name__ == '__main__':
    print('开始爬取')
    getFilmReview(input('请输入要爬取的影视名称:'))
    print('结束爬取')