still broken, i did some manual search/replace but get

```
bash-3.2$ ./generate.sh
INFO[2017-10-27T07:34:18+02:00] generating file result_directory/client_utils.py
INFO[2017-10-27T07:34:18+02:00] generating file result_directory/api_service.py
INFO[2017-10-27T07:34:18+02:00] generating file result_directory/self.py
panic: interface conversion: interface {} is nil, not string

goroutine 1 [running]:
github.com/Jumpscale/go-raml/raml.newItems(0x13f5b80, 0xc4202b2c90, 0x13d7f40, 0xc42038e1a0, 0x0, 0x0)
	/Users/kristofdespiegeleer/go/src/github.com/Jumpscale/go-raml/raml/items.go:15 +0x1ba
github.com/Jumpscale/go-raml/raml.toProperty.func2(0xc4202b2c60, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, ...)
	/Users/kristofdespiegeleer/go/src/github.com/Jumpscale/go-raml/raml/types.go:239 +0x7ae
github.com/Jumpscale/go-raml/raml.toProperty(0xc420219a60, 0xd, 0x13f5b80, 0xc4202b2c60, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, ...)
	/Users/kristofdespiegeleer/go/src/github.com/Jumpscale/go-raml/raml/types.go:256 +0x149
github.com/Jumpscale/go-raml/raml.ToProperty(0xc420219a60, 0xd, 0x13f5b80, 0xc4202b2c60, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, ...)
	/Users/kristofdespiegeleer/go/src/github.com/Jumpscale/go-raml/raml/types.go:177 +0x98
github.com/Jumpscale/go-raml/codegen/python.getTypeProperties(0xc4202cd1e0, 0x1, 0x1, 0x0)
	/Users/kristofdespiegeleer/go/src/github.com/Jumpscale/go-raml/codegen/python/class.go:144 +0xed
github.com/Jumpscale/go-raml/codegen/python.newClass(0xc420242de0, 0x16, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, ...)
	/Users/kristofdespiegeleer/go/src/github.com/Jumpscale/go-raml/codegen/python/class.go:48 +0x4a4
github.com/Jumpscale/go-raml/codegen/python.newClassFromType(0xc420242de0, 0x16, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, ...)
	/Users/kristofdespiegeleer/go/src/github.com/Jumpscale/go-raml/codegen/python/class.go:156 +0xd5
github.com/Jumpscale/go-raml/codegen/python.generateAllClasses(0xc4200aa500, 0x7fff5fbffb17, 0x12, 0xc4201b3360, 0x18, 0xc4202ce060, 0x1469969, 0x8)
	/Users/kristofdespiegeleer/go/src/github.com/Jumpscale/go-raml/codegen/python/class.go:243 +0x448
github.com/Jumpscale/go-raml/codegen/python.Client.Generate(0xc4202e1a60, 0x12, 0xc4200aa500, 0xc4201b3360, 0x18, 0xc4202ce060, 0x1469969, 0x8, 0x1476546, 0x26, ...)
	/Users/kristofdespiegeleer/go/src/github.com/Jumpscale/go-raml/codegen/python/client.go:92 +0x203
github.com/Jumpscale/go-raml/codegen.GenerateClient(0xc4200aa500, 0x7fff5fbffb17, 0x12, 0x1468e05, 0x6, 0x7fff5fbffb0a, 0x6, 0x0, 0x0, 0x1469969, ...)
	/Users/kristofdespiegeleer/go/src/github.com/Jumpscale/go-raml/codegen/client.go:23 +0x14c
github.com/Jumpscale/go-raml/commands.(*ClientCommand).Execute(0x18393e0, 0xc4200ad7a0, 0x1468628)
	/Users/kristofdespiegeleer/go/src/github.com/Jumpscale/go-raml/commands/client.go:38 +0x210
main.main.func3(0xc4200ad7a0)
	/Users/kristofdespiegeleer/go/src/github.com/Jumpscale/go-raml/main.go:166 +0x2d
github.com/Jumpscale/go-raml/vendor/github.com/codegangsta/cli.Command.Run(0x1468e05, 0x6, 0x0, 0x0, 0x0, 0x0, 0x0, 0x14772ac, 0x28, 0x0, ...)
	/Users/kristofdespiegeleer/go/src/github.com/Jumpscale/go-raml/vendor/github.com/codegangsta/cli/command.go:137 +0x7f2
github.com/Jumpscale/go-raml/vendor/github.com/codegangsta/cli.(*App).Run(0xc4200ad560, 0xc420010080, 0x8, 0x8, 0x0, 0x0)
	/Users/kristofdespiegeleer/go/src/github.com/Jumpscale/go-raml/vendor/github.com/codegangsta/cli/app.go:176 +0x8c1
main.main()
	/Users/kristofdespiegeleer/go/src/github.com/Jumpscale/go-raml/main.go:256 +0x1792
```