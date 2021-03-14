import json,requests,os,time,sys,datetime,random
from webUI import Ui_MainWindow
from MainUI import CUi_MainWindow
from LoadingUI import LUi_MainWindow
from PyQt5.QtWidgets import QApplication,QMainWindow,QMessageBox,QWidget
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from selenium import webdriver

class UpdateWinData(QThread):
    signal = pyqtSignal()
    signal2 = pyqtSignal(int)
    signal3 = pyqtSignal(int)
    def __init__(self,Window,Status):
        super(UpdateWinData,self).__init__()
        self.window = Window
        self.s = Status

    def run(self):
        if self.s == 0:
            while True:
                UpdateTimer()
                time.sleep(1)
        elif self.s == 1:
            while True:
                data = getData(0)
                if data != False:
                    UpdateData(data[0],self.signal3)
                    UpdateImg(data[1])
                    time.sleep(2)
                else:
                   self.signal.emit()
                   break
        else:
            Loading(self.signal2)       


class mainWindow(QMainWindow):
    def __init__(self):
        super(mainWindow, self).__init__()
        self.ui = Ui_MainWindow()  
        self.ui.setupUi(self)

    def getUI(self):
        return self.ui

    ##状态窗口
    def toOPEN(self):
        global u
        u.show()
        self.Thread1 = UpdateWinData(self,0)
        self.Thread1.start()
        self.Thread2 = UpdateWinData(self,1)
        self.Thread2.signal.connect(self.showWarning)
        self.Thread2.signal3.connect(self.setMainBar)
        self.Thread2.start()
    
    def toCLOSE(self):
        global u
        u.close()

    def getChildUI(self):
        self.f = ChildWindow()
        global u
        u = self.f 
        return u.getUI()

    def setBar(self,Int):
        global LUi,l
        if Int > 100:
            getData(1)
            l.close()
            return False
        LUi.progressBar.setValue(Int)

    def setMainBar(self,Int):
        global C_Ui
        if Int <= 100:
            C_ui.progressBar.setValue(Int)

    def showWarning(self):
        global MainWindow
        String = '登录过期，请重新登录！'
        u.close()
        QMessageBox.warning(MainWindow,'关于',String)
        OpenBrowser()

    ##加载窗口
    def LoadWin(self):
        global l
        l.show()
        self.Thread3 = UpdateWinData(self,2)
        self.Thread3.signal2.connect(self.setBar)
        self.Thread3.start()
        
    def getLoadUI(self):
        self.lw = LWindow()
        global l
        l = self.lw
        return l.getUI()

        

class LWindow(QMainWindow):
    def __init__(self):
        super(LWindow, self).__init__()
        self.ui = LUi_MainWindow()  
        self.ui.LsetupUi(self)

    def getUI(self):
        return self.ui


class ChildWindow(QMainWindow):
    def __init__(self):
        super(ChildWindow, self).__init__()
        self.ui = CUi_MainWindow()  
        self.ui.CsetupUi(self)

    def getUI(self):
        return self.ui


    
def writeCookie(cookieData):
    with open('cookie','w') as cookieFile:
        cookieFile.write(json.dumps(cookieData))
        return True

def readCookie():
    try:
        with open('cookie','r') as cookieFile:
            cookieData = json.loads(cookieFile.read())
            return cookieData
    except:
        return ''

def writeConfig(config):
    with open('config.json','w') as cookieFile:
        cookieFile.write(json.dumps(config))
        return True

def readConfig():
    try:
        with open('config.json','r') as cookieFile:
            configData = json.loads(cookieFile.read())
            return configData['status']
    except:
        return False

def detector(WinLogin):
    global ui
    while True:
        time.sleep(0.2)
        if WinLogin.current_url.find('passport.bilibili.com') == -1:
            global cookie
            cookie = WinLogin.get_cookies()
            if ui.Remember.isChecked():
                writeCookie(cookie)
            WinLogin.quit()
            global LUi
            LUi = MainWindow.getLoadUI()
            MainWindow.LoadWin()
            return cookie

