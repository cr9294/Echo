import websocket  # 导入 WebSocket 库
import threading  # 导入线程库
import time  # 导入时间库

def on_close(ws):
    '''
    - WebSocket client 重试机制
    '''
    print("重试：%s" % time.ctime())  # 打印重试时间
    time.sleep(2)  # 等待2秒
    connect_websocket()  # 每2秒重试一次连接

def on_open(ws):
    '''
    - 当系统连接上后的提示
    '''
    print('连接已建立')  # 打印连接已建立提示

def on_message(wsapp, message):
    '''
    - 接收服务器 WebSocket 发送来的消息
    '''
    print(message)  # 打印接收到的消息

def connect_websocket():
    '''
    - 尝试连接 WebSocket 服务器
    - 并给该线程设置守护
    '''
    ws = websocket.WebSocketApp(
        "ws://10.191.31.211:8000/ws/2323",  # WebSocket 服务器地址
        on_open=on_open,  # 连接成功时调用的函数
        on_close=on_close,  # 连接关闭时调用的函数
        cookie="chocolate",  # 发送的cookie
        on_message=on_message  # 收到消息时调用的函数
    )
    wst = threading.Thread(target=ws.run_forever)  # 创建线程，运行 WebSocket 连接
    wst.daemon = True  # 设置线程为守护线程
    wst.start()  # 启动线程

def run():
    '''
    - WebSocket 组件会跟随 FastAPI 主进程启动
    - 客户端系统会每隔2秒尝试一次连接
    '''
    try:
        connect_websocket()  # 尝试连接 WebSocket 服务器
    except Exception as err:
        print(err)  # 打印错误信息
        print("连接失败")  # 打印连接失败提示

if __name__ == "__main__":
    run()  # 运行主函数
