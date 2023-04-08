#!/bin/bash
cd react
npm run build
cp build/index.html ../website/template/
cp -rf build/* ../website/static/
cd ..
