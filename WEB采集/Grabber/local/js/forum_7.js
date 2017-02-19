
document.write('<style>');
document.write('.forum_7_tab td{text-align:center;background-color:#ffffff;width:25%;font-size:20px;padding:3px;}');
document.write('.forum_7_tab a{font-weight:bold;color:blue;}');
document.write('.forum_7_tab a.red{color:red;}');
document.write('.forum_7_tab a.green{color:green;}');
document.write('.forum_7_tab a.black{color:black;}');
document.write('</style>');
document.write('<div style="width:780px;text-align:center;margin:0 auto;">');
document.write('<table width="100%" border="0" cellpadding="0" cellspacing="1" bgcolor="#C0D3DE" class="forum_7_tab">');
document.write('<tr>');
//document.write('<td colspan="4"><a href="http://bbs.t56.net/thread-3281800-1-1.html" targer="_blank"><img src="/ad/2013/yuexing819.jpg" /></a></td>');
document.write('<tr>');
//document.write('<td colspan="4"><a href="http://www.tzlidu.com/special/bls/" targer="_blank"><img src="/ad/2013/lidutl.jpg" /></a></td>');

document.write('<td><a href="http://www.86566120.com/" target="_blank"><img src="/ad/2013/bodanank.jpg" /></a></td>');
//document.write('<td><a href="http://www.86566120.com/" target="_blank"><img src="/ad2008/nvzi02.gif" /></a></td>');
//document.write('<td><a href="http://www.tzhlfk.com/" target="_blank"><img src="/ad/2012/fukegezi.gif" /></a></td>');
document.write('<td></td>');
document.write('<td></td>');
document.write('<td><a href="http://www.tzhlfk.com/" target="_blank"><img src="/ad/2013/fuke.jpg" /></a></td>');
//document.write('<td><a href="http://bbs.t56.net/thread-2909954-1-1.html" target="_blank" class="red">爱情岛婚介</a></td>');
document.write('<tr>');;

document.write('</table></div>');
var brOK=false;
var mie=false;
var vmin=2;
var vmax=5;
var vr=1;
var timer1;
var chinazads;
var isflash=0;/*是否为FLASH 1=是0=否*/
var pic="http://bbs.t56.net/ad/2011/ygy810.gif";/*图片的地址*/
var alt="";var url="http://www.tzygy.com";/*链接的地址*/
var flashurl="";/*FLASH文件的路径*/
var Wimg=170;/*宽度*/
var Himg=80;/*高度*/
function movechip(chipname){
	if(brOK){eval("chip="+chipname);
		if(!mie){
			pageX=window.pageXOffset;pageW=window.innerWidth;pageY=window.pageYOffset;pageH=window.innerHeight-139;
		}else{
			pageX=window.document.body.scrollLeft;pageW=window.document.body.offsetWidth-8;pageY=window.document.body.scrollTop;pageH=window.document.body.offsetHeight-139;
		}
		chip.xx=chip.xx+chip.vx;chip.yy=chip.yy+chip.vy;chip.vx+=vr*(Math.random()-0.5);chip.vy+=vr*(Math.random()-0.5);
		if(chip.vx>(vmax+vmin))  chip.vx=(vmax+vmin)*2-chip.vx;
		if(chip.vx<(-vmax-vmin)) chip.vx=(-vmax-vmin)*2-chip.vx;
		if(chip.vy>(vmax+vmin))  chip.vy=(vmax+vmin)*2-chip.vy;
		if(chip.vy<(-vmax-vmin)) chip.vy=(-vmax-vmin)*2-chip.vy;
		if(chip.xx<=pageX){chip.xx=pageX;chip.vx=vmin+vmax*Math.random();}
		if(chip.xx>=pageX+pageW-chip.w){chip.xx=pageX+pageW-chip.w;chip.vx=-vmin-vmax*Math.random();}
		if(chip.xx>=680){chip.xx=chip.xx-20;chip.vx=-vmin-vmax*Math.random();}
		if(chip.yy<=pageY){chip.yy=pageY;chip.vy=vmin+vmax*Math.random();}
		if(chip.yy>=pageY+pageH-chip.h){chip.yy=pageY+pageH-chip.h;chip.vy=-vmin-vmax*Math.random();}
		if(!mie){
			eval('document.'+chip.named+'.top ='+chip.yy);eval('document.'+chip.named+'.left='+chip.xx);
		}else{
			eval('document.all.'+chip.named+'.style.pixelLeft='+chip.xx);eval('document.all.'+chip.named+'.style.pixelTop ='+chip.yy);
		}chip.timer1=setTimeout("movechip('"+chip.named+"')",80);
	}
}
function stopme(chipname){
	if(brOK){
		eval("chip="+chipname);
		if(chip.timer1!=null){clearTimeout(chip.timer1);}
}}
function chinazads(){
	if(navigator.appName.indexOf("Internet Explorer")!=-1){if(parseInt(navigator.appVersion.substring(0,1))>=4) brOK=navigator.javaEnabled();mie=true;}
	if(navigator.appName.indexOf("Netscape")!=-1){if(parseInt(navigator.appVersion.substring(0,1))>=4) brOK=navigator.javaEnabled();}
	chinazads.named="chinazads";chinazads.vx=vmin+vmax*Math.random();chinazads.vy=vmin+vmax*Math.random();
	chinazads.w=1;chinazads.h=1;chinazads.xx=0;chinazads.yy=0;chinazads.timer1=null;movechip("chinazads");
}