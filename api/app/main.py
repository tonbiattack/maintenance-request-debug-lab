from flask import Flask, jsonify, request
from .service import ValidationProblem, error_status, request_id_for_log
app = Flask(__name__)
@app.before_request
def correlation_id(): request.environ['request_id'] = request_id_for_log(request.headers.get('X-Request-Id'))
@app.after_request
def add_request_id(response): response.headers['X-Request-Id'] = request.environ['request_id']; return response
@app.errorhandler(ValidationProblem)
def validation_error(error): return jsonify({'error': str(error)}), error_status(error)
@app.get('/api/requests')
def list_requests(): return jsonify({'items': [], 'requestId': request.environ['request_id']})
@app.get('/health')
def health(): return jsonify({'status': 'ok'})
