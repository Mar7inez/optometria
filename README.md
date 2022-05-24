# Optometría 😎

Proyecto frontend + backend para clínica optometría "Sarasa".

## 📚 Stack

- Frontend:
    - ⚛ React
    - ⚡ Vite
    - 🎨 Prettier
    - 😐 ESlint
    - 🚚 Axios
    - 🌌 ChakraUI
- Backend:
    - 🐍 Python
    - 🦗 Django Ninja
- Infra: WIP


## 📄 Instalación

```sh
git clone https://github.com/JaviCeRodriguez/optometria.git

# Backend
cd ./backend
python -m virtualenv venv
source ./venv/bin/activate
pip install -r requirements.txt
python manage.py makemigrations
python manage.py migrate
python manage.py runserver

# Frontend (en otra consola)
cd ./frontend # (desde el root del proyecto)
yarn install
yarn dev
```