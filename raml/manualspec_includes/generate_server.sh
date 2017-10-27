rm -rf py_server
set -ex
go-raml server --language python --dir ./py_server --ramlfile main.raml
pushd py_server
touch __init__.py
pip3 install -r requirements.txt
python3 app.py
popd