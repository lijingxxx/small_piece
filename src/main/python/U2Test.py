import uiautomator2 as u2
# import commands
import os
import time


<<<<<<< Updated upstream
def auto_ui(phone_ip):
    # device = u2.connect('192.168.0.101')  # alias for u2.connect_wifi('10.0.0.1')
    device = u2.connect(phone_ip)
    print(device.info)
    device.healthcheck()

    # device.app_start('com.android.browser')
    start_monkey_cmd = 'adb shell monkey -p com.taobao.taobao --throttle 100 --ignore-crashes --ignore-timeouts --ignore-security-exceptions --ignore-native-crashes --monitor-native-crashes -v -v -v 500 > /tmp/test.log'

    # run adb
    rt = os.system(start_monkey_cmd)
    # print("adb result: %s" % rt)

    # 黑屏
    print("screen off")
    device.screen_off()

    time.sleep(3)
=======
device = u2.connect('172.18.8.25')  # 手机和电脑的网络是同一个网段时使用该链接方式
print(device.info)
device.healthcheck()

# device.app_start('com.android.browser')

start_monkey_cmd = 'adb shell monkey -p com.tencent.mm -p com.tencent.mobileqq -p com.taobao.taobao -p com.eg.android.AlipayGphone -p com.sina.weibo -p com.netease.cloudmusic --throttle 100 --ignore-crashes --ignore-timeouts --ignore-security-exceptions --ignore-native-crashes --monitor-native-crashes -v -v -v 100 > /tmp/test.log'

#run adb
rt = os.system(start_monkey_cmd)
# print("adb result: %s" % rt)

#app = device.session('com.android.browser', True)

# 黑屏
print("screen off")
device.screen_off()
>>>>>>> Stashed changes

    # 亮屏
    print("screen on")
    device.screen_on()

<<<<<<< Updated upstream
    # browser = device.app_start('com.android.browser')
    # device(resourceId="com.android.browser:id/search_hint").click()
    #
    #
    # print("screen shot")
    device.app_stop('com.taobao.taobao')
    device.app_start('com.android.browser')
    # app = device.session('com.android.browser', True)

    start_time = int(time.time())
    shot_count = 0

    while True:
        # 每隔2秒截一张图, 截10次
        cpp = device.current_app()
        print("current app: %s" % cpp)

        if cpp['package'] == 'com.android.browser':
            device.screenshot('/tmp/shot_%s.jpg' % shot_count)
            shot_count = shot_count + 1

        # sleep 2s
        time.sleep(2)
=======
# 亮屏
print("screen on")
device.screen_on()

device.app_start('com.android.browser')
# device(resourceId="com.android.browser:id/search_hint").click()
#
#
# print("screen shot")

start_time = int(time.time())
print(start_time)
shot_count = 0

while True:
    # 每隔2秒截一张图, 截10次
    cpp = device.current_app()  # 获取当前应用程序信息
    # print("current app: %s" % cpp)

    if cpp['package'] == 'com.android.browser':
        device.screenshot('/tmp/shot_%s.jpg' % start_time)
        shot_count = shot_count + 1
>>>>>>> Stashed changes

        end_time = int(time.time())
        if end_time - start_time > 6:
            break

    print("test end!!!")


phone_ips = ['192.168.0.1', '192.168.0.2', '192.168.0.3', '192.168.0.4']

auto_ui('1')
auto_ui('1')
auto_ui('1')
auto_ui('1')
