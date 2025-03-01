# VISTA 后端 API 接口文档

本文档描述了 VISTA 后端 API 接口，用于与 Flutter 前端应用进行通信。

## 基本信息

- 基础 URL: `http://localhost:8000/api`
- 内容类型: 
  - 图像请求: `application/octet-stream`
  - 音频请求: `audio/wav`
- 响应格式: JSON

## API 端点

### 1. 场景分析

分析图像中的场景，识别环境类型和物体。

- **URL**: `/scene/analyze`
- **方法**: POST
- **请求体**: 图像二进制数据
- **响应**:
  ```json
  {
    "scene_type": "室内",
    "environment": "办公室",
    "lighting": "明亮",
    "objects": ["桌子", "椅子", "电脑", "书籍"],
    "confidence": 0.85,
    "processing_time": 0.123
  }
  ```

### 2. 文字识别 (OCR)

识别图像中的文字内容。

- **URL**: `/ocr/recognize`
- **方法**: POST
- **请求体**: 图像二进制数据
- **响应**:
  ```json
  {
    "text": "识别到的完整文本内容",
    "language": "中文",
    "confidence": 0.92,
    "text_regions": [
      {
        "text": "区域文本",
        "bbox": [10, 10, 300, 50],
        "confidence": 0.95
      }
    ],
    "processing_time": 0.234
  }
  ```

### 3. 物体检测

检测图像中的物体并返回位置信息。

- **URL**: `/object/detect`
- **方法**: POST
- **请求体**: 图像二进制数据
- **响应**:
  ```json
  {
    "objects": [
      {
        "class": "人",
        "confidence": 0.96,
        "bbox": [50, 30, 250, 380]
      },
      {
        "class": "椅子",
        "confidence": 0.87,
        "bbox": [300, 200, 450, 400]
      }
    ],
    "object_count": 2,
    "processing_time": 0.345
  }
  ```

### 4. 语音识别

识别音频中的语音内容并解析可能的命令。

- **URL**: `/voice/recognize`
- **方法**: POST
- **请求体**: 音频二进制数据
- **响应**:
  ```json
  {
    "text": "打开相机并拍照",
    "confidence": 0.88,
    "language": "中文",
    "command": {
      "action": "open_camera",
      "parameters": {
        "mode": "photo"
      },
      "confidence": 0.92
    },
    "processing_time": 0.456
  }
  ```

## 错误处理

所有 API 在发生错误时将返回适当的 HTTP 状态码和错误详情：

```json
{
  "detail": "错误详情描述"
}
```

常见状态码：
- 400: 请求参数错误
- 404: 资源不存在
- 500: 服务器内部错误

## 测试工具

项目包含一个测试脚本 `test_api.py`，可用于测试各个 API 端点：

```bash
# 测试所有 API
python test_api.py

# 测试特定 API
python test_api.py --test scene
python test_api.py --test ocr
python test_api.py --test object
python test_api.py --test voice

# 指定测试图像和音频
python test_api.py --image path/to/image.jpg --audio path/to/audio.wav

# 指定 API 服务器地址
python test_api.py --url http://localhost:8000
```

## 调试信息

所有 API 端点都会在控制台输出详细的日志信息，包括：
- 请求接收时间
- 接收到的数据大小
- 处理过程中的关键步骤
- 处理结果
- 处理时间

这些日志信息有助于在开发和测试过程中进行调试。
