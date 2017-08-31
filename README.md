# howto_howto

# blueprint

## generate html 

### snowboard

install on macosx
```
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

### aglio

make sure node has been installed
```
npm install -g aglio
```

start server which reloads
```
aglio -i input.apib -s
```