def UpdateData(Tuple,signal):
    JTime,UserName,TimeNow,Level,Exp,Percent,Sign,coin,birthday,Fans,EnterBilibili = Tuple
    CTime = JTime.replace('y','/').replace('M','/').replace('D','')[0:JTime.find('|')-1]
    CTime = [int(x) for x in CTime.split('/')]
    JTime = JTime.replace('y','年').replace('M','月').replace('D','日')
    birthday = birthday.replace('y','年').replace('M','月').replace('D','日')
    if 18 <= TimeNow.hour <=24 or 0 <= TimeNow.hour <5:
        NowStatus = '晚上'
    elif 5 <= TimeNow.hour <7:
        NowStatus = '清晨'
    elif 7<= TimeNow.hour < 12:
        NowStatus = '上午'
    else:
        NowStatus = '下午'
    
    global C_ui
    C_ui.label_12.setText('<html><head/><body><p><span style=" font-size:12pt; font-weight:600;">'+birthday+'</span></p></body></html>')
    C_ui.label_10.setText('<html><head/><body><p><span style=" font-size:12pt; font-weight:600;">'+coin+'</span></p></body></html>')
    C_ui.label_6.setText('<html><head/><body><p><span style=" font-size:14pt; font-weight:600; color:#d00dea;">'+Sign+'</span></p></body></html>')
    try:
        signal.emit(Percent)
    except:
        pass
    C_ui.Level.setText('<html><head/><body><p><span style=" font-size:11pt; font-weight:600;">'+Exp+'</span></p></body></html>')
    C_ui.label_7.setText('<html><head/><body><p><span style=" font-size:16pt; font-weight:600; color:#2c8bff;">Level '+Level+'</span></p></body></html>')
    C_ui.UserShow.setText('<html><head/><body><p><span style=" font-size:18pt; font-weight:600; color:#f09920;">'+UserName+'</span><span style=" font-size:18pt;">,'+NowStatus+'好！</span></p></body></html>')
    C_ui.Timer.setText('<html><head/><body><p><span style=" font-size:12pt; font-weight:600;">'+JTime+'</span></p></body></html>')
    C_ui.FansNum.setText('<html><head/><body><p><span style=" font-size:12pt; font-weight:600; color:#f18293;">'+Fans+'</span></p></body></html>')
    C_ui.label_14.setText('<html><head/><body><p align="center"><span style=" font-size:16pt; font-weight:600; color:#ff5d0c;">'+EnterBilibili+'</span></p></body></html>')    
    C_ui.calendar.setSelectedDate(QDate(CTime[0],CTime[1],CTime[2]))
    
def UpdateTimer():
    global C_ui
    Now = time.strftime("%Y{}%m{}%d{} | %H{}%M{}%S",time.localtime()).format('年','月','日',':',':')
    C_ui.label_17.setText('<html><head/><body><p><span style=" font-size:14pt; font-weight:600;">'+Now+'</span></p></body></html>')


def UpdateImg(imgurl):
    global C_ui
    req = requests.get(imgurl)
    photo = QPixmap()
    photo.loadFromData(req.content)
    C_ui.ImageLabel.setPixmap(photo)
    C_ui.ImageLabel.setScaledContents(True)

    
    
