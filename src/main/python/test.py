import uiautomator2 as u2
import os
import time
from threading import Thread


# 链接设备
device = u2.connect('172.18.8.16')
print(device.info)
# print(device.healthcheck())
time.sleep(1)
device.screen_off()
time.sleep(2)
device.screen_on()
time.sleep(2)
# print(device(packageName="com.android.systemui"))
if device(packageName="com.android.systemui"):
    print("开屏界面")
    device.swipe(0.5, 0.835, 0.5, 0.295, duration=0.2)
else:
    print("这里")



# 记录开始时间
# start_time = int(time.time())

# 执行monkey  ['微信', 'QQ', '手机淘宝', '支付宝', '微博', '京东-挑好物,上京东', '网易云音乐']


def start_monkey(device):
    # monkey_cmd = 'adb shell monkey -p jingdong.app.mall -p com.sina.weibo -p com.eg.android.AlipayGphone -p com.tencent.mobileqq -p com.netease.cliudmusic -p com.taobao.taobao -p com.tencent.mm --throttle 100 --ignore-crashes --ignore-timeouts --ignore-security-exceptions --ignore-native-crashes --monitor-native-crashes -v -v -v 100'
    # print(os.popen(monkey_cmd))

    rt = device.adb_shell('monkey -p jingdong.app.mall -p com.sina.weibo -p com.eg.android.AlipayGphone -p com.tencent.mobileqq -p com.netease.cliudmusic -p com.taobao.taobao -p com.tencent.mm --throttle 100 --ignore-crashes --ignore-timeouts --ignore-security-exceptions --ignore-native-crashes --monitor-native-crashes -v -v -v 100')
    print("adb shell result: %s" % rt)

    # p.wait()
    # Popen.kill()

    # device = MonkeyRunner.waitForConnection()
    # device.startActivity('com.android.browser')

#def monkey_test():
    #t3 = Thread(target=start_monkey())
    #t3.start()
    # adb shell kill -9 `adb shell ps | grep com.android.commands.monkey | awk '{print $2}'`
    # time.sleep(10)
    # pid = os.popen("adb shell ps | grep monkey | awk '{print $2}'").read()
    # print(pid)
    # pid = pid.replace("\n", "")
    # print("monkey pid is: %s" % pid + ",kill it")
    # os.system("adb shell kill -9 " + pid)


#if __name__ == '__main__':
    #t1 = Thread(target=monkey_test())
    #t1.start()


# start_monkey(device)


