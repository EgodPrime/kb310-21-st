#include <iostream>
using namespace std;
#define  MAXSIZE  100          						//˳������󳤶�
typedef struct
{
	int key;//�ؼ�����
	char* otherinfo;//����������
}ElemType;//��¼����
//˳���Ĵ洢�ṹ  
typedef struct
{
	ElemType* r;	         						//�洢�ռ�Ļ���ַ
	int  length;            						//˳�����
}SqList;											//˳�������

int a=0,b=0;//������¼ð��������ƶ��ͽ�������											
void BubbleSort(SqList L)
{//��˳���L��ð���������Ƚ���һ����¼�Ĺؼ��ֺ͵ڶ�����¼�Ĺؼ��ֽ��бȽϣ���Ϊ�����򽻻����������ƣ�ֱ����n-1����¼�͵�n����¼�Ĺؼ��ֽ��й��Ƚ�Ϊֹ��
 //�������̳�Ϊ��һ��ð������ÿһ�������ظ�����������ֱ����ĳһ�˹�����û�н��й�������¼�Ĳ�����˵��������ȫ���ﵽ����Ҫ��
	int m, j, flag;
	ElemType t;
	m = L.length - 1; flag = 1; 				//flag�������ĳһ�������Ƿ�������
	while ((m > 0) && (flag == 1))
	{
		flag = 0;           				//flag��Ϊ0�������������û�з����������򲻻�ִ����һ������
		for (j = 1; j <= m; j++)
		{
			
			if (L.r[j].key > L.r[j + 1].key)
			{
				a++;//ð������Ƚϴ���
				flag = 1;					//flag��Ϊ1����ʾ�����������˽���
				t = L.r[j]; L.r[j] = L.r[j + 1]; L.r[j + 1] = t;	//����ǰ��������¼
				b=b+3;//ð�������ƶ�����
			}
		}				//if
		--m;
	}									//while
}										//BubbleSort


int h = 0, g = 0;//��¼�鲢����ıȽϺ��ƶ�����
//��������������ͬһ���������ڵ�λ���ϣ�r[low...mid]��r[mid...high],ÿ�ηֱ����������ȡ��һ����¼���бȽϣ�����С�߷���r1[low...high]��
//�ظ��˹��̣�ֱ��һ����Ϊ�գ������һ�ǿձ������µĲ���ֱ�Ӹ��Ƶ�r1��
void Merge(ElemType r[], ElemType r1[], int low, int mid, int high)
{//�鲢���򣬽������r[low...mid]��r[mid...high]�鲢Ϊ�����r1[low...high]
	int i = low, j = mid + 1, k = low;
	while (i != mid + 1 && j != high + 1)
	{
		if (r[i].key > r[j].key)
		{
			r1[k++] = r[j++]; 
			g++; //�ƶ��Ĵ���
			h++;//�鲢��������ȽϵĴ���
		}
		else
		{
			r1[k++] = r[i++];
			g++; 
			h++;
		}
	}
	while (i != mid + 1)
	{
		r1[k++] = r[i++];//��ʣ���r[low...mid]���Ƶ�r1��
		g++;
	}
	while (j != high + 1)
	{
		r1[k++] = r[j++]; //��ʣ���r[j.high]���Ƶ�r1��
		g++;
	}
	for (i = low; i <= high; i++)
	{
		r[i] = r1[i];
	}
}

void MergeSort(ElemType r[], ElemType r1[], int low, int high) 
{//r[low...high]�ݹ���������r1[low...high]��
	int m;
	if (low < high) 
	{
		//h++;//�鲢����Ƚϴ���
		m = low + (high - low) / 2;//����ǰ����һ��Ϊ����������ѵ�mid
		MergeSort(r, r1, low, m);//��������r[low...mid]�ݹ�鲢�����򣬽������r1[low...mid]
		MergeSort(r, r1, m + 1, high);//��������r[mid+1...high]�ݹ�鲢�����򣬽������r1[mid+1...high]
		Merge(r, r1, low, m, high); // ��������r[low...mid]��r[mid+1...high]�鲢��r1[low...high]
	}
}

void MSort(SqList& L)
{//��˳���L���鲢����
	MergeSort(L.r,L.r,1,L.length);
}

