<?php
/*
神龙 QQ：29295842
接收CMS识别信息 保存成文本数据
使用 Excel 中的 CSV 编辑文本
http://127.0.0.1:8888/cms/cms.php?url=www.1234.com&cms=dedecms&hand_url=/install/images/00.png&KEY_MD5=c5ee1709a853229d2c91d736eda10051
*/
ini_set("date.timezone","Asia/Chongqing");  //调整时间
$tim=date('Y-m-d H:i:s',time());
@$url=@$_GET["url"];  //URL地址
@$cms=@$_GET["cms"];  //CMS名称
@$hand_url=@$_GET["hand_url"]; //连接地址
@$KEY_MD5=@$_GET["KEY_MD5"];  //关键字或者MD5

function file_add($file_name,$file_data)  //写入txt文件
{
$fp=fopen($file_name.".txt","a+");
fputs($fp,$file_data);
fputs($fp,"\r\n");
fclose($fp);
}

if ($url!="")
{
	$data=$url."|".$cms."|".$hand_url."|".$KEY_MD5."|".$tim;
	echo $data;
	file_add($cms,$data);  //写入txt文件
}

?>