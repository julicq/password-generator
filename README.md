# password-generator

- to create exe for Windows: 
`nuitka --onefile --follow-imports --enable-plugin=pyside6 --windows-disable-console --windows-icon-from-ico=ui\icons\app-icon.ico --remove-output -o password-generator.exe app.py`

- to create app for MacOS:
`python3 -m nuitka --onefile --follow-imports --enable-plugin=pyside6 --macos-create-app-bundle --remove-output -o password-generator.app app.py`
