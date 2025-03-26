import streamlit as st
import random

# Lista de preguntas
quiz = [
    {
        "question": "Se basa en el uso de números aleatorios y probabilidad estadística. Estamos hablando de:",
        "options": ["Método de Monte Carlo", "Redes Bayesianas", "Distribución Gaussiana", "Ley de Murphy"],
        "correct": 1  # El Método de Monte Carlo usa números aleatorios y probabilidad estadística.
    },
    {
        "question": "¿Cuáles son los componentes de los sistemas basados en reglas?",
        "options": ["Conocimiento, almacenaje y diferencias", "Base de conocimiento, Base de datos y mecanismos de inferencia", "Bases, reglas y normas", "Ninguna es correcta"],
        "correct": 2  # Los componentes correctos son base de conocimiento, base de datos y mecanismos de inferencia.
    },
    {
        "question": "Selecciona la respuesta correcta con respecto a los mecanismos basados en reglas:",
        "options": ["En el “modus ponens” tenemos las premisas y las normas", "Son poco eficaces aunque las reglas cubran las entradas almacenadas en la BD", "Son mecanismos poco costosos de ejecutar dada su simplicidad", "Se pueden considerar como la forma más compleja de representar sistemas de IA."],
        "correct": 3  # Son simples y poco costosos de ejecutar.
    },
    {
        "question": "¿Cuáles son las fuentes de incertidumbre en el razonamiento aproximado?",
        "options": ["Deficiencias de la información, agentes del mundo real y deficiencias de las realidades sociales.", "Deficiencias de la información, agentes del mundo real y deficiencia de los modelos que intentan explicar el problema.", "Agentes del mundo real, deficiencias de la información y realidades sociopolíticas de la posmodernidad.", "Deficiencias en el sistema ideológico neoliberal, agentes del mundo distópico y deficiencias del idealismo político."],
        "correct": 2  # La opción B es la más precisa en el contexto del razonamiento aproximado.
    },
    {
        "question": "¿Cuál de las siguientes opciones describe mejor el Método Monte Carlo?",
        "options": ["Un método de resolución numérica de ecuaciones diferenciales.", "Un método de estimación estadística basado en la generación de números aleatorios.", "Un método de clasificación de datos basado en árboles de decisión.", "Un método de interpolación de datos a partir de puntos discretos"],
        "correct": 2  # El Método Monte Carlo se basa en números aleatorios para estimaciones estadísticas.
    },
    {
        "question": "¿En teoría de grafos e informática qué es un DAG?",
        "options": ["Digital Agreement Graphics.", "Un grafo dirigido en el que no hay ciclos.", "Diseño Adquirido de Grafos.", "Ninguna de las anteriores."],
        "correct": 2  # DAG significa "Directed Acyclic Graph" (grafo dirigido acíclico).
    },
    {
        "question": "La lógica difusa sirve para:",
        "options": ["Poder cuantificar la incertidumbre del mundo que nos rodea.", "Poder calcular la probabilidad que ocurra un suceso no aleatorio.", "Establecer reglas de funcionamiento del mundo abstracto", "Establece los principios de funcionamiento de la naturaleza humana"],
        "correct": 1  # La lógica difusa cuantifica incertidumbre con valores intermedios.
    },
    {
        "question": "¿Qué son las redes bayesianas?",
        "options": ["Son representaciones de mecanismos poco costosos de ejecutar dada su simplicidad.", "Son estructuras matemáticas representadas por nodos dependientes.", "Son representaciones a través de grafos acíclicos dirigidos, donde los nodos representan variables aleatorias y los arcos sus dependencias.", "Son las representaciones lógicas basadas en la Ley de Bayes."],
        "correct": 3  # Las redes bayesianas son grafos acíclicos dirigidos con dependencias entre variables.
    },
    {
        "question": "Es la probabilidad de una variable aleatoria basada en datos del experimento, es decir, después de considerar la evidencia, estamos hablando de:",
        "options": ["Probabilidad condicionada", "Probabilidad conjunta", "Probabilidad posterior", "Todas son correctas"],
        "correct": 3  # La probabilidad posterior se calcula tras considerar evidencia (Teorema de Bayes).
    },
    {
        "question": "Redes bayesianas (Grafos acíclicos). Indica la falsa:",
        "options": ["Un grafo se compone de vértices y aristas, con cada arista apuntando al vértice siguiente.", "Se considera que un grafo es dirigido cuando todas las direcciones son consistentes y los vértices tienen un orden lineal.", "Un DAG es un grafo dirigido con múltiples ciclos.", "Se considera que un grafo es acíclico cuando sigue las direcciones nunca conduce a un bucle cerrado."],
        "correct": 3  # Un DAG no tiene ciclos, por lo que esta afirmación es falsa.
    },
    {
        "question": "Sobre la Teoría de Dempster-Shafer:",
        "options": ["Un modelo de clasificación no supervisada para la segmentación de imágenes.", "Es una generalización del método bayesiano donde se combinan entre sí todas las posibilidades a las que nos podemos enfrentar en un problema dado.", "Una técnica de reducción de dimensionalidad para datos de alta dimensionalidad.", "Todas las anteriores son correctas"],
        "correct": 2  # Es una generalización del método bayesiano para manejar incertidumbre.
    },
    {
        "question": "Sobre el método de Aceptación-Rechazo:",
        "options": ["Se puede enfocar aplicando el método de Monte Carlo.", "Consiste en la generación sistemática de puntos aleatorios en un determinado rango.", "Permite la aproximación del área de una determinada región.", "Todas las anteriores son correctas."],
        "correct": 4  # Todas las afirmaciones son ciertas sobre el método de Aceptación-Rechazo.
    },
    {
        "question": "¿Cuál de las siguientes opciones es una característica de las redes bayesianas?",
        "options": ["Son modelos gráficos probabilísticos", "Son modelos de regresión lineal", "Son modelos de clasificación no supervisada", "Son modelos de aprendizaje por refuerzo"],
        "correct": 1  # Las redes bayesianas son modelos gráficos probabilísticos.
    },
    {
        "question": "¿Cuál de las siguientes opciones es una característica de la lógica difusa?",
        "options": ["Permite tomar decisiones más o menos intensas en función de grados intermedios de cumplimiento de una premisa", "Es una lógica paraconsistente multivaluada en la cual los valores de verdad de las variables pueden ser cualquier número real comprendido entre 0 y 1", "Es una lógica que se utiliza para representar relaciones de dependencia entre variables aleatorias y para realizar inferencias sobre ellas", "Es una lógica que se utiliza para modelar sistemas complejos y no lineales"],
        "correct": 1  # Permite tomar decisiones más o menos intensas en función de grados intermedios de cumplimiento de una premisa
    },
    {
        "question": "¿Cuál es la principal ventaja del método de inferencia de Takagi-Sugeno sobre el método de inferencia de Mandani?",
        "options": ["El método de Takagi-Sugeno es más simple y fácil de implementar, siendo el más utilizado en lógica difusa.", "El método de Takagi-Sugeno proporciona resultados más precisos.", "El método de Takagi-Sugeno es más rápido en el procesamiento de datos.", "La salida del sistema de Mamdani se representa como una expresión matemática."],
        "correct": 2  # El método de Takagi-Sugeno proporciona resultados más precisos.
    },
    {
        "question": "Indica las partes de un controlador difuso",
        "options": ["Codificación o fuzzificación, base de conocimiento, motor de inferencia y decodificador o defuzzificador", "Codificación o fuzzificación, base de conocimiento y motor de inferencia", "Decodificador, base de conocimiento y motor diferencial", "Decodificador, base de conocimiento y motor de lógica difusa"],
        "correct": 1  # Todas las partes listadas en A son correctas.
    },
    {
        "question": "Sobre el método de Monte Carlo, indica la opción correcta:",
        "options": ["Aplicarlo para casos sencillos, unidimensionales, no compensa.", "Al calcular una aproximación, no permite resolver problemas complejos", "Es buena elección para problemas unidimensionales", "Ninguna es correcta."],
        "correct": 1  # No compensa usarlo en problemas sencillos debido a su costo computacional.
    },
    {
        "question": "Variational Bayes vs Monte Carlo",
        "options": ["El método de Montecarlo es computacional más costoso", "Variational Bayes es adecuado para explorar muchos modelos en conjuntos grandes de datos", "El método de Monte Carlo proporciona una aproximación numérica al posterior exacto", "Todas las anteriores"],
        "correct": 4  # Todas las afirmaciones son correctas.
    },
    {
        "question": "Indica la correcta sobre el método de inferencia Mamdani:",
        "options": ["Para obtener una conclusión, se calcula la función de pertenencia a cada variable de entrada y, al final, se combinan todas las reglas en un único conjunto difuso para definir la pertenencia", "Es el método más utilizado en la lógica difusa", "La salida del sistema se representa como un conjunto difuso", "Todas son correctas"],
        "correct": 4  # Todas las afirmaciones son ciertas sobre Mamdani.
    },
    {
        "question": "¿Qué es un conjunto difuso?",
        "options": ["Una función que indica el grado de pertenencia de un valor difuso.", "Un conjunto de valores numéricos", "Un conjunto de variables lingüísticas", "Una función que indica el grado de pertenencia de un valor numérico para una variable lingüística o difusa"],
        "correct": 4  # Un conjunto difuso mide el grado de pertenencia a una variable lingüística.
    }
]

