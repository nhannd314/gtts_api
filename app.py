from flask import Flask, request, send_file
from gtts import gTTS
import io

app = Flask(__name__)

@app.route("/tts", methods=["POST"])
def tts():
    data = request.get_json()
    text = data.get("text", "")
    lang = data.get("lang", "en")

    # Tạo âm thanh bằng gTTS
    tts = gTTS(text=text, lang=lang)
    mp3_fp = io.BytesIO()
    tts.write_to_fp(mp3_fp)
    mp3_fp.seek(0)

    # Trả về file nhị phân .mp3
    return send_file(
        mp3_fp,
        mimetype="audio/mpeg",
        as_attachment=True,
        download_name="speech.mp3"
    )

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
