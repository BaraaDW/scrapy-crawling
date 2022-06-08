import scrapy


class SpiderMan(scrapy.Spider):

    name = "scrapy_spider"

    def start_requests(self):
        yield scrapy.Request(url='https://quotes.toscrape.com/page/1/', callback=self.parse_target)

    def parse_target(self, response):
        print('-------------Start-------------')

        # title_css = response.css('span small.author::text').getall()
        # print(title_css)

        # title_xpath = response.xpath('//span//small[@class="author"]').getall()
        # print(title_xpath)

        print('-------------phase(1)-------------')

        # for quote in response.css("div.quote"):
        #     text = quote.css("span.text::text").get()
        #     author = quote.css("small.author::text").get()
        #     tags = quote.css("div.tags a.tag::text").getall()
        #     print(dict(text=text, author=author, tags=tags))

        print('-------------phase(2)-------------')

        # for quote in response.xpath("//div[@class='quote']"):
        #     text = quote.xpath(".//span[@class='text']/text()").get()
        #     author = quote.xpath(".//small[@class='author']/text()").get()
        #     tags = quote.xpath(".//div[@class='tags']//a[@class='tag']/text()").getall()
        #     print(dict(text=text, author=author, tags=tags))

        print('-------------phase(3)-------------')

        # link_css = response.css('li.next a::attr(href)').get()
        # print(link_css)

        # link_xpath = response.xpath('//li[@class="next"]/a/@href').get()
        # print(link_xpath)

        # link_css2 = response.css('li.next a').attrib['href']
        # print(link_css2)

        # link_xpath2 = response.xpath('//li[@class="next"]/a').attrib['href']
        # print(link_xpath2)

        print('-------------phase(4)-------------')

        # _____________(crawling next page)______________

        # _____method(-1-)_____
        # next_page_css = response.css('li.next a').attrib['href']
        # if next_page_css is not None:
        #     next_page = response.urljoin(next_page_css)
        #     yield scrapy.Request(next_page, callback=self.parse_target)  # run 'parse_target' again for new_url with same form

        # next_page_xpath = response.xpath('//li[@class="next"]/a').attrib['href']
        # if next_page_xpath is not None:
        #     next_page = response.urljoin(next_page_xpath)
        #     yield scrapy.Request(next_page, callback=self.parse_target)  # run 'parse_target' again for new_url with same form

        # _____method(-2-)_____
        # next_page_css = response.css('li.next a::attr(href)').get()
        # if next_page_css is not None:
        #     yield response.follow(next_page_css, callback=self.parse_target)  # run 'parse_target' again for new_url with same form

        # next_page_xpath = response.xpath('//li[@class="next"]/a').attrib['href']
        # if next_page_xpath is not None:
        #     yield response.follow(next_page_xpath, callback=self.parse_target)  # run 'parse_target' again for new_url with same form

        print('-------------END-------------')

# ______________________________________________________________________________________________________________________
# ______________________________________________________________________________________________________________________
# ______________________________________________________________________________________________________________________
# ______________________________________________________________________________________________________________________
# ____________________________________________[--selenium VS scrapy--]__________________________________________________

# ( -to get elements-)-->[ -find_elements_by_xpath()- ]:
# elements = response.xpath("//xpath")  # [not found]--> return [] || [found it]--> list of elements
# elements = response.css("css")  # [not found]--> return [] || [found it]--> list of elements

# ( -to get one element- ) --> elements[0]

# ______________________________________________________________________________________________________________________

#(-1-) get (content, attribute, ...):
# find_element ----> get()   # [not found]--> return None || [found it]--> 'str'
# find_elements ----> getall()   # [not found]--> return []

#(-2-) get content:
# find_element_by_xpath(//xpath).text ----> response.xpath('//xpath/text()').get()

# ______________________________________________________________________________________________________________________

# response.css('title') "return list of Selector to element it'is name 'title'"

# response.css('title').get()  "return the element it'is name 'title' , not the value"
# response.css('title').getall()  "return list of elements it'is name 'title' , not the value"

# response.css('title::text').get()  "return the content of element it'is name 'title'"
# response.css('title::text').getall()  "return list of contents of elements it'is name 'title'"

