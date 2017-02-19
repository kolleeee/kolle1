document.write('<ul class="clearfix">');
document.write('<li class="t56first"><script>showImage("http://bbs.t56.net/ad/2012/lidu.jpg","http://www.tzlidu.com/")</script></li>');
/*document.write('<li><script>showFlash("http://bbs.t56.net/ad/2012/fuyou628.swf")</script></li>');*/
document.write('<li><script>showImage("http://bbs.t56.net/ad/2013/renbao701.gif","http://www.epicc.com.cn/?cmpid=3seb2pz0AIXS02&utm_source=baidu&utm_medium=search%5Fpinpaizhuanqu&utm_term=%E6%A0%87%E9%A2%9824&utm_campaign=%E7%89%88%E6%9C%AC24&utm_adgroup=%E6%A0%87%E9%A2%98")</script></li>');
/*document.write('<li><script>showImage("http://bbs.t56.net/ad/2012/jiankang108.gif","http://bbs.t56.net/ad/2012/yiyuan108/")</script></li>');*/
document.write('<li><script>showImage("http://bbs.t56.net/ad/2013/dajuyuan528.gif","http://bbs.t56.net/forum-335-1.html")</script></li>');
document.write('<li><script>showImage("http://bbs.t56.net/ad/2013/boda.jpg","http://www.86566120.com/")</script></li>');
/*document.write('<li><script>showImage("http://bbs.t56.net/ad/2012/fuke61.jpg","http://www.tzhlfk.com/")</script></li>');*/
document.write('</ul>');
document.write('<ul class="clearfix">');
/*document.write('<li class="t56first"><script>showImage("http://bbs.t56.net/ad/2012/huochezhan61.gif","http://bbs.t56.net/ad/page2011/huochezhan/")</script></li>');*/
document.write('<li class="t56first"><script>showImage("http://bbs.t56.net/ad/2012/dadi1207.gif","http://www.95590.cn/")</script></li>');
document.write('<li><script>showImage("http://bbs.t56.net/ad/2012/qintian.gif","http://www.19750.cn")</script></li>');
document.write('<li><script>showImage("http://bbs.t56.net/ad/2013/mianhua.gif","http://www.sttzm.com")</script></li>');
document.write('<li><script>showImage("http://bbs.t56.net/ad/2013/jiaoyu626.jpg","http://bbs.t56.net/ad/2013/jiaoyu626/")</script></li>');
document.write('</ul>');


/*document.write('<li class="t56first"><script>showImage("http://bbs.t56.net/ad/2012/silu61.gif","http://www.ideasm.com/")</script></li>');*/


			

//JS Function
function showImage(imageurl,linkurl){
	if(linkurl!=''){
		document.write('<a href="'+linkurl+'" target="_blank"><img src="'+imageurl+'" border="0" width="242" height="70" /></a>');
	}else{
		document.write('<img src="'+imageurl+'" border="0" width="242" height="70" />');
	}
}

function showFlash(flashurl,width,height){
	if(!width || width=='') width='242';
	if(!height || height=='') height='70';
	document.write('<object classid="clsid:D27CDB6E-AE6D-11cf-96B8-444553540000" codebase="http://download.macromedia.com/pub/shockwave/cabs/flash/swflash.cab#version=6,0,29,0"');
	document.write('width="'+width+'" height="'+height+'">');
	document.write('<param value="false" name="menu"/><param value="opaque" name="wmode"/>');
	document.write('<param name="quality" value="high"> ');
	document.write('<param name="movie" value="'+flashurl+'">');
	document.write('<embed src="'+flashurl+'" quality="high"');
	document.write('pluginspage="http://www.macromedia.com/go/getflashplayer"');
	document.write(' type="application/x-shockwave-flash" width="'+width+'" height="'+height+'"></embed></object>');
}
