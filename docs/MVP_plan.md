# BLV助手 MVP设计方案

## 一、MVP定位

### 1. 核心价值主张
为BLV人群提供基于多模态大模型的场景理解和交互辅助服务，帮助他们更好地感知和理解周围环境。

### 2. 关键功能选择
聚焦于最急迫且技术相对成熟的场景：
- **场景理解与描述**：理解环境并提供语音反馈
- **文字识别与朗读**：识别文本内容并语音播报
- **简单物品识别**：识别日常物品并进行语音描述

### 3. MVP目标
1. 验证产品价值
2. 获取用户反馈
3. 测试技术可行性
4. 为后续迭代打基础

## 二、技术方案

### 1. 系统架构
```plaintext
移动端 App (Flutter)
    ↓↑ 
云服务 (FastAPI)
    ↓↑
AI 服务 (GPT-4V等)
```

### 2. 核心技术栈

#### 2.1 前端(Flutter)
- 相机实时预览
- 语音交互界面
- WebSocket通信
- 本地状态管理

#### 2.2 后端(FastAPI)
- 视频流处理
- AI服务调用
- WebSocket服务
- 简单用户管理

#### 2.3 AI能力
- GPT-4V：场景理解
- OCR：文字识别
- YOLO：物体检测
- Whisper：语音识别
- Edge TTS：语音合成

## 三、功能设计

### 1. 场景理解模式
```plaintext
工作流程：
1. 用户启动场景理解
2. 实时捕获视频帧
3. 调用GPT-4V分析场景
4. 生成场景描述
5. 转换为语音反馈
```

### 2. 文字识别模式
```plaintext
工作流程：
1. 用户启动文字识别
2. 捕获图像
3. OCR提取文字
4. 格式化处理
5. 语音播报
```

### 3. 物品识别模式
```plaintext
工作流程：
1. 用户启动物品识别
2. 实时物体检测
3. 目标物体分析
4. 生成物品描述
5. 语音反馈
```

### 4. 交互设计
- 语音指令控制
- 简单手势操作
- 触摸辅助操作
- 声音反馈机制

## 四、开发规划

### 1. 第一阶段（1天）：基础框架
- 搭建Flutter项目框架
- 实现相机和语音基础功能
- 搭建后端服务
- 完成AI服务对接

### 2. 第二阶段（2天）：核心功能
- 实现场景理解功能
- 完成文字识别功能
- 开发物品识别功能
- 优化语音交互体验

### 3. 第三阶段（1天）：优化打磨
- 性能优化
- 交互体验改进
- Bug修复
- 准备演示

## 五、项目目录结构

设计一个完整的 FastAPI 项目目录结构，并添加必要的文件和配置。这个项目结构将包括主应用程序、开发文档、数据模型以及模块化的路由。
完整的 FastAPI 项目目录结构
以下是完整的项目目录结构，包括主应用、模块化的路由、数据模型和开发文档：
```plaintext
vista_backend/
├── app/                       # 主应用目录
│   ├── main.py                # 主应用入口
│   ├── routers/               # 路由模块
│   │   ├── __init__.py
│   │   ├── perception.py      # 感知模块路由
│   │   ├── inference.py       # 推理模块路由
│   │   ├── interaction.py     # 交互模块路由
│   │   └── execution.py       # 执行模块路由
│   ├── models/                # 数据模型
│   │   ├── __init__.py
│   │   ├── vision.py          # 视觉相关模型
│   │   ├── inference.py       # 推理相关模型
│   │   ├── interaction.py     # 交互相关模型
│   │   └── execution.py       # 执行相关模型
├── perception/                # 感知模块
│   ├── vision_recognition.py  # YOLOv8封装
│   ├── multimodal_sensing.py  # 传感器数据采集
│   └── data_preprocessing.py  # 图像增强/噪声过滤
├── inference/                 # 推理模块
│   ├── scene_understanding.py # GPT-4V集成
│   └── decision_making.py     # 规则引擎
├── interaction/               # 交互模块
│   ├── voice_interaction.py   # Whisper + Edge TTS
│   └── haptic_feedback.py     # 振动模式映射
├── execution/                 # 执行模块
│   ├── task_planner.py        # 有限状态机
│   └── execution_monitor.py   # 异常检测
├── docs/                      # 开发文档
│   ├── architecture.md        # 系统架构文档
│   ├── api.md                 # API 文档
│   └── README.md              # 项目说明文档
├── requirements.txt           # 依赖文件
└── README.md                  # 项目根目录说明文档
```
1. 主应用文件 (app/main.py)
这是 FastAPI 的入口文件，负责注册所有模块的路由。
```python
from fastapi import FastAPI
from routers.perception import router as perception_router
from routers.inference import router as inference_router
from routers.interaction import router as interaction_router
from routers.execution import router as execution_router

app = FastAPI(title="VISTA API", description="API for VISTA - Visual Intelligence Support & Technical Assistant")

# 注册路由模块
app.include_router(perception_router, prefix="/api/perception", tags=["Perception"])
app.include_router(inference_router, prefix="/api/inference", tags=["Inference"])
app.include_router(interaction_router, prefix="/api/interaction", tags=["Interaction"])
app.include_router(execution_router, prefix="/api/execution", tags=["Execution"])
```
2. 路由模块
每个模块的路由文件负责定义该模块的 API 接口。
- app/routers/perception.py
```python
from fastapi import APIRouter
from perception.vision_recognition import recognize_objects
from perception.multimodal_sensing import collect_sensor_data
from perception.data_preprocessing import preprocess_data

router = APIRouter()

@router.get("/vision/")
def vision_recognition():
    return recognize_objects()

@router.get("/sensing/")
def multimodal_sensing():
    return collect_sensor_data()

@router.get("/preprocessing/")
def data_preprocessing():
    return preprocess_data()
```
- app/routers/inference.py
```python
from fastapi import APIRouter
from inference.scene_understanding import understand_scene
from inference.decision_making import make_decision

router = APIRouter()

@router.get("/scene/")
def scene_understanding():
    return understand_scene()

@router.get("/decision/")
def decision_making():
    return make_decision()
```
- app/routers/interaction.py
```python
from fastapi import APIRouter
from interaction.voice_interaction import voice_to_text, text_to_speech
from interaction.haptic_feedback import generate_haptic_pattern

router = APIRouter()

@router.get("/voice/")
def voice_interaction():
    return voice_to_text()

@router.get("/speech/")
def text_to_speech_interaction():
    return text_to_speech()

@router.get("/haptic/")
def haptic_feedback():
    return generate_haptic_pattern()
```
- app/routers/execution.py
```python
from fastapi import APIRouter
from execution.task_planner import plan_task
from execution.execution_monitor import monitor_execution

router = APIRouter()

@router.get("/plan/")
def task_planning():
    return plan_task()

@router.get("/monitor/")
def execution_monitoring():
    return monitor_execution()
```

