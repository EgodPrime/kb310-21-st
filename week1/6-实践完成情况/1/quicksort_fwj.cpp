#include <iostream>
using namespace std;
#define  MAXSIZE  100          						//顺序表的最大长度
typedef struct
{
	int key;//关键字项
	char* otherinfo;//其他数据项
}ElemType;//记录类型
//顺序表的存储结构  
typedef struct
{
	ElemType* r;	         						//存储空间的基地址
	int  length;            						//顺序表长度
}SqList;											//顺序表类型

int a=0,b=0;//用来记录冒泡排序的移动和交换次数											
void BubbleSort(SqList L)
{//对顺序表L做冒泡排序，首先将第一个记录的关键字和第二个记录的关键字进行比较，若为逆序，则交换，依此类推，直到第n-1个记录和第n个记录的关键字进行过比较为止。
 //上述过程称为第一趟冒泡排序，每一趟排序重复上述操作，直到在某一趟过程中没有进行过交换记录的操作，说明序列已全部达到排序要求。
	int m, j, flag;
	ElemType t;
	m = L.length - 1; flag = 1; 				//flag用来标记某一趟排序是否发生交换
	while ((m > 0) && (flag == 1))
	{
		flag = 0;           				//flag置为0，如果本趟排序没有发生交换，则不会执行下一趟排序
		for (j = 1; j <= m; j++)
		{
			
			if (L.r[j].key > L.r[j + 1].key)
			{
				a++;//冒泡排序比较次数
				flag = 1;					//flag置为1，表示本趟排序发生了交换
				t = L.r[j]; L.r[j] = L.r[j + 1]; L.r[j + 1] = t;	//交换前后两个记录
				b=b+3;//冒泡排序移动次数
			}
		}				//if
		--m;
	}									//while
}										//BubbleSort