# Inicialización del estado
if 'quiz' not in st.session_state:
    st.session_state.quiz = quiz.copy()
    random.shuffle(st.session_state.quiz)
    for q in st.session_state.quiz:
        q["options_shuffled"] = q["options"].copy()
        random.shuffle(q["options_shuffled"])
        q["correct_index"] = q["options_shuffled"].index(q["options"][q["correct"] - 1]) + 1
        q["user_answer"] = None  # Respuesta del usuario
    st.session_state.submitted = False

# Interfaz de la aplicación
st.title("Test de Razonamiento Aproximado (Curso IA-ML 2025)")

# Mostrar cada pregunta
for i, q in enumerate(st.session_state.quiz, 1):
    st.subheader(f"Pregunta {i}: {q['question']}")
    
    # Selección de respuesta por el usuario
    answer = st.radio(
        "Selecciona una opción",
        q["options_shuffled"],
        key=f"q{i}",
        index=None if q["user_answer"] is None else q["options_shuffled"].index(q["user_answer"])
    )
    q["user_answer"] = answer  # Guardar la respuesta seleccionada
    
    # Botón "Corregir" para retroalimentación opcional
    if st.button("Corregir", key=f"check_q{i}"):
        if q["user_answer"] is None:
            st.warning("Por favor, selecciona una opción antes, que no soy adivino!.")
        else:
            if q["options_shuffled"].index(q["user_answer"]) + 1 == q["correct_index"]:
                st.success("¡Opa! ¡Correcto!")
            else:
                correct_answer = q["options"][q["correct"] - 1]
                st.error(f"Vaya tela... la respuesta correcta es: {correct_answer}. Revísalo anda!")

