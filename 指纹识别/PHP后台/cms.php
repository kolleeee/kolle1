<?php  //添加数据
include("conn.php");
$tim=date('Y-m-d H:i:s',time());
$psotip=$_SERVER["REMOTE_ADDR"];   #获取提交服务器的IP
//http://xxxx.com/ftppassword.php?IP=www.baidu.com&user=1111&password=2222&root=2
//http://www.999kankan.com/cms.php?url=baidu.com&cms=33333


$sql="insert into cms(url,cms,postIP,time) VALUES('$_REQUEST[url]','$_REQUEST[cms]','$psotip','$tim')";
//print $sql;
mysql_query($sql)or die("添加数据错误!!!33333333");
print "添加数据成功！！333";

?>


