# rfkill-unblock
ubuntuで、自動的に機内モードになってwifi、bluetoothがブロックされる時があるため、ブロック解除するスクリプトを作成しました。

## 動作確認環境
ubuntu23.10  
python3.11.6

## rfkill-unblock.py
機内モードになってwifi、bluetoothがブロックされている時、rfkillコマンドでブロック解除する  
常駐し、指定秒数毎に処理を行う  
引数：  
--interval_sec  ブロック状態をチェックする間隔秒。デフォルト=10

## インストール
systemdにスクリプトをサービス登録  
```
$sudo ./install.py
```
## アンインストール
systemdからスクリプトを登録解除  
```
$sudo ./uninstall.py
```
