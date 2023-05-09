# coding:utf-8
import gpxpy.parser as parser

# 1 读文件并解析
gpx_file = open( './demo-01.gpx', 'r' )  
gpx_parser = parser.GPXParser( gpx_file )
gpx = gpx_parser.parse() 
gpx_file.close()

# 2 文件元信息
print ('======================')
print (gpx.name)
print (gpx.description)
print (gpx.author_name)
print ('======================')

# 3 轨迹
for track in gpx.tracks:
    for segment in track.segments:
        for point in segment.points:
            print('Point at ({0},{1}) -> {2},{3}'.format( point.latitude, point.longitude, point.elevation, point.geoid_height))


# 4 路线
for waypoint in gpx.waypoints:
    print('waypoint {0} -> ({1},{2},{3})'.format( waypoint.name, waypoint.latitude, waypoint.longitude, waypoint.elevation))


# 5 坐标点
for route in gpx.routes:
    for point in route.points:
        print('Point at ({0},{1}) -> {2}'.format( point.latitude, point.longitude, point.name ))


# 6 转换成的 XML 文件
print('GPX:', gpx.to_xml())
