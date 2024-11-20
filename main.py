import re
from nltk import CFG, Tree
from nltk.parse.chart import ChartParser
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QLabel, QLineEdit, QPushButton, QWidget, QMessageBox, QTextEdit
import sys

# Definición de la gramática
gramatica = CFG.fromstring("""
    S -> E
    E -> E '+' T | E '-' T | T
    T -> T '*' F | T '/' F | F
    F -> '(' E ')' | VAR | NUM
    VAR -> 'a' | 'b' | 'c' | 'd' | 'e' | 'f' | 'g' | 'h' | 'i' | 'j' | 'k' | 'l' | 'm' | 'n' | 'o' | 'p' | 'q' | 'r' | 's' | 't' | 'u' | 'v' | 'w' | 'x' | 'y' | 'z'
    NUM -> '0' | '1' | '2' | '3' | '4' | '5' | '6' | '7' | '8' | '9'
""")

# analizar la gramatica brindada 
parser = ChartParser(gramatica)

class GrammarApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Árbol de Derivación y AST")
        self.setGeometry(100, 100, 500, 500)

        layout = QVBoxLayout()

    
        self.label = QLabel("Ingresa una expresión para analizar:")
        layout.addWidget(self.label)

        self.input_line = QLineEdit()
        layout.addWidget(self.input_line)

        # Botón para la derivación por izquierda
        self.btn_left_derivation = QPushButton("Mostrar Derivación por Izquierda")
        self.btn_left_derivation.clicked.connect(self.generate_left_derivation)
        layout.addWidget(self.btn_left_derivation)

        # Botón para la derivación por derecha
        self.btn_right_derivation = QPushButton("Mostrar Derivación por Derecha")
        self.btn_right_derivation.clicked.connect(self.generate_right_derivation)
        layout.addWidget(self.btn_right_derivation)

        # Botón para generar el ast
        self.btn_ast = QPushButton("Generar AST")
        self.btn_ast.clicked.connect(self.generate_ast)
        layout.addWidget(self.btn_ast)

        # mostrar caja de texto
        self.derivation_output = QTextEdit()
        self.derivation_output.setReadOnly(True)
        layout.addWidget(self.derivation_output)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)
        
        #analizar la expresion gramatica en caracteres
    def tokenize_expression(self, expression):
        """Analizar la expresión para obtener los tokens."""
        tokens = re.findall(r'\d+|[a-zA-Z]+|[()+\-*/=]', expression)
        return tokens
   
     # derivaciones 
    def generate_left_derivation(self):
        """Generar y mostrar derivación por izquierda."""
        self.generate_derivation("izquierda")

    def generate_right_derivation(self):
        """Generar y mostrar derivación por derecha."""
        self.generate_derivation("derecha")

    def generate_derivation(self, mode):
        """Generar y mostrar derivaciones por izquierda o derecha."""
        try:
            expresion_texto = self.input_line.text()
            tokens = self.tokenize_expression(expresion_texto)
            parse_tree = None

            for tree in parser.parse(tokens):
                parse_tree = tree
                break

            if parse_tree:
                derivation_steps = []
                if mode == "izquierda":
                    self.extract_left_derivation_steps(parse_tree, derivation_steps)
                elif mode == "derecha":
                    self.extract_right_derivation_steps(parse_tree, derivation_steps)

                derivation_text = "\n".join(derivation_steps)
                self.derivation_output.setText(f"Derivación por {mode.capitalize()}:\n{derivation_text}")
                parse_tree.draw()
            else:
                self.derivation_output.setText(f"No se pudo derivar la expresión por {mode}.")
        except Exception as e:
            QMessageBox.warning(self, "Error", f"Error en derivación por {mode}: {e}")

    def extract_left_derivation_steps(self, tree, derivation_steps):
        """Extraer producciones para derivación por izquierda."""
        if isinstance(tree, Tree):
            derivation_steps.append(f"{tree.label()} -> {' '.join(child.label() if isinstance(child, Tree) else child for child in tree)}")
            for subtree in tree:
                self.extract_left_derivation_steps(subtree, derivation_steps)

    def extract_right_derivation_steps(self, tree, derivation_steps):
        """Extraer producciones para derivación por derecha."""
        if isinstance(tree, Tree):
            derivation_steps.append(f"{tree.label()} -> {' '.join(child.label() if isinstance(child, Tree) else child for child in tree)}")
            for subtree in reversed(tree):
                self.extract_right_derivation_steps(subtree, derivation_steps)
 
 # generador del ast
    def generate_ast(self):
        """Generar y mostrar el AST."""
        try:
            expresion_texto = self.input_line.text()
            tokens = self.tokenize_expression(expresion_texto)
            parse_tree = None

            for tree in parser.parse(tokens):
                parse_tree = tree
                break

            if parse_tree:
                ast = self.build_ast(parse_tree)
                self.derivation_output.setText(f"Árbol Sintáctico Abstracto (AST):\n{ast}")
                ast.draw()
            else:
                QMessageBox.warning(self, "Error", "No se pudo generar el AST para la expresión proporcionada.")
        except Exception as e:
            QMessageBox.warning(self, "Error", f"Error al generar el AST: {e}")

    def build_ast(self, tree):
        """Construir un AST simplificado a partir del árbol de derivación."""
        if isinstance(tree, Tree):
            if tree.label() in {'E', 'T', 'F'}:
                if len(tree) == 1:
                    return self.build_ast(tree[0])  
                else:
                    return Tree(tree[1], [self.build_ast(tree[0]), self.build_ast(tree[2])])  
            elif tree.label() in {'VAR', 'NUM'}:
                return Tree(tree.label(), [tree[0]])  
            else:
                return Tree(tree.label(), [self.build_ast(child) for child in tree])
        else:
            return tree

# función principal
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = GrammarApp()
    window.show()
    sys.exit(app.exec_())



