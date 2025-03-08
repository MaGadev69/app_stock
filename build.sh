
source .venv/bin/activate
# en gitbash source .venv/Scripts/activate
pip install --upgrade pip
pip install -r requirements.txt

reflex init
#esta es la url de la api en produccion, la misma esta en railway
API_URL=https://appstock-production-132c.up.railway.app reflex export --frontend-only

rm -fr public
unzip frontend.zip -d public
rm -f frontend.zip
source .venv/Scripts/deactivate
# en gitbash source .venv/Scripts/
#deactivate




#API_URL=http://localhost:8000 reflex export --frontend-only

# .venv/Script/activate
