from PyQt6.QtCore import *
from PyQt6.QtGui import *
from PyQt6.QtGui import QMouseEvent, QPaintEvent
from PyQt6.QtWidgets import *
import geopandas as gpd


class Draw(QWidget):
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__q = None
        self.__pol = QPolygonF()
        self.__add_vertex = True
        
        # Check shapefile loading
        self.shp_loaded = False
        
        # List of polygons
        self.shp_polygons = []

        # Highlighted result pol
        self.highlighted_pol = []
        
        
    def openFile(self):
        """
        Open file and read file
        """
        file_name, _ = QFileDialog.getOpenFileName(None, "Open File", "", "Shapefile (*.shp)")

        if file_name:
            
            try:
                # Load shp
                self.shp = gpd.read_file(file_name)
                
                # Shp geometry
                self.geomShapefile()
                                
            except Exception as e:
                QMessageBox.critical(None, "Error", f"Could not open file: {str(e)}")

    def geomShapefile(self):
        """
        Geometry for drawing
        """
        self.shp_polygons.clear()
        
        # Chatgpt + own line 51 to 74
        if self.shp is None or self.shp.empty:
            QMessageBox.critical(None, "Error", "No geometry in shapefile")
            return

        # Find min/max to normalize coordinates
        min_x, min_y, max_x, max_y = self.shp.total_bounds

        width = self.width()
        height = self.height()
        
        for geom in self.shp.geometry:
            if geom.geom_type == "Polygon":                
                pol = QPolygonF([QPointF((float(x) - min_x) / (max_x - min_x) * width,
                    height - (float(y) - min_y) / (max_y - min_y) * height
                    )
                    for x, y in geom.exterior.coords
                ])
                
                self.shp_polygons.append(pol)
                        
            else:
                print(f"Geometry: {str(geom.geom_type)}")
                QMessageBox.critical(None, "Error", f"Shapefile contains: {str(geom.geom_type)}")
                break

        self.shp_loaded = True
        self.repaint()

    def exit(self):
        """
        Exit GUI
        """
        QApplication.instance().quit()
    
    def clearAll(self):
        """
        Clear polygon and point
        """
        if self.shp_loaded:
            self.shp_polygons.clear()
        else:
            self.__pol.clear()
            
        self.__q = None
        self.shp_loaded = False
        self.highlighted_pol = []
        self.repaint()
        print("All Clear")
    
    def clearRes(self):
        """
        Clear point
        """
        self.__q = None
        self.highlighted_pol = []
        self.repaint()
        print("Clear")

    def mousePressEvent(self, e:QMouseEvent):
        # Reset highlighted polygons
        self.highlighted_pol = []
        
        # Get coordinates x,y
        x = e.position().x()
        y = e.position().y()
        
        # Add polygon vertex
        if self.__add_vertex:
            
            # Create new point
            p = QPointF(x, y)
        
            # Add to point to polygon
            self.__pol.append(p)
        
        # Change q coordinates
        else:
            self.__q = QPointF(x, y)
        
        # Repaint screen
        self.repaint()
 
 
    def paintEvent(self, e:QPaintEvent):
        # Create new graphic object
        qp = QPainter(self)
        
        # Start draw
        qp.begin(self)

        
        if self.shp_loaded:
            qp.setPen(QPen(Qt.GlobalColor.black, 2))
            qp.setBrush(Qt.GlobalColor.lightGray)
            # Draw polygon
            for pol in self.shp_polygons:
                qp.drawPolygon(pol)        
            
        else:
            # Set graphic attributes, polygon
            qp.setPen(Qt.GlobalColor.black)
            qp.setBrush(Qt.GlobalColor.yellow)
            # Draw polygon
            qp.drawPolygon(self.__pol)
        
        if self.highlighted_pol:
            qp.setPen(QPen(Qt.GlobalColor.black, 2))
            qp.setBrush(Qt.GlobalColor.cyan)
            for hl_pol in self.highlighted_pol:
                qp.drawPolygon(hl_pol)
        
        if self.__q != None:
            # Set graphic attributes, point
            qp.setPen(Qt.GlobalColor.black)
            qp.setBrush(Qt.GlobalColor.red)
            # Draw point
            r = 10
            qp.drawEllipse(int(self.__q.x()-r), int(self.__q.y()-r), 2*r, 2*r)
        
        # End drawing
        qp.end()
        
    def paintRes(self, pol):
        self.highlighted_pol.append(pol)
        self.repaint()
    
    def switchInput(self):
        # Input point or polygon vertex
        self.__add_vertex = not (self.__add_vertex)
    
    def getQ(self):
        # Get point
        return self.__q
    
    def getPol(self):
        # Get polygon
        if self.shp_loaded:
            return self.shp_polygons
        else:
            return [self.__pol]