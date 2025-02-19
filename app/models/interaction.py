"""
交互相关数据模型
定义与语音交互和触觉反馈相关的数据结构

包含：
1. 语音输入输出模型
2. 触觉反馈模型
3. 交互配置模型
"""

from pydantic import BaseModel, Field
from typing import List, Dict, Any, Optional
from datetime import datetime
from enum import Enum

class AudioFormat(str, Enum):
    """音频格式枚举"""
    WAV = "wav"
    MP3 = "mp3"
    PCM = "pcm"
    OGG = "ogg"

class VoiceType(str, Enum):
    """语音类型枚举"""
    COMMAND = "command"
    QUERY = "query"
    RESPONSE = "response"
    ALERT = "alert"

class SpeechInput(BaseModel):
    """
    语音输入模型
    
    属性说明：
    - audio_id: 音频ID
    - format: 音频格式
    - duration: 音频时长
    - language: 语言代码
    """
    audio_id: str = Field(..., description="音频ID")
    format: AudioFormat = Field(..., description="音频格式")
    duration: float = Field(..., gt=0, description="音频时长(秒)")
    language: str = Field("zh-CN", description="语言代码")
    sample_rate: int = Field(16000, description="采样率")
    channels: int = Field(1, description="声道数")
    created_at: datetime = Field(default_factory=datetime.now, description="创建时间")

class SpeechOutput(BaseModel):
    """
    语音输出模型
    
    属性说明：
    - text: 待合成文本
    - voice_id: 声音ID
    - parameters: 合成参数
    """
    text: str = Field(..., description="待合成文本")
    voice_id: str = Field(..., description="声音ID")
    voice_type: VoiceType = Field(..., description="语音类型")
    parameters: Dict[str, Any] = Field(
        default_factory=lambda: {
            "speed": 1.0,
            "pitch": 1.0,
            "volume": 1.0
        },
        description="合成参数"
    )
    format: AudioFormat = Field(AudioFormat.WAV, description="输出格式")
    created_at: datetime = Field(default_factory=datetime.now, description="创建时间")

class VibrationPattern(BaseModel):
    """
    振动模式模型
    
    属性说明：
    - duration: 持续时间
    - intensity: 强度
    - frequency: 频率
    """
    duration: float = Field(..., gt=0, description="持续时间(毫秒)")
    intensity: float = Field(..., ge=0, le=1, description="强度(0-1)")
    frequency: float = Field(..., gt=0, description="频率(Hz)")

class HapticPattern(BaseModel):
    """
    触觉反馈模式模型
    
    属性说明：
    - pattern_id: 模式ID
    - pattern_type: 模式类型
    - patterns: 振动模式序列
    """
    pattern_id: str = Field(..., description="模式ID")
    pattern_type: str = Field(..., description="模式类型")
    patterns: List[VibrationPattern] = Field(..., description="振动模式序列")
    repeat_count: int = Field(1, ge=0, description="重复次数(0表示无限)")
    interval: float = Field(0, ge=0, description="重复间隔(毫秒)")
    created_at: datetime = Field(default_factory=datetime.now, description="创建时间")

class InteractionConfig(BaseModel):
    """
    交互配置模型
    
    属性说明：
    - user_id: 用户ID
    - voice_settings: 语音设置
    - haptic_settings: 触觉设置
    """
    user_id: str = Field(..., description="用户ID")
    voice_settings: Dict[str, Any] = Field(
        default_factory=lambda: {
            "preferred_voice": "zh-CN-XiaoxiaoNeural",
            "speed": 1.0,
            "volume": 1.0,
            "auto_play": True
        },
        description="语音设置"
    )
    haptic_settings: Dict[str, Any] = Field(
        default_factory=lambda: {
            "intensity_scale": 1.0,
            "enabled": True,
            "pattern_presets": {}
        },
        description="触觉设置"
    )
    updated_at: datetime = Field(default_factory=datetime.now, description="更新时间")

class InteractionEvent(BaseModel):
    """
    交互事件模型
    
    属性说明：
    - event_id: 事件ID
    - event_type: 事件类型
    - source: 事件来源
    - data: 事件数据
    """
    event_id: str = Field(..., description="事件ID")
    event_type: str = Field(..., description="事件类型")
    source: str = Field(..., description="事件来源")
    data: Dict[str, Any] = Field(..., description="事件数据")
    timestamp: datetime = Field(default_factory=datetime.now, description="事件时间")

class InteractionSession(BaseModel):
    """
    交互会话模型
    
    属性说明：
    - session_id: 会话ID
    - user_id: 用户ID
    - events: 事件列表
    - metadata: 会话元数据
    """
    session_id: str = Field(..., description="会话ID")
    user_id: str = Field(..., description="用户ID")
    events: List[InteractionEvent] = Field(default_factory=list, description="事件列表")
    metadata: Dict[str, Any] = Field(default_factory=dict, description="会话元数据")
    start_time: datetime = Field(default_factory=datetime.now, description="开始时间")
    end_time: Optional[datetime] = Field(None, description="结束时间")