def getData(status):
    global MainWindow
    global cookie
    Bilibili_cookie = [item["name"] + "=" + item["value"] for item in cookie]
    cookiestr = '; '.join(item for item in Bilibili_cookie)
    headers={
    'cookie':cookiestr,
    'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36'
    }
    Data=requests.get(url='https://member.bilibili.com/x2/creative/h5/calendar/event?ts=0',headers=headers)
    Dict = json.loads(Data.text)
    try:
        JoinTime = Dict['data']['pfs']['profile']['jointime']
    except:
        if status:
            OpenBrowser()
        else:
            pass
        return False
    
    JTime = time.strftime("%Yy%mM%dD | %H:%M:%S", time.localtime(JoinTime))
    DateJTime = datetime.datetime.strptime(JTime,"%Yy%mM%dD | %H:%M:%S")
    TimeNow = datetime.datetime.now()
    UserName = Dict['data']['pfs']['profile']['name']
    Level = str(Dict['data']['pfs']['level_info']['current_level'])
    Exp = str(Dict['data']['pfs']['level_info']['current_exp'])+'/'+str(json.loads(Data.text)['data']['pfs']['level_info']['next_exp'])
    Percent = int(Dict['data']['pfs']['level_info']['current_exp']/json.loads(Data.text)['data']['pfs']['level_info']['next_exp']*100)
    Sign = Dict['data']['pfs']['profile']['sign']
    coin = str(Dict['data']['pfs']['coins'])
    Fans = str(Dict['data']['pfs']['follower'])
    birthday = time.strftime("%Yy%mM%dD", time.localtime(Dict['data']['pfs']['profile']['birthday']))
    global imgurl
    imgurl = Dict['data']['pfs']['profile']['face']
    EnterBilibili = '今天距离你入站已有'+str((TimeNow - DateJTime).days)+'天啦！'
    if status:
        global C_ui
        C_ui = MainWindow.getChildUI()
        C_ui.Logout.triggered.connect(Exit)
        C_ui.LogoutWithClear.triggered.connect(Exit_with_clear)
        MainWindow.toOPEN()
        UpdateData((JTime,UserName,TimeNow,Level,Exp,Percent,Sign,coin,birthday,Fans,EnterBilibili),None)
        UpdateImg(imgurl)
    else:
        return [(JTime,UserName,TimeNow,Level,Exp,Percent,Sign,coin,birthday,Fans,EnterBilibili),imgurl]

def Exit():
    os._exit(0)

def Exit_with_clear():
    try:
        os.remove('cookie')
    except:
        pass
    writeConfig({'status':False})
    os._exit(0)
    

def Help():
    global MainWindow
    QMessageBox.information(MainWindow,'如何使用?','点击登录按钮后，程序将会自动调用下方选中的浏览器,\n而后将会自动跳转至B站官网，按照提示登录您的账号后，\n即可开启属于你的小世界啦!',QMessageBox.Ok)

def AboutCookie():
    global MainWindow
    String = '''
    Cookie类似于一个小小的“身份证”，用于网站判断用户信息，
    当您选择下方“记住我”的时候，该文件会自动生成，用于后续
    免密登录。

    但请注意，这也意味着，若被他人窃取走该Cookie文件，其同样
    可以在未经您允许的情况下免密登录，这是很危险的！！！

    因此，请不要随便将程序生成的Cookie文件随意拷贝给他人，或
    让他人随意拷贝；同时请放心，本程序不会收集您的Cookie信息
    '''
    QMessageBox.information(MainWindow,'Cookie与安全性',String)

def About():
    global MainWindow
    String = '''
    ==============关于==============        \t
    
    软件作者：Disy
    作者QQ：1481567451
    使用语言：Python
    兼容系统：Windows with x86_64
    
    转载前请联系原作者
    需要源代码可联系原作者
    （代码混乱，请在成年人的陪同下观看[狗头]）
    '''
    QMessageBox.information(MainWindow,'关于',String)

def OpenBrowser():
    path = os.getcwd().replace('\\','/')
    try:
        global MainWindow
        if ui.chooseBrowser.currentText().find('Chrome') != -1:
            browser = webdriver.Chrome(executable_path = path+'/driver/chromedriver.exe')
        elif ui.chooseBrowser.currentText().find('Edge') != -1:
            browser = webdriver.Edge(executable_path = path+'/driver/msedgedriver.exe')
        else:
            browser = webdriver.Firefox(executable_path = path+'/driver/geckodriver.exe')
        try:
            MainWindow.close()
            browser.get('https://member.bilibili.com')
        except:
            MainWindow.show()
    except:
        QMessageBox.critical(MainWindow,'浏览器错误','启动浏览器失败，可能由于您并未安装该浏览器，\n或浏览器的内核并非89版，请检查后重试!')
        return False
    time.sleep(2)
    detector(browser)

