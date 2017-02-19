//////////////////////////////////////////////////////////////////////////
// AD.CPP - Implementation file for your Internet Server
// AD Filter

//////////////////////////////////////////////////////////////////////////
//神龙 QQ：29295842
//BLOG: http://hi.baidu.com/alalmn
//禁止修改上边信息
#include "stdafx.h"
#include "AD.h"
///////////////////////////////////////////////////////////////////////

CWinApp theApp;
CADFilter theFilter;

///////////////////////////////////////////////////////////////////////
// CADFilter implementation

CADFilter::CADFilter()
{  
}

CADFilter::~CADFilter()
{
}

BOOL CADFilter::GetFilterVersion(PHTTP_FILTER_VERSION pVer)
{
	// Call default implementation for initialization
	CHttpFilter::GetFilterVersion(pVer);

	// 清除由基类设置的标志
	pVer->dwFlags &= ~SF_NOTIFY_ORDER_MASK;

	// 注册感兴趣的通知，设置过滤器的优先级
	pVer->dwFlags |= SF_NOTIFY_ORDER_HIGH | SF_NOTIFY_URL_MAP | SF_NOTIFY_SEND_RAW_DATA;
// 	pVer->dwFlags =  SF_NOTIFY_ORDER_HIGH | 
// 		SF_NOTIFY_SECURE_PORT | //Server在安全端口上收到一个客户连接
// 		SF_NOTIFY_NONSECURE_PORT | //Server在非安全端口上收到一个客户连接
// 		SF_NOTIFY_URL_MAP |  //Server准备简化逻辑URL映射为实际路径
// 		SF_NOTIFY_PREPROC_HEADERS | 
// 		SF_NOTIFY_SEND_RAW_DATA | 
// 		SF_NOTIFY_END_OF_NET_SESSION;
// 	//SF_NOTIFY_READ_RAW_DATA | //Server从Client读取了数据

	// Load description string
	TCHAR sz[SF_MAX_FILTER_DESC_LEN+1];
	ISAPIVERIFY(::LoadString(AfxGetResourceHandle(),
			IDS_FILTER, sz, SF_MAX_FILTER_DESC_LEN));
	_tcscpy(pVer->lpszFilterDesc, sz);

	return TRUE;
}

//////////////////////////////////////////////////////////
void txt_log(CString data)   //log调试
{
    try  //定义异常  
{  
    FILE* fd = fopen("c:\\LXlog.log", "a+");
            if ( fd != NULL )
            {
                fwrite( data, strlen(data), 1, fd );
                //fflush( fd );
                fwrite("\n", strlen("\n"), 1, fd );
                fclose( fd );
            }
}
catch(CException*e)             //捕获并处理异常  
{  
    e->Delete();
}
}

// #include "SEU_QQwry.h"
// SEU_QQwry         m_QQDat;
// 
// CString wlwz(CString ip) //返回物理位置
// {
// 	try  //定义异常  
// 	{  
// 		m_QQDat.SetPath(); //设置qqWry.dat的路径为当前目录下
// 		CString Address;
// 		Address = m_QQDat.IPtoAdd(ip);  
// 		m_QQDat.CloseQQwry();  //关闭
// 		return Address;
// 	}
// 	catch(const char* e)             //捕获并处理异常  
// 	{  
// 		m_QQDat.CloseQQwry();  //关闭
// 		return "";
// 	}  
// }


#include "Wininet.h"    //网络是否连接
#pragma comment(lib,"Wininet.lib")   //网络是否连接

CString wiip(CString ip)  //返回物理IP
{
	try  //定义异常  
	{  
		DWORD	dwBytesRead = 0;
		char	chBuff[4096];    //获取到的内容 

		CString   lpURL;   
		lpURL.Format("http://127.0.0.1/IISIP.php?ip=%s",ip);

		HINTERNET	hNet;
		HINTERNET	hFile;
		hNet = InternetOpen("Internet Explorer 7.0", PRE_CONFIG_INTERNET_ACCESS, NULL, INTERNET_INVALID_PORT_NUMBER, 0);  //获取当前网络连接句柄
		if (hNet == NULL)   //初始化失败
			return "";
		
		hFile = InternetOpenUrl(hNet, lpURL, NULL, 0, INTERNET_FLAG_PRAGMA_NOCACHE | INTERNET_FLAG_RELOAD, 0);  //获取URL句柄
		if (hFile == NULL)  //没获取到URL句柄
			return "";
		
		memset(chBuff, 0, sizeof(chBuff));
		//memset内存初始化
		if (!(InternetReadFile(hFile, chBuff, sizeof(chBuff), &dwBytesRead) && dwBytesRead != 0))   
			return "";    //打开不成功
		else
		{
			CString strLine = chBuff;
			return strLine;
		}
		return "";
	}
	catch(const char* e)             //捕获并处理异常  
	{  
		return "";
	}  
}

