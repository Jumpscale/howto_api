mkdir -p out
api-spec-converter -f api_blueprint input.apib -t swagger_2 -c -d --syntax=yaml > out/api_swagger2.yaml
# api-spec-converter -f api_blueprint input.apib -t swagger_2 -c -d > out/api_swagger2.json
# api-spec-converter -f api_blueprint input.apib -t raml > out/api.raml