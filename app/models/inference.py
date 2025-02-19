"""
推理相关数据模型
定义与场景理解和决策制定相关的数据结构

包含：
1. 场景描述模型
2. 决策结果模型
3. 反馈数据模型
"""

from pydantic import BaseModel, Field
from typing import List, Dict, Any, Optional
from datetime import datetime
from enum import Enum

class SceneType(str, Enum):
    """场景类型枚举"""
    INDOOR = "indoor"
    OUTDOOR = "outdoor"
    TRAFFIC = "traffic"
    SOCIAL = "social"
    UNKNOWN = "unknown"

class Confidence(BaseModel):
    """
    置信度模型
    
    属性说明：
    - value: 置信度值
    - factors: 影响因素
    """
    value: float = Field(..., ge=0, le=1, description="置信度值(0-1)")
    factors: Dict[str, float] = Field(default_factory=dict, description="影响因素")

class SceneElement(BaseModel):
    """
    场景元素模型
    
    属性说明：
    - element_id: 元素ID
    - element_type: 元素类型
    - properties: 元素属性
    - position: 空间位置
    """
    element_id: str = Field(..., description="元素ID")
    element_type: str = Field(..., description="元素类型")
    properties: Dict[str, Any] = Field(default_factory=dict, description="元素属性")
    position: Dict[str, float] = Field(..., description="空间位置")
    confidence: Confidence = Field(..., description="识别置信度")

class SpatialRelation(BaseModel):
    """
    空间关系模型
    
    属性说明：
    - relation_type: 关系类型
    - source_id: 源元素ID
    - target_id: 目标元素ID
    - properties: 关系属性
    """
    relation_type: str = Field(..., description="关系类型")
    source_id: str = Field(..., description="源元素ID")
    target_id: str = Field(..., description="目标元素ID")
    properties: Dict[str, Any] = Field(default_factory=dict, description="关系属性")
    confidence: Confidence = Field(..., description="关系置信度")

class SceneDescription(BaseModel):
    """
    场景描述模型
    
    属性说明：
    - scene_id: 场景ID
    - scene_type: 场景类型
    - elements: 场景元素列表
    - relations: 空间关系列表
    - description: 场景描述文本
    """
    scene_id: str = Field(..., description="场景ID")
    scene_type: SceneType = Field(..., description="场景类型")
    elements: List[SceneElement] = Field(default_factory=list, description="场景元素列表")
    relations: List[SpatialRelation] = Field(default_factory=list, description="空间关系列表")
    description: str = Field(..., description="场景描述文本")
    confidence: Confidence = Field(..., description="整体置信度")
    timestamp: datetime = Field(default_factory=datetime.now, description="分析时间")

class ActionPlan(BaseModel):
    """
    行动计划模型
    
    属性说明：
    - action_type: 行动类型
    - parameters: 行动参数
    - priority: 优先级
    """
    action_type: str = Field(..., description="行动类型")
    parameters: Dict[str, Any] = Field(default_factory=dict, description="行动参数")
    priority: float = Field(..., ge=0, le=1, description="优先级(0-1)")
    estimated_duration: float = Field(..., gt=0, description="预计耗时(秒)")

class Decision(BaseModel):
    """
    决策结果模型
    
    属性说明：
    - decision_id: 决策ID
    - scene_id: 关联场景ID
    - action_plans: 行动计划列表
    - reasoning: 决策推理过程
    """
    decision_id: str = Field(..., description="决策ID")
    scene_id: str = Field(..., description="关联场景ID")
    action_plans: List[ActionPlan] = Field(..., description="行动计划列表")
    reasoning: List[str] = Field(..., description="决策推理过程")
    confidence: Confidence = Field(..., description="决策置信度")
    created_at: datetime = Field(default_factory=datetime.now, description="决策时间")

class Feedback(BaseModel):
    """
    反馈数据模型
    
    属性说明：
    - feedback_id: 反馈ID
    - decision_id: 关联决策ID
    - feedback_type: 反馈类型
    - content: 反馈内容
    """
    feedback_id: str = Field(..., description="反馈ID")
    decision_id: str = Field(..., description="关联决策ID")
    feedback_type: str = Field(..., description="反馈类型")
    content: Dict[str, Any] = Field(..., description="反馈内容")
    rating: Optional[float] = Field(None, ge=0, le=5, description="评分(0-5)")
    submitted_at: datetime = Field(default_factory=datetime.now, description="提交时间")
