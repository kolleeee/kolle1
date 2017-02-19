<?php
include("qqwry.php");  //调用IP纯真数据库
@$ip=$_GET["ip"];     //http://127.0.0.1:8888/IISIP.php?ip=127.0.0.1
$wl = convertip($ip);  //返回物理位置

echo $wl; 


?>