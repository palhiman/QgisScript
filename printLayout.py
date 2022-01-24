# basic imports
import os
import iface
from qgis.core import (
    QgsGeometry,
    QgsMapSettings,
    QgsPrintLayout,
    QgsMapSettings,
    QgsMapRendererParallelJob,
    QgsLayoutItemLabel,
    QgsLayoutItemLegend,
    QgsLayoutItemMap,
    QgsLayoutItemPolygon,
    QgsLayoutItemScaleBar,
    QgsLayoutExporter,
    QgsLayoutItem,
    QgsLayoutPoint,
    QgsLayoutSize,
    QgsUnitTypes,
    QgsProject,
    QgsFillSymbol,
)

from qgis.PyQt.QtGui import (
    QPolygonF,
    QColor,
)

from qgis.PyQt.QtCore import (
    QPointF,
    QRectF,
    QSize,
)

# rendering layers with different CRS
# if you have more than one layer and they have different CRS. we need to explicitly
# set the destination CRS

layers = [iface.activeLayer()]
settings.setLayers(layers)
settings.setDestinationCrs(layers[0].crs())

# output using print layout
project = QgsProject.instance() # to create instance of the project
layout = QgsPrintLayout(project) # to create layout
layout.initializeDefaults() # initialize with default setting (by adding empty A4 page to the layout)

layout.setName("MyLayout")  # this will give name to the layout
project.layoutManager().addLayout(layout) # adding layout to our project

# map — Here we create a map of a custom size and render the current map canvas

map = QgsLayoutItemMap(layout)
# Set map item position and size (by default, it is a 0 width/0 height item placed at 0,0)
map.attemptMove(QgsLayoutPoint(5,5, QgsUnitTypes.LayoutMillimeters))
map.attemptResize(QgsLayoutSize(200,200, QgsUnitTypes.LayoutMillimeters))
# Provide an extent to render
map.zoomToExtent(iface.mapCanvas().extent())
layout.addLayoutItem(map)

# label — allows displaying labels. It is possible to modify its font, color, alignment and margin

label = QgsLayoutItemLabel(layout)
label.setText("Human world")
label.adjustSizeToText()
layout.addLayoutItem(label)

# scale bar
item = QgsLayoutItemScaleBar(layout)
item.setStyle('Numeric') # optionally modify the style
item.setLinkedMap(map) # map is an instance of QgsLayoutItemMap
item.applyDefaultSize()
layout.addLayoutItem(item)


# arrow, picture, basic shape and nodes based shape
polygon = QPolygonF()
polygon.append(QPointF(0.0, 0.0))
polygon.append(QPointF(100.0, 0.0))
polygon.append(QPointF(200.0, 100.0))
polygon.append(QPointF(100.0, 200.0))

polygonItem = QgsLayoutItemPolygon(polygon, layout)
layout.addLayoutItem(polygonItem)

props = {}
props["color"] = "green"
props["style"] = "solid"
props["style_border"] = "solid"
props["color_border"] = "black"
props["width_border"] = "10.0"
props["joinstyle"] = "miter"

symbol = QgsFillSymbol.createSimple(props)
polygonItem.setSymbol(symbol)

# once an item is added to the layout, it can be moved and resized
item.attemptMove(QgsLayoutPoint(1.4, 1.8, QgsUnitTypes.LayoutCentimeters))
item.attemptResize(QgsLayoutSize(2.8, 2.2, QgsUnitTypes.LayoutCentimeters))


# finally exporting the layout
base_path = os.path.join(QgsProject.instance().homePath())
pdf_path = os.path.join(base_path, "output.pdf")

exporter = QgsLayoutExporter(layout)
# export to pdf
exporter.exportToPdf(pdf_path, QgsLayoutExporter.PdfExportSettings())

