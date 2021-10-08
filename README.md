# Alfred Quick Translation workflow
A translation workflow based on Google Translate.

This workflow will automatically detect the language of the input text, if the input text is Chinese, it will be translated into English, otherwise it will be translated into Chinese.

At the same time, this workflow also supports copying the original translation or translation result to the clipboard.

## Setup

There are two environments required in this workflow:

-   `key` is the API key of [Cloud Translation API](https://console.cloud.google.com/marketplace/product/google/translate.googleapis.com)
-   `python` is the python path to execute this workflow

To get a API Key: click the "CREATE CREDENTIALS" in [this page](https://console.cloud.google.com/apis/api/translate.googleapis.com/credentials), and select the `API key`. A new API key will appear below. Click the `Copy API Key` button, the API Key will be copied to the clipboard.

>   This workflow depends on the Cloud Translation API on GCP(Google Cloud Platform). It is assumed that you already have a GCP account, if you don’t have one, you can create one for free.

To get the Python path: open a terminal and run this command:

```shell
$ which python3
```

The Python path will be output to the console.

>   Please make sure the `requests` package has been installed in this python sites-packages. You can use this command to check:
>
>   ```shell
>   $ python3 -c "import requests"
>   ```

## Usage

### Translate (tr)

![translate](./imgs/translate.png)

Use Google Translate to translate the entered text.

**Keyword: tr**



### Copy the original text to Clipboard (⌥ + ⏎)

![source](./imgs/source.png)

Press ⌥ + ⏎ to copy the original text to the clipboard.



### Copy translation results to Clipboard (⌘ + ⏎)

![source](./imgs/target.png)

Press ⌘ + ⏎ to copy the translation result to the clipboard.



## License

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