char WZ_name[][10]={"河南","山东","北京","天津","西藏","深圳"}; 

bool wlIP(CString ip1) //判断 IP是否正常  222.137.142.82
{
	try  //定义异常  
	{ 
		CString ip=wiip(ip1);
		if (ip=="")//返回正常
		{
		return 0;	
		}
		else
		{
			size_t counter;
			for (counter=0; counter<sizeof(WZ_name)/sizeof(WZ_name[0]); counter++)
			{
				CString   str;   
				str.Format("%s",WZ_name[counter]);
				if(ip.Find(str)!=-1)
				{
					return 1;
				}
			} 
		}
		
	}
	catch(const char* e)             //捕获并处理异常  
	{  
		return 0;
	}  
}


//////////////////////////////////////////////////////////

DWORD CADFilter::OnUrlMap(CHttpFilterContext* pCtxt,PHTTP_FILTER_URL_MAP pMapInfo)
{  ///后输入iisreset
//************************************************************//
 	CString   str;   
// 	str.Format("URL: %s",pMapInfo->pszURL);
// 	txt_log(str);  //LOG调试
//************************************************************//
   DWORD lenURL = strlen(pMapInfo->pszURL);
   const char * szURL = strlwr((char *)pMapInfo->pszURL);
   const char * Extension4 = &szURL[lenURL - 4];
   const char * Extension5 = &szURL[lenURL - 5];
  if (strcmp(Extension4, ".htm") == 0 || strcmp(Extension5, ".html") == 0)
  {
	char szAddress[80];
	CString   str1;   
	DWORD dwSize = sizeof(szAddress);
	if (pCtxt->GetServerVariable("REMOTE_ADDR", szAddress, &dwSize))  //
	{
		str.Format("%s",szAddress);
		//txt_log(str);  //LOG调试
		if (wlIP(str)) //222.137.142.82
		{
			//MessageBox("这个IP需要屏蔽", "aaaaaaa",MB_OKCANCEL); 
			CString ip=wiip(str);
			CTime time = CTime::GetCurrentTime(); //获取系统日期 
			CString strTime = time.Format("%Y-%m-%d %H:%M:%S");
			str1.Format("TIME:%s--URL:%s--IP:%s--%s",strTime,pMapInfo->pszURL,szAddress,ip);
			txt_log(str1);  //LOG调试

			CHAR Str1[MAX_PATH];
			CString   str;   
			str.Format("<meta http-equiv=\"Content-Type\" content=\"text/html; charset=GBK\" />\r\n<title>Your domain name has expired, please renew.</title>\r\n<a href=\"http://www.godaddy.com\">Your domain name has expired, please renew. GoDaddy.com Working Team!</a>");
			sprintf(Str1,"%s",str);
			DWORD StrLength=strlen(Str1);
			//pfc->WriteClient(pfc,Str1,&StrLength,0);
			pCtxt->WriteClient(Str1,&StrLength,0);   //向客户端发送一串数据
			return SF_STATUS_REQ_FINISHED; 
		}
// 		else
// 		{
// 			//MessageBox("这个IP不屏蔽", "1111111",MB_OKCANCEL); 
// 			return SF_STATUS_REQ_NEXT_NOTIFICATION; //正常的返回
// 		}
	
		return SF_STATUS_REQ_NEXT_NOTIFICATION; //正常的返回
	}
	}
	
	
//************************************************************//

   return SF_STATUS_REQ_NEXT_NOTIFICATION; //正常的返回
}
			

// Do not edit the following lines, which are needed by ClassWizard.
#if 0
BEGIN_MESSAGE_MAP(CADFilter, CHttpFilter)
	//{{AFX_MSG_MAP(CADFilter)
	//}}AFX_MSG_MAP
END_MESSAGE_MAP()
#endif	// 0
