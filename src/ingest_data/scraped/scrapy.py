# import scrapy

# class MySpider(scrapy.Spider):
#     name = 'my_spider'
#     start_urls = ['https://example.com']  # Replace with the starting URL of your choice
#     allowed_domains = ['example.com']     # Replace with the domain of the website

#     def __init__(self, *args, **kwargs):
#         super(MySpider, self).__init__(*args, **kwargs)
#         self.page_count = 0

#     def parse(self, response):
#         # Extract the title tag, meta description, and image URLs
#         page_title = response.css('title::text').get()
#         meta_description = response.xpath("//meta[@name='description']/@content").get()
#         image_urls = response.css('img::attr(src)').getall()

#         if page_title or meta_description or image_urls:
#             yield {
#                 'title': page_title,
#                 'meta_description': meta_description,
#                 'image_urls': image_urls,
#                 'url': response.url
#             }

#         # Increment the page count
#         self.page_count += 1

#         # Define the URL pattern for the pages you want to follow
#         url_pattern = 'specific_keyword'  # Replace with the keyword or pattern in the URL

#         if self.page_count < 10:
#             # Follow links to pages that match the URL pattern
#             for next_page in response.css('a::attr(href)').getall():
#                 if url_pattern in next_page:
#                     yield response.follow(next_page, self.parse)

# # To run the spider, use the following command:
# # scrapy crawl my_spider -o output.json