def Loading(signal):
    Tips = [
    '<html><head/><body><p><span style=" font-size:12pt; font-weight:600; color:#e70000;">Tips:界面的所有数据都是实时更新的，你的动作可以立刻看到哦！</span></p></body></html>',
    '<html><head/><body><p><span style=" font-size:12pt; font-weight:600; color:#e70000;">Tips:想退出登录了？进入程序后注意左上角哦！</span></p></body></html>',
    '<html><head/><body><p><span style=" font-size:12pt; font-weight:600; color:#e70000;">Tips:别忘了看一下登录界面左上角的Cookie相关的内容！</span></p></body></html>',
    '<html><head/><body><p><span style=" font-size:12pt; font-weight:600; color:#e70000;">Tips:你知道吗？这个软件基于Python & PyQt5</span></p></body></html>',
    '<html><head/><body><p><span style=" font-size:12pt; font-weight:600; color:#e70000;">Tips:登录失败不要慌张，记得检查一下网络连接哦！</span></p></body></html>',
    '<html><head/><body><p><span style=" font-size:12pt; font-weight:600; color:#e70000;">Tips:有bug可以及时向作者反馈，作者QQ:1481567451</span></p></body></html>',
    '<html><head/><body><p><span style=" font-size:12pt; font-weight:600; color:#e70000;">Tips:你知道吗，替换/icon下的图片可以自由更换自己喜欢的主题哦!</span></p></body></html>',
    '<html><head/><body><p><span style=" font-size:12pt; font-weight:600; color:#e70000;">Tips:程序自动生成的cookie文件请不要随意修改哦!</span></p></body></html>',
    '<html><head/><body><p><span style=" font-size:12pt; font-weight:600; color:#bc1ad1;">Tips:你有没有发现，我是紫色的诶！</span></p></body></html>',
    '<html><head/><body><p><span style=" font-size:12pt; font-weight:600; color:#e70000;">Tips:天知道这里有多少个Tips！</span></p></body></html>',
    '<html><head/><body><p><span style=" font-size:12pt; font-weight:600; color:#e70000;">Tips:登录界面的左上角一定要看哦！你会用到它们的</span></p></body></html>',
    '<html><head/><body><p><span style=" font-size:12pt; font-weight:600; color:#e70000;">Tips:哼哧哼哧...主人我在努力加载了呢！</span></p></body></html>',
    '<html><head/><body><p><span style=" font-size:12pt; font-weight:600; color:#e70000;">Tips:本程序开源哦，源码链接可以管作者要呢！(作者QQ见主界面)</span></p></body></html>',
    ]
    global LUi
    LUi.label_2.setText(random.choice(Tips))
    time.sleep(2)
    LUi.label_2.setText(random.choice(Tips))
    LUi.LoadStatus.setText('<html><head/><body><p align="center"><span style=" font-size:14pt; font-weight:600; color:#1942c8;">读取配置文件...</span></p></body></html>')
    signal.emit(20)
    LUi.label_2.setText(random.choice(Tips))
    try:
        readConfig()
    except:
        LUi.LoadStatus.setText('<html><head/><body><p align="center"><span style=" font-size:14pt; font-weight:600; color:#1942c8;">配置文件读取失败，请重启程序！</span></p></body></html>')
        return False
    time.sleep(2)
    LUi.LoadStatus.setText('<html><head/><body><p align="center"><span style=" font-size:14pt; font-weight:600; color:#1942c8;">生成Cookie文件...</span></p></body></html>')
    signal.emit(40)
    LUi.label_2.setText(random.choice(Tips))
    try:
        rCookie = readCookie()
        if rCookie == '' or rCookie == {}:
            writeCookie({})
        rCookie = readCookie()
        time.sleep(0.5)
        if rCookie == '':
            LUi.LoadStatus.setText('<html><head/><body><p align="center"><span style=" font-size:14pt; font-weight:600; color:#1942c8;">Cookie创建失败，请重启程序！</span></p></body></html>')
            return False
    except:
        LUi.LoadStatus.setText('<html><head/><body><p align="center"><span style=" font-size:14pt; font-weight:600; color:#1942c8;">Cookie读取失败，请重启程序！</span></p></body></html>')
        return False
    time.sleep(2)
    LUi.label_2.setText(random.choice(Tips))
    LUi.LoadStatus.setText('<html><head/><body><p align="center"><span style=" font-size:14pt; font-weight:600; color:#1942c8;">连接B站服务器...</span></p></body></html>')
    signal.emit(65)
    for i in range(5,0,-1):
        try:
            global cookie
            Bilibili_cookie = [item["name"] + "=" + item["value"] for item in cookie]
            cookiestr = '; '.join(item for item in Bilibili_cookie)
            headers={
            'cookie':cookiestr,
            'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36'
            }
            r = requests.get(url='https://member.bilibili.com/x2/creative/h5/calendar/event?ts=0',headers=headers,timeout = 5)
            if r.status_code != 200 and i >= 2:
                LUi.LoadStatus.setText('<html><head/><body><p align="center"><span style=" font-size:14pt; font-weight:600; color:#1942c8;">连接B站服务器超时，准备重试，剩余重连次数：'+str(i-1)+'</span></p></body></html>')
                signal.emit(65+(6-i)*5)
                time.sleep(2)
                LUi.label_2.setText(random.choice(Tips))
            else:
                time.sleep(1)
                Dict = json.loads(r.text)
                JoinTime = Dict['data']['pfs']['profile']['jointime']
                LUi.LoadStatus.setText('<html><head/><body><p align="center"><span style=" font-size:14pt; font-weight:600; color:#1942c8;">准备就绪！</span></p></body></html>')
                signal.emit(100)
                LUi.label_2.setText(random.choice(Tips))
                time.sleep(1.5)
                signal.emit(101)
                break
        except:
            LUi.LoadStatus.setText('<html><head/><body><p align="center"><span style=" font-size:14pt; font-weight:600; color:#1942c8;">连接B站服务器超时，准备重试，剩余重连次数：'+str(i-1)+'</span></p></body></html>')
            signal.emit(65+(6-i)*5)
            LUi.label_2.setText(random.choice(Tips))
            time.sleep(2)
    else:
        LUi.LoadStatus.setText('<html><head/><body><p align="center"><span style=" font-size:14pt; font-weight:600; color:#1942c8;">无法连接至B站服务器，请检查网络连接后重启程序尝试</span></p></body></html>')
        LUi.label_2.setText(random.choice(Tips))
        return False

        
def Login():
    global cookie,MainWindow,ui
    
    if ui.Remember.isChecked():
        writeConfig({'status':True})
        cookie = readCookie()
    else:
        writeConfig({'status':False})
        cookie = ''

    
    if cookie == '':
        OpenBrowser()
    else:
        try:
            MainWindow.close()
        except:
            pass
        global LUi
        LUi = MainWindow.getLoadUI()
        MainWindow.LoadWin()
        

##########################################

if __name__ == '__main__':
    QCoreApplication.setAttribute(Qt.AA_EnableHighDpiScaling)
    global MainWindow,ui
    app = QApplication(sys.argv)
    MainWindow = mainWindow()
    ui = MainWindow.getUI()
    hadChecked = readConfig()
    if hadChecked:
        ui.Remember.setChecked(True)
    MainWindow.show()
    ui.help.triggered.connect(Help)
    ui.about_Cookie.triggered.connect(AboutCookie)
    ui.about.triggered.connect(About)
    ui.startLogin.clicked.connect(Login)
    sys.exit(app.exec_())




