# rfkill-unblock
ubuntuで、自動的に機内モードになってwifi、bluetoothがブロックされる時があるため、ブロック解除するスクリプトを作成しました。

## 動作確認環境
ubuntu23.10  
python3.11.6

## 既知の問題
systemdにスクリプトを登録しても、スリープからの復帰後にブロックが解除されない

## rfkill-unblock.py
機内モードになってwifi、bluetoothがブロックされている時、rfkillコマンドでブロック解除する  

## インストール
cronにスクリプトを登録し、１分毎に実行  
systemdにスクリプトを登録し、スリープからの復帰後にスクリプトを実行
```
$sudo ./install.sh
```
## アンインストール
スクリプトを登録解除  
```
$sudo ./uninstall.py
```
