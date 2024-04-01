# -*- coding: utf-8 -*-
# !/usr/bin/env python

import jieba  # 中文分词
import jieba.analyse
import wordcloud  # 绘制词云
import os
import numpy as np
from PIL import Image
# 显示数据
def analysis(film):
    path=os.path.join(os.getcwd(),'DouBan_FilmReviews\\'+film+'.txt')
    # 词云mask
    mask_img="Binary_image_p2892190808.png"
    mask = np.array(Image.open(mask_img)) if os.path.isfile(mask_img) else None

    f = open(path, encoding='utf-8')
    txt = f.read()
    #设置禁/停用词
    stopword=open('stopwords.txt', encoding='utf-8')
    stopwords=stopword.read()

    txt_list = jieba.lcut(txt)
    #将分词后的结果进行去重，清洗无用字词
    txt_string=[]
    txt_string += [word for word in txt_list if word not in stopwords]

    string = ' '.join(txt_string)
    print(string)


    w = wordcloud.WordCloud(
                            background_color="white",
                            font_path='C:/Windows/Fonts/simsun.ttc',
                            mask=mask ,
                            # scale=15,
                            stopwords={' '},
                            contour_width=2,
                            contour_color='steelblue'
                            )

    w.generate(string)
    w.to_file(film+'.png')
    print(film,'图片生成成功！')

if __name__ == '__main__':
    analysis("过把瘾")
