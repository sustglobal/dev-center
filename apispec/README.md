# Generating the HTML

Run a node container
```bash
docker run -v $(pwd):/home -it node bash
```

Generate the HTML (hit `y` to proceed when prompted)
```bash
cd /home/compose
npx @redocly/cli build-docs /home/compose/compositions_api.yaml
```

There should be a file called `redoc-static.html` in your compose folder. Rename it to `index.html`.

Copy `index.html` into ./docs/compose.