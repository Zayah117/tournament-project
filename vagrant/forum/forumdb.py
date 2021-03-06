#
# Database access functions for the web forum.
# 

import time
import psycopg2

## Get posts from database.
def GetAllPosts():
    '''Get all the posts from the database, sorted with the newest first.'''
    db = psycopg2.connect("dbname=forum")
    c = db.cursor()
    query = "SELECT time, content FROM posts ORDER BY time DESC"
    c.execute(query)

    # c.execute("UPDATE posts SET content = 'cheese' WHERE content LIKE '%spam%'")

    posts = ({'content': str(row[1]), 'time':str(row[0])} for row in c.fetchall())

    db.close()
    return posts

## Add a post to the database.
def AddPost(content):
    '''Add a new post to the database.

    Args:
      content: The text content of the new post.
    '''
    t = time.strftime('%c', time.localtime())

    db = psycopg2.connect("dbname=forum")
    c = db.cursor()
    c.execute("insert into posts (content) values (%s)", (content,))
    db.commit()
    db.close()
