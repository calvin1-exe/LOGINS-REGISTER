from website import create_app
from website.models import db, User

app = create_app()

@app.route('/test')
def test():
    return "Test route working!"

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
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
    app.run(debug=True)