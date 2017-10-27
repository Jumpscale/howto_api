rm -rf result_directory
rm -f index.html
go-raml client --language python --dir ./result_directory --ramlfile zerotier_1file_converted_apimatic.raml
