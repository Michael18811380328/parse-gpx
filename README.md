# 使用 gpx-py 解析 gpx 文件

## 1、实际问题

使用某些运动软件，可以把路径导出一个 gpx 文件，我想弄明白这个文件的格式和原理，并导入到其他运动软件中。

## 2、基本名词

### 2.1 GPX

GPX (the GPS Exchange Format) is a light-weight XML data format for the interchange of GPS data (waypoints, routes, and tracks) between applications and Web services on the Internet.

[GPX](https://www.topografix.com/gpx.asp) 一种用于存储坐标数据的轻量级 XML 文件格式，它可以储存在一条路上的路点，轨迹，路线，且易于处理和转换到其他格式。这是各种运动软件或者地理软件常见的数据格式，类似于 XML 格式。

### 2.2 gpx-py

gpx-py is a python GPX parser. GPX (GPS eXchange Format) is an XML based file format for GPS tracks.

[gpx-py](https://github.com/tkrajina/gpxpy) 是一个 python gpx 解析器。GPX（GPS eXchange Format）是一种用于GPS轨道的基于XML的文件格式。

这个案例中，我们使用 gpx-py 解析文件（把字符串转换成对象，并分析属性等）

### 2.3 路点 waypoint、轨迹 route、路线 track

路点 waypoint、轨迹 route、路线 track 3者之间如下图所示：

![路点、路线、轨迹](https://img-blog.csdn.net/2018081023183077?watermark/2/text/aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzI0NDUyNDc1/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70)

## 3、模型测试

安装依赖

```bash
pip install -r requirement.txt
```

执行脚本

```bash
python ./parse-gpx.py
```

## 4、实际案例

4.1 以行者为例，访问 PC 端行者网页（ http://www.imxingzhe.com/lushu/3605372/ ），把某个轨迹或者路书，导出成 gpx 文件并下载到本地（demo-02.gpx）

4.2 使用 parse-gpx 解析 gpx 文件，可以获取元数据

4.3 把 gpx 文件上传到 strava 中
