source .venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt

reflex init
reflex export --frontend-only

rm -fr public
unzip frontend.zip -d public
rm -f frontend.zip
deactivate




#API_URL=http://localhost:8000 reflex export --frontend-only

#rm -f frontend.zip
