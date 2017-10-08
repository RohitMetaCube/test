#!/usr/bin/python
# -*- coding: utf-8 -*-
import config
from db_handler import MongoController
from linkedin_client import LinkdeinClient
import csv

if __name__ == "__main__":
    lc = LinkdeinClient()
    moc = MongoController()
    
    status = raw_input("Are You Readey:(Y/n)")
    if status.lower().startswith("y"):
        moc.ensure_indexes(config.COLLECTION_NAME)
        f = open('dataset/profile_links.csv', 'rb')
        fr = csv.reader(f)
        for i, row in enumerate(fr):
            profile_link = row[0]
            user_details = lc.html_fetcher(profile_link)
            moc.insert_into_db(config.COLLECTION_NAME, user_details)
            print "Done Index: {}, Profile: {}".format(i+1, profile_link)
        f.close()