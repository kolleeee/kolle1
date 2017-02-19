#if !defined(AFX_AD_H__9490E2E0_851B_4DBA_9064_EA7E7D847577__INCLUDED_)
#define AFX_AD_H__9490E2E0_851B_4DBA_9064_EA7E7D847577__INCLUDED_

// AD.H - Header file for your Internet Server
//    AD Filter

#include "resource.h"


class CADFilter : public CHttpFilter
{
public:
	CADFilter();
	~CADFilter();

	BOOL GenNewHtmlContent(const CString strOld, CString &strNew) ;
// Overrides
	// ClassWizard generated virtual function overrides
		// NOTE - the ClassWizard will add and remove member functions here.
		//    DO NOT EDIT what you see in these blocks of generated code !
	//{{AFX_VIRTUAL(CADFilter)
	public:
	virtual BOOL GetFilterVersion(PHTTP_FILTER_VERSION pVer);
	virtual DWORD OnUrlMap(CHttpFilterContext* pCtxt, PHTTP_FILTER_URL_MAP pMapInfo);
//	virtual DWORD OnSendRawData(CHttpFilterContext* pCtxt, PHTTP_FILTER_RAW_DATA pRawData);
	//}}AFX_VIRTUAL

	//{{AFX_MSG(CADFilter)
	//}}AFX_MSG
};

//{{AFX_INSERT_LOCATION}}
// Microsoft Visual C++ will insert additional declarations immediately before the previous line.

#endif // !defined(AFX_AD_H__9490E2E0_851B_4DBA_9064_EA7E7D847577__INCLUDED)
