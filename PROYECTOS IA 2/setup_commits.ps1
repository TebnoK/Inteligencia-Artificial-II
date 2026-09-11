# setup_commits.ps1
# Inicializa el repo, conecta el remoto y crea los commits de la Sesion 1
# ya organizados (analiticos -> laboratorios) con la fecha correcta.
#
# ANTES DE CORRER:
#   1) Edita la linea $fecha con la fecha de entrega de la Sesion 1.
#   2) Corre este script UNA vez desde la terminal de VS Code, parado en
#      la carpeta "PROYECTOS IA 2" (donde esta este mismo archivo).

$fecha = "2026-08-15T19:00:00"   # <-- EDITA esta fecha (formato yyyy-MM-ddTHH:mm:ss)
$remoto = "https://github.com/TebnoK/Inteligencia-Artificial-II.git"

if (-not (git config user.name)) {
    Write-Host "Aviso: no tienes user.name/user.email configurados en git. Corre primero:"
    Write-Host '  git config --global user.name "Tu Nombre"'
    Write-Host '  git config --global user.email "tu@correo.com"'
    exit 1
}

if (-not (Test-Path ".git")) {
    git init
    git branch -M main
}

if (-not (git remote)) {
    git remote add origin $remoto
} else {
    Write-Host "Remoto ya configurado: $(git remote get-url origin)"
}

$env:GIT_AUTHOR_DATE = $fecha
$env:GIT_COMMITTER_DATE = $fecha

git add "sesion-01-refuerzo-python-algebra-lineal/taller-analitico-1-indexacion-tensores.md"
git commit -m "Sesion 1: taller analitico 1 - indexacion y tensores"

git add "sesion-01-refuerzo-python-algebra-lineal/taller-analitico-2-transformaciones.md"
git commit -m "Sesion 1: taller analitico 2 - transformaciones"

git add "sesion-01-refuerzo-python-algebra-lineal/taller-laboratorio-1-transformaciones-afines.py"
git commit -m "Sesion 1: taller laboratorio 1 - transformaciones afines"

git add "sesion-01-refuerzo-python-algebra-lineal/taller-laboratorio-final-kernel.py"
git commit -m "Sesion 1: taller laboratorio final - kernel de convolucion"

Remove-Item Env:\GIT_AUTHOR_DATE -ErrorAction SilentlyContinue
Remove-Item Env:\GIT_COMMITTER_DATE -ErrorAction SilentlyContinue

git add README.md requirements.txt .gitignore
git commit -m "docs: README principal del repositorio de talleres"

Write-Host ""
Write-Host "Listo. Revisa el historial con: git log --oneline"
Write-Host ""
Write-Host "Para subirlo a GitHub:"
Write-Host "  - Si el repo remoto esta vacio:        git push -u origin main"
Write-Host "  - Si el remoto ya tiene commits/archivos que quieres conservar:"
Write-Host "      git pull origin main --allow-unrelated-histories"
Write-Host "      (resuelve conflictos si aparecen, luego) git push -u origin main"
