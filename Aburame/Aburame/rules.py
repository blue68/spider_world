#!/usr/bin/env python 
# coding:utf-8
# @Time :9/17/18 09:58

from scrapy.linkextractors import LinkExtractor
from scrapy.spider import Rule

rules = {
    "dytt8":
        (
            # 追踪除游戏外的所有列表页
            Rule(LinkExtractor(deny=r'.*game.*', allow='.*/index\.html')),
            # 对下一页进行追踪
            Rule(LinkExtractor(restrict_xpaths=u'//a[text()="下一页"]')),
            # 对文章进行提取并回调给parse_item处理, 过滤掉游戏
            Rule(LinkExtractor(allow=r'.*/\d+/\d+\.html', deny=r".*game.*"), callback='parse_item', follow=True),
        ),

    'china': (
        Rule(LinkExtractor(allow='article\/.*\.html', restrict_xpaths='//div[@id="left_side"]//div[@class="con_item"]'),
             callback='parse_item'),
        Rule(LinkExtractor(restrict_xpaths='//div[@id="pageStyle"]//a[contains(., "下一页")]'))
    ),

    'zcool': (
        Rule(LinkExtractor(restrict_xpaths='//a[@class="laypage_next"]')),
        Rule(LinkExtractor(allow='.*www.zcool.com.cn\/u\/\d+$')),
        Rule(LinkExtractor(restrict_xpaths='//a[@z-st="user_content_card_1_user_name"]')),
        Rule(LinkExtractor(restrict_xpaths='//a[starts-with(@z-st, "desinger_filter_recommend")]')),
        Rule(LinkExtractor(restrict_xpaths='//a[starts-with(@z-st, "desinger_filter_profession")]')),
        # Rule(LinkExtractor(restrict_xpaths='//a[@class="usernick"]')),
        # Rule(LinkExtractor(restrict_xpaths='//a[@class="visitor-name"]')),
        Rule(LinkExtractor(allow='.*?fans.*')),
        Rule(LinkExtractor(allow='.*?follow.*')),
        Rule(LinkExtractor(allow='.*?profile.*'), callback='parse_item'),
    )
}
