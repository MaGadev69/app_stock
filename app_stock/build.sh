pip install -r requirements.txt
rm -rf public
reflex init
reflex export --frontend-only
API_URL=http://localhost:8000 reflex export --frontend-only
unzip frontend.zip -d public
rm -f frontend.zip
deactivate