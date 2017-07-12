import xmltodict
import time
import hashlib

total_count = 0
m = hashlib.md5()

with open('big_data.xml') as fd:
    cfg = xmltodict.parse(fd.read())

for item in cfg['rss']['channel']['item']:
    print ""
    print "Title: " + item['title']
    print ""
    try:
        for comment in item['wp:comment']:
            total_count += 1
            try:
                date_time = comment['wp:comment_date_gmt']
                pattern = '%Y-%m-%d %H:%M:%S'
                epoch = int(time.mktime(time.strptime(date_time, pattern)))
                print "Comment File Name: comment-" + str(epoch) + ".yml"
            except:
                pass
            try:
                print "_id: " + comment['wp:comment_id']
            except:
                pass
            try:
                print "name: " + comment['wp:comment_author']
            except:
                pass
            try:
                if comment['wp:comment_parent'] != '0':
                    print "reply_to: " + comment['wp:comment_parent']
            except:
                pass
            try:
                temp_email = comment['wp:comment_author_email']
                temp_email = temp_email.strip()
                temp_email = temp_email.lower()
                m.update(temp_email)

                print "email: " + m.hexdigest()
            except:
                pass
            try:
                print "body: " + comment['wp:comment_content']
            except:
                pass
            try:
                print "date: " + comment['wp:comment_date_gmt']
            except:
                pass
            print ""
    except:
        pass

print "Total Count: " + str(total_count)
