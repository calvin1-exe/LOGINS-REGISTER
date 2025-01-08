from website import create_app
from website.models import db, User
import os
from dotenv import load_dotenv

load_dotenv()

app = create_app()

# Initialize database and admin user
@app.before_first_request
def initialize_database():
    with app.app_context():
        try:
            db.create_all()
            
            # Create default admin if it doesn't exist
            admin = User.query.filter_by(email='admin@example.com').first()
            if not admin:
                admin = User(
                    email='admin@example.com',
                    first_name='Admin',
                    role='admin',
                    is_active=True
                )
                admin.set_password('admin123')
                db.session.add(admin)
                db.session.commit()
        except Exception as e:
            app.logger.error(f"Database initialization error: {str(e)}")

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    if os.environ.get('FLASK_ENV') == 'production':
        app.run(host='0.0.0.0', port=port)
    else:
        app.run(host='0.0.0.0', port=port, debug=True)