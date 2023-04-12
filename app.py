from flask import Response
from flask import Flask, jsonify, request, json
from calculation import *
from flask import abort, make_response, jsonify, request
from validation import *

app = Flask(__name__)
@app.route('/api', methods=['POST'])
def scrap():
    request_data = validate_schema(request.get_json())
    inputs = request_data.get('inputs')

    mid_score = request_data.get('mid_score')
    overall_mid_weight = request_data.get('overall_mid_weight')
    mid_weight = request_data.get('mid_weight')

    final_score = request_data.get('final_score')
    overall_final_weight = request_data.get('overall_final_weight')
    final_weight = request_data.get('final_weight')

    quiz_score = request_data.get('quiz_score')
    overall_quiz_weight = request_data.get('overall_quiz_weight')
    quiz_weight = request_data.get('quiz_weight')

    performance = request_data.get('performance')
    overall_perform_weight = request_data.get('overall_perform_weight')
    perform_weight = request_data.get('perform_weight')

    AKHLAK = request_data.get('AKHLAK')

    CO_mid_weight = request_data.get('CO_mid_weight')
    CO_final_weight = request_data.get('CO_final_weight')
    CO_quiz_weight = request_data.get('CO_quiz_weight')
    CO_perform_weight = request_data.get('CO_perform_weight')
    contribution = request_data.get('contribution')

    credit = request_data.get('credit')
    course = request_data.get('course')

    if inputs == 'score course':
        return jsonify(score_course(mid_score, overall_mid_weight, final_score, overall_final_weight, CO_mid_weight, CO_final_weight, quiz_score, overall_quiz_weight, CO_quiz_weight, contribution))
    elif inputs == 'score subcourse':
        return jsonify(score_subcourse(mid_score,overall_mid_weight, mid_weight, final_score, overall_final_weight, final_weight, quiz_score, overall_quiz_weight, quiz_weight, performance, overall_perform_weight, perform_weight, AKHLAK))
    elif inputs == 'score grouping':
        return jsonify(score_grouping(mid_score, overall_mid_weight, CO_mid_weight, final_score, overall_final_weight, CO_final_weight, quiz_score, overall_quiz_weight, CO_quiz_weight, performance, overall_perform_weight, CO_perform_weight, AKHLAK, contribution))
    elif inputs == 'ipk':
        return jsonify(ipk(credit, course))
    
if __name__ == "__main__":
    app.run(debug=True, host='127.0.0.1', port=7000)