int h = 0, g = 0;//记录归并排序的比较和移动次数
//设两个有序表放在同一数组中相邻的位置上：r[low...mid]和r[mid...high],每次分别从两个表中取出一个记录进行比较，将较小者放入r1[low...high]，
//重复此过程，直至一个表为空，最后将另一非空表中余下的部分直接复制到r1中
void Merge(ElemType r[], ElemType r1[], int low, int mid, int high)
{//归并排序，将有序表r[low...mid]和r[mid...high]归并为有序表r1[low...high]
	int i = low, j = mid + 1, k = low;
	while (i != mid + 1 && j != high + 1)
	{
		if (r[i].key > r[j].key)
		{
			r1[k++] = r[j++]; 
			g++; //移动的次数
			h++;//归并排序排序比较的次数
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
		r1[k++] = r[i++];//将剩余的r[low...mid]复制到r1中
		g++;
	}
	while (j != high + 1)
	{
		r1[k++] = r[j++]; //将剩余的r[j.high]复制到r1中
		g++;
	}
	for (i = low; i <= high; i++)
	{
		r[i] = r1[i];
	}
}

void MergeSort(ElemType r[], ElemType r1[], int low, int high) 
{//r[low...high]递归排序后放入r1[low...high]中
	int m;
	if (low < high) 
	{
		//h++;//归并排序比较次数
		m = low + (high - low) / 2;//将当前序列一分为二，求出分裂点mid
		MergeSort(r, r1, low, m);//对子序列r[low...mid]递归归并并排序，结果放入r1[low...mid]
		MergeSort(r, r1, m + 1, high);//对子序列r[mid+1...high]递归归并并排序，结果放入r1[mid+1...high]
		Merge(r, r1, low, m, high); // 对子序列r[low...mid]和r[mid+1...high]归并到r1[low...high]
	}
}

void MSort(SqList& L)
{//对顺序表L做归并排序
	MergeSort(L.r,L.r,1,L.length);
}

//①设待排序的记录存放在数组r[1...n]中，r[1]是一个有序序列；②循环n-1次，每次使用折半查找法，
//查找r[i]在已排好序的序列r[1...i-1]中的插入位置，然后将r[i]插入表长为i-1的有序序列r[1...i-1]，直到将r[n]插入表长为n-1的有序序列r[1...n-1]，最后得到一个表长为n的有序序列。
int c = 0, d = 0;
void B_InsertSort(SqList L)
{//对顺序表L做折半插入排序
	int i = 0, j = 0;
	int low = 1, mid = 1, high = 1;
	for (i = 2; i <= L.length; ++i)
	{
		low = 1; high = i - 1;//置查找区间初值
		L.r[0] = L.r[i];//将待插入的记录暂存到监视哨中
		d = d + 1;
		while (low <= high)//在r[low...high]中折半查找插入的位置
		{
			mid = (low + high) / 2;//折半
			c++;//折半插入排序比较的次数
			if (L.r[mid].key > L.r[0].key)
			{
				high = mid - 1; //插入点在前一子表
			}
			else
			{
				low = mid + 1;// 插入点在后一子表
			}
		}
		for (j = i - 1; j >= high + 1; --j)
		{
			L.r[j + 1] = L.r[j];//记录后移
			++d;//折半插入排序移动的次数
		}
		L.r[high + 1] = L.r[0];//将r[0]即原r[i]，插入到正确位置
		d = d + 1;
	}
}

int e = 0, f = 0;
int Partition(SqList L, int low, int high)
{//对顺序表L中的子表r[low..high]进行一趟排序，返回枢轴位置
	int pivotkey;
	L.r[0] = L.r[low];                    	//用子表的第一个记录做枢轴记录
	pivotkey = L.r[low].key;		   	    //枢轴记录关键字保存在pivotkey中
	while (low < high)                      //从表的两端交替地向中间扫描
	{	
		while (low < high && L.r[high].key >= pivotkey)
		{
			--high; e++;
		}
		L.r[low] = L.r[high];	f = f + 1;				//将比枢轴记录小的记录移到低端
		while (low < high && L.r[low].key <= pivotkey)
		{
			++low; e++;
		}
		L.r[high] = L.r[low];	f = f + 1;				//将比枢轴记录大的记录移到高端
	}//while
	L.r[low] = L.r[0];						//枢轴记录到位
	f = f + 1;
	return  low;							//返回枢轴位置
}//Partition

void QSort(SqList L, int low, int high)
{	//调用前置初值：low=1; high=L.length;
	//对顺序表L中的子序列L.r[low..high]做快速排序
	int pivotloc;
	if (low < high)
	{	
		//长度大于1
		//e++;//快速排序比较的次数
		pivotloc = Partition(L, low, high); 		//将L.r[low..high]一分为二，pivotloc是枢轴位置
		QSort(L, low, pivotloc - 1);				//对左子表递归排序
		QSort(L, pivotloc + 1, high);        	//对右子表递归排序
	}
}											//QSort

void QuickSort(SqList L)
{
	//对顺序表L做快速排序
	QSort(L, 1, L.length);
}
void Create_Sq(SqList& L)
{
	int i, n;
	cout << "请输入数据个数，不超过" << MAXSIZE << "个。" << endl;
	cin >> n;											//输入个数
	cout << "请输入待排序的数据:\n";
	while (n > MAXSIZE)
	{
		cout << "个数超过上限，不能超过" << MAXSIZE << "，请重新输入" << endl;
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
	printf("                    排序                            \n");
	printf("********************************************************\n");
	printf("*                1-----冒泡排序                        *\n");
	printf("*                2-----折半插入                        *\n");
	printf("*                3-----快速排序                        *\n");
	printf("*                4-----归并选择                        *\n");
	printf("\n");
	while (1) {
		cout << "\n请选择：\n";
		cin >> j;
		switch (j)
		{
		case 1:BubbleSort(L);
			cout << "冒泡排序：" << endl;
			show(L);
			printf("\n");
			printf("冒泡排序比较的次数为：%d\n",a);
			printf("冒泡排序交换的次数为：%d\n",b);
			break;
		case 2:B_InsertSort(L);
			cout << "折半插入：" << endl;
			show(L);
			printf("\n");
			printf("折半插入排序比较的次数为：%d\n", c);
			printf("折半插入移动的次数为：%d\n", d);
			break;
		case 3:	QuickSort(L);
			cout << "快速排序：" << endl;
			show(L);
			printf("\n");
			printf("快速排序比较的次数为：%d\n", e);
			printf("快速排序移动的次数为：%d\n", f);
			break;
		case 4:	MSort(L);
			cout << "归并选择：" << endl;
			show(L);
			printf("\n");
			printf("归并排序排序比较的次数为：%d\n", h);
			printf("移动的次数为：%d\n", g);
			break;
		}
	}
}