# title_css = response.css('title::text').get()
# title_xpath = response.xpath('//title/text()').get()

#_______________________________________________________________________________________________________________________
# ( -UseLess information [just to know]- )
# <div class="quote" ......>
# response.css('div.quote').get()
# response.css('div[class="quote"]').get()  # (-DW-) < - - - - - - - - - - -||
# response.xpath('//div[@class='quote']').get()   # return "str" of html  [-(UseLess)-]

# ______________________________________________________________________________________________________________________
# (-get content-)-->[css]&[xpath]

# contents_css = response.css('span.text::text').getall()
# contents_css2 = response.css('span[class="text"]::text').getall()  # (-DW-)  < - - - - - - - - - - -||
# contents_xpath = response.xpath('//span[@class="text"]/text()').getall()  # return list of "str"

# father_css = response.css('span small.author::text').getall()  " the space is father not directly '//' "
# father_css2 = response.css('span small[class="author"]::text').getall()   # (-DW-)  < - - - - - - - - - - -||
# father_xpath = response.xpath('//span//small[@class="author"]/text()').getall()  # return list of "str"

# ______________________________________________________________________________________________________________________
# (-use parent-)-->[css]&[xpath]

# for quote in response.css("div.quote"):  # list of elements or selectors
#     text = quote.css("span.text::text").get()
#     author = quote.css("small.author::text").get()
#     tags = quote.css("div.tags a.tag::text").getall()
#     print(dict(text=text, author=author, tags=tags))

# for quote in response.xpath("//div[@class='quote']"):  # list of elements or selectors
#     text = quote.xpath(".//span[@class='text']/text()").get()
#     author = quote.xpath(".//small[@class='author']/text()").get()
#     tags = quote.xpath(".//div[@class='tags']//a[@class='tag']/text()").getall()
#     print(dict(text=text, author=author, tags=tags))

# ______________________________________________________________________________________________________________________
# (-get attribute-)-->[css]&[xpath]

# (--use [element] to get just [one] attribute--):
# link_css = response.css('li.next a::attr(href)').get()
# link_xpath = response.xpath('//li[@class="next"]/a/@href').get()

# (--use [selector] to get [more then one] attribute--):
# link_css2 = response.css('li.next a').attrib['href']
# link_xpath2 = response.xpath('//li[@class="next"]/a').attrib['href']

# ((--DW--))
# Valid_url = response.urljoin(link) " link='/page/2/' --> Valid_url='https://quotes.toscrape.com/page/2/' "

# ______________________________________________________________________________________________________________________
# (-contains-) = * --> [css]&[xpath]
# response.xpath('//a[contains(@href, "image")]/img').attrib['src']
# response.css('a[href*="image"] img').attrib['src']

# ______________________________________________________________________________________________________________________
# (-not-) = * --> [css]&[xpath]
# response.xpath(//div[@class="quote"]//span[not(@class='text')])
# response.xpath(//div[@class="quote"]//span[not(@class)])
# response.css('span:not([class="text"])')
# response.css('span:not([class])')

# ______________________________________________________________________________________________________________________
# _____________(crawling next page)______________

# _____method(-1-)_____
# next_page_css = response.css('li.next a').attrib['href']
# if next_page_css is not None:
#     next_page = response.urljoin(next_page_css)
#     yield scrapy.Request(next_page, callback=self.parse_target)  # run 'parse_target' again for new_url with same form

# next_page_xpath = response.xpath('//li[@class="next"]/a').attrib['href']
# if next_page_xpath is not None:
#     next_page = response.urljoin(next_page_xpath)
#     yield scrapy.Request(next_page, callback=self.parse_target)  # run 'parse_target' again for new_url with same form

# _____method(-2-)_____
# next_page_css = response.css('li.next a::attr(href)').get()
# if next_page_css is not None:
#     yield response.follow(next_page_css, callback=self.parse_target)  # run 'parse_target' again for new_url with same form

# next_page_xpath = response.xpath('//li[@class="next"]/a').attrib['href']
# if next_page_xpath is not None:
#     yield response.follow(next_page_xpath, callback=self.parse_target)  # run 'parse_target' again for new_url with same form
