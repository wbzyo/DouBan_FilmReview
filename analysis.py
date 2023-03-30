# -*- coding: utf-8 -*-
# !/usr/bin/env python

import jieba  # 中文分词
import wordcloud  # 绘制词云
import os
# 显示数据
def analysis(film):
    path=os.path.join(os.getcwd(),'DouBan_FilmReviews\\'+film+'.txt')

    f = open(path, encoding='utf-8')

    txt = f.read()
    txt_list = jieba.lcut(txt)
    # print(txt_list)
    string = ' '.join(txt_list)
    print(string)

    # 很据得到的弹幕数据绘制词云图
    # mk = imageio.imread(r'图片路径')

    w = wordcloud.WordCloud(width=1000,
                            height=700,
                            background_color='white',
                            font_path='C:/Windows/Fonts/simsun.ttc',
                            # mask=mk,
                            scale=15,
                            stopwords={' '},
                            contour_width=5,
                            contour_color='red'
                            )

    w.generate(string)
    w.to_file(film+'.png')

if __name__ == '__main__':
    analysis()