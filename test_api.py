"""
API测试脚本
用于测试Flutter前端API接口
"""

import requests
import time
import os
from PIL import Image
import io
import argparse

def test_scene_analysis(image_path, base_url):
    """测试场景分析API"""
    print("\n===== 测试场景分析API =====")
    url = f"{base_url}/api/scene/analyze"
    
    # 读取图像文件
    with open(image_path, "rb") as f:
        image_data = f.read()
    
    # 发送请求
    print(f"发送请求到: {url}")
    print(f"图像大小: {len(image_data)} 字节")
    start_time = time.time()
    
    response = requests.post(url, data=image_data, headers={
        "Content-Type": "application/octet-stream"
    })
    
    elapsed = time.time() - start_time
    print(f"请求耗时: {elapsed:.2f}秒")
    
    # 处理响应
    if response.status_code == 200:
        result = response.json()
        print("请求成功!")
        print(f"场景类型: {result.get('scene_type')}")
        print(f"环境: {result.get('environment')}")
        print(f"照明: {result.get('lighting')}")
        print(f"检测到的物体: {', '.join(result.get('objects', []))}")
        print(f"置信度: {result.get('confidence')}")
        print(f"服务器处理时间: {result.get('processing_time', 0):.2f}秒")
    else:
        print(f"请求失败: {response.status_code}")
        print(response.text)

def test_text_recognition(image_path, base_url):
    """测试文字识别API"""
    print("\n===== 测试文字识别API =====")
    url = f"{base_url}/api/ocr/recognize"
    
    # 读取图像文件
    with open(image_path, "rb") as f:
        image_data = f.read()
    
    # 发送请求
    print(f"发送请求到: {url}")
    print(f"图像大小: {len(image_data)} 字节")
    start_time = time.time()
    
    response = requests.post(url, data=image_data, headers={
        "Content-Type": "application/octet-stream"
    })
    
    elapsed = time.time() - start_time
    print(f"请求耗时: {elapsed:.2f}秒")
    
    # 处理响应
    if response.status_code == 200:
        result = response.json()
        print("请求成功!")
        print(f"识别文本: {result.get('text')}")
        print(f"语言: {result.get('language')}")
        print(f"置信度: {result.get('confidence')}")
        print(f"识别到的文本区域数量: {len(result.get('text_regions', []))}")
        print(f"服务器处理时间: {result.get('processing_time', 0):.2f}秒")
    else:
        print(f"请求失败: {response.status_code}")
        print(response.text)

def test_object_detection(image_path, base_url):
    """测试物体检测API"""
    print("\n===== 测试物体检测API =====")
    url = f"{base_url}/api/object/detect"
    
    # 读取图像文件
    with open(image_path, "rb") as f:
        image_data = f.read()
    
    # 发送请求
    print(f"发送请求到: {url}")
    print(f"图像大小: {len(image_data)} 字节")
    start_time = time.time()
    
    response = requests.post(url, data=image_data, headers={
        "Content-Type": "application/octet-stream"
    })
    
    elapsed = time.time() - start_time
    print(f"请求耗时: {elapsed:.2f}秒")
    
    # 处理响应
    if response.status_code == 200:
        result = response.json()
        print("请求成功!")
        print(f"检测到的物体数量: {result.get('object_count')}")
        
        for i, obj in enumerate(result.get('objects', [])):
            print(f"物体 {i+1}: {obj.get('class')}, 置信度: {obj.get('confidence'):.2f}")
            print(f"  边界框: {obj.get('bbox')}")
        
        print(f"服务器处理时间: {result.get('processing_time', 0):.2f}秒")
    else:
        print(f"请求失败: {response.status_code}")
        print(response.text)

def test_voice_recognition(audio_path, base_url):
    """测试语音识别API"""
    print("\n===== 测试语音识别API =====")
    url = f"{base_url}/api/voice/recognize"
    
    # 读取音频文件
    with open(audio_path, "rb") as f:
        audio_data = f.read()
    
    # 发送请求
    print(f"发送请求到: {url}")
    print(f"音频大小: {len(audio_data)} 字节")
    start_time = time.time()
    
    response = requests.post(url, data=audio_data, headers={
        "Content-Type": "audio/wav"
    })
    
    elapsed = time.time() - start_time
    print(f"请求耗时: {elapsed:.2f}秒")
    
    # 处理响应
    if response.status_code == 200:
        result = response.json()
        print("请求成功!")
        print(f"识别文本: {result.get('text')}")
        print(f"语言: {result.get('language')}")
        print(f"置信度: {result.get('confidence')}")
        
        command = result.get('command', {})
        if command:
            print(f"识别到的命令: {command.get('action')}")
            print(f"命令参数: {command.get('parameters')}")
            print(f"命令置信度: {command.get('confidence')}")
        
        print(f"服务器处理时间: {result.get('processing_time', 0):.2f}秒")
    else:
        print(f"请求失败: {response.status_code}")
        print(response.text)

def main():
    parser = argparse.ArgumentParser(description="测试VISTA API接口")
    parser.add_argument("--url", default="http://localhost:8000", help="API服务器基础URL")
    parser.add_argument("--image", default="test_image.jpg", help="测试图像文件路径")
    parser.add_argument("--audio", default="test_audio.wav", help="测试音频文件路径")
    parser.add_argument("--test", choices=["all", "scene", "ocr", "object", "voice"], default="all", help="要测试的API")
    
    args = parser.parse_args()
    
    # 检查文件是否存在
    if not os.path.exists(args.image):
        print(f"警告: 图像文件 {args.image} 不存在")
        if args.test in ["all", "scene", "ocr", "object"]:
            print("将创建一个测试图像...")
            # 创建一个简单的测试图像
            img = Image.new('RGB', (640, 480), color=(73, 109, 137))
            img.save(args.image)
            print(f"已创建测试图像: {args.image}")
    
    if not os.path.exists(args.audio) and args.test in ["all", "voice"]:
        print(f"警告: 音频文件 {args.audio} 不存在")
        print("请提供一个有效的音频文件用于测试语音识别API")
    
    # 执行测试
    if args.test in ["all", "scene"]:
        test_scene_analysis(args.image, args.url)
    
    if args.test in ["all", "ocr"]:
        test_text_recognition(args.image, args.url)
    
    if args.test in ["all", "object"]:
        test_object_detection(args.image, args.url)
    
    if args.test in ["all", "voice"] and os.path.exists(args.audio):
        test_voice_recognition(args.audio, args.url)

if __name__ == "__main__":
    main()
