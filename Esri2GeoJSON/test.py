#coding=utf-8
import codecs
from esri2geojson import *

def esrif2geof(ifile,ofile):
    fp = open(ifile)
    sgeo = esri2GeoJSON(fp.read())
    fp.close()
    fp = codecs.open(ofile,"w","utf-8")
    fp.write(sgeo)
    fp.close()

if __name__ == "__main__":
    print "Test Point: esript.json"
    esrif2geof("data/esript.json","data/geopt.geojson")
    print "geopt.geojson is created."

    print "Test Polyline: esriln.json"
    esrif2geof("data/esriln.json","data/geoln.geojson")
    print "geoln.geojson is created."

    print "Test Polygon: esripl.json"
    esrif2geof("data/esripl.json","data/geopl.geojson")
    print "geopl.geojson is created."