3. 数据模型
在 app/models 文件夹中，你可以定义与每个模块相关的数据模型。
- 例如：
- app/models/vision.py
```python
from pydantic import BaseModel

class VisionRecognitionResult(BaseModel):
    objects: list[str]
    confidence: float
```
- app/models/inference.py
```python
from pydantic import BaseModel  
```
- app/models/interaction.py
```python
from pydantic import BaseModel
```
- app/models/execution.py
```python
from pydantic import BaseModel
```

4. 开发文档

### VISTA 系统架构

#### 模块划分
1. **感知模块 (Perception)**：
   - 视觉识别
   - 多模态感知
   - 数据预处理
2. **推理模块 (Inference)**：
   - 场景理解
   - 决策制定
3. **交互模块 (Interaction)**：
   - 语音交互
   - 触觉反馈
4. **执行模块 (Execution)**：
   - 任务规划
   - 执行监控
docs/api.md
markdown复制
# VISTA API 文档

## 感知模块
- `GET /api/perception/vision/`：视觉识别
- `GET /api/perception/sensing/`：多模态感知
- `GET /api/perception/preprocessing/`：数据预处理

## 推理模块
- `GET /api/inference/scene/`：场景理解
- `GET /api/inference/decision/`：决策制定

## 交互模块
- `GET /api/interaction/voice/`：语音识别
- `GET /api/interaction/speech/`：语音合成
- `GET /api/interaction/haptic/`：触觉反馈

## 执行模块
- `GET /api/execution/plan/`：任务规划
- `GET /api/execution/monitor/`：执行监控
5. 运行项目
在项目根目录下运行以下命令启动 FastAPI 应用：
```bash
uvicorn app.main:app --reload
```
6. 访问 API 和文档
- API 访问：
  - http://127.0.0.1:8000/api/perception/vision/
  - http://127.0.0.1:8000/api/inference/scene/
  - http://127.0.0.1:8000/api/interaction/voice/
  - http://127.0.0.1:8000/api/execution/plan/
- 自动生成的文档：
  - Swagger UI：http://127.0.0.1:8000/docs
  - ReDoc：http://127.0.0.1:8000/redoc
### 总结
  通过这种模块化的结构，vista项目后端代码更加清晰、易于维护和扩展。每个模块的功能被封装在单独的文件中，通过主应用动态注册路由，使得整个项目的结构更加合理。

## 五、关键指标

### 1. 性能指标
- 场景理解响应时间 < 2s
- 文字识别准确率 > 90%
- 物品识别准确率 > 85%
- App启动时间 < 3s

### 2. 体验指标
- 语音交互准确率 > 90%
- 操作步骤 ≤ 3步
- 无网络延迟感
- 电池消耗合理

## 六、后续扩展性

### 1. 技术扩展
- 边缘计算迁移准备
- AI模型本地部署
- 多模态融合架构
- 实时性能优化

### 2. 功能扩展
- 导航功能集成
- 社交功能接入
- 个性化定制
- 场景化应用

## 七、演示重点

### 1. 核心场景展示
- 室内场景理解
- 文档阅读辅助
- 物品识别分类
- 语音交互体验

### 2. 技术亮点
- 多模态融合能力
- 实时处理性能
- 交互体验设计
- 架构扩展性

### 3. 发展潜力
- 技术进化路线
- 产品规划愿景
- 商业化可能性
- 社会价值展现

## 八、风险管理

### 1. 技术风险
- AI服务稳定性
- 网络延迟影响
- 设备兼容性
- 电池消耗问题

### 2. 应对策略
- 备用服务方案
- 离线功能支持
- 广泛设备测试
- 性能优化机制
