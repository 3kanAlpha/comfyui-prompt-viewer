# ComfyUI Prompt Viewer
自分のワークフローでしか動作確認してないので、各自改造してください…

## Requirements
- pypng

## Usage
```bash
$ pip install -r requirements.txt
$ python extractor.py <path to generated image file>
```

## How it works
ComfyUIで生成された画像ファイルには、生成時に使用したワークフローの情報が埋め込まれている。  
ファイルの先頭にあるIHDRチャンクの直後にtEXtチャンクとしてプロンプトとワークフローの情報が埋め込まれているので、そこからワークフローの情報を取得する。
