from flask_smorest import Blueprint
from flask.views import MethodView

party_blp = Blueprint("party", __name__)


@party_blp.route("/parties/<int:id>")
class Party(MethodView):
    def get(self, id: int) -> None:
        pass
