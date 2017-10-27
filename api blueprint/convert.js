var transformer = require('api-spec-transformer');
var fs = require('fs');

// Convert swagger to raml, from a url.

var swaggerToRaml = new transformer.Converter(transformer.Formats.SWAGGER, transformer.Formats.RAML10);

swaggerToRaml.loadFile('out/api_swagger2.yaml', function(err) {
  if (err) {
    console.log(err.stack);
    return;
  }

  swaggerToRaml.convert('yaml')
    .then(function(convertedData) {
      // convertedData is a raml YAML string
    //   console.log(convertedData)
      fs.writeFile("out/api_raml1.raml",convertedData, function(err) {
        if(err) {
            return console.log(err);
        }
      }  )  
    })
    .catch(function(err){
      console.log(err);
    });
});