from flask import jsonify, render_template, Blueprint
from operations import perform_operation
from exceptions import DivisionByZeroError, InvalidOperationError, InvalidInputError

calculator_bp = Blueprint('calculator', __name__)

@calculator_bp.route('/<operation>/<num1>/<num2>')
def calculator(operation, num1, num2):
    """
    Main route handler for calculator operations
    Returns JSON response with result
    """
    try:
        result = perform_operation(operation, num1, num2)
        return jsonify({
            'status': 200,
            'result': result
        })
    except DivisionByZeroError as e:
        return jsonify({
            'status': 400,
            'error': str(e),
            'error_type': 'division_by_zero'
        }), 400
    except InvalidOperationError as e:
        return jsonify({
            'status': 400,
            'error': str(e),
            'error_type': 'invalid_operation'
        }), 400
    except InvalidInputError as e:
        return jsonify({
            'status': 400,
            'error': str(e),
            'error_type': 'invalid_input'
        }), 400
    except Exception as e:
        return jsonify({
            'status': 500,
            'error': 'An unexpected error occurred',
            'error_type': 'server_error'
        }), 500

@calculator_bp.route('/')
def home():
    """Home route with usage instructions"""
    return render_template('index.html')