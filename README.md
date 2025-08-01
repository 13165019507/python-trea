# 加减法出题器 - Streamlit Web应用

一个现代化的加减法练习工具，基于Streamlit构建的Web应用程序。

## 功能特点

- 🧮 支持加法和减法练习
- 📊 可选择10以内或100以内的数值范围
- ⚙️ 两种批改模式：每题批改或全部答完后批改
- 📈 实时进度跟踪和成绩统计
- 🎯 智能题目生成，避免重复
- 📱 响应式设计，支持各种设备

## 快速开始

### 方法一：Streamlit Cloud 部署 (推荐)

1. **Fork 或 Clone 此仓库**
2. **注册 Streamlit Cloud 账户**：https://share.streamlit.io/
3. **连接 GitHub 仓库**
4. **部署应用**：
   - 选择仓库
   - 设置主文件路径：`app.py`
   - 点击 "Deploy!"

### 方法二：本地开发

#### 1. 安装依赖

```bash
pip install -r requirements.txt
```

#### 2. 运行应用

```bash
streamlit run app.py
```

#### 3. 访问应用

打开浏览器访问：http://localhost:8501

### 方法三：使用 DevContainer (开发环境)

1. **安装 VS Code 和 Docker**
2. **安装 Dev Containers 扩展**
3. **打开项目文件夹**
4. **按 F1 或 Ctrl+Shift+P，选择 "Dev Containers: Reopen in Container"**
5. **等待容器构建完成**
6. **运行应用**：
   ```bash
   streamlit run app.py
   ```

## 使用说明

1. **设置参数**：在左侧边栏选择运算类型、数值范围和出题数量
2. **选择批改模式**：
   - 每题批改：答完一题立即知道对错
   - 全部答完后批改：答完所有题目后统一查看结果
3. **开始答题**：点击"开始答题"按钮开始练习
4. **查看结果**：完成后查看详细成绩和错题分析

## 技术特性

- 使用Streamlit构建现代化Web界面
- 会话状态管理，支持答题进度保存
- 响应式布局设计
- 实时统计和进度显示
- 智能题目去重算法
- 优化的Streamlit Cloud配置

## 文件结构

```
├── app.py                    # 主应用程序文件
├── requirements.txt          # Python依赖包
├── packages.txt              # 系统依赖包
├── .streamlit/               # Streamlit配置
│   └── config.toml          # Streamlit配置文件
├── README.md                # 说明文档
├── .gitignore               # Git忽略文件
├── .devcontainer/           # DevContainer配置 (可选)
│   └── devcontainer.json    # DevContainer配置文件
└── 加减法出题器.py          # 原始命令行版本
```

## Streamlit Cloud 部署

### 部署步骤

1. **准备代码**：
   - 确保 `app.py` 是主文件
   - 确保 `requirements.txt` 包含所有依赖
   - 确保 `.streamlit/config.toml` 配置正确

2. **上传到 GitHub**：
   ```bash
   git add .
   git commit -m "Initial commit"
   git push origin main
   ```

3. **部署到 Streamlit Cloud**：
   - 访问 https://share.streamlit.io/
   - 连接 GitHub 账户
   - 选择仓库
   - 设置部署参数
   - 点击 "Deploy!"

### 配置说明

- **主文件**：`app.py`
- **Python 版本**：3.9+
- **依赖管理**：`requirements.txt`
- **系统依赖**：`packages.txt` (如需要)

## 开发环境

### 本地开发
- 本地 Python 环境
- DevContainer (可选)

### 生产部署
- Streamlit Cloud (推荐)
- 其他云平台

## 系统要求

- Python 3.7+
- Streamlit 1.47.1
- pandas 1.5.3
- numpy 1.26.4

## 许可证

MIT License 