//���������ļ�¼���������r[1...n]�У�r[1]��һ���������У���ѭ��n-1�Σ�ÿ��ʹ���۰���ҷ���
//����r[i]�����ź��������r[1...i-1]�еĲ���λ�ã�Ȼ��r[i]�����Ϊi-1����������r[1...i-1]��ֱ����r[n]�����Ϊn-1����������r[1...n-1]�����õ�һ����Ϊn���������С�
int c = 0, d = 0;
void B_InsertSort(SqList L)
{//��˳���L���۰��������
	int i = 0, j = 0;
	int low = 1, mid = 1, high = 1;
	for (i = 2; i <= L.length; ++i)
	{
		low = 1; high = i - 1;//�ò��������ֵ
		L.r[0] = L.r[i];//��������ļ�¼�ݴ浽��������
		d = d + 1;
		while (low <= high)//��r[low...high]���۰���Ҳ����λ��
		{
			mid = (low + high) / 2;//�۰�
			c++;//�۰��������ȽϵĴ���
			if (L.r[mid].key > L.r[0].key)
			{
				high = mid - 1; //�������ǰһ�ӱ�
			}
			else
			{
				low = mid + 1;// ������ں�һ�ӱ�
			}
		}
		for (j = i - 1; j >= high + 1; --j)
		{
			L.r[j + 1] = L.r[j];//��¼����
			++d;//�۰���������ƶ��Ĵ���
		}
		L.r[high + 1] = L.r[0];//��r[0]��ԭr[i]�����뵽��ȷλ��
		d = d + 1;
	}
}

int e = 0, f = 0;
int Partition(SqList L, int low, int high)
{//��˳���L�е��ӱ�r[low..high]����һ�����򣬷�������λ��
	int pivotkey;
	L.r[0] = L.r[low];                    	//���ӱ�ĵ�һ����¼�������¼
	pivotkey = L.r[low].key;		   	    //�����¼�ؼ��ֱ�����pivotkey��
	while (low < high)                      //�ӱ�����˽�������м�ɨ��
	{	
		while (low < high && L.r[high].key >= pivotkey)
		{
			--high; e++;
		}
		L.r[low] = L.r[high];	f = f + 1;				//���������¼С�ļ�¼�Ƶ��Ͷ�
		while (low < high && L.r[low].key <= pivotkey)
		{
			++low; e++;
		}
		L.r[high] = L.r[low];	f = f + 1;				//���������¼��ļ�¼�Ƶ��߶�
	}//while
	L.r[low] = L.r[0];						//�����¼��λ
	f = f + 1;
	return  low;							//��������λ��
}//Partition

void QSort(SqList L, int low, int high)
{	//����ǰ�ó�ֵ��low=1; high=L.length;
	//��˳���L�е�������L.r[low..high]����������
	int pivotloc;
	if (low < high)
	{	
		//���ȴ���1
		//e++;//��������ȽϵĴ���
		pivotloc = Partition(L, low, high); 		//��L.r[low..high]һ��Ϊ����pivotloc������λ��
		QSort(L, low, pivotloc - 1);				//�����ӱ�ݹ�����
		QSort(L, pivotloc + 1, high);        	//�����ӱ�ݹ�����
	}
}											//QSort

void QuickSort(SqList L)
{
	//��˳���L����������
	QSort(L, 1, L.length);
}
void Create_Sq(SqList& L)
{
	int i, n;
	cout << "���������ݸ�����������" << MAXSIZE << "����" << endl;
	cin >> n;											//�������
	cout << "����������������:\n";
	while (n > MAXSIZE)
	{
		cout << "�����������ޣ����ܳ���" << MAXSIZE << "������������" << endl;
		cin >> n;
	}
	for (i = 1; i <= n; i++)
	{
		cin >> L.r[i].key;
		L.length++;
	}
}

void show(SqList& L)
{
	int i;
	for (i = 1; i <= L.length; i++)
		printf("%d ", L.r[i].key);
		//cout <<  L.r[i].key ;
}

int main()
{
	int j;
	SqList L;
	L.r = new ElemType[MAXSIZE + 1];
	L.length = 0;
	Create_Sq(L);
	printf("                    ����                            \n");
	printf("********************************************************\n");
	printf("*                1-----ð������                        *\n");
	printf("*                2-----�۰����                        *\n");
	printf("*                3-----��������                        *\n");
	printf("*                4-----�鲢ѡ��                        *\n");
	printf("\n");
	while (1) {
		cout << "\n��ѡ��\n";
		cin >> j;
		switch (j)
		{
		case 1:BubbleSort(L);
			cout << "ð������" << endl;
			show(L);
			printf("\n");
			printf("ð������ȽϵĴ���Ϊ��%d\n",a);
			printf("ð�����򽻻��Ĵ���Ϊ��%d\n",b);
			break;
		case 2:B_InsertSort(L);
			cout << "�۰���룺" << endl;
			show(L);
			printf("\n");
			printf("�۰��������ȽϵĴ���Ϊ��%d\n", c);
			printf("�۰�����ƶ��Ĵ���Ϊ��%d\n", d);
			break;
		case 3:	QuickSort(L);
			cout << "��������" << endl;
			show(L);
			printf("\n");
			printf("��������ȽϵĴ���Ϊ��%d\n", e);
			printf("���������ƶ��Ĵ���Ϊ��%d\n", f);
			break;
		case 4:	MSort(L);
			cout << "�鲢ѡ��" << endl;
			show(L);
			printf("\n");
			printf("�鲢��������ȽϵĴ���Ϊ��%d\n", h);
			printf("�ƶ��Ĵ���Ϊ��%d\n", g);
			break;
		}
	}
}
