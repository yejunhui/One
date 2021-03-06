from aip import AipSpeech

""" 你的 APPID AK SK """
APP_ID = '14603516'
API_KEY = 'ycBsqwCkB5U64WX7P1wV8SpX'
SECRET_KEY = 'Bon0Kxv4pcHQfUQ3nIA8a6hHKZKET8CZ'

client = AipSpeech(APP_ID, API_KEY, SECRET_KEY)

# 读取文件
def get_file_content(filePath):
    with open(filePath,'rb') as fp:
        return fp.read()

# 识别本地文件
'''
speech	Buffer	建立包含语音内容的Buffer对象, 语音文件的格式，pcm 或者 wav 或者 amr。不区分大小写	是
format	String	语音文件的格式，pcm 或者 wav 或者 amr。不区分大小写。推荐pcm文件	是
rate	int	采样率，16000，固定值	是
cuid	String	用户唯一标识，用来区分用户，填写机器 MAC 地址或 IMEI 码，长度为60以内	否
dev_pid	Int	不填写lan参数生效，都不填写，默认1537（普通话 输入法模型），dev_pid参数见本节开头的表格	否
lan(已废弃)	String	历史兼容参数，请使用dev_pid。如果dev_pid填写，该参数会被覆盖。语种选择,输入法模型，默认中文（zh）。 中文=zh、粤语=ct、英文=en，不区分大小写。	否

dev_pid	语言	模型	是否有标点	备注
1536	普通话(支持简单的英文识别)	搜索模型	无标点	支持自定义词库
1537	普通话(纯中文识别)	输入法模型	有标点	不支持自定义词库
1737	英语		有标点	不支持自定义词库
1637	粤语		有标点	不支持自定义词库
1837	四川话		有标点	不支持自定义词库
1936	普通话远场	远场模型	有标点	不支持
'''

print('正在识别...')
resu = client.asr(get_file_content('F:/py/One/testfile/200.wav'), 'wav', 8000, {'dev_pid': 1637,})

if resu['err_no'] == 0:
    print(resu['result'])
else :
    print('Error：%s' %resu['err_no'])

'''
3300	用户输入错误	输入参数不正确	请仔细核对文档及参照demo，核对输入参数
3301	用户输入错误	音频质量过差	请上传清晰的音频
3302	用户输入错误	鉴权失败	token字段校验失败。请使用正确的API_KEY 和 SECRET_KEY生成
3303	服务端问题	语音服务器后端问题	请将api返回结果反馈至论坛或者QQ群
3304	用户请求超限	用户的请求QPS超限	请降低识别api请求频率 （qps以appId计算，移动端如果共用则累计）
3305	用户请求超限	用户的日pv（日请求量）超限	请“申请提高配额”，如果暂未通过，请降低日请求量
3307	服务端问题	语音服务器后端识别出错问题	目前请确保16000的采样率音频时长低于30s，8000的采样率音频时长低于60s。如果仍有问题，请将api返回结果反馈至论坛或者QQ群
3308	用户输入错误	音频过长	音频时长不超过60s，请将音频时长截取为60s以下
3309	用户输入错误	音频数据问题	服务端无法将音频转为pcm格式，可能是长度问题，音频格式问题等。 请将输入的音频时长截取为60s以下，并核对下音频的编码，是否是8K或者16K， 16bits，单声道。
3310	用户输入错误	输入的音频文件过大	语音文件共有3种输入方式： json 里的speech 参数（base64后）； 直接post 二进制数据，及callback参数里url。 分别对应三种情况：json超过10M；直接post的语音文件超过10M；callback里回调url的音频文件超过10M
3311	用户输入错误	采样率rate参数不在选项里	目前rate参数仅提供8000,16000两种，填写4000即会有此错误
3312	用户输入错误	音频格式format参数不在选项里	目前格式仅仅支持pcm，wav或amr，如填写mp3即会有此错误
'''