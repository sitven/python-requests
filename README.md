# interface-python
ע�����<br>
<br>
���д���Ŀǰ�����޸�[config.ini](https://github.com/zhangmoumou1/interface_python/blob/master/config/config.ini)��·������·��Ϊ��Ŀ����·�����˽ӿ�����Ϊ�ֵ��ʽ���õ�ʵ����Ŀ����ת����json��xml��������ʽ<br>
## һ��ʵ�ַ���<br>
1.ͨ��python+flask��дRestful API��������Դ˿��<br>
<br>
2.����Restful_Api�µ�[resfulapi.py](https://github.com/zhangmoumou1/interface_python/blob/master/Restful_Api/resfulapi.py)������ͨ��postman�������ӿڹ����Բ�ӿ��Ƿ�����������ֹͣ���пɽ������̣�<br>
�����������ɲ鿴����http://www.zhangyanc.club/blog/82<br>
<br>
3.ʹ��python��requestsģ������ӿڣ��ٷ��ĵ�http://docs.python-requests.org/zh_CN/latest/user/quickstart.html<br>
<br>
4.����ʹ��ddt����������ȡExcel�еĲ�������ִ��<br>
<br>
5.������Ա������־<br>

## �������Ŀ¼�Ľ���<br>
![no view](https://github.com/zhangmoumou1/interface_python/blob/master/readme/%E6%9E%B6%E6%9E%84%E5%9B%BE.jpg)<br>
<br>
1.Public��branch�ļ�����ҪдһЩ������������,������Ķ��η�װ����ȡExcel���ݡ���־��������Ա����Ż�,�����ļ���ȡ��;<br>
<br>
2.Restful_Api�ļ���Ϊ�ӿڵ�ʵ�֣�����[resfulapi.py](https://github.com/zhangmoumou1/interface_python/blob/master/Restful_Api/resfulapi.py),ͨ��postman������֤;<br>
<br>
![no view](https://github.com/zhangmoumou1/interface_python/blob/master/readme/postman.jpg)<br>
<br>
3.config�ļ�����������·��,[config.ini](https://github.com/zhangmoumou1/interface_python/blob/master/config/config.ini)Ϊ��Ŀ����·��,[globalparam.py](https://github.com/zhangmoumou1/interface_python/blob/master/config/globalparam.py)Ϊ��־�ļ�������������ȡ�ʹ洢��·��;<br>
<br>
4.report�ļ����´����־�Ͳ��Ա���;<br>
<br>
![no view](https://github.com/zhangmoumou1/interface_python/blob/master/readme/%E6%B5%8B%E8%AF%95%E6%8A%A5%E5%91%8A.jpg)<br>
<br>
![no view](https://github.com/zhangmoumou1/interface_python/blob/master/readme/%E6%97%A5%E5%BF%97.jpg)<br>
<br>
5.testCase�ļ���д�˲�������,ͨ��ddt����������ȡExcel�ļ�,��unittest��Ԫ���Կ�ܹ�������;<br>
<br>
6.testdata�ļ����ǲ�������;<br>
<br>
7.����[run_ddt_case.py](https://github.com/zhangmoumou1/interface_python/blob/master/run_ddt_case.py)ִ������(��������������̲�̫���Ŀ��Կ�readme�µ�xmind����ͼ)��<br>

## ���������Ż���. . .
### 2018.11.02---����flask�ӿڴ��룬��������post��put��delete����ʽ<br>
1.�ڴ�֮ǰֻ�е�һ��get�ӿ���������������������ʽ<br>
2.�����а�������ɹ���ʧ�ܵİ���<br>
### 2018.11.04---�Ż�֧�ֶ���ԣ��ɶ�resultcode��ָ�������ֶν��ж���<br>
ʵ���߼���<br>
1.Excel������"����2"�У��ṩ��������ֵ<br>
2.������Ӧ�ֶ�Ϊ�ֵ��ʽ��ָ���ֶζ��ԣ�ǰ�����Excel����ֵ�л�ȡkeyֵ����ָ�����������valueֵ<br>
3.��ӿ�ֻ��resultcode���ԣ���Excel������2���в���Ϊ"param=null"��Ϊ�ж����ݣ����[ddt_case.py](https://github.com/zhangmoumou1/interface_python/blob/master/testCase/ddt_case.py)����<br>
4.��������������޸Ĵ���<br>
### 2018.11.05---����mysql��oracle��SQLserver���ݿ�Ĳ���<br>
ʵ���߼���<br>
1.����[readyaml.py](https://github.com/zhangmoumou1/interface_python/blob/master/config/readyaml.py)��[db.yaml](https://github.com/zhangmoumou1/interface_python/blob/master/config/db.yaml)��[operate_db.py](https://github.com/zhangmoumou1/interface_python/blob/master/Public/operate_db.py)<br>
1.ʹ��yaml�ļ��������ݿ�������Ϣ����Ϊ���˷����������ݿ��벻Ҫ����Ķ����ݣ�<br>
2.ͨ���ӿ�url�����ݿ������������ж�ִ�нӿ��������Ӧ��<br>
3.ͨ���ӿ�url��SQL�����������ж�ִ�нӿ���Ҫִ�е�SQL<br>
4.��[select_request.py](https://github.com/zhangmoumou1/interface_python/blob/master/Public/select_request.py)�н������ݿ������ȡ��������<br>
### 2018.11.07---���Ա������������Ż��ͽ�������<br>
1.ʹ�����е�ddt���������������־����������ƣ��޸�ddtԴ���Excel�д������������ο�https://www.cnblogs.com/Simple-Small/p/9230382.html<br>
2.���������Ա���������ͨ���ٷֱȺ������Ż�<br>
### 2018.12.07---֧�ֶ�ȡ���Excel�ļ�<br>
ʵ���߼���<br>
1.��ʵ�ʹ����в�������������ֻд��һ��Excel�У�֧�ֶ�ȡ���<br>
2.����[get_excel.py](https://github.com/zhangmoumou1/interface_python/blob/master/Public/get_excel.py)����ָ���ļ����»�ȡExcel�ļ�����ȡ���������浽�б���<br>
3.ע��Excel�ļ�����������ʵ�ʴ��봦��Ϊ׼<br>
<br>
<br>
