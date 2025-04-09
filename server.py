"""Servidor Flask para detección de emociones."""
from flask import Flask, request, render_template
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)


@app.route('/')
def index():
    """Renderiza la página principal."""
    return render_template('index.html')


@app.route('/emotionDetector', methods=['GET'])
def emotion_route():
    """Procesa el texto enviado por el cliente y retorna el análisis emocional."""
    text_to_analyze = request.args.get('textToAnalyze')
    result = emotion_detector(text_to_analyze)

    if result.get('dominant_emotion') is None:
        return "¡Texto inválido! ¡Por favor, intenta de nuevo!"

    response = (
        f"Para la declaración dada, la respuesta del sistema es "
        f"'anger': {result['anger']}, "
        f"'disgust': {result['disgust']}, "
        f"'fear': {result['fear']}, "
        f"'joy': {result['joy']} y "
        f"'sadness': {result['sadness']}. "
        f"La emoción dominante es {result['dominant_emotion']}."
    )
    return response


if __name__ == '__main__':
    app.run(debug=True)
