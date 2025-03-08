
FROM python:3.11 AS init

WORKDIR /app
COPY . .    

ENV VIRTUAL_ENV=/app/.venv_docker
ENV PATH="$VIRTUAL_ENV/bin:$PATH"
RUN python3.11 -m venv $VIRTUAL_ENV
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

# Formato JSON para CMD
CMD reflex run --env prod --backend-only

#--------------------------------------------backend
# backend https://www.youtube.com/watch?v=bNy8OZJfA6I
# https://railway.com/project/9a9cff0e-da58-4129-a371-e0aca5b34fc9/service/0fe6c233-6cfe-4ac8-b6e9-1b7712a0d278?environmentId=23f49f8b-038d-4336-a67a-99a2710c9e61
# https://appstock-production-132c.up.railway.app/
#--------------------------------------------frontend
# desde aqui la guia para frontend simple https://www.youtube.com/watch?v=h8Tn0ITRoQs&t=2191s
# https://vercel.com/max3669s-projects/app-stock



# docker run -d -p 8000:8000 --name app app_stock:latest
# comando para iniciar un contenedor con la imagen creada

#--------------------------------------------
# #  Inicializar proyecto



# git init
# git add .
# git commit -m "Subida limpia sin archivos grandes"
# git remote add origin https://github.com/MaGadev69/app_stock.git
# git branch -M master
# git push -u origin master --force

#  move ..\backup_node_modules node_modules



# hacer primero build.sh, luego pasos para github
# todo se centraliza alli
#--------------------------------------------
# # Pasos para subir cambios a GitHub

# git status
# git add .
# git commit -m "Descripción de los cambios"
# git push