# Botón para finalizar el test
if st.button("Finalizar el Test"):
    st.session_state.submitted = True

# Mostrar resultados al finalizar
if st.session_state.submitted:
    total_questions = len(st.session_state.quiz)
    correct = 0
    incorrect = 0
    unanswered = 0
    
    # Evaluar todas las respuestas
    for q in st.session_state.quiz:
        if q["user_answer"] is None:
            unanswered += 1
        elif q["options_shuffled"].index(q["user_answer"]) + 1 == q["correct_index"]:
            correct += 1
        else:
            incorrect += 1
    
    # Calcular porcentajes
    percentage_correct = (correct / total_questions) * 100 if total_questions > 0 else 0
    percentage_incorrect = (incorrect / total_questions) * 100 if total_questions > 0 else 0
    percentage_unanswered = (unanswered / total_questions) * 100 if total_questions > 0 else 0
    
    # Mostrar resultados
    st.success(f"Test finalizado. Tu puntuación: {correct}/{total_questions}")
    st.write(f"**Número de aciertos:** {correct} ({percentage_correct:.2f}%)")
    st.write(f"**Número de fallos:** {incorrect} ({percentage_incorrect:.2f}%)")
    st.write(f"**Preguntas no contestadas:** {unanswered} ({percentage_unanswered:.2f}%)")
    
    # Opción para reiniciar
    if st.button("Reiniciar"):
        st.session_state.clear()
        st.experimental_rerun()
