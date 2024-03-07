# rfkill-unblock
ubuntuで、自動的に機内モードになってwifi、bluetoothがブロックされる時があるため、ブロック解除するスクリプトを作成しました。

## 動作確認環境
ubuntu23.10  
python3.11.6

## rfkill-unblock.py
機内モードになってwifi、bluetoothがブロックされている時、rfkillコマンドでブロック解除する  
常駐し、10秒毎に処理を行う

## インストール
systemdにスクリプトをサービス登録  
```
$sudo ./install.sh
```
## アンインストール
systemdからスクリプトを登録解除  
```
$sudo ./uninstall.py
```
