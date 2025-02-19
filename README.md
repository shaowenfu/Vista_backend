# VISTA Backend

VISTA (Visual Intelligence Support & Technical Assistant) 是一个基于多模态大模型的场景理解和交互辅助服务后端系统。

## 功能特点

- **场景理解与描述**：使用GPT-4V进行场景分析和描述
- **文字识别与朗读**：集成OCR和Edge TTS实现文本识别和语音合成
- **物品识别**：基于YOLOv8的实时物体检测
- **多模态交互**：支持语音和触觉反馈的自然交互

## 系统架构

```plaintext
VISTA Backend
├── 感知模块 (Perception)
│   ├── 视觉识别 (YOLOv8)
│   ├── 多模态感知
│   └── 数据预处理
├── 推理模块 (Inference)
│   ├── 场景理解 (GPT-4V)
│   └── 决策制定
├── 交互模块 (Interaction)
│   ├── 语音交互 (Whisper + Edge TTS)
│   └── 触觉反馈
└── 执行模块 (Execution)
    ├── 任务规划
    └── 执行监控
```

## 技术栈

- **Web框架**: FastAPI
- **AI模型**: 
  - GPT-4V (场景理解)
  - YOLOv8 (物体检测)
  - Whisper (语音识别)
  - Edge TTS (语音合成)
- **异步处理**: asyncio
- **状态管理**: 有限状态机
- **监控**: Prometheus

## 快速开始

### 环境要求

- Python 3.9+
- pip

### 安装

1. 克隆仓库
```bash
git clone https://github.com/your-username/vista-backend.git
cd vista-backend
```

2. 创建虚拟环境
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows
```

3. 安装依赖
```bash
pip install -r requirements.txt
```

4. 配置环境变量
```bash
cp .env.example .env
# 编辑.env文件，填入必要的配置信息
```

### 运行

```bash
uvicorn app.main:app --reload
```

访问 http://localhost:8000/docs 查看API文档

## API接口

### 感知模块

- `POST /api/perception/vision/detect`: 物体检测
- `GET /api/perception/sensing/collect`: 传感器数据采集
- `POST /api/perception/preprocessing/enhance`: 数据增强处理

### 推理模块

- `POST /api/inference/scene/understand`: 场景理解
- `POST /api/inference/decision/make`: 决策制定

### 交互模块

- `POST /api/interaction/speech/recognize`: 语音识别
- `POST /api/interaction/speech/synthesize`: 语音合成
- `POST /api/interaction/haptic/generate`: 触觉反馈生成

### 执行模块

- `POST /api/execution/task/plan`: 任务规划
- `GET /api/execution/task/{task_id}/status`: 任务状态查询
- `GET /api/execution/metrics`: 执行指标查询

## 项目结构

```plaintext
vista_backend/
├── app/                    # 主应用目录
│   ├── main.py            # 主应用入口
│   ├── routers/           # 路由模块
│   └── models/            # 数据模型
├── perception/            # 感知模块
├── inference/            # 推理模块
├── interaction/          # 交互模块
├── execution/           # 执行模块
├── docs/                # 文档
├── tests/              # 测试用例
├── requirements.txt    # 项目依赖
└── README.md          # 项目说明
```

## 开发指南

### 代码规范

- 使用Black进行代码格式化
- 使用isort进行import排序
- 使用flake8进行代码检查
- 遵循PEP 8命名规范

### 测试

```bash
# 运行单元测试
pytest

# 生成测试覆盖率报告
pytest --cov=app tests/
```

### 文档生成

API文档自动生成于：
- Swagger UI: http://localhost:8000/docs
- ReDoc: http://localhost:8000/redoc

## 部署

### Docker部署

1. 构建镜像
```bash
docker build -t vista-backend .
```

2. 运行容器
```bash
docker run -d -p 8000:8000 vista-backend
```

### 生产环境配置

- 使用gunicorn作为WSGI服务器
- 配置反向代理（如Nginx）
- 启用HTTPS
- 设置适当的CORS策略

## 贡献指南

1. Fork 项目
2. 创建特性分支 (`git checkout -b feature/AmazingFeature`)
3. 提交更改 (`git commit -m 'Add some AmazingFeature'`)
4. 推送到分支 (`git push origin feature/AmazingFeature`)
5. 创建Pull Request

## 许可证

[MIT License](LICENSE)

## 联系方式

- 项目维护者: Your Name
- Email: your.email@example.com
- GitHub: [your-username](https://github.com/your-username)
