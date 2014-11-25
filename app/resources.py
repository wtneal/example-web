from flask.ext import restful


class Test(restful.Resource):
    def get(self):
        return {'hello': 'world'}
