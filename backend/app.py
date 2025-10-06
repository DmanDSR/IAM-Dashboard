"""
Cybersecurity Dashboard Flask Application
Main application entry point with API endpoints for AWS integrations
"""

import os
import logging
from flask import Flask, jsonify, request, send_from_directory
from flask_cors import CORS
from flask_restful import Api
from werkzeug.exceptions import NotFound

# Import API resources
from api.aws_iam import IAMResource
from api.aws_ec2 import EC2Resource
from api.aws_s3 import S3Resource
from api.aws_security_hub import SecurityHubResource
from api.aws_config import ConfigResource
from api.grafana import GrafanaResource
from api.dashboard import DashboardResource
from api.health import HealthResource

# Import services
from services.aws_service import AWSService
from services.grafana_service import GrafanaService
from services.database_service import DatabaseService

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

def create_app():
    """Create and configure the Flask application"""
    app = Flask(__name__, static_folder='../static')
    
    # Configuration
    app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'dev-secret-key-change-in-production')
    app.config['DATABASE_URL'] = os.environ.get('DATABASE_URL', 'sqlite:///cybersecurity.db')
    app.config['REDIS_URL'] = os.environ.get('REDIS_URL', 'redis://localhost:6379/0')
    
    # Enable CORS for frontend integration
    CORS(app, origins=['http://localhost:3000', 'http://localhost:5173'])
    
    # Initialize API
    api = Api(app, prefix='/api/v1')
    
    # Initialize services
    aws_service = AWSService()
    grafana_service = GrafanaService()
    database_service = DatabaseService()
    
    # Register API resources
    api.add_resource(HealthResource, '/health')
    api.add_resource(DashboardResource, '/dashboard')
    api.add_resource(IAMResource, '/aws/iam')
    api.add_resource(EC2Resource, '/aws/ec2')
    api.add_resource(S3Resource, '/aws/s3')
    api.add_resource(SecurityHubResource, '/aws/security-hub')
    api.add_resource(ConfigResource, '/aws/config')
    api.add_resource(GrafanaResource, '/grafana')
    
    # Serve static files (React frontend)
    @app.route('/')
    def serve_frontend():
        return send_from_directory(app.static_folder, 'index.html')
    
    @app.route('/<path:path>')
    def serve_static(path):
        return send_from_directory(app.static_folder, path)
    
    # Error handlers
    @app.errorhandler(404)
    def not_found(error):
        return jsonify({'error': 'Not found'}), 404
    
    @app.errorhandler(500)
    def internal_error(error):
        return jsonify({'error': 'Internal server error'}), 500
    
    # Initialize database
    with app.app_context():
        database_service.init_db()
        logger.info("Database initialized")
    
    return app

if __name__ == '__main__':
    app = create_app()
    port = int(os.environ.get('PORT', 5000))
    debug = os.environ.get('FLASK_DEBUG', 'False').lower() == 'true'
    
    logger.info(f"Starting Cybersecurity Dashboard on port {port}")
    app.run(host='0.0.0.0', port=port, debug=debug)
