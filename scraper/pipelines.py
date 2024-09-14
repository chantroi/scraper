# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
import workers_kv
from itemadapter import ItemAdapter


class ScraperPipeline:
    def process_item(self, item, spider):
        with open("img.html", "a") as f:
            f.write(f"<img src='{item['src']}' alt=''>")


class WorkersPipeline:
    def __init__(self):
        self.kv = None

    def open_spider(self, spider):
        self.kv = workers_kv.Namespace(
            account_id="946282dda63e80ac718f83cb14b86729",
            namespace_id="3901b74a7896471cb63ddb0ff440b54a",
            api_key="KGMqzP9ooqshspxZFDMf6Z2WVNVMwHhY0npZRXOM",
        )

    def process_item(self, item, spider):
        return self.kv.write({item["src"]: item["src"]})


class HtmlWriterPipeline:
    def open_spider(self, spider):
        # Tạo hoặc mở tệp HTML để ghi
        self.file = open('output.html', 'w')
        self.file.write('''<html>
                        <style>
                          img {
                             width: 100%;
                             margin: 0 auto;
                        }
                        </style>
                        <body>''')
        self.seen = set()

    def close_spider(self, spider):
        # Kết thúc nội dung và đóng tệp
        self.file.write('</body></html>\n')
        self.file.close()

    def process_item(self, item, spider):
        item = item['src']
        if item in self.seen:
            return
        self.file.write(f'<img src="{item}" />\n')
        self.seen.add(item)
        return item