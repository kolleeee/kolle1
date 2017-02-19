
document.write('<script type="text/javascript" src="http://bbs.t56.net/static/js/yanue.pop.js"></script>');
	  jq(document).ready(function(){
			var pop=new Pop("",
			"",
			"<a href=\"http://bbs.t56.net/ad/2013/xierdun\" target=\"_blank\"><img src=\"http://bbs.t56.net/ad/2013/xierdun.gif\"/></a>");
		});		
document.write('<div id="pop">');
document.write('<style type="text/css">');
document.write('*{margin:0;padding:0;}');
document.write('#pop{background:#fff;width:300px;font-size:12px;position: fixed;right:0px;bottom:0px;}');
document.write('#popHead{line-height:32px;background:#f6f0f3;border-bottom:1px solid #e0e0e0;position:relative;font-size:12px;padding:0 0 0 10px;}');
document.write('#popHead #popClose{position:absolute;right:10px;top:1px;color:#ccc;}');
document.write('#popHead a#popClose:hover{color:#fff;cursor:pointer; font-weight:600;}');
document.write('#popIntro{margin:0;color:#666;width:300px;height:255px;overflow:hidden;}');
document.write('</style>');
document.write('<div id="popHead">');
document.write('<a id="popClose" title="关闭">关闭</a>');
document.write('</div>');
document.write('<div id="popContent">');
document.write('<div id="popIntro"></div>');
document.write('</div>');
document.write('</div>');
