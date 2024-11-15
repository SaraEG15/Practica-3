import re
from nltk import CFG, Tree
from nltk.parse.chart import ChartParser
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QLabel, QLineEdit, QPushButton, QWidget, QMessageBox, QRadioButton, QButtonGroup
import sys


gramatica = CFG.fromstring("""
    S -> E
    E -> E '+' T | E '-' T | T
    T -> T '*' F | T '/' F | F
    F -> '(' E ')' | VAR | NUM
    VAR -> 'a' | 'b' | 'c' | 'd' | 'e' | 'f' | 'g' | 'h' | 'i' | 'j' | 'k' | 'l' | 'm' | 'n' | 'o' | 'p' | 'q' | 'r' | 's' | 't' | 'u' | 'v' | 'w' | 'x' | 'y' | 'z'
    NUM -> '0' | '1' | '2' | '3' | '4' | '5' | '6' | '7' | '8' | '9'
""")
# gramatica que nos proporciono el codigo base de nuestro profesor 


parser = ChartParser(gramatica)
# analizador sintactico que nos proporciono el codigo base 

class GrammarApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Árbol de Derivación")
        self.setGeometry(100, 100, 400, 300)

        layout = QVBoxLayout()

        
        self.label = QLabel("Ingresa una expresión para derivar:")
        layout.addWidget(self.label)


        self.input_line = QLineEdit()
        layout.addWidget(self.input_line)


        self.label_derivacion = QLabel("Selecciona el tipo de derivación:")
        layout.addWidget(self.label_derivacion)

 
        self.left_derivation = QRadioButton("Derivación por Izquierda")
        self.right_derivation = QRadioButton("Derivación por Derecha")
        self.left_derivation.setChecked(True)  

      
        self.derivation_group = QButtonGroup()
        self.derivation_group.addButton(self.left_derivation)
        self.derivation_group.addButton(self.right_derivation)

        layout.addWidget(self.left_derivation)
        layout.addWidget(self.right_derivation)

      
        self.btn_generate = QPushButton("Siguiente")
        self.btn_generate.clicked.connect(self.generate_tree)
        layout.addWidget(self.btn_generate)

        
        container = QWidget()            
        container.setLayout(layout)
        self.setCentralWidget(container)
     # https://gist.github.com/jalfonsosuarez/23273751501855099382 ,https://misovirtual.virtual.uniandes.edu.co/codelabs/interfaces-graficas-pyqt5/index.html?index=..%2F..index#7
     # me guie de estas paginas para realizar la interfaz 

    def tokenize_expression(self, expression):
        # Analizar la expresion por sus partes, es decir, desenglozar la expresion en las letras y simbolos
        tokens = re.findall(r'\d+|[a-zA-Z]+|[()+\-*/=]', expression)
        return tokens

    def generate_tree(self):
        # Se adquiere la informacion del usuario
        expresion_texto = self.input_line.text()
        derivacion_izquierda = self.left_derivation.isChecked()

        try:
            
            tokens = self.tokenize_expression(expresion_texto)

            
            if derivacion_izquierda:
                self.force_left_derivation(tokens)
            else:
                self.force_right_derivation(tokens)

        except Exception as e:
            QMessageBox.warning(self, "Error", f"Ha ocurrido un error: {e}")  # se muestra un error si la expresion no es correcta

    def force_left_derivation(self, tokens):  # derivacion por derecha 
        """Forzar derivación por izquierda"""
        try:
            
            parse_tree = None
            for tree in parser.parse(tokens):
                parse_tree = tree
                break  # Se toma el arbol como valido
            if parse_tree:
                parse_tree.draw()  # se muetsra el árbol gráficamente
            else:
                QMessageBox.warning(self, "Error", "No se pudo derivar la expresión.")
        except Exception as e:
            QMessageBox.warning(self, "Error", f"Error al generar árbol de derivación por izquierda: {e}")

    def force_right_derivation(self, tokens): # derivacion por izquierda
        """Forzar derivación por derecha"""
        try:
            
            parse_tree = None
            for tree in parser.parse(tokens):
                parse_tree = tree
                break  # Tomamos el primer árbol válido

            if parse_tree:
                parse_tree.draw()  # Mostrar el árbol gráficamente
            else:
                QMessageBox.warning(self, "Error", "No se pudo derivar la expresión.")
        except Exception as e:
            QMessageBox.warning(self, "Error", f"Error al generar árbol de derivación por derecha: {e}")

# Función principal para ejecutar la aplicación
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = GrammarApp()
    window.show()
    sys.exit(app.exec_())

