import sys, os
import sqlite3

bibpath = "/pathto/BIB/"
dbpath = "/pathto/zotero.sqlite"
dbh = sqlite3.connect(dbpath)

def getBIBDir():
  colls = os.listdir(bibpath)
  for c in colls:
    if not os.path.isdir(os.path.join(bibpath,c)):
      continue
    print c
    kc = genKey()
    addCollection(c, kc)
    pid = getMaxId()
    subcolls = os.listdir(os.path.join(bibpath,c))
    for sc in subcolls:
      if not os.path.isdir(os.path.join(bibpath,c,sc)):
        continue
      ksc = genKey()
      addCollection(sc, ksc, pid)

def getMaxId():
  cur = dbh.cursor()
  sql = "select max(collectionID) from collections"
  cur.execute(sql)
  re = cur.fetchone()
  return re[0]

def addCollection(name,key,pid="NULL"):
  cur = dbh.cursor()
  key = genKey()
  if pid == "NULL":
    pid = pid
  else:
    pid = str(pid)
  sql = "insert into collections (collectionName,parentCollectionID, key) values ('" + name + "'," + pid + ",'" + key +"');"
  # print sql
  cur.execute(sql)
  cur.close()
  dbh.commit()

import random
def genKey(n=8,bstr=None):
  if n is None:
    n = 8
  if bstr is None:
    bstr = "23456789ABCDEFGHIJKMNPQRSTUVWXZ"
    # bstr = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
  rndstr = ""
  for i in range(n):
    inx = random.randrange(0,len(bstr))
    rndstr += bstr[inx]
  return rndstr

if __name__ == "__main__":
  getBIBDir()
  dbh.commit()
  dbh.close()
