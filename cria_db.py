from app import db, create_app
from app.models import User,Veicles

# Cria a aplicação
app = create_app()

# Cria o bd
with app.app_context():
    db.create_all()
    print("foi certinho")
