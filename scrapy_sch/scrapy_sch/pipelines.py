# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import logging

class ScrapySchPipeline(object):
    def process_item(self, item, spider):
        if item['answer'] is None or item['answer'] == '':
            return item
        with open("conversation.txt", "a") as f:
            question = ''.join(item['question'].split('\r\n'))
            question = ''.join(question.split('\n'))
            question = question.replace('　', '')
            question = question.replace(' ', '')
            question = question.replace('\t', '')

            answer = ''.join(item['answer'].split('\r\n'))
            answer = answer.replace('　', '')
            answer = answer.replace(' ', '')
            answer = answer.replace('\n', '')
            answer = answer.replace('\t', '')
            logging.debug('hoge %s', answer)
            f.write(question)
            f.write('\n')
            f.write(answer)
            f.write('\n')
            f.write('\n')

            f.close
        return item
