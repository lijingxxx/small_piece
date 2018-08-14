import uiautomator2 as u2
# import commands
import os
import time


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

    # 亮屏
    print("screen on")
    device.screen_on()

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

        end_time = int(time.time())
        if end_time - start_time > 6:
            break

    print("test end!!!")


phone_ips = ['192.168.0.1', '192.168.0.2', '192.168.0.3', '192.168.0.4']

auto_ui('1')
auto_ui('1')
auto_ui('1')
auto_ui('1')
