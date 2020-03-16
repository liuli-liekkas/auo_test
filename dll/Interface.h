#pragma once;  
using namespace std;
#ifdef DLL_IMPLEMENT
#define DLL_API __declspec(dllexport)  
#else  
#define DLL_API __declspec(dllimport)  
#endif  
//*******************************ɨ��ܱ�׼�ӿں���**************************************//
//����˵����
//iDevice=0
//nAxis = 1------X��
//nAxis = 2------Y��
//nAxis = 3------Z��
//nAxis = 4------P��
//pos----��������Ҫ�˶��ľ���ֵ����λΪmm
//vel----��������Ҫ�˶����ٶ�ֵ����λΪmm/s
//fToStart----��������Ҫ�˶��ľ���ֵ��λ��ֵ�ڷ���������ʼ��֮ǰ����λΪmm
//fToEnd----��������Ҫ�˶��ľ���ֵ��λ��ֵ�ڷ���������ʼ��֮ǰ����λΪmm
//fToSpeed----�����ᵽfToStartλ��ʱ���ٶȣ���λΪmm/s
//fStartEqu----�����ᷢ���������ʼλ��ֵ����λΪmm
//fEndEqu----�����ᷢ���������ֹλ��ֵ����λΪmm
//fStepPos----�����ᷢ������ļ��ֵ����λΪmm
//fSpeed----�����ᷢ�������˶������е��ٶ�ֵ����λΪmm/s
//fDeltaStep----Ĭ��Ϊ0
//iTime----Ĭ��Ϊ0

//���ӿ�����
extern "C" DLL_API BOOL ConnectImac(short iDevice);

//�Ͽ�����
extern "C" DLL_API BOOL DisConnectImac(short iDevice);

//ֹͣ�˶�
extern "C" DLL_API BOOL Stop(short iDevice, short nAxis);

//Ѱ��
extern "C" DLL_API BOOL SHome(short iDevice, short nAxis) ;

//��������isAbsolute��ʾ�����˶�������˶�,����pos��ʾ�˶�����λ��
extern "C" DLL_API BOOL MoveDeviceToPos(short iDevice, short nAxis, double pos,double vel, bool isAbsolute = true);

//���������˶�
extern "C" DLL_API BOOL MoveToPosByType(short iDevice, short nAxis, double fToStart,double fToEnd,double fToSpeed,double fStartEqu, double fEndEqu, double fStepPos,  double fSpeed, double fDeltaStep = 0, int iTime = 0);

//����˶�״̬
//�Ƿ�ֹͣ��TRUE-ֹͣ��FALSE-�˶���
extern "C" DLL_API BOOL GetMotorIdle(short iDevice,short nAxis);

//�Ƿ�����λ��TRUE-����λ��FALSE-δ����λ��
extern "C" DLL_API BOOL GetPosLimit(short iDevice,short nAxis);

//�Ƿ���λ��TRUE-����λ��FALSE-δ����λ��
extern "C" DLL_API BOOL GetNegLimit(short iDevice,short nAxis);

//�Ƿ���λ��TRUE-Ѱ����ɣ�FALSE-Ѱ��δ��ɣ�
extern "C" DLL_API BOOL GetHomeComplete(short iDevice,short nAxis);


//��ȡ��ǰλ��
extern "C" DLL_API double  GetPos(short iDevice,short nAxis);

//��������
extern "C" DLL_API BOOL SinglePulse(short iDevice,short nAxis);

//��ȡ�������Ƿ���������
extern "C" DLL_API BOOL GetPmacPower(short iDevice);

extern "C" DLL_API BOOL SetAccTime(short iDevice,short nAxis,short nTime);

//*******************************ɨ��ܱ�׼�ӿں���**************************************//




