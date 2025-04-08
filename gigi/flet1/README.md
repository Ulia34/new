git config --global http.proxy http://ID101:11625@223.254.253.4:80
git config --global https.proxy http://ID101:11625@223.254.253.4:80

git clone https://github.com/vlakondra/flet1.git
pip list

cd flet1
py -m vevn .venv
venv\Scripts\activate

py -m pip install  --proxy http://username:password@223.254.254.4:80 --upgrade pip          !!!

py -m pip install  --proxy http://username:password@223.254.254.4:80 -r requirements.txt    !!!

py -m pip install  --proxy http://username:password@223.254.254.4:80 --upgrade flet         !!!
pip list

git log

pyright (MS)

# Flet1 app

## Run the app

### uv

Run as a desktop app:

```
uv run flet run
```

Run as a web app:

```
uv run flet run --web
```

### Poetry

Install dependencies from `pyproject.toml`:

```
poetry install
```

Run as a desktop app:

```
poetry run flet run
```

Run as a web app:

```
poetry run flet run --web
```

For more details on running the app, refer to the [Getting Started Guide](https://flet.dev/docs/getting-started/).

## Build the app

### Android

```
flet build apk -v
```

For more details on building and signing `.apk` or `.aab`, refer to the [Android Packaging Guide](https://flet.dev/docs/publish/android/).

### iOS

```
flet build ipa -v
```

For more details on building and signing `.ipa`, refer to the [iOS Packaging Guide](https://flet.dev/docs/publish/ios/).

### macOS

```
flet build macos -v
```

For more details on building macOS package, refer to the [macOS Packaging Guide](https://flet.dev/docs/publish/macos/).

### Linux

```
flet build linux -v
```

For more details on building Linux package, refer to the [Linux Packaging Guide](https://flet.dev/docs/publish/linux/).

### Windows

```
flet build windows -v
```

For more details on building Windows package, refer to the [Windows Packaging Guide](https://flet.dev/docs/publish/windows/).