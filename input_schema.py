from marshmallow import Schema, fields

class InputSchema(Schema):
    inputs = fields.String(required=True)

    mid_score = fields.Float(required=True)
    overall_mid_weight = fields.Float(required=True)
    mid_weight = fields.Float(required=True)

    final_score = fields.Float(required=True)
    overall_final_weight = fields.Float(required=True)
    final_weight = fields.Float(required=True)

    quiz_score = fields.Float(required=True)
    overall_quiz_weight = fields.Float(required=True)
    quiz_weight = fields.Float(required=True)

    performance = fields.Float(required=True)
    overall_perform_weight = fields.Float(required=True)
    perform_weight = fields.Float(required=True)

    AKHLAK = fields.Float(required=True)

    CO_mid_weight = fields.List(fields.Float(), required=True)
    CO_final_weight = fields.List(fields.Float(), required=True)
    CO_quiz_weight = fields.List(fields.Float(), required=True)
    CO_perform_weight = fields.List(fields.Float(), required=True)
    contribution = fields.List(fields.Float(), required=True)

    credit = fields.List(fields.Float(), required=True)
    course = fields.List(fields.Float(), required=True)