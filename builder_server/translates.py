import translators as ts
from flask import Flask, request, jsonify, make_response, redirect

app = Flask(__name__)


@app.route("/", methods=['GET'])
def index():
    return jsonify(google_help=[])

@app.route("/translate", methods=['GET', 'POST'])
def translate():

    source_type = request.args['type'] if 'type' in request.args else 'google'
    source_from = request.args['from'] if 'from' in request.args else 'en'
    source_to = request.args['to'] if 'to' in request.args else 'es'
    source_text = request.args['text'] if 'text' in request.args else 'Free sex Videos'

    args = request.args

    if source_type == 'google':
        try:
            translate = ts.google(source_text, from_language=source_from, to_language=source_to)
            response = make_response(
                jsonify(
                    {"from": source_from, "to": source_to, "type": source_type, "original": source_text, "text": translate}
                ),
                200,
            )
            response.headers["Content-Type"] = "application/json"
            return response
        except Exception:
            response = make_response(jsonify({"message": "try_other_source", "severity": "warning"}), 200)
            return response
            pass
    elif source_type == 'deepl':
        try:
            translated_response = ts.deepl(query_text=source_text, from_language=source_from, to_language=source_to)
            response = make_response(
                jsonify(
                    {"from": source_from, "to": source_to, "type": source_type, "original": source_text, "text": translated_response}
                ),
                200,
            )
            response.headers["Content-Type"] = "application/json"
            return response
        except Exception:
            response = make_response(jsonify({"message": "try_other_source", "severity": "warning"}), 200)
            return response
            pass
    elif source_type == 'alibaba':
        try:
            translated_response = ts.alibaba(query_text=source_text, from_language=source_from, to_language=source_to)
            response = make_response(
                jsonify(
                    {"from": source_from, "to": source_to, "type": source_type, "original": source_text, "text": translated_response}
                ),
                200,
            )
            response.headers["Content-Type"] = "application/json"
            return response
        except Exception:
            response = make_response(jsonify({"message": "try_other_source", "severity": "warning"}), 200)
            return response
            pass
    elif source_type == 'baidu':
        try:
            translated_response = ts.baidu(query_text=source_text, from_language=source_from, to_language=source_to)
            response = make_response(
                jsonify(
                    {"from": source_from, "to": source_to, "type": source_type, "original": source_text, "text": translated_response}
                ),
                200,
            )
            response.headers["Content-Type"] = "application/json"
            return response
        except Exception:
            response = make_response(jsonify({"message": "try_other_source", "severity": "warning"}), 200)
            return response
            pass
    elif source_type == 'iciba':

        try:
            translated_response = ts.iciba(query_text=source_text, from_language=source_from, to_language=source_to)
            response = make_response(
                jsonify(
                    {"from": source_from, "to": source_to, "type": source_type, "original": source_text, "text": translated_response}
                ),
                200,
            )
            response.headers["Content-Type"] = "application/json"
            return response
        except Exception:
            response = make_response(jsonify({"message": "try_other_source", "severity": "warning"}), 200)
            return response
            pass
    elif source_type == 'bing':
        try:
            translated_response = ts.bing(query_text=source_text, from_language=source_from, to_language=source_to)
            response = make_response(
                jsonify(
                    {"from": source_from, "to": source_to, "type": source_type, "original": source_text, "text": translated_response}
                ),
                200,
            )
            response.headers["Content-Type"] = "application/json"
            return response
        except Exception:
            response = make_response(jsonify({"message": "try_other_source", "severity": "warning"}), 200)
            return response
            pass
    elif source_type == 'yandex':
        try:
            translated_response = ts.yandex(query_text=source_text, from_language=source_from, to_language=source_to)
            response = make_response(
                jsonify(
                    {"from": source_from, "to": source_to, "type": source_type, "original": source_text, "text": translated_response}
                ),
                200,
            )
            response.headers["Content-Type"] = "application/json"
            return response
        except Exception:
            response = make_response(jsonify({"message": "try_other_source", "severity": "warning"}), 200)
            return response
            pass
    elif source_type == 'itranslate':
        try:
            translated_response = ts.itranslate(query_text=source_text, from_language=source_from, to_language=source_to)
            response = make_response(
                jsonify(
                    {"from": source_from, "to": source_to, "type": source_type, "original": source_text, "text": translated_response}
                ),
                200,
            )
            response.headers["Content-Type"] = "application/json"
            return response
        except Exception:
            response = make_response(jsonify({"message": "try_other_source", "severity": "warning"}), 200)
            return response
            pass
    elif source_type == 'sogou':
        try:
            translated_response = ts.sogou(query_text=source_text, from_language=source_from, to_language=source_to)
            response = make_response(
                jsonify(
                    {"from": source_from, "to": source_to, "type": source_type, "original": source_text, "text": translated_response}
                ),
                200,
            )
            response.headers["Content-Type"] = "application/json"
            return response
        except Exception:
            response = make_response(jsonify({"message": "try_other_source", "severity": "warning"}), 200)
            return response
            pass
    elif source_type == 'reverso':
        try:
            translated_response = ts.reverso(query_text=source_text, from_language=source_from, to_language=source_to)
            response = make_response(
                jsonify(
                    {"from": source_from, "to": source_to, "type": source_type, "original": source_text, "text": translated_response}
                ),
                200,
            )
            response.headers["Content-Type"] = "application/json"
            return response
        except Exception:
            response = make_response(jsonify({"message": "try_other_source", "severity": "warning"}), 200)
            return response
            pass
    elif source_type == 'tencent':
        try:
            translated_response = ts.tencent(query_text=source_text, from_language=source_from, to_language=source_to)
            response = make_response(
                jsonify(
                    {"from": source_from, "to": source_to, "type": source_type, "original": source_text, "text": translated_response}
                ),
                200,
            )
            response.headers["Content-Type"] = "application/json"
            return response
        except Exception:
            response = make_response(jsonify({"message": "try_other_source", "severity": "warning"}), 200)
            return response
            pass
    elif source_type == 'argos':
        try:
            translated_response = ts.argos(query_text=source_text, from_language=source_from, to_language=source_to)
            response = make_response(
                jsonify(
                    {"from": source_from, "to": source_to, "type": source_type, "original": source_text, "text": translated_response}
                ),
                200,
            )
            response.headers["Content-Type"] = "application/json"
            return response
        except Exception:
            response = make_response(jsonify({"message": "try_other_source", "severity": "warning"}), 200)
            return response
            pass
    else:
        response = make_response(
            jsonify(
                {"message": "source is mandatory field", "severity": "danger"}
            ),
            401,
        )
        response.headers["Content-Type"] = "application/json"
        return response

