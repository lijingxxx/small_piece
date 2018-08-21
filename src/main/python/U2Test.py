import uiautomator2 as u2
import time
from threading import Thread


def monkey(device):
    device.adb_shell('monkey -p jingdong.app.mall -p com.sina.weibo -p com.tencent.mobileqq -p com.netease.cliudmusic -p com.taobao.taobao -p com.tencent.mm --throttle 500 --ignore-crashes --ignore-timeouts --ignore-security-exceptions --ignore-native-crashes --monitor-native-crashes -v -v -v 1200000000')


def auto_ui(phone_ip):
    device = u2.connect(phone_ip)
    print(device.info)

    monkey_start = Thread(target=monkey, args=(device,))
    monkey_start.start()

    # adb shell kill -9 `adb shell ps | grep com.android.commands.monkey | awk '{print $2}'`
    time.sleep(30)
    pidstr = device.adb_shell("ps | grep monkey")
    print(pidstr)
    pid = device.adb_shell("ps | grep monkey").split()[1]
    print("%s monkey pid is: %s" % (phone_ip, pid) + ",kill it")
    device.adb_shell("kill -9 " + pid)

    print("执行完monkey，%s sleep 2 second..." % phone_ip)
    time.sleep(2)

    # 灭屏
    print("%s screen off" % phone_ip)
    device.screen_off()

    print("%s sleep 5 second..." % phone_ip)
    time.sleep(5)

    # 亮屏
    print("%s screen on" % phone_ip)
    device.screen_on()

    print("亮屏后%s sleep 1 second..." % phone_ip)
    time.sleep(1)
    if device(packageName="com.android.systemui"):
        print("%s 上划开屏" % phone_ip)
        device.swipe(0.5, 0.835, 0.5, 0.295, duration=0.2)

    print("%s sleep 10 second...检查是否自动打开浏览器" % phone_ip)
    time.sleep(10)

    # 获取当前界面应用包名
    cpp = device.current_app()

    if cpp['package'] == 'com.android.browser':
        print("%s 自启动浏览器，复现问题" % phone_ip)
        return False

    # 打开浏览器后判断当前界面是否为网页
    device.app_start('com.android.browser')
    print("%s sleep 10 second...检查是否自动打开网页" % phone_ip)
    time.sleep(10)
    if device(className="android.webkit.WebView") or device(className="com.uc.webview.export.WebView"):
        print("%s has web view，复现问题" % phone_ip)
        return False
    else:
        print("%s has't web view" % phone_ip)

    print("没有复现，%s sleep 1 second..." % phone_ip)
    time.sleep(1)

    # 退出浏览器应用
    device.app_stop('com.android.browser')
    print("%s 没有复现，重新执行脚本" % phone_ip)

    print("%s sleep 1 second..." % phone_ip)
    time.sleep(1)

    print("auto_ui(phone_ip)方法的返回值：" + auto_ui(phone_ip))
    return True


def find_bugs(phone_ip):
    while auto_ui(phone_ip) is True:
        auto_ui(phone_ip)


if __name__ == '__main__':

    t1 = Thread(target=find_bugs, args=('172.18.8.16',))
    t1.start()
    print('线程1启动')

    t2 = Thread(target=find_bugs, args=('172.18.8.240',))
    t2.start()
    print('线程2启动')

    # 3 = Thread(target=find_bugs, args=('172.18.8.12',))  # 7912
    # t3.start()
    # print('线程3启动')

    # t4 = Thread(target=find_bugs, args=('172.18.8.13',))
    # t4.start()
    # print('线程4启动')


