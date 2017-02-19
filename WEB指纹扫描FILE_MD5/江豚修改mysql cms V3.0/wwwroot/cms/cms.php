

<?php
    define ('DB_USER_O', 'root');
    define ('DB_PASSWORD_O', '111111');
    define ('DB_HOST_O', 'localhost');
    define ('DB_NAME_O', 'webxscan');
    $debug = 0 ;
    if( $debug )
        echo "Debug option is [on]<br>";
?>

<?php
    $domain = addslashes($_REQUEST['domain']);
    $cms = addslashes($_REQUEST['cms']);

    if( !$domain | strlen($domain) >= 100 ){
        echo "-10" ;
        exit(0) ;
    }
    if( !$cms | strlen($cms) >= 50){
        echo "-11" ;
        exit(0) ;
    }
 ?>


<?php
function &GetIP(){
    if(!empty($_SERVER["HTTP_CLIENT_IP"])){
        $cip = $_SERVER["HTTP_CLIENT_IP"];
    }
    elseif(!empty($_SERVER["HTTP_X_FORWARDED_FOR"])){
        $cip = $_SERVER["HTTP_X_FORWARDED_FOR"];
    }
    elseif(!empty($_SERVER["REMOTE_ADDR"])){
        $cip = $_SERVER["REMOTE_ADDR"];
    }
    else{
        $cip = "";
    }
    return $cip;
}

?>

<?php
    $remoteip = GetIP() ;
    if($debug)
        echo "domain=$domain, cms=$cms, remoteip=$remoteip<br>" ;

    $db_gather = mysql_connect (DB_HOST_O, DB_USER_O, DB_PASSWORD_O) OR die ('Could not connect to SQL!'.mysql_error());
    mysql_select_db (DB_NAME_O, $db_gather) OR die ('Could not select the database!');

    $sql = "insert into `cms` value('$domain','$cms','$remoteip',now());" ;
    if($debug)
        echo "sql=$sql<br>";
    $res = mysql_query($sql,$db_gather) ;
    mysql_close($db_gather) ;
    echo "ok";
?>


