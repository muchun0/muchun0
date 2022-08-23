from test import test_redis
css_front = "div.wy-table-responsive:nth-child(2) > table:nth-child(1) > tbody:nth-child(2) > tr:nth-child(1) > td:nth-child(2) > div:nth-child(1) > ul:nth-child(1) > li:nth-child(1) > ul:nth-child(2) > li:nth-child("
css_last = ") > a:nth-child(1)"
title = "string"
data = test_redis.get_data(title,css_front,css_last)
test_redis.write_docx(title,data)