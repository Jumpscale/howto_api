
# blueprint

- [specs](https://github.com/apiaryio/api-blueprint/blob/master/API%20Blueprint%20Specification.md)
- [tutorial](https://github.com/apiaryio/api-blueprint/blob/master/Advanced%20Tutorial.md)

## generic

see bash files in root of this dir, to show/install/generate ...

## generate html 


### aglio (recommended, nicer than snowboard)

https://github.com/danielgtaylor/aglio

make sure node has been installed
```
npm install -g aglio
```

start server which reloads
```
aglio -i input.apib -s
```
### snowboard

install on macosx
```
brew tap bukalapak/packages
brew install snowboard
```
install on others
```
wget https://github.com/bukalapak/snowboard/releases/download/${version}/snowboard-${version}.${os}-${arch}.tar.gz
tar -zxvf snowboard-${version}.${os}-${arch}.tar.gz
cp snowboard /usr/local/bin
```

example (in root of this repo)
```bash
snowboard html -i input.apib -s
```
will start webserver which reloads on changes on the spec file

## transform 

### online: transformer

https://apimatic.io/transformer

### local (only  works to swagger2 for now)
 
install
```
npm install -g api-spec-converter
```

- also online: https://lucybot-inc.github.io/api-spec-converter/

- REMARK: could not get it to work for raml

