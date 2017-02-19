function _showVFlink() {
	if($('ft')){
		var viewPortHeight = parseInt(document.documentElement.clientHeight);
		var scrollHeight = parseInt(document.body.getBoundingClientRect().top);
		var basew = parseInt($('ft').clientWidth);
		var sw = $('t56_erweima').clientWidth;
		if (basew < 1000) {
			var left = parseInt(fetchOffset($('ft'))['left']);
			left = left < sw ? left * 2 - sw : left;
			$('t56_erweima').style.left = ( basew + left ) + 'px';
		} else {
			$('t56_erweima').style.left = 'auto';
			$('t56_erweima').style.right = 0;
		}

		if (BROWSER.ie && BROWSER.ie < 7) {
			$('t56_erweima').style.top = viewPortHeight - scrollHeight - 215 + 'px';
		}
		if (scrollHeight < -100) {
			$('t56_erweima').style.visibility = 'visible';
		} else {
			$('t56_erweima').style.visibility = 'hidden';
		}
	}
}
_attachEvent(window, 'scroll', function(){_showVFlink();});

$('t56_erweima').onmouseover=function(){
	$('t56_ewm').style.display = 'block';
	};
$('t56_erweima').onmouseout=function(){
	$('t56_ewm').style.display = 'none';
	};