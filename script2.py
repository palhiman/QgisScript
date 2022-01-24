# to get the current layer
import iface

mc = iface.mapCanvas
layer = mc.currentLayer()

# to get layername
layer.name()

# to open attribute table
iface.showAttributeTable(layer)

# to display features
for f in layer.getFeatures():
    print(f["ADMIN"])

# give the location o f the file
# uniform resource indicator
URI = "C:\\Users\\DCC_MHA\\Desktop\\QGIS\\qgis_sample_data\\shapefiles\\alaska.shp"

# adding vector layer
vlayer = iface.addVectorLayer(URI, "alaska", "ogr")
# to open attribute table
iface.showAttributeTable(vlayer)
# to display each fields in the attribute table and data type of the field
for f in vlayer.fields():
    print(f.name(), f.typeName())

# iterating each features in the layer
for feature in vlayer.getFeatures():
    print(feature["NAME", "AREA_MI"])
