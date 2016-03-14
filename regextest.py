#regex test

import re

line ="""<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
   <head>
      <title>DotA [void] - Game Overview</title>
      <link rel="stylesheet" type="text/css" href="/stylesheets/void.css" />
      <meta http-equiv="Content-Type" content="text/html;charset=utf-8" />
      <style type="text/css">
         div.progress {
            margin-left: 0px;
            margin-top: 3px;
            height: 3px;
            display: inline-block;
         }
      </style>
      <script type="text/javascript">

  var _gaq = _gaq || [];
  _gaq.push(['_setAccount', 'UA-27864161-1']);
  _gaq.push(['_setDomainName', 'dota-void.com']);
  _gaq.push(['_trackPageview']);

  (function() {
    var ga = document.createElement('script'); ga.type = 'text/javascript'; ga.async = true;
    ga.src = ('https:' == document.location.protocol ? 'https://ssl' : 'http://www') + '.google-analytics.com/ga.js';
    var s = document.getElementsByTagName('script')[0]; s.parentNode.insertBefore(ga, s);
  })();

</script>
   </head>
   <body>
      <div id="divHeader" class="header"><h1><a class="plain" href="/main.php"><span class="lightvoid">DotA</span> <span class="darkvoid">[</span><span class="void">void</span><span class="darkvoid">]</span></a></h1><table><tr><td><a class="plain" href="/main.php">News</a> <span class="darkvoid">|</span> <a class="plain" href="/stats.php">Stats</a> <span class="darkvoid">|</span> <a class="plain" href="/playerLookup.php">Players</a> <span class="darkvoid">|</span> <a class="plain" href="/currentGames.php">Games</a> <span class="darkvoid">|</span> <a class="plain" href="/forum/index.php">Forum</a> <span class="darkvoid">|</span> <a class="plain" href="/contact.php">Contact</a></td></tr></table></div><div class="middle">
<h3>DotA apem [void] #11145</h3>
<p>Date: Mar 11, 2016 - 14:15</p>
<p>Winner: <span class="text_sentinel">Sentinel (by forfeit)</span> <span class="text_sentinel">29</span>-<span class="text_scourge">26</span></p>
<p>Length: 48:06</p>
<p>Replay Command<span class="text_explain"><a class="plain" href="http://www.dota-void.com/forum/index.php/topic,3779.msg25736.html#msg25736">[?]</a></span>: !replay 740613</p><table><tr><th>Hero</th><th>Player</th><th>Score</th><th>Hero K|D|A</th><th>Creep K|D|N</th><th>Left At</th><th>Final Items</th></tr>
<tr><th colspan="7"><span class="text_sentinel">Sentinel</span></th></tr><tr><td style="border-radius: 4px; border: 3px solid rgb(0,66,255)"><a href="/hero.php?heroid=H071"><img src="/images/heroes/H071.gif" alt="Hero Thumbnail" width="48" height="48"></img></a></td>
<td><a href="/player.php?playername=ALPERENLER&amp;realm=r">ALPERENLER</a></td>
<td><span class="text_negative">-1.664</span></td>
<td>1|10|4</td><td>40|0|25</td>
<td><span class="text_leaver" style="font-size: .75em;">40:41 (86%)</span><br><div class="progress" style="width: 86%; background-color: #40be40;"></div><div class="progress" style="width: 13%; background-color: #404040;"></div></td>
<td><img width="24" height="24" src="/images/items/empty.gif"></img><img width="24" height="24" src="/images/items/empty.gif"></img><img width="24" height="24" src="/images/items/empty.gif"></img><br /><img width="24" height="24" src="/images/items/empty.gif"></img><img width="24" height="24" src="/images/items/empty.gif"></img><img width="24" height="24" src="/images/items/empty.gif"></img></td>
</tr>
<tr><td style="border-radius: 4px; border: 3px solid rgb(28,230,185)"><a href="/hero.php?heroid=N0EG"><img src="/images/heroes/N0EG.gif" alt="Hero Thumbnail" width="48" height="48"></img></a></td>
<td><a href="/player.php?playername=Navi.Korean&amp;realm=e">Navi.Korean</a></td>
<td><span class="text_positive">+2.275</span></td>
<td>16|3|10</td><td>164|0|14</td>
<td><span style="font-size: .75em;">47:27 (100%)</span><br><div class="progress" style="width: 100%; background-color: #00ff40;"></div><div class="progress" style="width: 0%; background-color: #404040;"></div></td>
<td><img width="24" height="24" src="/images/items/empty.gif"></img><img width="24" height="24" src="/images/items/empty.gif"></img><img width="24" height="24" src="/images/items/empty.gif"></img><br /><img width="24" height="24" src="/images/items/empty.gif"></img><img width="24" height="24" src="/images/items/empty.gif"></img><img width="24" height="24" src="/images/items/empty.gif"></img></td>
</tr>
<tr><td style="border-radius: 4px; border: 3px solid rgb(84,0,129)"><a href="/hero.php?heroid=HMKG"><img src="/images/heroes/HMKG.gif" alt="Hero Thumbnail" width="48" height="48"></img></a></td>
<td><a href="/player.php?playername=Nydar&amp;realm=r">Nydar</a></td>
<td><span class="text_positive">+0.566</span></td>
<td>2|4|16</td><td>77|0|3</td>
<td><span style="font-size: .75em;">47:30 (100%)</span><br><div class="progress" style="width: 100%; background-color: #00ff40;"></div><div class="progress" style="width: 0%; background-color: #404040;"></div></td>
<td><img width="24" height="24" src="/images/items/empty.gif"></img><img width="24" height="24" src="/images/items/empty.gif"></img><img width="24" height="24" src="/images/items/empty.gif"></img><br /><img width="24" height="24" src="/images/items/empty.gif"></img><img width="24" height="24" src="/images/items/empty.gif"></img><img width="24" height="24" src="/images/items/empty.gif"></img></td>
</tr>
<tr><td style="border-radius: 4px; border: 3px solid rgb(255,252,1)"><a href="/hero.php?heroid=HARF"><img src="/images/heroes/HARF.gif" alt="Hero Thumbnail" width="48" height="48"></img></a></td>
<td><a href="/player.php?playername=moto2709&amp;realm=r">moto2709</a></td>
<td><span class="text_negative">-0.255</span></td>
<td>1|5|10</td><td>82|0|20</td>
<td><span style="font-size: .75em;">48:06 (100%)</span><br><div class="progress" style="width: 100%; background-color: #00ff40;"></div><div class="progress" style="width: 0%; background-color: #404040;"></div></td>
<td><img width="24" height="24" src="/images/items/empty.gif"></img><img width="24" height="24" src="/images/items/empty.gif"></img><img width="24" height="24" src="/images/items/empty.gif"></img><br /><img width="24" height="24" src="/images/items/empty.gif"></img><img width="24" height="24" src="/images/items/empty.gif"></img><img width="24" height="24" src="/images/items/empty.gif"></img></td>
</tr>
<tr><td style="border-radius: 4px; border: 3px solid rgb(254,138,14)"><a href="/hero.php?heroid=NC00"><img src="/images/heroes/NC00.gif" alt="Hero Thumbnail" width="48" height="48"></img></a></td>
<td><a href="/player.php?playername=LosPantalones&amp;realm=r">LosPantalones</a></td>
<td><span class="text_positive">+0.862</span></td>
<td>9|4|8</td><td>121|0|19</td>
<td><span style="font-size: .75em;">47:33 (100%)</span><br><div class="progress" style="width: 100%; background-color: #00ff40;"></div><div class="progress" style="width: 0%; background-color: #404040;"></div></td>
<td><img width="24" height="24" src="/images/items/empty.gif"></img><img width="24" height="24" src="/images/items/empty.gif"></img><img width="24" height="24" src="/images/items/empty.gif"></img><br /><img width="24" height="24" src="/images/items/empty.gif"></img><img width="24" height="24" src="/images/items/empty.gif"></img><img width="24" height="24" src="/images/items/empty.gif"></img></td>
</tr>
<tr><th colspan="7"><span class="text_scourge">Scourge</span></th></tr><tr><td style="border-radius: 4px; border: 3px solid rgb(229,91,176)"><a href="/hero.php?heroid=UC91"><img src="/images/heroes/UC91.gif" alt="Hero Thumbnail" width="48" height="48"></img></a></td>
<td><a href="/player.php?playername=Mommy&amp;realm=r">Mommy</a></td>
<td><span class="text_negative">-0.431</span></td>
<td>6|10|8</td><td>81|0|38</td>
<td><span style="font-size: .75em;">47:53 (100%)</span><br><div class="progress" style="width: 100%; background-color: #00ff40;"></div><div class="progress" style="width: 0%; background-color: #404040;"></div></td>
<td><img width="24" height="24" src="/images/items/empty.gif"></img><img width="24" height="24" src="/images/items/empty.gif"></img><img width="24" height="24" src="/images/items/empty.gif"></img><br /><img width="24" height="24" src="/images/items/empty.gif"></img><img width="24" height="24" src="/images/items/empty.gif"></img><img width="24" height="24" src="/images/items/empty.gif"></img></td>
</tr>
<tr><td style="border-radius: 4px; border: 3px solid rgb(149,150,151)"><a href="/hero.php?heroid=O00J"><img src="/images/heroes/O00J.gif" alt="Hero Thumbnail" width="48" height="48"></img></a></td>
<td><a href="/player.php?playername=DeadLockeD&amp;realm=r">DeadLockeD</a></td>
<td><span class="text_negative">-0.476</span></td>
<td>5|10|7</td><td>117|0|15</td>
<td><span style="font-size: .75em;">47:26 (100%)</span><br><div class="progress" style="width: 100%; background-color: #00ff40;"></div><div class="progress" style="width: 0%; background-color: #404040;"></div></td>
<td><img width="24" height="24" src="/images/items/empty.gif"></img><img width="24" height="24" src="/images/items/empty.gif"></img><img width="24" height="24" src="/images/items/empty.gif"></img><br /><img width="24" height="24" src="/images/items/empty.gif"></img><img width="24" height="24" src="/images/items/empty.gif"></img><img width="24" height="24" src="/images/items/empty.gif"></img></td>
</tr>
<tr><td style="border-radius: 4px; border: 3px solid rgb(126,191,241)"><a href="/hero.php?heroid=H00U"><img src="/images/heroes/H00U.gif" alt="Hero Thumbnail" width="48" height="48"></img></a></td>
<td><a href="/player.php?playername=dqwe&amp;realm=e">dqwe</a></td>
<td><span class="text_negative">-0.150</span></td>
<td>4|5|7</td><td>88|0|20</td>
<td><span class="text_leaver" style="font-size: .75em;">42:17 (89%)</span><br><div class="progress" style="width: 89%; background-color: #31cd40;"></div><div class="progress" style="width: 10%; background-color: #404040;"></div></td>
<td><img width="24" height="24" src="/images/items/BTNTransmute.gif"></img><img width="24" height="24" src="/images/items/BTNBootsOfSpeed.gif"></img><img width="24" height="24" src="/images/items/BTNOrbOfFire.gif"></img><br /><img width="24" height="24" src="/images/items/BTNGem_Borrowed.gif"></img><img width="24" height="24" src="/images/items/BTNOrbofSlowness.gif"></img><img width="24" height="24" src="/images/items/empty.gif"></img></td>
</tr>
<tr><td style="border-radius: 4px; border: 3px solid rgb(16,98,70)"><a href="/hero.php?heroid=USYL"><img src="/images/heroes/USYL.gif" alt="Hero Thumbnail" width="48" height="48"></img></a></td>
<td><a href="/player.php?playername=DrUnKeNcHicKeN&amp;realm=r">DrUnKeNcHicKeN</a></td>
<td><span class="text_negative">-0.030</span></td>
<td>5|4|4</td><td>123|0|12</td>
<td><span style="font-size: .75em;">47:29 (100%)</span><br><div class="progress" style="width: 100%; background-color: #00ff40;"></div><div class="progress" style="width: 0%; background-color: #404040;"></div></td>
<td><img width="24" height="24" src="/images/items/empty.gif"></img><img width="24" height="24" src="/images/items/empty.gif"></img><img width="24" height="24" src="/images/items/empty.gif"></img><br /><img width="24" height="24" src="/images/items/empty.gif"></img><img width="24" height="24" src="/images/items/empty.gif"></img><img width="24" height="24" src="/images/items/empty.gif"></img></td>
</tr>
<tr><td style="border-radius: 4px; border: 3px solid rgb(78,42,4)"><a href="/hero.php?heroid=H00K"><img src="/images/heroes/H00K.gif" alt="Hero Thumbnail" width="48" height="48"></img></a></td>
<td><a href="/player.php?playername=ofner&amp;realm=r">ofner</a></td>
<td><span class="text_negative">-0.698</span></td>
<td>6|8|4</td><td>60|0|2</td>
<td><span style="font-size: .75em;">47:30 (100%)</span><br><div class="progress" style="width: 100%; background-color: #00ff40;"></div><div class="progress" style="width: 0%; background-color: #404040;"></div></td>
<td><img width="24" height="24" src="/images/items/empty.gif"></img><img width="24" height="24" src="/images/items/empty.gif"></img><img width="24" height="24" src="/images/items/empty.gif"></img><br /><img width="24" height="24" src="/images/items/empty.gif"></img><img width="24" height="24" src="/images/items/empty.gif"></img><img width="24" height="24" src="/images/items/empty.gif"></img></td>
</tr>
</table>
      </div><div class="footer">Copyright &copy; [void] 2011-2015<br />
<br>[0.1 sec]</div>
   </body>
</html>

"""
l = re.findall('playername=([a-zA-Z\.\_\(\)\-]+)\&amp\;realm\=(\w)',line)

print(l)
