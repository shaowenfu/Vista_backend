"""
视觉相关数据模型
定义与视觉处理相关的数据结构

包含：
1. 图像数据模型
2. 检测结果模型
3. 传感器数据模型
"""

from pydantic import BaseModel, Field
from typing import List, Dict, Any, Optional
from datetime import datetime

class ImageData(BaseModel):
    """
    图像数据模型
    
    属性说明：
    - image_id: 图像唯一标识符
    - format: 图像格式(jpg, png等)
    - width: 图像宽度
    - height: 图像高度
    - channels: 图像通道数
    - metadata: 图像元数据
    """
    image_id: str = Field(..., description="图像唯一标识符")
    format: str = Field(..., description="图像格式")
    width: int = Field(..., description="图像宽度(像素)")
    height: int = Field(..., description="图像高度(像素)")
    channels: int = Field(3, description="图像通道数")
    metadata: Dict[str, Any] = Field(default_factory=dict, description="图像元数据")
    created_at: datetime = Field(default_factory=datetime.now, description="创建时间")

class BoundingBox(BaseModel):
    """
    边界框模型
    
    属性说明：
    - x1, y1: 左上角坐标
    - x2, y2: 右下角坐标
    - confidence: 置信度
    """
    x1: float = Field(..., description="左上角x坐标")
    y1: float = Field(..., description="左上角y坐标")
    x2: float = Field(..., description="右下角x坐标")
    y2: float = Field(..., description="右下角y坐标")
    confidence: float = Field(..., description="检测置信度")

class DetectionResult(BaseModel):
    """
    检测结果模型
    
    属性说明：
    - object_id: 检测对象ID
    - class_name: 对象类别名称
    - bbox: 边界框
    - attributes: 对象属性
    """
    object_id: str = Field(..., description="检测对象ID")
    class_name: str = Field(..., description="对象类别名称")
    bbox: BoundingBox = Field(..., description="边界框")
    attributes: Dict[str, Any] = Field(default_factory=dict, description="对象属性")
    timestamp: datetime = Field(default_factory=datetime.now, description="检测时间")

class SensorReading(BaseModel):
    """
    传感器读数模型
    
    属性说明：
    - sensor_id: 传感器ID
    - sensor_type: 传感器类型
    - value: 读数值
    - unit: 单位
    """
    sensor_id: str = Field(..., description="传感器ID")
    sensor_type: str = Field(..., description="传感器类型")
    value: float = Field(..., description="读数值")
    unit: str = Field(..., description="单位")
    timestamp: datetime = Field(default_factory=datetime.now, description="读数时间")

class SensorData(BaseModel):
    """
    传感器数据集合模型
    
    属性说明：
    - device_id: 设备ID
    - readings: 传感器读数列表
    - metadata: 数据元信息
    """
    device_id: str = Field(..., description="设备ID")
    readings: List[SensorReading] = Field(default_factory=list, description="传感器读数列表")
    metadata: Dict[str, Any] = Field(default_factory=dict, description="数据元信息")
    collected_at: datetime = Field(default_factory=datetime.now, description="数据采集时间")

class ProcessedImage(BaseModel):
    """
    处理后的图像模型
    
    属性说明：
    - original_image: 原始图像数据
    - processed_data: 处理后的数据
    - processing_info: 处理信息
    """
    original_image: ImageData
    processed_data: Dict[str, Any] = Field(default_factory=dict, description="处理后的数据")
    processing_info: Dict[str, Any] = Field(default_factory=dict, description="处理信息")
    processing_time: float = Field(..., description="处理耗时(秒)")
    processed_at: datetime = Field(default_factory=datetime.now, description="处理时间")

class VisionAnalysisResult(BaseModel):
    """
    视觉分析结果模型
    
    属性说明：
    - image_data: 图像数据
    - detections: 检测结果列表
    - sensor_data: 相关传感器数据
    - analysis_info: 分析信息
    """
    image_data: ProcessedImage
    detections: List[DetectionResult] = Field(default_factory=list, description="检测结果列表")
    sensor_data: Optional[SensorData] = Field(None, description="相关传感器数据")
    analysis_info: Dict[str, Any] = Field(default_factory=dict, description="分析信息")
    analyzed_at: datetime = Field(default_factory=datetime.now, description="分析时间")
