# coding: UTF-8
import json
import re
import urllib


def results(fields, original_query):
  twq = fields['~twitterquery']
  quotedquery = urllib.quote_plus(twq.encode('utf_8'))
  
  reptn = r".*(?=\s)"
  rechk = re.match(reptn , original_query)
  if rechk:
    searchtype = rechk.group()

  if searchtype.startswith("tw"):
    titlestr = u"'{0}'をTwitterで検索".format(twq)
    searchurl = "https://twitter.com/search?q={0}".format(quotedquery)
    useragent = "Mozilla/5.0 (Nintendo 3DS; U; ; ja) Version/1.7498.JP"
  elif searchtype.startswith("ytw"):
  	titlestr = u"'{0}'をYahoo!リアルタイム検索".format(twq)
  	searchurl = "http://realtime.search.yahoo.co.jp/search?p={0}".format(quotedquery)
  	useragent = "Mozilla/5.0 (iPhone; CPU iPhone OS 8_0 like Mac OS X) AppleWebKit/600.1.4 (KHTML, like Gecko) Version/8.0 Mobile/12A365 Safari/600.1.4P"
  elif searchtype.startswith("tvch"):
  	titlestr = u"{0}chのテレビ放送のツイート（東京）".format(twq)
  	searchurl = "http://realtime.search.yahoo.co.jp/search?lz=1&ei=UTF-8&rkf=1&ch={0}".format(quotedquery)
  	useragent = "Mozilla/5.0 (iPhone; CPU iPhone OS 8_0 like Mac OS X) AppleWebKit/600.1.4 (KHTML, like Gecko) Version/8.0 Mobile/12A365 Safari/600.1.4P"

  return {
  	"title": titlestr,
  	"run_args": [searchurl],
  	"html": (u"<script>"
		u"var url = '{0}';".format(searchurl)
		+ u"setTimeout(function(){window.location=url},800)"
		+ u"</script>"),
	"webview_user_agent": useragent,
	"webview_links_open_in_browser": True
  }

def run(link):
  import os
  os.system('open "{0}"'.format(link).encode('utf_8'))

