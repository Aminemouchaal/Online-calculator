from flask import Flask, jsonify
from routes import calculator_bp

def create_app():
    """Application factory function"""
    app = Flask(__name__)
    
    # Register blueprints
    app.register_blueprint(calculator_bp)
    
    # Register error handlers
    @app.errorhandler(404)
    def not_found_error(error):
        return jsonify({
            'status': 404,
            'error': 'Resource not found',
            'error_type': 'not_found'
        }), 404
    
    @app.errorhandler(500)
    def internal_error(error):
        return jsonify({
            'status': 500,
            'error': 'An unexpected error occurred',
            'error_type': 'server_error'
        }), 500
    
    return app

app = create_app()
