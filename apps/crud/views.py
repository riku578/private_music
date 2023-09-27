from apps.crud.forms import UserForm
from flask import Blueprint,render_template,redirect,url_for
from apps.app import db
from apps.crud.models import User
crud = Blueprint(
    "crud",
    __name__,
    template_folder="templates",
    static_folder="static",
)
@crud.route("/")
def index():
    return render_template("crud/index.html")

@crud.route("/sql")
def sql():
    db.session.query(User).all()
    return "コンソールログを確認してください"
@crud.route("/users/<user_id>", methods=["GET", "POST"])
def edit_user(user_id):
    form = UserForm()

    # Userモデルを利用してユーザーを取得する
    user = User.query.filter_by(id=user_id).first()

    # formからサブミットされた場合はユーザーを更新しユーザーの一覧画面へリダイレクトする
    if form.validate_on_submit():
        user.username = form.username.data
        user.email = form.email.data
        user.password = form.password.data
        db.session.add(user)
        db.session.commit()
        return redirect(url_for("crud.users"))

    # GETの場合はHTMLを返す
    return render_template("crud/edit.html", user=user, form=form)
@crud.route("/users")
def users():
    """ユーザーの一覧を取得する"""
    users = User.query.all()
    return render_template("crud/index.html", users=users)