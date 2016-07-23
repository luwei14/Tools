# EchartsDecoding

> Fetch and decode the [map data](http://echarts.baidu.com/download-map.html) used by [Echarts](http://echarts.baidu.com/). Because the map data from Echarts is compressed with zizag coding. It should be decoded when use it outside Echarts library.

> 现在并解码[Echarts](http://echarts.baidu.com/)的[地图数据](http://echarts.baidu.com/download-map.html). Echarts地图数据是经过压缩的，在Echarts之外使用该地图数据需要解压缩处理。

## Dependence
> Node is need to run decoding functions.

> 需要Node来执行解码函数

## Usage
Execute:
* Clone this repository `git clone https://github.com/luwei14/Tools`
* Change directory `cd Tools/EchartsDecoding`
* Run `bash fetch.sh`

> Then, in directory `json/` is the origin json files, and directory `jsondecode/` contains the decoded map data json files.

> 运行完毕后`json/` 目录包含所有原始压缩的json文件
`jsondecode/` 目录包含解压后的GeoJSON地图数据文件
