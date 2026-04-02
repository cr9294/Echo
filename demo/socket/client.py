from fastapi import FastAPI, BackgroundTasks  # 导入 FastAPI 和 BackgroundTasks 类
from starlette.concurrency import run_in_threadpool  # 导入 run_in_threadpool 函数


def create_app():
    '''
    - 创建 FastAPI 应用程序实例
    '''
    app = FastAPI()  # 创建 FastAPI 应用程序实例
    return app

app = create_app()  # 创建 FastAPI 应用程序实例

@app.on_event("startup")
async def init_scheduler():
    '''
    - 当应用程序启动时初始化调度程序
    '''
    from task import run  # 从 task 模块导入 run 函数
    run()  # 运行初始化调度程序的函数


if __name__ == '__main__':
    import uvicorn  # 导入 uvicorn 模块

    uvicorn.run(
        app='client:app',  # 指定应用程序位置
        host="10.191.31.211",  # 设置主机地址
        log_level="debug",  # 设置日志级别为调试
        port=8888,  # 设置端口号
        loop="asyncio",  # 设置事件循环为 asyncio
        # workers=4,  # 设置工作进程数量
    )
