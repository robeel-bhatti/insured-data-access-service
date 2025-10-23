from flask_smorest import Blueprint
from flask.views import MethodView


hc_blp = Blueprint("health", "health")


@hc_blp.route("/health-check")
class HealthCheck(MethodView):
    @hc_blp.response(200)  # type: ignore
    def get(self) -> dict[str, str]:
        return {"message": "Party Service is healthy"}
