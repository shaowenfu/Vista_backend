"""
主应用入口文件
主要功能：
1. 配置FastAPI应用程序
2. 注册各个模块的路由
3. 配置中间件和事件处理
4. 启动应用服务器
"""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# 导入各个模块的路由
from app.routers import perception, inference, interaction, execution

# 创建FastAPI应用实例
app = FastAPI(
    title="VISTA API",
    description="视觉智能支持与技术助手API服务",
    version="1.0.0"
)

# 配置CORS中间件
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # 在生产环境中应该设置具体的源
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 注册路由模块
app.include_router(
    perception,
    prefix="/api/perception",
    tags=["感知模块"],
    responses={404: {"description": "Not found"}},
)

app.include_router(
    inference,
    prefix="/api/inference",
    tags=["推理模块"],
    responses={404: {"description": "Not found"}},
)

app.include_router(
    interaction,
    prefix="/api/interaction",
    tags=["交互模块"],
    responses={404: {"description": "Not found"}},
)

app.include_router(
    execution,
    prefix="/api/execution",
    tags=["执行模块"],
    responses={404: {"description": "Not found"}},
)

@app.get("/")
async def root():
    """
    根路由
    返回API服务的基本信息
    """
    return {
        "message": "欢迎使用VISTA API服务",
        "version": "1.0.0",
        "status": "running"
    }

# 启动事件
@app.on_event("startup")
async def startup_event():
    """
    应用启动时的初始化操作
    - 初始化数据库连接
    - 加载AI模型
    - 初始化缓存
    """
    pass

# 关闭事件
@app.on_event("shutdown")
async def shutdown_event():
    """
    应用关闭时的清理操作
    - 关闭数据库连接
    - 释放模型资源
    - 清理缓存
    """
    pass
