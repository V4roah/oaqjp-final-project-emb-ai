import requests
import json


def emotion_detector(text_to_analyze):
    url = "https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict"
    headers = {
        "Content-Type": "application/json",
        "grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"
    }
    input_json = {"raw_document": {"text": text_to_analyze}}

    response = requests.post(url, headers=headers, json=input_json)

    if response.status_code == 200:
        result = response.json()
        try:
            emotions = result["emotionPredictions"][0]["emotion"]

            # Encontrar emoción dominante
            dominant_emotion = max(emotions, key=emotions.get)

            # Construir diccionario de salida con emoción dominante
            output = {
                'anger': emotions.get('anger', 0),
                'disgust': emotions.get('disgust', 0),
                'fear': emotions.get('fear', 0),
                'joy': emotions.get('joy', 0),
                'sadness': emotions.get('sadness', 0),
                'dominant_emotion': dominant_emotion
            }
            return output

        except (KeyError, IndexError):
            return {"error": "Unexpected response structure"}
    else:
        return {
            "error": f"Request failed with status code {response.status_code}",
            "response": response.text
        }


# Para testear desde línea de comandos:
if __name__ == "__main__":
    resultado = emotion_detector("Estoy tan feliz de estar haciendo esto.")
    print(json.dumps(resultado, indent=2))
