# OCR Backend

## 快速开始

### 环境准备

**这里推荐使用Docker**

#### 运行Docker

安装docker后执行以下命令构建docker镜像

```shell
docker build -t ocr_backend:latest .
```

然后运行镜像

```shell
docker run -itd -p 9292:9292 --name ocr_dev ocr_backend:latest
```

进入容器

```shell
docker exec -it ocr_dev bash
```

#### 依赖安装

Docker 内部自带`Python 3.6`/`3.7`/`3.8`/`3.9`环境，选择所需Python版本，执行以下命令
> 注意：例如要使用`Python 3.9`版本，以下`python3.x`替换为`python3.9`，`pip3.x`替换为`pip3.9`

```shell
pip3.x install -r requirements.txt
python3.x setup.py
```

### 启动程序

```shell
python3.x -m src
```