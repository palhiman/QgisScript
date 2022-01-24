project = QgsProject.instance() # to create instance of the project
layout = QgsPrintLayout(project) # to create layout
layout.initializeDefaults() # initialize with default setting (by adding empty A4 page to the layout)

layout.setName("MyLayout")  # this will give name to the layout
project.layoutManager().addLayout(layout) # adding layout to our project

# adding map to the layout
map = QgsLayoutItemMap(layout)
map.zoomToExtent(iface.mapCanvas().extent())
layout.addLayoutItem(map)

# adding label
label = QgsLayoutItemLabel(layout)
label.setText("Human world")
label.adjustSizeToText()
layout.addLayoutItem(label)

# finally exporting the layout
base_path = os.path.join(QgsProject.instance().homePath())
pdf_path = os.path.join(base_path, "output.pdf")
img_path = os.path.join(base_path, "output.svg")
exporter = QgsLayoutExporter(layout)
# export to pdf
exporter.exportToPdf(pdf_path, QgsLayoutExporter.PdfExportSettings())

# export to image
exporter.exportToImage(img_path, "svg", QgsLayoutExporter.ImageExportSettings())