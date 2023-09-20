# 用于存匹配的规则
import re

findLink = re.compile(r'<a href="(.*?)">')              # 链接
findImgSrc = re.compile(r'<img.*src="(.*?)"',re.S)      # 图片链接
findTitle = re.compile(r'<span class="title">(.*)</span>')      # 电影标题
findRating = re.compile(r'<span class="rating_num" property="v:average">(.*)</span>')   # 电影评分
findJudge = re.compile(r'<span>(\d*)人评价</span>')        # 评价人数
findInq = re.compile(r'<span class="inq">(.*)</span>')    # 概况
findBd = re.compile(r'<p class="">(.*?)</p>',re.S)         # 电影相关内容