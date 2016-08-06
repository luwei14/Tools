# Dir2Zotero

## 说明
个人文献目录转换成[Zotero](http://zotero.org)集合树结构。

我有一个文献目录，目录深度为两层，如下：
* Books
  * Cartography
  * CS
* Articles
  * Mathematics
  * Geography

因此， 我想讲这个目录按照同样的结构自动更新到Zotero的集合层次目录中。

这个Python程序读取文献目录路径，讲结构插入到`zotero.sqlite`数据库中

## Introduction
Personal bibliography directory structure to [Zotero](http://zotero.org) collection.

I have a bibliography directory in two levels, such as:
* Books
  * Cartography
  * CS
* Articles
  * Mathematics
  * Geography

So, I want to turn it into a Zotero collection hierarchical structure in the same way.

This python code read the bibliography path and insert collection items into the `zotero.sqlite` database.
