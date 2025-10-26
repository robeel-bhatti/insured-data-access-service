from flask.views import MethodView
from flask_smorest import Blueprint

party_blp = Blueprint("party", __name__)


@party_blp.route("/parties/<int:id>")
class Party(MethodView):
    def get(self, id: int) -> None:
        pass
