"""
路由模块初始化文件
用于导出各个子模块的路由，实现模块化的API结构

导出内容：
- perception: 感知模块路由
- inference: 推理模块路由
- interaction: 交互模块路由
- execution: 执行模块路由
"""

from app.routers.perception import router as perception
from app.routers.inference import router as inference
from app.routers.interaction import router as interaction
from app.routers.execution import router as execution

__all__ = ['perception', 'inference', 'interaction', 'execution']
