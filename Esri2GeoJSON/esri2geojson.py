#coding=utf-8
import json
import os
import codecs

def esri2GeoJSON(esrijson):
    GeoJSON = {}
    data = json.loads(esrijson)
    esrifeatures = data["features"]
    esriType = data["geometryType"]
    GeoJSON["type"] = "FeatureCollection"
    features = []
    for esrifeature in esrifeatures:
        feature = {}
        feature["type"] = "Feature"
        esrigeom = esrifeature["geometry"]
        geometryType = getGeometryType(esrigeom, esriType)
        geometry = {}
        geometry["type"] = geometryType
        geometry["coordinates"] = getEsriCoordinates(esrigeom,geometryType)
        if geometry["coordinates"] == []:
            continue
        feature["geometry"] = geometry
        feature["properties"] = esrifeature["attributes"]
        features.append(feature)
    GeoJSON["features"] = features
    return features
    return json.dumps(GeoJSON, indent=2, ensure_ascii=False)

def getGeometryType(geometry, esriType):
    if esriType == "esriGeometryPoint":
        return "Point"
    elif esriType == "esriGeometryMultiPoint":
        return "MultiPoint"
    elif esriType == "esriGeometryPolyline":
        #print geometry["paths"]
        if len(geometry["paths"])>0 and type(geometry["paths"][0]) == list:
            return "MultiLineString"
        return "LineString"
    elif esriType == "esriGeometryPolygon":
        return "Polygon"
    else:
        return "unknown"

def getEsriCoordinates(geometry,geometryType):
    if geometryType == "Polygon":
        return geometry["rings"]
    elif geometryType == "LineString" or geometryType == "MultiLineString":
        return geometry["paths"]
    elif geometryType == "Point":
        return [geometry["x"],geometry["y"]]
    else:
        return []

def road2geojson():
    files = os.listdir("data/roadnow/")
    GeoJSON = {}
    GeoJSON["type"] = "FeatureCollection"
    GeoJSON["features"] = []
    for file in files:
        print file
        fp = open("data/roadnow/%s" % file)
        sgeo = esri2GeoJSON(fp.read())
        GeoJSON["features"].extend(sgeo)
        fp.close()
        #fname,sfix = file.split(".")
        #fp = codecs.open("data/roadnowgeo/%s.geojson" % fname,"w","utf-8")
        #fp.write(sgeo)
        #fp.close()
    fp = codecs.open("data/whroad.geojson","w","utf-8")
    fp.write(json.dumps(GeoJSON))
    fp.close()
    
if __name__=="__main__":
    print "Main"
    road2geojson()
