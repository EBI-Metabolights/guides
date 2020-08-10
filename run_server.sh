#!/bin/bash
rm -r metabolights-editor/assets/guides/*
ln -s "$PWD"/I10n/ ./metabolights-editor/assets/guides/I10n
ln -s "$PWD"/media/ ./metabolights-editor/assets/guides/media
ln -s "$PWD"/mapping.json ./metabolights-editor/assets/guides/mapping.json
cd metabolights-editor/
php -S localhost:8080