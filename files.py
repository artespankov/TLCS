import urllib.request
import pickle
from anagram_sets import all_anagrams, print_anagram_sets_in_order, filter_length
import dbm

import os, requests
def download(url):
    get_response = requests.get(url,stream=True)
    url = url.split('?')[0]
    file_name = url.split("/")[-1]
    with open(file_name, 'wb') as f:
        for chunk in get_response.iter_content(chunk_size=1024):
            if chunk: # filter out keep-alive new chunks
                f.write(chunk)
#
# filelink = ("https://storage.googleapis.com/bucket-studystuff/26_Pages.pdf?x-goog-signature=061f2890fb0e5beb1a24c7384301bcfba15f0ce98ae6fda460444a0dd95233ad8b7d17f2a7b8a2fe80b576b8acdf9255410fad6dbdd833bcdf6a4fe14a02dce6b7f3e77f70323462b78ef1459b52a275edc92ba8c33cc0e13dca9534a4e50a1d0f54456bb1616319648d1660893923fc3de0df0b9f74e49454203152a447c76d43ef784ac662525d37f113b7a0acddc4dd8bdae4813a467881d3ef191fcc215660c054c8a57b7840c2de7abd2b1a42c11562d065fc7a47da94e4afafeae234bf1eeb71be1603f907823ba4bdd7718da2088aa74ccf9fb3dc55ecca77589c0d7fa11d60e5a891e543ce223ac8a1f3f590db1935ba66a9fc7787291caa8f080f27&x-goog-algorithm=GOOG4-RSA-SHA256&x-goog-credential=studystuff%40ss-links-223014.iam.gserviceaccount.com%2F20181119%2Fus%2Fstorage%2Fgoog4_request&x-goog-date=20181119T231635Z&x-goog-expires=600&x-goog-signedheaders=host")



def sed(str, rep, file1, file2):
    try:
        file2 = open(file2, 'w+')
        file1 = open(file1)
    except Exception as ex:
        print("File error")
        print(ex)
    for line in file1:
        try:
            line = line.replace(str, rep)
            file2.write(line)
        except Exception as ex:
            print(ex)
            continue

def write_data(dataset):
    db_name = 'new_db'
    db = dbm.open(db_name, 'c')
    for key, val in dataset.items():
        db[key] = pickle.dumps(val)
    db.close()

def get_data(key):
    db_name = 'new_db'
    item = ""
    db = dbm.open(db_name, 'c')
    for key_ in db:
        if key_ == key:
            item = db[key_]
    db.close()
    return item

def search_file_duplicates():
    checked_files = {}
    ttl, duplicates_cnt = 0, 0
    for root, dirs, filenames in os.walk('.'):
        for file in filenames:
            ttl += 1
            filepath = os.path.join(root, file)
            cmd = 'md5sum  {}'.format(filepath)
            fp = os.popen(cmd)
            res = fp.read()
            res = res.split(" ")[0]
            if res in checked_files.keys():
                print("Duplicate: ",  filepath)
                duplicates_cnt += 1
            else:
                checked_files[res] = filepath
            fp.close()
    print(duplicates_cnt)
    print(ttl)
    print(checked_files)



if __name__ == '__main__':
    search_file_duplicates()


    # print_anagram_sets_in_order(anagram_map)

    # eight_letters = filter_length(anagram_map, 8)
    # print_anagram_sets_in_order(eight_letters)
