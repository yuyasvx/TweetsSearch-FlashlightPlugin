# TweetsSearch-FlashlightPlugin

OS X YosemiteのSpotlight検索を拡張する[“Flashlight”](http://flashlight.nateparrott.com)向けのバンドル。出来上がりが雑なのでこっそりここで公開。

## 概要

ツイート検索するだけでしょ？と思った方。たしかにそれだけです。

が、Twitter公式の検索の性能って微妙だったりしませんか？例えば表記ゆれを考慮した検索をしてくれない等。

このプラグインはTwitter公式だけでなく、**Yahoo!リアルタイム検索**でのツイート検索も可能になっています。Yahoo!のツイート検索は、表記ゆれなどをある程度考慮した検索をしてくれるので、Twitter公式の検索とは得られるものが違ったりします。また、テレビ放送に関するツイートもYahoo!リアルタイム検索であれば簡単に調べられます。

## ダウンロードとインストール

ダウンロードは[こちら](https://github.com/yuyasvx/TweetsSearch-FlashlightPlugin/archive/master.zip)からどうぞ。

###インストール

ダウンロードしたZipを解凍して出てくる“tweets-search.bundle” を “~/Library/FlashlightPlugins/”にぶっこめばおしまいです。

## 使い方

**Twitter公式で検索する：**Spotlightに“tw *検索ワード*”と入力  
**Yahoo!リアルタイム検索：**Spotlightに“ytw *検索ワード*”と入力  
**Yahoo!リアルタイム検索でテレビ放送に関するツイートを調べる：**Spotlightに“tvch *チャンネル番号（東京のみ）*”と入力

### 例

**“ytw MacBook”**・・・Yahoo!リアルタイム検索で“MacBook”を検索  
**“tw りんご”**・・・Twitter公式で“りんご”を検索  
**“tvch 5”**・・・テレビ朝日の放送に関するツイートをYahoo!リアルタイム検索する

![スクリーンショット](https://raw.githubusercontent.com/yuyasvx/TweetsSearch-FlashlightPlugin/master/content/Screenshot.png)