# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import sys
reload(sys)
sys.setdefaultencoding('utf8')
class MetroPipeline(object):
    def __init__(self):
        pass
    def open_spider(self,spider):
        pass
        # self.fileStationName=open("./stationName.txt",'w')

    def process_item(self, item, spider):
        #  可以直接将pipitem转成dict,list等内建类型
        itemDict=dict(item)
        listItem=list(itemDict["stationName"])
        fileName=itemDict["fileName"]+".txt"
        with open(fileName,'w') as fileStationName:
            for ele in listItem:
                if len(ele)>=2:
                    fileStationName.write(str(ele).encode("utf8")+"\n")
        return item
    def close_spider(self, spider):
        pass
        # self.fileStationName.close()
