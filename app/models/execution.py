"""
执行相关数据模型
定义与任务规划和执行监控相关的数据结构

包含：
1. 任务模型
2. 执行状态模型
3. 监控指标模型
"""

from pydantic import BaseModel, Field
from typing import List, Dict, Any, Optional
from datetime import datetime
from enum import Enum

class TaskStatus(str, Enum):
    """任务状态枚举"""
    PENDING = "pending"      # 等待执行
    RUNNING = "running"      # 正在执行
    PAUSED = "paused"       # 已暂停
    COMPLETED = "completed"  # 已完成
    FAILED = "failed"       # 执行失败
    CANCELLED = "cancelled"  # 已取消

class TaskPriority(str, Enum):
    """任务优先级枚举"""
    LOW = "low"           # 低优先级
    MEDIUM = "medium"     # 中优先级
    HIGH = "high"         # 高优先级
    CRITICAL = "critical" # 关键优先级

class TaskType(str, Enum):
    """任务类型枚举"""
    SCENE_ANALYSIS = "scene_analysis"  # 场景分析
    OBJECT_DETECTION = "object_detection"  # 物体检测
    TEXT_RECOGNITION = "text_recognition"  # 文字识别
    NAVIGATION = "navigation"  # 导航辅助
    INTERACTION = "interaction"  # 交互响应

class TaskDependency(BaseModel):
    """
    任务依赖模型
    
    属性说明：
    - task_id: 依赖任务ID
    - dependency_type: 依赖类型
    - conditions: 依赖条件
    """
    task_id: str = Field(..., description="依赖任务ID")
    dependency_type: str = Field(..., description="依赖类型")
    conditions: Dict[str, Any] = Field(default_factory=dict, description="依赖条件")

class TaskStep(BaseModel):
    """
    任务步骤模型
    
    属性说明：
    - step_id: 步骤ID
    - name: 步骤名称
    - action: 执行动作
    - parameters: 执行参数
    """
    step_id: str = Field(..., description="步骤ID")
    name: str = Field(..., description="步骤名称")
    action: str = Field(..., description="执行动作")
    parameters: Dict[str, Any] = Field(default_factory=dict, description="执行参数")
    status: TaskStatus = Field(TaskStatus.PENDING, description="步骤状态")
    order: int = Field(..., description="执行顺序")
    timeout: Optional[float] = Field(None, description="超时时间(秒)")

class Task(BaseModel):
    """
    任务模型
    
    属性说明：
    - task_id: 任务ID
    - type: 任务类型
    - priority: 优先级
    - steps: 执行步骤
    - dependencies: 任务依赖
    """
    task_id: str = Field(..., description="任务ID")
    name: str = Field(..., description="任务名称")
    type: TaskType = Field(..., description="任务类型")
    priority: TaskPriority = Field(TaskPriority.MEDIUM, description="任务优先级")
    description: str = Field("", description="任务描述")
    steps: List[TaskStep] = Field(default_factory=list, description="执行步骤")
    dependencies: List[TaskDependency] = Field(default_factory=list, description="任务依赖")
    status: TaskStatus = Field(TaskStatus.PENDING, description="任务状态")
    progress: float = Field(0.0, ge=0, le=1, description="执行进度")
    created_at: datetime = Field(default_factory=datetime.now, description="创建时间")
    updated_at: datetime = Field(default_factory=datetime.now, description="更新时间")
    timeout: Optional[float] = Field(None, description="任务超时时间(秒)")

class ExecutionMetrics(BaseModel):
    """
    执行指标模型
    
    属性说明：
    - cpu_usage: CPU使用率
    - memory_usage: 内存使用率
    - battery_level: 电池电量
    - network_latency: 网络延迟
    """
    cpu_usage: float = Field(..., ge=0, le=100, description="CPU使用率(%)")
    memory_usage: float = Field(..., ge=0, le=100, description="内存使用率(%)")
    battery_level: float = Field(..., ge=0, le=100, description="电池电量(%)")
    network_latency: float = Field(..., ge=0, description="网络延迟(ms)")
    error_rate: float = Field(..., ge=0, le=1, description="错误率")
    timestamp: datetime = Field(default_factory=datetime.now, description="采集时间")

class ExecutionError(BaseModel):
    """
    执行错误模型
    
    属性说明：
    - error_id: 错误ID
    - task_id: 相关任务ID
    - error_type: 错误类型
    - message: 错误信息
    """
    error_id: str = Field(..., description="错误ID")
    task_id: str = Field(..., description="相关任务ID")
    step_id: Optional[str] = Field(None, description="相关步骤ID")
    error_type: str = Field(..., description="错误类型")
    message: str = Field(..., description="错误信息")
    stack_trace: Optional[str] = Field(None, description="堆栈跟踪")
    timestamp: datetime = Field(default_factory=datetime.now, description="发生时间")

class ExecutionLog(BaseModel):
    """
    执行日志模型
    
    属性说明：
    - log_id: 日志ID
    - task_id: 相关任务ID
    - level: 日志级别
    - message: 日志信息
    """
    log_id: str = Field(..., description="日志ID")
    task_id: str = Field(..., description="相关任务ID")
    step_id: Optional[str] = Field(None, description="相关步骤ID")
    level: str = Field(..., description="日志级别")
    message: str = Field(..., description="日志信息")
    metadata: Dict[str, Any] = Field(default_factory=dict, description="日志元数据")
    timestamp: datetime = Field(default_factory=datetime.now, description="记录时间")

class ExecutionSummary(BaseModel):
    """
    执行总结模型
    
    属性说明：
    - total_tasks: 总任务数
    - completed_tasks: 已完成任务数
    - failed_tasks: 失败任务数
    - average_duration: 平均执行时间
    """
    total_tasks: int = Field(..., ge=0, description="总任务数")
    completed_tasks: int = Field(..., ge=0, description="已完成任务数")
    failed_tasks: int = Field(..., ge=0, description="失败任务数")
    average_duration: float = Field(..., ge=0, description="平均执行时间(秒)")
    error_rate: float = Field(..., ge=0, le=1, description="错误率")
    period_start: datetime = Field(..., description="统计开始时间")
    period_end: datetime = Field(..., description="统计结束时间")
