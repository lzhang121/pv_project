from flask import Flask, request, jsonify
from flasgger import Swagger
from flask_cors import CORS
from models import db, User
from config import Config
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
app.config.from_object(Config)
CORS(app)
Swagger(app)
db.init_app(app)

# ✅ 创建数据库表（兼容 Flask 3.1）
with app.app_context():
    db.create_all()


@app.route('/api/users', methods=['GET'])
def get_users():
    """
    获取用户列表
    ---
    responses:
      200:
        description: 返回用户数组
    """
    users = User.query.all()
    return jsonify([u.to_dict() for u in users])


@app.route('/api/users', methods=['POST'])
def add_user():
    """
    添加新用户
    ---
    parameters:
      - in: body
        name: user
        schema:
          type: object
          required:
            - name
            - email
          properties:
            name:
              type: string
            email:
              type: string
    responses:
      201:
        description: 创建成功
    """
    data = request.get_json()
    new_user = User(name=data['name'], email=data['email'])
    db.session.add(new_user)
    db.session.commit()
    return jsonify(new_user.to_dict())


@app.route('/api/users', methods=['DELETE'])
def delete_user():
    """
    根据名称或邮箱删除用户
    ---
    parameters:
      - in: query
        name: name
        required: false
        schema:
          type: string
      - in: query
        name: email
        required: false
        schema:
          type: string
    responses:
      200:
        description: 删除成功
      404:
        description: 用户未找到
    """
    # 获取请求中的 name 和 email 查询参数
    name = request.args.get('name')
    email = request.args.get('email')

    # 检查是否提供了 name 或 email 参数
    if not name and not email:
        return jsonify({"message": "Please provide either name or email to delete the user."}), 400

    # 根据提供的参数查找用户
    user = None
    if name:
        user = User.query.filter_by(name=name).first()
    elif email:
        user = User.query.filter_by(email=email).first()

    # 如果没有找到用户，返回 404 错误
    if user is None:
        return jsonify({"message": "User not found"}), 404

    # 删除用户并提交
    db.session.delete(user)
    db.session.commit()

    return jsonify({"message": "User deleted successfully"}), 200


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)
