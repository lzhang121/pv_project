FROM python:3.11-slim

# 安装依赖
WORKDIR /app
COPY requirements.txt ./
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

# 拷贝代码
COPY . .


EXPOSE 5001
CMD ["python", "app.py"]
